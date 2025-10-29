"""
Test Script for Hash Table Simulator

This script verifies that all components are working correctly.
Run this to ensure everything is set up properly.

Author: Hash Table Simulator
Date: October 25, 2025
"""

import sys


def print_header(text):
    """Print a formatted header."""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)


def test_imports():
    """Test if all required modules can be imported."""
    print_header("TEST 1: Module Imports")
    
    try:
        import hash_table
        print("✅ hash_table.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import hash_table: {e}")
        return False
    
    try:
        import tkinter
        print("✅ tkinter is available (GUI ready)")
    except ImportError:
        print("⚠️  tkinter not available (GUI will not work)")
        print("   Console mode will still work")
    
    try:
        import gui_simulator
        print("✅ gui_simulator.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import gui_simulator: {e}")
        return False
    
    try:
        import console_simulator
        print("✅ console_simulator.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import console_simulator: {e}")
        return False
    
    try:
        import demo_examples
        print("✅ demo_examples.py imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import demo_examples: {e}")
        return False
    
    return True


def test_hash_table_basic():
    """Test basic hash table operations."""
    print_header("TEST 2: Basic Hash Table Operations")
    
    from hash_table import HashTable
    
    # Test chaining mode
    print("\nTesting CHAINING mode...")
    ht = HashTable(size=5, mode='chaining')
    
    # Insert
    success, _, _, msg = ht.insert(10)
    if success:
        print(f"  ✅ Insert: {msg}")
    else:
        print(f"  ❌ Insert failed: {msg}")
        return False
    
    # Search
    found, _, msg = ht.search(10)
    if found:
        print(f"  ✅ Search: {msg}")
    else:
        print(f"  ❌ Search failed: {msg}")
        return False
    
    # Delete
    success, _, msg = ht.delete(10)
    if success:
        print(f"  ✅ Delete: {msg}")
    else:
        print(f"  ❌ Delete failed: {msg}")
        return False
    
    return True


def test_collision_modes():
    """Test all collision handling modes."""
    print_header("TEST 3: Collision Handling Modes")
    
    from hash_table import HashTable
    
    keys = [10, 20, 30]
    
    for mode in ['chaining', 'linear', 'quadratic']:
        print(f"\nTesting {mode.upper()} mode...")
        ht = HashTable(size=5, mode=mode)
        
        success_count = 0
        for key in keys:
            success, _, _, msg = ht.insert(key)
            if success:
                success_count += 1
        
        if success_count == len(keys):
            print(f"  ✅ {mode}: All keys inserted successfully")
        else:
            print(f"  ❌ {mode}: Only {success_count}/{len(keys)} keys inserted")
            return False
    
    return True


def test_string_keys():
    """Test hash table with string keys."""
    print_header("TEST 4: String Keys")
    
    from hash_table import HashTable
    
    ht = HashTable(size=5, mode='chaining')
    
    names = ["Alice", "Bob", "Charlie"]
    
    print("\nInserting string keys...")
    for name in names:
        success, _, _, msg = ht.insert(name)
        if success:
            print(f"  ✅ {msg}")
        else:
            print(f"  ❌ Failed: {msg}")
            return False
    
    return True


def test_load_factor():
    """Test load factor calculation."""
    print_header("TEST 5: Load Factor")
    
    from hash_table import HashTable
    
    ht = HashTable(size=10, mode='chaining')
    
    # Insert 5 keys
    for i in range(5):
        ht.insert(i * 10)
    
    load_factor = ht.get_load_factor()
    expected = 0.5
    
    if abs(load_factor - expected) < 0.01:
        print(f"  ✅ Load factor correct: {load_factor:.2f}")
        return True
    else:
        print(f"  ❌ Load factor incorrect: {load_factor:.2f} (expected {expected})")
        return False


def test_resize():
    """Test table resizing."""
    print_header("TEST 6: Resize and Rehash")
    
    from hash_table import HashTable
    
    ht = HashTable(size=5, mode='chaining')
    
    # Insert keys
    keys = [10, 20, 30]
    for key in keys:
        ht.insert(key)
    
    # Resize
    msg = ht.resize(10)
    
    # Check all keys still present
    all_keys = ht.get_all_keys()
    
    if len(all_keys) == len(keys):
        print(f"  ✅ Resize successful: {msg}")
        print(f"     All {len(keys)} keys preserved")
        return True
    else:
        print(f"  ❌ Resize failed: Lost keys")
        return False


def test_console_display():
    """Test console display."""
    print_header("TEST 7: Console Display")
    
    from hash_table import HashTable
    
    ht = HashTable(size=5, mode='chaining')
    ht.insert(10)
    ht.insert(20)
    
    print("\nDisplaying hash table:")
    try:
        ht.display_console()
        print("  ✅ Console display working")
        return True
    except Exception as e:
        print(f"  ❌ Console display failed: {e}")
        return False


def run_all_tests():
    """Run all tests."""
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + " "*12 + "HASH TABLE SIMULATOR - TEST SUITE" + " "*13 + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    
    print(f"\nPython Version: {sys.version}")
    
    tests = [
        ("Module Imports", test_imports),
        ("Basic Operations", test_hash_table_basic),
        ("Collision Modes", test_collision_modes),
        ("String Keys", test_string_keys),
        ("Load Factor", test_load_factor),
        ("Resize", test_resize),
        ("Console Display", test_console_display),
    ]
    
    passed = 0
    failed = 0
    
    for name, test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"\n❌ Test '{name}' crashed: {e}")
            failed += 1
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Total Tests: {len(tests)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print("="*60)
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! 🎉")
        print("\nYou're ready to use the Hash Table Simulator!")
        print("\nNext steps:")
        print("  1. Run: python gui_simulator.py")
        print("  2. Or run: python console_simulator.py")
        print("  3. Or run: python demo_examples.py")
    else:
        print("\n⚠️  SOME TESTS FAILED")
        print("\nPlease check the error messages above.")
        print("Make sure all files are in the correct location.")
    
    print("\n" + "#"*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
