"""
Demo Examples for Hash Table Simulator

This script demonstrates various use cases and operations of the hash table
implementation with different collision handling techniques.

Author: Hash Table Simulator
Date: October 25, 2025
"""

from hash_table import HashTable


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "="*70)
    print(f" {title}")
    print("="*70 + "\n")


def demo_basic_operations():
    """Demonstrate basic hash table operations."""
    print_section("DEMO 1: Basic Operations with Chaining")
    
    # Create hash table
    ht = HashTable(size=5, mode='chaining')
    print(f"Created hash table: {ht}\n")
    
    # Insert keys
    print("Inserting keys: 10, 15, 20, 25, 30, 35...")
    keys = [10, 15, 20, 25, 30, 35]
    for key in keys:
        success, index, collision, message = ht.insert(key)
        print(f"  {message}")
    
    # Display table
    ht.display_console()
    
    # Search for keys
    print("Searching for keys...")
    for key in [15, 100]:
        found, index, message = ht.search(key)
        print(f"  {message}")
    
    print()
    
    # Delete a key
    print("Deleting key: 20")
    success, index, message = ht.delete(20)
    print(f"  {message}")
    
    ht.display_console()


def demo_collision_comparison():
    """Compare different collision handling techniques."""
    print_section("DEMO 2: Collision Handling Comparison")
    
    keys = [12, 22, 32, 42, 13, 23]
    size = 10
    
    # Chaining
    print("--- CHAINING MODE ---")
    ht_chain = HashTable(size=size, mode='chaining')
    for key in keys:
        ht_chain.insert(key)
    ht_chain.display_console()
    
    # Linear Probing
    print("--- LINEAR PROBING MODE ---")
    ht_linear = HashTable(size=size, mode='linear')
    for key in keys:
        success, index, collision, message = ht_linear.insert(key)
        if collision:
            print(f"  ⚠️  {message}")
    ht_linear.display_console()
    
    # Quadratic Probing
    print("--- QUADRATIC PROBING MODE ---")
    ht_quad = HashTable(size=size, mode='quadratic')
    for key in keys:
        success, index, collision, message = ht_quad.insert(key)
        if collision:
            print(f"  ⚠️  {message}")
    ht_quad.display_console()


def demo_string_keys():
    """Demonstrate hash table with string keys."""
    print_section("DEMO 3: String Keys with Chaining")
    
    ht = HashTable(size=7, mode='chaining')
    
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    
    print("Inserting names...")
    for name in names:
        success, index, collision, message = ht.insert(name)
        print(f"  {message} (hash value: {ht.hash_function(name)})")
    
    ht.display_console()
    
    # Search for specific names
    print("Searching for 'Charlie' and 'Zara'...")
    for name in ["Charlie", "Zara"]:
        found, index, message = ht.search(name)
        print(f"  {message}")


def demo_load_factor_and_resize():
    """Demonstrate load factor monitoring and resizing."""
    print_section("DEMO 4: Load Factor and Resizing")
    
    ht = HashTable(size=5, mode='linear')
    
    print("Starting with size 5, inserting keys one by one...\n")
    
    keys = [10, 20, 30, 40, 50, 60, 70]
    
    for key in keys:
        success, index, collision, message = ht.insert(key)
        
        if success:
            load_factor = ht.get_load_factor()
            print(f"Inserted {key} -> Load Factor: {load_factor:.2f}", end="")
            
            if load_factor >= 0.8:
                print(" ⚠️  HIGH!")
            elif load_factor >= 0.5:
                print(" ⚠️  MODERATE")
            else:
                print(" ✅ OK")
        else:
            print(f"Failed to insert {key}: {message}")
            break
    
    print("\nCurrent state:")
    ht.display_console()
    
    # Resize
    print("Resizing table to size 11...")
    message = ht.resize(11)
    print(f"  {message}")
    print(f"  New load factor: {ht.get_load_factor():.2f}")
    
    ht.display_console()


