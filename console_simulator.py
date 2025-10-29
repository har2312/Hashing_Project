"""
Console-based Hash Table Simulator

This module provides a command-line interface for hash table operations
with ASCII-based visualization.

Features:
- Text-based visualization of hash table
- Interactive menu for all operations
- Support for all collision handling modes
- Detailed output and statistics

Author: Hash Table Simulator
Date: October 25, 2025
"""

from hash_table import HashTable
from utils import normalize_key, hash1 as h1_fn, hash2 as h2_fn
import sys


class ConsoleSimulator:
    """
    Console-based interface for hash table simulation.
    
    Provides a text menu-driven interface for interacting with hash tables.
    """
    
    def __init__(self):
        """Initialize the console simulator."""
        self.hash_table = None
    
    def print_header(self):
        """Print the application header."""
        print("\n" + "="*70)
        print(" "*20 + "🔐 HASH TABLE SIMULATOR 🔐")
        print("="*70)
    
    def print_menu(self):
        """Print the main menu."""
        print("\n" + "-"*70)
        print("MAIN MENU")
        print("-"*70)
        print("1.  Create New Hash Table")
        print("2.  Insert Key(s)")
        print("3.  Search Key")
        print("4.  Delete Key")
        print("5.  Display Hash Table")
        print("6.  Show All Keys")
        print("7.  Get Load Factor")
        print("8.  Resize & Rehash")
        print("9.  Clear Table")
        print("10. Change Collision Mode")
        print("0.  Exit")
        print("-"*70)
    
    def create_table(self):
        """Create a new hash table."""
        print("\n--- CREATE NEW HASH TABLE ---")
        
        try:
            size = int(input("Enter table size (1-100): "))
            if size < 1 or size > 100:
                print("❌ Error: Size must be between 1 and 100")
                return
            
            print("\nCollision Handling Modes:")
            print("1. Chaining (Linked List)")
            print("2. Linear Probing (Open Addressing)")
            print("3. Quadratic Probing (Open Addressing)")
            print("4.  Double Hashing (Open Addressing)")
            
            mode_choice = input("Choose mode (1-3): ")
            mode_choice = input("Choose mode (1-4): ")
            mode_map = {
                '1': 'chaining',
                '2': 'linear',
                '3': 'quadratic'
            }
            
            mode = mode_map.get(mode_choice, 'chaining')
            
            self.hash_table = HashTable(size=size, mode=mode)
            print(f"\n✅ Hash table created successfully!")
            print(f"   Size: {size} buckets")
            print(f"   Mode: {mode.upper()}")
            
        except ValueError:
            print("❌ Error: Invalid input. Please enter a valid number.")
    
    def insert_keys(self):
        """Insert one or more keys."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        print("\n--- INSERT KEY(S) ---")
        keys_input = input("Enter key(s) (comma-separated for multiple): ")
        
        # Parse keys
        keys = [k.strip() for k in keys_input.split(',')]
        
        # Try to convert to integers
        parsed_keys = []
        for k in keys:
            try:
                parsed_keys.append(int(k))
            except ValueError:
                parsed_keys.append(k)
        
        print()
        for key in parsed_keys:
            success, index, collision, message = self.hash_table.insert(key)
            
            if success:
                symbol = "⚠️" if collision else "✅"
                print(f"{symbol} {message}")
                # Print a compact pseudocode breakdown for insert (console fallback)
                try:
                    self.print_pseudocode_insert(key)
                except Exception:
                    pass
            else:
                print(f"❌ {message}")
        
        print(f"\n📊 Current load factor: {self.hash_table.get_load_factor():.2f}")
        
        if self.hash_table.get_load_factor() > 0.7:
            print("⚠️  WARNING: Load factor is high! Consider resizing the table.")
    
    def search_key(self):
        """Search for a key."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        print("\n--- SEARCH KEY ---")
        key_input = input("Enter key to search: ")
        
        # Try to convert to integer
        try:
            key = int(key_input)
        except ValueError:
            key = key_input
        
        found, index, message = self.hash_table.search(key)
        
        if found:
            print(f"✅ {message}")
            print(f"   Hash value: {self.hash_table.hash_function(key)}")
        else:
            print(f"❌ {message}")
    
    def delete_key(self):
        """Delete a key."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        print("\n--- DELETE KEY ---")
        key_input = input("Enter key to delete: ")
        
        # Try to convert to integer
        try:
            key = int(key_input)
        except ValueError:
            key = key_input
        
        success, index, message = self.hash_table.delete(key)
        
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")

    def print_pseudocode_insert(self, key):
        """Console fallback: show pseudocode and steps for insert of a single key."""
        mode = self.hash_table.mode
        m = self.hash_table.size
        key_int, _ = normalize_key(key)
        h1, _ = h1_fn(key_int, m)
        h2 = None
        if mode == 'double':
            h2, _ = h2_fn(key_int, m)

        print("   Pseudocode (" + mode + "):")
        if mode == 'chaining':
            print("     1: h1 = hash(key) % m")
            print("    >>2: insert key at bucket h1 (append)")
            print(f"       vars: h1={h1}, m={m}")
            return

        # Open addressing
        if mode == 'linear':
            lines = [
                "     1: h1 = hash(key) % m",
                "     2: i = 0",
                "     3: while i < m:",
                "    >>4:   idx = (h1 + i) % m",
                "     5:   if slot[idx] empty/tombstone: place key; break",
                "     6:   i = i + 1",
            ]
        elif mode == 'quadratic':
            lines = [
                "     1: h1 = hash(key) % m",
                "     2: i = 0",
                "     3: while i < m:",
                "    >>4:   idx = (h1 + i*i) % m",
                "     5:   if slot[idx] empty/tombstone: place key; break",
                "     6:   i = i + 1",
            ]
        else:  # double
            lines = [
                "     1: h1 = hash(key) % m",
                "     2: h2 = 1 + (hash(key) % (m-1))",
                "     3: i = 0",
                "     4: while i < m:",
                "    >>5:   idx = (h1 + i*h2) % m",
                "     6:   if slot[idx] empty/tombstone: place key; break",
                "     7:   i = i + 1",
            ]
        for line in lines:
            print(line)
        vars_line = f"       vars: h1={h1}, m={m}"
        if h2 is not None:
            vars_line += f", h2={h2}"
        print(vars_line)
        
        # Show the actual probe sequence used, if logged
        if getattr(self.hash_table, 'collision_log', None):
            entry = self.hash_table.collision_log[-1]
            if entry.get('key') == key:
                probes = entry.get('probes', 0)
                original = entry.get('original_index')
                final_idx = entry.get('final_index')
                seq = []
                for i in range(probes + 1):
                    if mode == 'linear':
                        idx = (h1 + i) % m
                    elif mode == 'quadratic':
                        idx = (h1 + i*i) % m
                    else:
                        idx = (h1 + i*h2) % m
                    seq.append(idx)
                print(f"       steps: start at {original} -> probes={probes} -> sequence={seq} -> placed at {final_idx}")
    
    def display_table(self):
        """Display the hash table."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        self.hash_table.display_console()
    
    def show_all_keys(self):
        """Show all keys in the table."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        keys = self.hash_table.get_all_keys()
        
        print("\n--- ALL KEYS ---")
        if keys:
            print(f"Total keys: {len(keys)}")
            print(f"Keys: {', '.join([str(k) for k in keys])}")
        else:
            print("Hash table is empty")
    
    def show_load_factor(self):
        """Show current load factor."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        load_factor = self.hash_table.get_load_factor()
        print(f"\n📊 Current Load Factor: {load_factor:.2f}")
        print(f"   Elements: {self.hash_table.count}")
        print(f"   Size: {self.hash_table.size}")
        
        if load_factor < 0.5:
            print("   Status: ✅ Low (Efficient)")
        elif load_factor < 0.7:
            print("   Status: ⚠️  Moderate")
        else:
            print("   Status: ❌ High (Consider resizing)")
    
    def resize_table(self):
        """Resize the hash table."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        print("\n--- RESIZE & REHASH ---")
        try:
            new_size = int(input(f"Enter new size (current: {self.hash_table.size}): "))
            
            if new_size < 1 or new_size > 100:
                print("❌ Error: Size must be between 1 and 100")
                return
            
            message = self.hash_table.resize(new_size)
            print(f"✅ {message}")
            
        except ValueError:
            print("❌ Error: Invalid input. Please enter a valid number.")
    
    def clear_table(self):
        """Clear the hash table."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        confirm = input("Are you sure you want to clear the table? (yes/no): ")
        if confirm.lower() == 'yes':
            self.hash_table.clear()
            print("✅ Hash table cleared")
        else:
            print("❌ Operation cancelled")
    
    def change_mode(self):
        """Change collision handling mode."""
        if not self.hash_table:
            print("❌ Error: Please create a hash table first (Option 1)")
            return
        
        print("\n--- CHANGE COLLISION MODE ---")
        print(f"Current mode: {self.hash_table.mode.upper()}")
        print("\nAvailable modes:")
        print("1. Chaining (Linked List)")
        print("2. Linear Probing (Open Addressing)")
        print("3. Quadratic Probing (Open Addressing)")
        print("4. Double Hashing (Open Addressing)")
        
        mode_choice = input("Choose new mode (1-3): ")
        mode_choice = input("Choose new mode (1-4): ")
        mode_map = {
            '1': 'chaining',
            '2': 'linear',
            '3': 'quadratic'
        }
        
        new_mode = mode_map.get(mode_choice)
        if not new_mode:
            print("❌ Error: Invalid mode selection")
            return
        
        # Save current keys
        keys = self.hash_table.get_all_keys()
        size = self.hash_table.size
        
        # Create new table with new mode
        self.hash_table = HashTable(size=size, mode=new_mode)
        
        # Reinsert keys
        for key in keys:
            self.hash_table.insert(key)
        
        print(f"✅ Changed mode to {new_mode.upper()}")
        print(f"   Reinserted {len(keys)} keys")
    
    def run(self):
        """Run the console simulator."""
        self.print_header()
        
        while True:
            self.print_menu()
            
            try:
                choice = input("\nEnter your choice: ").strip()
                
                if choice == '0':
                    print("\n👋 Thank you for using Hash Table Simulator!")
                    print("="*70 + "\n")
                    sys.exit(0)
                elif choice == '1':
                    self.create_table()
                elif choice == '2':
                    self.insert_keys()
                elif choice == '3':
                    self.search_key()
                elif choice == '4':
                    self.delete_key()
                elif choice == '5':
                    self.display_table()
                elif choice == '6':
                    self.show_all_keys()
                elif choice == '7':
                    self.show_load_factor()
                elif choice == '8':
                    self.resize_table()
                elif choice == '9':
                    self.clear_table()
                elif choice == '10':
                    self.change_mode()
                else:
                    print("❌ Invalid choice. Please try again.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                input("\nPress Enter to continue...")


def main():
    """Main entry point for console simulator."""
    simulator = ConsoleSimulator()
    simulator.run()


if __name__ == "__main__":
    main()
