"""
Hash Table Implementation with Multiple Collision Handling Techniques

This module provides a comprehensive hash table implementation supporting:
- Chaining (linked list in each bucket)
- Open Addressing with Linear Probing
- Open Addressing with Quadratic Probing
- Open Addressing with Double Hashing

Includes optional tracing hooks for UI/console pseudocode and collision steps.

Author: Hash Table Simulator
Date: October 25, 2025
"""


from typing import Optional, Any, Callable
from utils import normalize_key, hash1 as h1_fn, hash2 as h2_fn


TOMBSTONE = object()


class Node:
    """
    Node class for linked list used in chaining collision resolution.
    
    Attributes:
        key: The key stored in this node
        next: Reference to the next node in the chain
    """
    def __init__(self, key):
        self.key = key
        self.next: Optional['Node'] = None


class HashTable:
    """
    A hash table implementation with configurable collision handling.
    
    Supports three collision resolution strategies:
    - 'chaining': Uses linked lists in each bucket
    - 'linear': Open addressing with linear probing
    - 'quadratic': Open addressing with quadratic probing
    
    Attributes:
        size (int): Number of buckets in the hash table
        table (list): The actual hash table storage
        mode (str): Collision handling mode
        count (int): Number of elements currently stored
        collision_log (list): Log of collision events for visualization
    """
    
    def __init__(self, size=10, mode='chaining', c1: int = 1, c2: int = 3):
        """
        Initialize a new hash table.
        
        Args:
            size (int): Number of buckets (default: 10)
            mode (str): Collision handling mode - 'chaining', 'linear', 'quadratic', 'double'
        """
        self.size = size
        self.mode = mode
        self.count = 0
        self.collision_log: list = []
        self.c1 = c1
        self.c2 = c2
        
        # Initialize table based on mode
        self.table: list[Any] = [None] * size  # Holds Node, key, TOMBSTONE, or None
    
    def hash_function(self, key):
        """
        Simple hash function using modulo operation.
        
        Converts string keys to integers using hash() built-in,
        then applies modulo to fit within table size.
        
        Args:
            key: The key to hash (int or str)
            
        Returns:
            int: Hash value (index) in range [0, size-1]
        """
        num, _ = normalize_key(key)
        return abs(num) % self.size

    def _compute_hashes(self, key):
        """Compute h1 (and h2 for double hashing) with explanations."""
        num, conv_exp = normalize_key(key)
        h1, h1_exp = h1_fn(abs(num), self.size)
        h2, h2_exp = (None, "")
        if self.mode == 'double':
            h2, h2_exp = h2_fn(abs(num), self.size)
        return {
            'num': abs(num),
            'conv': conv_exp,
            'h1': h1,
            'h1_exp': h1_exp,
            'h2': h2,
            'h2_exp': h2_exp,
        }
    
    def get_load_factor(self):
        """
        Calculate the current load factor of the hash table.
        
        Load factor = number of elements / table size
        
        Returns:
            float: Current load factor
        """
        return self.count / self.size
    
    def insert(self, key):
        """
        Insert a key into the hash table using the configured collision handling mode.
        
        Args:
            key: The key to insert (int or str)
            
        Returns:
            tuple: (success: bool, index: int, collision_occurred: bool, message: str)
        """
        if self.mode == 'chaining':
            return self._insert_chaining(key)
        elif self.mode == 'linear':
            return self._insert_linear_probing(key)
        elif self.mode == 'quadratic':
            return self._insert_quadratic_probing(key)
        elif self.mode == 'double':
            return self._insert_double_hashing(key)
    
    def _insert_chaining(self, key):
        """
        Insert using chaining (linked list) collision resolution.
        
        Args:
            key: The key to insert
            
        Returns:
            tuple: (success, index, collision_occurred, message)
        """
        index = self.hash_function(key)
        collision = False
        
        # Check if bucket is empty
        if self.table[index] is None:
            self.table[index] = Node(key)
            self.count += 1
            message = f"Inserted '{key}' at index {index}"
        else:
            # Collision occurred - check if key already exists
            current = self.table[index]
            collision = True
            
            # Traverse the chain
            while current:
                if current.key == key:
                    return (False, index, False, f"Key '{key}' already exists at index {index}")
                if current.next is None:
                    break
                current = current.next
            
            # Add to end of chain
            current.next = Node(key)
            self.count += 1
            message = f"Collision! Inserted '{key}' at index {index} (chained)"
        
        # Log collision for visualization
        if collision:
            self.collision_log.append({
                'key': key,
                'index': index,
                'type': 'chaining'
            })
        
        return (True, index, collision, message)
    
    def _insert_linear_probing(self, key):
        """
        Insert using linear probing collision resolution.
        
        Args:
            key: The key to insert
            
        Returns:
            tuple: (success, index, collision_occurred, message)
        """
        index = self.hash_function(key)
        original_index = index
        collision = False
        probes = 0
        
        # Check if table is full
        if self.count >= self.size:
            return (False, -1, False, "Hash table is full!")
        
        # Linear probing: try index, index+1, index+2, ...
        first_tombstone = None
        while self.table[index] is not None:
            if self.table[index] != TOMBSTONE and self.table[index] == key:
                return (False, index, False, f"Key '{key}' already exists at index {index}")
            
            # Track first tombstone encountered
            if first_tombstone is None and self.table[index] is TOMBSTONE:
                first_tombstone = index
            
            collision = True
            probes += 1
            index = (original_index + probes) % self.size
            
            # Safety check (shouldn't happen if count is correct)
            if probes >= self.size:
                return (False, -1, False, "Could not find empty slot!")
        
        # Found empty or tombstone slot
        target_index = first_tombstone if first_tombstone is not None else index
        self.table[target_index] = key
        self.count += 1
        
        if collision:
            message = f"Collision! Inserted '{key}' at index {index} after {probes} probe(s)"
            self.collision_log.append({
                'key': key,
                'original_index': original_index,
                'final_index': target_index,
                'probes': probes,
                'type': 'linear'
            })
        else:
            message = f"Inserted '{key}' at index {target_index}"
        
        return (True, target_index, collision, message)
    
    def _insert_quadratic_probing(self, key):
        """
        Insert using quadratic probing collision resolution.
        
        Args:
            key: The key to insert
            
        Returns:
            tuple: (success, index, collision_occurred, message)
        """
        index = self.hash_function(key)
        original_index = index
        collision = False
        probes = 0
        
        # Check if table is full
        if self.count >= self.size:
            return (False, -1, False, "Hash table is full!")
        
        # Quadratic probing: try index + 1^2, index + 2^2, index + 3^2, ...
        first_tombstone = None
        while self.table[index] is not None:
            if self.table[index] != TOMBSTONE and self.table[index] == key:
                return (False, index, False, f"Key '{key}' already exists at index {index}")
            
            # Track first tombstone encountered
            if first_tombstone is None and self.table[index] is TOMBSTONE:
                first_tombstone = index
            
            collision = True
            probes += 1
            index = (original_index + probes * probes) % self.size
            
            # Safety check
            if probes >= self.size:
                return (False, -1, False, "Could not find empty slot!")
        
        # Found empty or tombstone slot
        target_index = first_tombstone if first_tombstone is not None else index
        self.table[target_index] = key
        self.count += 1
        
        if collision:
            message = f"Collision! Inserted '{key}' at index {index} after {probes} probe(s) (quadratic)"
            self.collision_log.append({
                'key': key,
                'original_index': original_index,
                'final_index': target_index,
                'probes': probes,
                'type': 'quadratic'
            })
        else:
            message = f"Inserted '{key}' at index {target_index}"
        
        return (True, target_index, collision, message)

    def _insert_double_hashing(self, key):
        """
        Insert using double hashing collision resolution.
        """
        if self.count >= self.size:
            return (False, -1, False, "Hash table is full!")

        hashes = self._compute_hashes(key)
        h1 = hashes['h1']
        h2 = hashes['h2'] or 1
        index = h1
        collision = False
        probes = 0
        first_tombstone = None

        while self.table[index] is not None:
            if self.table[index] != TOMBSTONE and self.table[index] == key:
                return (False, index, False, f"Key '{key}' already exists at index {index}")
            if first_tombstone is None and self.table[index] is TOMBSTONE:
                first_tombstone = index
            collision = True
            probes += 1
            if probes >= self.size:
                return (False, -1, False, "Could not find empty slot!")
            index = (h1 + probes * h2) % self.size

        target_index = first_tombstone if first_tombstone is not None else index
        self.table[target_index] = key
        self.count += 1

        if collision:
            message = (
                f"Collision! Inserted '{key}' at index {target_index} after {probes} probe(s) (double)"
            )
            self.collision_log.append({
                'key': key,
                'original_index': h1,
                'final_index': target_index,
                'probes': probes,
                'h2': h2,
                'type': 'double'
            })
        else:
            message = f"Inserted '{key}' at index {target_index}"

        return (True, target_index, collision, message)
    
    def search(self, key):
        """
        Search for a key in the hash table.
        
        Args:
            key: The key to search for
            
        Returns:
            tuple: (found: bool, index: int, message: str)
        """
        if self.mode == 'chaining':
            return self._search_chaining(key)
        elif self.mode == 'linear':
            return self._search_linear_probing(key)
        elif self.mode == 'quadratic':
            return self._search_quadratic_probing(key)
        elif self.mode == 'double':
            return self._search_double_hashing(key)
    
    def _search_chaining(self, key):
        """Search using chaining."""
        index = self.hash_function(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return (True, index, f"Found '{key}' at index {index}")
            current = current.next
        
        return (False, index, f"Key '{key}' not found")
    
    def _search_linear_probing(self, key):
        """Search using linear probing."""
        index = self.hash_function(key)
        original_index = index
        probes = 0
        
        while self.table[index] is not None and probes < self.size:
            if self.table[index] != TOMBSTONE and self.table[index] == key:
                return (True, index, f"Found '{key}' at index {index}")
            probes += 1
            index = (original_index + probes) % self.size
        
        return (False, -1, f"Key '{key}' not found")
    
    def _search_quadratic_probing(self, key):
        """Search using quadratic probing."""
        index = self.hash_function(key)
        original_index = index
        probes = 0
        
        while self.table[index] is not None and probes < self.size:
            if self.table[index] != TOMBSTONE and self.table[index] == key:
                return (True, index, f"Found '{key}' at index {index}")
            probes += 1
            index = (original_index + probes * probes) % self.size
        
        return (False, -1, f"Key '{key}' not found")

    def _search_double_hashing(self, key):
        hashes = self._compute_hashes(key)
        h1 = hashes['h1']
        h2 = hashes['h2'] or 1
        index = h1
        probes = 0
        while self.table[index] is not None and probes < self.size:
            if self.table[index] != TOMBSTONE and self.table[index] == key:
                return (True, index, f"Found '{key}' at index {index}")
            probes += 1
            index = (h1 + probes * h2) % self.size
        return (False, -1, f"Key '{key}' not found")
    
    def delete(self, key):
        """
        Delete a key from the hash table.
        
        Args:
            key: The key to delete
            
        Returns:
            tuple: (success: bool, index: int, message: str)
        """
        if self.mode == 'chaining':
            return self._delete_chaining(key)
        elif self.mode == 'linear':
            return self._delete_linear_probing(key)
        elif self.mode == 'quadratic':
            return self._delete_quadratic_probing(key)
        elif self.mode == 'double':
            return self._delete_double_hashing(key)
    
    def _delete_chaining(self, key):
        """Delete using chaining."""
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev is None:
                    # Deleting head of chain
                    self.table[index] = current.next
                else:
                    # Deleting middle or end
                    prev.next = current.next
                
                self.count -= 1
                return (True, index, f"Deleted '{key}' from index {index}")
            
            prev = current
            current = current.next
        
        return (False, index, f"Key '{key}' not found")
    
    def _delete_linear_probing(self, key):
        """Delete using linear probing."""
        found, index, _ = self._search_linear_probing(key)
        
        if not found:
            return (False, -1, f"Key '{key}' not found")
        
        # Mark tombstone for robust open addressing
        self.table[index] = TOMBSTONE
        self.count -= 1
        return (True, index, f"Deleted '{key}' from index {index}")
    
    def _delete_quadratic_probing(self, key):
        """Delete using quadratic probing."""
        found, index, _ = self._search_quadratic_probing(key)
        
        if not found:
            return (False, -1, f"Key '{key}' not found")
        
        self.table[index] = TOMBSTONE
        self.count -= 1
        return (True, index, f"Deleted '{key}' from index {index}")

    def _delete_double_hashing(self, key):
        found, index, _ = self._search_double_hashing(key)
        if not found:
            return (False, -1, f"Key '{key}' not found")
        self.table[index] = TOMBSTONE
        self.count -= 1
        return (True, index, f"Deleted '{key}' from index {index}")
    
    def clear(self):
        """Clear all elements from the hash table."""
        if self.mode == 'chaining':
            self.table = [None] * self.size
        else:
            self.table = [None] * self.size
        
        self.count = 0
        self.collision_log = []
    
    def resize(self, new_size):
        """
        Resize the hash table and rehash all elements.
        
        Args:
            new_size (int): New table size
            
        Returns:
            str: Message about the resize operation
        """
        old_table = self.table
        old_size = self.size
        old_mode = self.mode
        
        # Create new table
        self.size = new_size
        self.count = 0
        self.collision_log = []
        
        if self.mode == 'chaining':
            self.table = [None] * new_size
        else:
            self.table = [None] * new_size
        
        # Rehash all elements
        rehashed = 0
        if old_mode == 'chaining':
            for bucket in old_table:
                current = bucket
                while current:
                    self.insert(current.key)
                    rehashed += 1
                    current = current.next
        else:
            for key in old_table:
                if key is not None:
                    self.insert(key)
                    rehashed += 1
        
        return f"Resized from {old_size} to {new_size} buckets. Rehashed {rehashed} keys."
    
    def get_bucket_contents(self, index):
        """
        Get all keys in a specific bucket.
        
        Args:
            index (int): Bucket index
            
        Returns:
            list: List of keys in the bucket
        """
        if index < 0 or index >= self.size:
            return []
        
        if self.mode == 'chaining':
            keys = []
            current = self.table[index]
            while current:
                keys.append(current.key)
                current = current.next
            return keys
        else:
            key = self.table[index]
            if key is TOMBSTONE:
                return []  # Return empty list for tombstone (UI will show "DEL")
            return [key] if key is not None else []
    
    def get_all_keys(self):
        """
        Get all keys currently stored in the hash table.
        
        Returns:
            list: All keys in the table
        """
        keys = []
        
        if self.mode == 'chaining':
            for bucket in self.table:
                current = bucket
                while current:
                    keys.append(current.key)
                    current = current.next
        else:
            for key in self.table:
                if key is not None and key is not TOMBSTONE:
                    keys.append(key)
        
        return keys
    
    def display_console(self):
        """
        Display the hash table in console using ASCII art.
        
        Provides a visual representation of buckets and their contents.
        """
        print("\n" + "="*60)
        print(f"HASH TABLE VISUALIZATION ({self.mode.upper()} mode)")
        print(f"Size: {self.size} | Elements: {self.count} | Load Factor: {self.get_load_factor():.2f}")
        print("="*60)
        
        for i in range(self.size):
            keys = self.get_bucket_contents(i)
            
            if not keys:
                print(f"[{i:2d}] -> [ EMPTY ]")
            elif self.mode == 'chaining':
                chain = " -> ".join([str(k) for k in keys])
                print(f"[{i:2d}] -> {chain}")
            else:
                print(f"[{i:2d}] -> [ {keys[0]} ]")
        
        print("="*60 + "\n")
    
    def __str__(self):
        """String representation of the hash table."""
        return f"HashTable(size={self.size}, mode={self.mode}, count={self.count})"
    
    def __repr__(self):
        """Detailed representation of the hash table."""
        return self.__str__()