def demo_mixed_operations():
    """Demonstrate a mix of operations."""
    print_section("DEMO 5: Mixed Operations Workflow")
    
    ht = HashTable(size=8, mode='chaining')
    
    print("Step 1: Insert initial keys")
    initial_keys = [15, 23, 8, 42, 16, 31]
    for key in initial_keys:
        ht.insert(key)
    ht.display_console()
    
    print("Step 2: Show all keys")
    all_keys = ht.get_all_keys()
    print(f"All keys: {', '.join([str(k) for k in all_keys])}\n")
    
    print("Step 3: Delete some keys")
    for key in [8, 16]:
        success, index, message = ht.delete(key)
        print(f"  {message}")
    ht.display_console()
    
    print("Step 4: Insert more keys")
    for key in [100, 200]:
        ht.insert(key)
    ht.display_console()
    
    print("Step 5: Search for various keys")
    for key in [23, 8, 100]:
        found, index, message = ht.search(key)
        print(f"  {message}")


def demo_quadratic_probing_detail():
    """Detailed demonstration of quadratic probing."""
    print_section("DEMO 6: Quadratic Probing in Detail")
    
    ht = HashTable(size=11, mode='quadratic')
    
    # Keys that will cause collisions
    keys = [22, 33, 44, 55, 66]  # All hash to 0 in size 11
    
    print("Inserting keys that hash to the same index:")
    print("(These keys will demonstrate quadratic probing)\n")
    
    for key in keys:
        hash_val = ht.hash_function(key)
        print(f"Key {key}: hash = {hash_val}")
        success, index, collision, message = ht.insert(key)
        print(f"  {message}\n")
    
    ht.display_console()
    
    print("Collision log:")
    for i, collision_info in enumerate(ht.collision_log, 1):
        print(f"  {i}. Key {collision_info['key']}: "
              f"Original index {collision_info['original_index']} → "
              f"Final index {collision_info['final_index']} "
              f"({collision_info['probes']} probes)")


def demo_edge_cases():
    """Demonstrate edge cases and error handling."""
    print_section("DEMO 7: Edge Cases")
    
    # Small table with linear probing
    print("Creating small table (size=3) with linear probing...")
    ht = HashTable(size=3, mode='linear')
    
    print("\nInserting 4 keys into 3-bucket table:")
    for key in [10, 20, 30, 40]:
        success, index, collision, message = ht.insert(key)
        print(f"  {message}")
    
    ht.display_console()
    
    # Duplicate insertion
    print("Attempting to insert duplicate key (20):")
    success, index, collision, message = ht.insert(20)
    print(f"  {message}\n")
    
    # Delete and reinsert
    print("Delete key 20 and insert key 40:")
    ht.delete(20)
    success, index, collision, message = ht.insert(40)
    print(f"  {message}")
    
    ht.display_console()


def run_all_demos():
    """Run all demonstration examples."""
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#" + " "*15 + "HASH TABLE SIMULATOR - DEMO EXAMPLES" + " "*17 + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    def demo_double_hashing_and_tombstones():
        """Demonstrate double hashing probe sequence and tombstone behavior."""
        print_section("DEMO 8: Double Hashing and Tombstones")
        ht = HashTable(size=7, mode='double')
        keys = [10, 24, 31]
        for k in keys:
            ok, idx, coll, msg = ht.insert(k)
            print(" ", msg)
        ht.display_console()
        print("Deleting 10 to create tombstone...")
        ok, idx, msg = ht.delete(10)
        print(" ", msg)
        ht.display_console()
        print("Re-inserting 38 to reuse tombstone if available...")
        ok, idx, coll, msg = ht.insert(38)
        print(" ", msg)
        ht.display_console()

    demos = [
        demo_basic_operations,
        demo_collision_comparison,
        demo_string_keys,
        demo_load_factor_and_resize,
        demo_mixed_operations,
        demo_quadratic_probing_detail,
        demo_edge_cases,
        demo_double_hashing_and_tombstones
    ]
    
    for i, demo in enumerate(demos, 1):
        try:
            demo()
            
            if i < len(demos):
                input("\n>>> Press Enter to continue to next demo...")
        except Exception as e:
            print(f"\n❌ Error in demo: {e}")
            continue
    
    print("\n" + "#"*70)
    print("#" + " "*20 + "ALL DEMOS COMPLETED!" + " "*27 + "#")
    print("#"*70 + "\n")


if __name__ == "__main__":
    run_all_demos()
