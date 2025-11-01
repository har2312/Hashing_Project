"""
Flask API for Hash Table Simulator Web Application
Provides REST API endpoints for all hash table operations
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Import from the same directory (for Vercel deployment)
from hash_table import HashTable, TOMBSTONE
from utils import normalize_key, hash1 as h1_fn, hash2 as h2_fn

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Store hash tables in memory (keyed by session or simple storage)
# For production, consider using Redis or sessions
hash_tables = {}
current_id = 0


def get_table_state(table):
    """Convert hash table to JSON-serializable state"""
    if not table:
        return None
    
    buckets = []
    for i in range(table.size):
        contents = table.get_bucket_contents(i)
        # Check if the actual slot is a tombstone
        is_tombstone = (table.mode != 'chaining' and table.table[i] is TOMBSTONE)
        
        bucket_data = {
            'index': i,
            'contents': contents,
            'type': 'tombstone' if is_tombstone else ('empty' if not contents else 'filled')
        }
        buckets.append(bucket_data)
    
    return {
        'size': table.size,
        'mode': table.mode,
        'count': table.count,
        'load_factor': table.get_load_factor(),
        'buckets': buckets,
        'all_keys': table.get_all_keys(),
        'collisions': len(table.collision_log) if hasattr(table, 'collision_log') else 0
    }


def build_insert_steps(table, key):
    """Build detailed execution steps for insert operation based on current table contents.
    Accurately simulates probing, detects full-table condition, and mirrors pseudocode lines.
    """
    steps = []
    mode = table.mode
    m = table.size
    nk_val, _ = normalize_key(key)
    h1_val, _ = h1_fn(abs(nk_val), m)

    # CHAINING: straightforward
    if mode == 'chaining':
        steps.append({"line": 1, "text": f"FUNCTION Insert({key}, {m})", "vars": {"key": key, "m": m}, "highlight_bucket": None})
        steps.append({"line": 2, "text": f"h1 = hash(key) % m = {h1_val}", "vars": {"h1": h1_val, "m": m}, "highlight_bucket": h1_val})
        steps.append({"line": 3, "text": f"bucket[{h1_val}].append({key})", "vars": {"h1": h1_val, "key": key}, "highlight_bucket": h1_val})
        steps.append({"line": 4, "text": "RETURN success", "vars": {}, "highlight_bucket": h1_val})
        return steps

    # OPEN ADDRESSING: line mapping
    if mode == 'double':
        # Lines per get_pseudocode for double hashing
        # 1 FUNC, 2 h1, 3 h2, 4 i=0, 5 while, 6 idx, 7 if, 8 assign, 9 return success, 10 i++, 11 return full
        h2_val, _ = h2_fn(abs(nk_val), m)
        steps.append({"line": 1, "text": f"FUNCTION Insert({key}, {m})", "vars": {"key": key, "m": m}, "highlight_bucket": None})
        steps.append({"line": 2, "text": f"h1 = hash(key) % m = {h1_val}", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
        steps.append({"line": 3, "text": f"h2 = 1 + (hash(key) % (m-1)) = {h2_val}", "vars": {"h2": h2_val}, "highlight_bucket": None})
        steps.append({"line": 4, "text": "i = 0", "vars": {"i": 0}, "highlight_bucket": None})
        while_line, idx_line, if_line, assign_line, ret_ok_line, incr_line, ret_full_line = 5, 6, 7, 8, 9, 10, 11
    else:
        # linear and quadratic share mapping
        # 1 FUNC, 2 h1, 3 i=0, 4 while, 5 idx, 6 if, 7 assign, 8 return success, 9 i++, 10 return full
        steps.append({"line": 1, "text": f"FUNCTION Insert({key}, {m})", "vars": {"key": key, "m": m}, "highlight_bucket": None})
        steps.append({"line": 2, "text": f"h1 = hash(key) % m = {h1_val}", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
        steps.append({"line": 3, "text": "i = 0", "vars": {"i": 0}, "highlight_bucket": None})
        while_line, idx_line, if_line, assign_line, ret_ok_line, incr_line, ret_full_line = 4, 5, 6, 7, 8, 9, 10

    # If table already full, immediately show full path without probing
    if table.count >= table.size:
        steps.append({"line": while_line, "text": f"Checking: i (0) < m ({m}) → False", "vars": {"i": 0, "m": m}, "highlight_bucket": None})
        steps.append({"line": ret_full_line, "text": "RETURN table_full", "vars": {}, "highlight_bucket": None})
        return steps

    # Simulate probing loop using actual table contents
    first_tombstone = None
    for i in range(m):
        # WHILE check
        steps.append({"line": while_line, "text": f"Checking: i ({i}) < m ({m}) → True", "vars": {"i": i, "m": m}, "highlight_bucket": None})

        # Compute index per mode
        if mode == 'linear':
            idx = (h1_val + i) % m
            idx_text = f"idx = (h1 + i) % m = {idx}"
        elif mode == 'quadratic':
            idx = (h1_val + i*i) % m
            idx_text = f"idx = (h1 + i^2) % m = {idx}"
        else:  # double
            step = (h2_val or 1)
            idx = (h1_val + i * step) % m
            idx_text = f"idx = (h1 + i*h2) % m = {idx}"

        steps.append({"line": idx_line, "text": idx_text, "vars": {"idx": idx, "i": i, "h1": h1_val}, "highlight_bucket": idx})

        # Inspect slot
        slot_val = table.table[idx]
        if slot_val is None or slot_val is TOMBSTONE:
            # Track first tombstone if we haven't seen one yet
            if first_tombstone is None and slot_val is TOMBSTONE:
                first_tombstone = idx
                # Show that we found a tombstone but will keep probing
                steps.append({"line": if_line, "text": f"bucket[{idx}] is TOMBSTONE (reusable, but continue probing)", "vars": {"idx": idx}, "highlight_bucket": idx})
                steps.append({"line": incr_line, "text": f"i = {i} + 1", "vars": {"i": i + 1}, "highlight_bucket": None})
                continue
            
            # Found truly empty slot or we're at a tombstone and continuing
            if slot_val is None:
                steps.append({"line": if_line, "text": f"bucket[{idx}] is EMPTY → True", "vars": {"idx": idx}, "highlight_bucket": idx})
            else:
                steps.append({"line": if_line, "text": f"bucket[{idx}] is TOMBSTONE → reusable", "vars": {"idx": idx}, "highlight_bucket": idx})
            
            dest = first_tombstone if first_tombstone is not None else idx
            steps.append({"line": assign_line, "text": f"bucket[{dest}] = {key}", "vars": {"idx": dest, "key": key}, "highlight_bucket": dest})
            steps.append({"line": ret_ok_line, "text": "RETURN success", "vars": {"idx": dest}, "highlight_bucket": dest})
            return steps
        else:
            # Occupied
            occ_text = f"bucket[{idx}] is OCCUPIED → False"
            steps.append({"line": if_line, "text": occ_text, "vars": {"idx": idx}, "highlight_bucket": idx})
            # Increment i
            steps.append({"line": incr_line, "text": f"i = {i} + 1", "vars": {"i": i + 1}, "highlight_bucket": None})

    # If loop completes without insertion → table full
    steps.append({"line": while_line, "text": f"Checking: i ({m}) < m ({m}) → False", "vars": {"i": m, "m": m}, "highlight_bucket": None})
    steps.append({"line": ret_full_line, "text": "RETURN table_full", "vars": {}, "highlight_bucket": None})
    return steps


def build_delete_steps(table, key):
    """Build detailed execution steps for delete operation based on current table contents."""
    steps = []
    mode = table.mode
    m = table.size
    nk_val, _ = normalize_key(key)
    h1_val, _ = h1_fn(abs(nk_val), m)

    # CHAINING
    if mode == 'chaining':
        steps.append({"line": 1, "text": f"FUNCTION Delete({key}, {m})", "vars": {"key": key, "m": m}, "highlight_bucket": None})
        steps.append({"line": 2, "text": f"h1 = hash(key) % m = {h1_val}", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
        steps.append({"line": 3, "text": f"node = bucket[{h1_val}]", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
        
        # Traverse chain
        current = table.table[h1_val]
        found = False
        chain_pos = 0
        while current:
            steps.append({"line": 4, "text": f"Checking: node is not NULL → True (pos {chain_pos})", "vars": {"chain_pos": chain_pos}, "highlight_bucket": h1_val})
            if current.key == key:
                steps.append({"line": 5, "text": f"node.key ({current.key}) == key ({key}) → True", "vars": {"key": key}, "highlight_bucket": h1_val})
                steps.append({"line": 6, "text": f"Remove node from chain at bucket[{h1_val}]", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
                steps.append({"line": 7, "text": "RETURN success", "vars": {}, "highlight_bucket": h1_val})
                found = True
                break
            steps.append({"line": 5, "text": f"node.key ({current.key}) == key ({key}) → False", "vars": {}, "highlight_bucket": h1_val})
            steps.append({"line": 8, "text": "node = node.next", "vars": {}, "highlight_bucket": h1_val})
            current = current.next
            chain_pos += 1
        
        if not found:
            steps.append({"line": 4, "text": "Checking: node is not NULL → False", "vars": {}, "highlight_bucket": h1_val})
            steps.append({"line": 9, "text": "RETURN not_found", "vars": {}, "highlight_bucket": None})
        return steps

    # OPEN ADDRESSING
    if mode == 'double':
        h2_val, _ = h2_fn(abs(nk_val), m)
        steps.append({"line": 1, "text": f"FUNCTION Delete({key}, {m})", "vars": {"key": key, "m": m}, "highlight_bucket": None})
        steps.append({"line": 2, "text": f"h1 = hash(key) % m = {h1_val}", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
        steps.append({"line": 3, "text": f"h2 = 1 + (hash(key) % (m-1)) = {h2_val}", "vars": {"h2": h2_val}, "highlight_bucket": None})
        steps.append({"line": 4, "text": "i = 0", "vars": {"i": 0}, "highlight_bucket": None})
        while_line, idx_line, if_empty_line, if_match_line, assign_line, ret_ok_line, incr_line, ret_nf_line = 5, 6, 7, 8, 9, 10, 11, 12
    else:
        steps.append({"line": 1, "text": f"FUNCTION Delete({key}, {m})", "vars": {"key": key, "m": m}, "highlight_bucket": None})
        steps.append({"line": 2, "text": f"h1 = hash(key) % m = {h1_val}", "vars": {"h1": h1_val}, "highlight_bucket": h1_val})
        steps.append({"line": 3, "text": "i = 0", "vars": {"i": 0}, "highlight_bucket": None})
        while_line, idx_line, if_empty_line, if_match_line, assign_line, ret_ok_line, incr_line, ret_nf_line = 4, 5, 6, 7, 8, 9, 10, 11

    # Probe loop
    for i in range(m):
        steps.append({"line": while_line, "text": f"Checking: i ({i}) < m ({m}) → True", "vars": {"i": i, "m": m}, "highlight_bucket": None})
        
        if mode == 'linear':
            idx = (h1_val + i) % m
            idx_text = f"idx = (h1 + i) % m = {idx}"
        elif mode == 'quadratic':
            idx = (h1_val + i*i) % m
            idx_text = f"idx = (h1 + i²) % m = {idx}"
        else:  # double
            step = h2_val or 1
            idx = (h1_val + i * step) % m
            idx_text = f"idx = (h1 + i*h2) % m = {idx}"
        
        steps.append({"line": idx_line, "text": idx_text, "vars": {"idx": idx, "i": i}, "highlight_bucket": idx})
        
        slot_val = table.table[idx]
        if slot_val is None:
            steps.append({"line": if_empty_line, "text": f"bucket[{idx}] is EMPTY → True", "vars": {"idx": idx}, "highlight_bucket": idx})
            steps.append({"line": ret_nf_line, "text": "RETURN not_found", "vars": {}, "highlight_bucket": None})
            return steps
        
        steps.append({"line": if_empty_line, "text": f"bucket[{idx}] is EMPTY → False", "vars": {"idx": idx}, "highlight_bucket": idx})
        
        if slot_val != TOMBSTONE and slot_val == key:
            steps.append({"line": if_match_line, "text": f"bucket[{idx}] ({slot_val}) == key ({key}) → True", "vars": {"idx": idx, "key": key}, "highlight_bucket": idx})
            steps.append({"line": assign_line, "text": f"bucket[{idx}] = TOMBSTONE", "vars": {"idx": idx}, "highlight_bucket": idx})
            steps.append({"line": ret_ok_line, "text": "RETURN success", "vars": {}, "highlight_bucket": idx})
            return steps
        
        steps.append({"line": if_match_line, "text": f"bucket[{idx}] ({slot_val if slot_val!=TOMBSTONE else 'TOMBSTONE'}) == key ({key}) → False", "vars": {"idx": idx}, "highlight_bucket": idx})
        steps.append({"line": incr_line, "text": f"i = {i} + 1", "vars": {"i": i+1}, "highlight_bucket": None})
    
    steps.append({"line": while_line, "text": f"Checking: i ({m}) < m ({m}) → False", "vars": {"i": m, "m": m}, "highlight_bucket": None})
    steps.append({"line": ret_nf_line, "text": "RETURN not_found", "vars": {}, "highlight_bucket": None})
    return steps


def build_search_steps(table, key):
    """Build step-by-step execution for search operation"""
    steps = []
    mode = table.mode
    m = table.size
    
    if mode == 'chaining':
        # Chaining search pseudocode lines: 1=func, 2=idx, 3=node, 4=while, 5=if, 6=return found, 7=node=next, 8=return not_found
        steps.append({"line": 1, "text": f"SEARCH(key={key})", "vars": {"key": key}, "highlight_bucket": None})
        
        # Compute h1 using the same helpers used elsewhere
        nk_val, _ = normalize_key(key)
        h1_val, _ = h1_fn(abs(nk_val), m)
        idx = h1_val
        steps.append({"line": 2, "text": f"idx = h1(key) % m = {idx}", "vars": {"idx": idx, "key": key, "m": m}, "highlight_bucket": idx})
        
        # Traverse the chain
        current = table.table[idx]
        steps.append({"line": 3, "text": f"node = bucket[{idx}].head", "vars": {"idx": idx}, "highlight_bucket": idx})
        
        chain_pos = 0
        while current is not None:
            steps.append({"line": 4, "text": f"node != NULL → True (position {chain_pos})", "vars": {"chain_pos": chain_pos}, "highlight_bucket": idx})
            steps.append({"line": 5, "text": f"node.key ({current.key}) == key ({key}) → {current.key == key}", "vars": {"node_key": current.key, "key": key}, "highlight_bucket": idx})
            
            if current.key == key:
                steps.append({"line": 6, "text": f"RETURN found at index {idx}, position {chain_pos}", "vars": {"idx": idx, "chain_pos": chain_pos}, "highlight_bucket": idx})
                return steps
            
            steps.append({"line": 7, "text": "node = node.next", "vars": {"chain_pos": chain_pos + 1}, "highlight_bucket": idx})
            current = current.next
            chain_pos += 1
        
        steps.append({"line": 4, "text": "node != NULL → False", "vars": {}, "highlight_bucket": idx})
        steps.append({"line": 8, "text": "RETURN not_found", "vars": {}, "highlight_bucket": None})
        return steps
    
    else:
        # Open addressing search
        # Compute hashes consistently with insert/delete
        nk_val, _ = normalize_key(key)
        h1_val, _ = h1_fn(abs(nk_val), m)
        h2_val, _ = (h2_fn(abs(nk_val), m) if mode == 'double' else (None, None))
        
        if mode == 'double':
            # Double hashing: 1=func, 2=h1, 3=h2, 4=i=0, 5=while, 6=idx, 7=if empty, 8=return not_found, 9=if match, 10=return found, 11=i++, 12=return not_found
            steps.append({"line": 1, "text": f"SEARCH(key={key})", "vars": {"key": key}, "highlight_bucket": None})
            steps.append({"line": 2, "text": f"h1 = hash1(key) % m = {h1_val}", "vars": {"h1": h1_val, "key": key, "m": m}, "highlight_bucket": None})
            steps.append({"line": 3, "text": f"h2 = hash2(key) = {h2_val}", "vars": {"h2": h2_val, "key": key}, "highlight_bucket": None})
            steps.append({"line": 4, "text": "i = 0", "vars": {"i": 0}, "highlight_bucket": None})
            while_line, idx_line, if_empty_line, ret_nf1_line, if_match_line, ret_found_line, incr_line, ret_nf2_line = 5, 6, 7, 8, 9, 10, 11, 12
        else:
            # Linear/Quadratic: 1=func, 2=h1, 3=i=0, 4=while, 5=idx, 6=if empty, 7=return not_found, 8=if match, 9=return found, 10=i++, 11=return not_found
            steps.append({"line": 1, "text": f"SEARCH(key={key})", "vars": {"key": key}, "highlight_bucket": None})
            steps.append({"line": 2, "text": f"h1 = hash1(key) % m = {h1_val}", "vars": {"h1": h1_val, "key": key, "m": m}, "highlight_bucket": None})
            steps.append({"line": 3, "text": "i = 0", "vars": {"i": 0}, "highlight_bucket": None})
            while_line, idx_line, if_empty_line, ret_nf1_line, if_match_line, ret_found_line, incr_line, ret_nf2_line = 4, 5, 6, 7, 8, 9, 10, 11
        
        # Probing loop
        for i in range(m):
            steps.append({"line": while_line, "text": f"Checking: i ({i}) < m ({m}) → True", "vars": {"i": i, "m": m}, "highlight_bucket": None})
            
            if mode == 'linear':
                idx = (h1_val + i) % m
                idx_text = f"idx = (h1 + i) % m = {idx}"
            elif mode == 'quadratic':
                idx = (h1_val + i*i) % m
                idx_text = f"idx = (h1 + i²) % m = {idx}"
            else:  # double
                step = h2_val or 1
                idx = (h1_val + i * step) % m
                idx_text = f"idx = (h1 + i*h2) % m = {idx}"
            
            steps.append({"line": idx_line, "text": idx_text, "vars": {"idx": idx, "i": i}, "highlight_bucket": idx})
            
            slot_val = table.table[idx]
            if slot_val is None:
                steps.append({"line": if_empty_line, "text": f"bucket[{idx}] is EMPTY → True", "vars": {"idx": idx}, "highlight_bucket": idx})
                steps.append({"line": ret_nf1_line, "text": "RETURN not_found", "vars": {}, "highlight_bucket": None})
                return steps
            
            steps.append({"line": if_empty_line, "text": f"bucket[{idx}] is EMPTY → False", "vars": {"idx": idx}, "highlight_bucket": idx})
            
            if slot_val != TOMBSTONE and slot_val == key:
                steps.append({"line": if_match_line, "text": f"bucket[{idx}] ({slot_val}) == key ({key}) → True", "vars": {"idx": idx, "key": key}, "highlight_bucket": idx})
                steps.append({"line": ret_found_line, "text": f"RETURN found at index {idx}", "vars": {"idx": idx}, "highlight_bucket": idx})
                return steps
            
            steps.append({"line": if_match_line, "text": f"bucket[{idx}] ({slot_val if slot_val!=TOMBSTONE else 'TOMBSTONE'}) == key ({key}) → False", "vars": {"idx": idx}, "highlight_bucket": idx})
            steps.append({"line": incr_line, "text": f"i = {i} + 1", "vars": {"i": i+1}, "highlight_bucket": None})
        
        steps.append({"line": while_line, "text": f"Checking: i ({m}) < m ({m}) → False", "vars": {"i": m, "m": m}, "highlight_bucket": None})
        steps.append({"line": ret_nf2_line, "text": "RETURN not_found", "vars": {}, "highlight_bucket": None})
        return steps


@app.route('/api/create', methods=['POST'])
def create_table():
    """Create a new hash table"""
    global current_id
    data = request.json
    size = data.get('size', 10)
    mode = data.get('mode', 'chaining')
    
    if size < 1 or size > 100:
        return jsonify({'error': 'Size must be between 1 and 100'}), 400
    
    table_id = f"table_{current_id}"
    current_id += 1
    
    hash_tables[table_id] = HashTable(size=size, mode=mode)
    
    return jsonify({
        'table_id': table_id,
        'state': get_table_state(hash_tables[table_id]),
        'message': f'Created hash table with size {size} and mode {mode}'
    })


@app.route('/api/<table_id>/insert', methods=['POST'])
def insert_key(table_id):
    """Insert a key into the hash table"""
    if table_id not in hash_tables:
        return jsonify({'error': 'Table not found'}), 404
    
    data = request.json
    key = data.get('key')
    
    if key is None:
        return jsonify({'error': 'Key is required'}), 400
    
    # Try to convert to int
    try:
        key = int(key)
    except (ValueError, TypeError):
        pass
    
    table = hash_tables[table_id]
    
    # Build steps before insertion
    steps = build_insert_steps(table, key)
    
    # Perform insertion
    success, index, collision, message = table.insert(key)
    
    # Get pseudocode based on mode
    pseudocode = get_pseudocode(table.mode, 'insert')
    
    return jsonify({
        'success': success,
        'index': index,
        'collision': collision,
        'message': message,
        'state': get_table_state(table),
        'steps': steps,
        'pseudocode': pseudocode
    })


@app.route('/api/<table_id>/search', methods=['POST'])
def search_key(table_id):
    """Search for a key in the hash table"""
    if table_id not in hash_tables:
        return jsonify({'error': 'Table not found'}), 404
    
    data = request.json
    key = data.get('key')
    
    if key is None:
        return jsonify({'error': 'Key is required'}), 400
    
    try:
        key = int(key)
    except (ValueError, TypeError):
        pass
    
    table = hash_tables[table_id]
    
    # Build steps before search
    steps = build_search_steps(table, key)
    
    # Perform search
    found, index, message = table.search(key)
    
    # Get pseudocode based on mode
    pseudocode = get_pseudocode(table.mode, 'search')
    
    return jsonify({
        'found': found,
        'index': index,
        'message': message,
        'state': get_table_state(table),
        'steps': steps,
        'pseudocode': pseudocode
    })


@app.route('/api/<table_id>/delete', methods=['POST'])
def delete_key(table_id):
    """Delete a key from the hash table"""
    if table_id not in hash_tables:
        return jsonify({'error': 'Table not found'}), 404
    
    data = request.json
    key = data.get('key')
    
    if key is None:
        return jsonify({'error': 'Key is required'}), 400
    
    try:
        key = int(key)
    except (ValueError, TypeError):
        pass
    
    table = hash_tables[table_id]
    
    # Build steps before deletion
    steps = build_delete_steps(table, key)
    
    # Perform deletion
    success, index, message = table.delete(key)
    
    # Get pseudocode based on mode
    pseudocode = get_pseudocode(table.mode, 'delete')
    
    return jsonify({
        'success': success,
        'index': index,
        'message': message,
        'state': get_table_state(table),
        'steps': steps,
        'pseudocode': pseudocode
    })


@app.route('/api/<table_id>/resize', methods=['POST'])
def resize_table(table_id):
    """Resize the hash table"""
    if table_id not in hash_tables:
        return jsonify({'error': 'Table not found'}), 404
    
    data = request.json
    new_size = data.get('new_size')
    
    if not new_size or new_size < 1 or new_size > 100:
        return jsonify({'error': 'New size must be between 1 and 100'}), 400
    
    table = hash_tables[table_id]
    message = table.resize(new_size)
    
    return jsonify({
        'message': message,
        'state': get_table_state(table)
    })


@app.route('/api/<table_id>/clear', methods=['POST'])
def clear_table(table_id):
    """Clear the hash table"""
    if table_id not in hash_tables:
        return jsonify({'error': 'Table not found'}), 404
    
    table = hash_tables[table_id]
    table.clear()
    
    return jsonify({
        'message': 'Table cleared',
        'state': get_table_state(table)
    })


@app.route('/api/<table_id>/state', methods=['GET'])
def get_state(table_id):
    """Get current state of hash table"""
    if table_id not in hash_tables:
        return jsonify({'error': 'Table not found'}), 404
    
    return jsonify({
        'state': get_table_state(hash_tables[table_id])
    })


def get_pseudocode(mode, operation='insert'):
    """Get pseudocode for the operation"""
    if operation == 'insert':
        if mode == 'chaining':
            return [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  bucket[h1].append(key)",
                "  RETURN success"
            ]
        elif mode == 'linear':
            return [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i) % m",
                "    IF bucket[idx] is EMPTY:",
                "      bucket[idx] = key",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN table_full"
            ]
        elif mode == 'quadratic':
            return [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i²) % m",
                "    IF bucket[idx] is EMPTY:",
                "      bucket[idx] = key",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN table_full"
            ]
        else:  # double
            return [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  h2 = 1 + (hash(key) % (m-1))",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i*h2) % m",
                "    IF bucket[idx] is EMPTY:",
                "      bucket[idx] = key",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN table_full"
            ]
    elif operation == 'delete':
        if mode == 'chaining':
            return [
                "FUNCTION Delete(key, m):",
                "  h1 = hash(key) % m",
                "  node = bucket[h1]",
                "  WHILE node is not NULL:",
                "    IF node.key == key:",
                "      remove node from chain",
                "      RETURN success",
                "    node = node.next",
                "  RETURN not_found"
            ]
        elif mode == 'linear':
            return [
                "FUNCTION Delete(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i) % m",
                "    IF bucket[idx] is EMPTY:",
                "      RETURN not_found",
                "    IF bucket[idx] == key:",
                "      bucket[idx] = TOMBSTONE",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN not_found"
            ]
        elif mode == 'quadratic':
            return [
                "FUNCTION Delete(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i²) % m",
                "    IF bucket[idx] is EMPTY:",
                "      RETURN not_found",
                "    IF bucket[idx] == key:",
                "      bucket[idx] = TOMBSTONE",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN not_found"
            ]
        else:  # double
            return [
                "FUNCTION Delete(key, m):",
                "  h1 = hash(key) % m",
                "  h2 = 1 + (hash(key) % (m-1))",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i*h2) % m",
                "    IF bucket[idx] is EMPTY:",
                "      RETURN not_found",
                "    IF bucket[idx] == key:",
                "      bucket[idx] = TOMBSTONE",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN not_found"
            ]
    elif operation == 'search':
        if mode == 'chaining':
            return [
                "FUNCTION Search(key, m):",
                "  idx = hash(key) % m",
                "  node = bucket[idx]",
                "  WHILE node is not NULL:",
                "    IF node.key == key:",
                "      RETURN found",
                "    node = node.next",
                "  RETURN not_found"
            ]
        elif mode == 'linear':
            return [
                "FUNCTION Search(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i) % m",
                "    IF bucket[idx] is EMPTY:",
                "      RETURN not_found",
                "    IF bucket[idx] == key:",
                "      RETURN found",
                "    i = i + 1",
                "  RETURN not_found"
            ]
        elif mode == 'quadratic':
            return [
                "FUNCTION Search(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i²) % m",
                "    IF bucket[idx] is EMPTY:",
                "      RETURN not_found",
                "    IF bucket[idx] == key:",
                "      RETURN found",
                "    i = i + 1",
                "  RETURN not_found"
            ]
        else:  # double
            return [
                "FUNCTION Search(key, m):",
                "  h1 = hash(key) % m",
                "  h2 = 1 + (hash(key) % (m-1))",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i*h2) % m",
                "    IF bucket[idx] is EMPTY:",
                "      RETURN not_found",
                "    IF bucket[idx] == key:",
                "      RETURN found",
                "    i = i + 1",
                "  RETURN not_found"
            ]
    return []


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'tables': len(hash_tables)})


@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        'message': 'Hash Table Simulator API',
        'version': '1.0.0',
        'endpoints': {
            'POST /api/create': 'Create a new hash table',
            'POST /api/<table_id>/insert': 'Insert a key',
            'POST /api/<table_id>/search': 'Search for a key',
            'POST /api/<table_id>/delete': 'Delete a key',
            'POST /api/<table_id>/resize': 'Resize the table',
            'POST /api/<table_id>/clear': 'Clear the table',
            'GET /api/<table_id>/state': 'Get table state',
            'GET /api/health': 'Health check'
        }
    })


# For Vercel serverless functions
if __name__ == '__main__':
    app.run(debug=True, port=5000)
