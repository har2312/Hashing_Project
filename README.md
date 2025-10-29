# 🔐 Hash Table Simulator - Interactive Visualization# 🔐 Hash Table Simulator - Interactive Visualization



A comprehensive educational tool for learning hash table data structures with beautiful visualizations, real-time pseudocode, and multiple collision resolution strategies.**✨ NOW WITH ENHANCED PSEUDOCODE VISUALIZATION! ✨**



![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)---

![License](https://img.shields.io/badge/license-MIT-green)

![Status](https://img.shields.io/badge/status-active-success)## 🚀 Quick Links



## ✨ Features**New to the project?** Start here:

- 👉 **[README_FIRST.md](README_FIRST.md)** - Start here for quick orientation!

### 🎯 Core Functionality- 📊 **[STATUS.md](STATUS.md)** - Quick project status overview

- **Four Collision Handling Modes:**- ⭐ **[LATEST_UPDATE.md](LATEST_UPDATE.md)** - See what's new in this version

  - 🔗 **Chaining** - Linked lists in each bucket- 📖 **[INDEX.md](INDEX.md)** - Master index to all documentation

  - ➡️ **Linear Probing** - Open addressing with linear search

  - 📐 **Quadratic Probing** - Open addressing with quadratic search**Want to try it right now?**

  - 🔁 **Double Hashing** - Secondary hash function for probe sequence```bash

python test_pseudocode.py

- **Complete Operations:**```

  - ➕ Insert keys (single or batch)

  - 🔍 Search for keys**Want the pseudocode features?**

  - 🗑️ Delete keys (with tombstone support)- 📘 **[HOW_TO_USE_PSEUDOCODE.md](HOW_TO_USE_PSEUDOCODE.md)** - User guide

  - 📊 Display current state- 📗 **[PSEUDOCODE_GUIDE.md](PSEUDOCODE_GUIDE.md)** - Complete feature documentation

  - 🔄 Resize and rehash dynamically- 📙 **[VISUAL_EXAMPLES.md](VISUAL_EXAMPLES.md)** - Detailed execution examples



### 🖼️ Dual Interface Options---

1. **GUI Mode** (Recommended)

   - Beautiful tkinter-based interface## 📋 Table of Contents

   - Real-time canvas visualization

   - Color-coded bucket states**Four Collision Handling Modes:**

   - Step-by-step pseudocode panel  - 🔗 **Chaining** - Uses linked lists in each bucket

   - Collision steps viewer  - ➡️ **Linear Probing** - Open addressing with linear search

   - Animated operations  - 📐 **Quadratic Probing** - Open addressing with quadratic search

  - 🔁 **Double Hashing** - Open addressing using a secondary hash step size

2. **Console Mode**- [Overview](#overview)

   - Text-based ASCII visualization- [Project Structure](#project-structure)

   - Menu-driven interface- [Installation](#installation)

   - Perfect for terminals  - 🖼️ **GUI Mode** - Tkinter-based graphical interface with Pseudocode Panel and Collision Steps

  - 💻 **Console Mode** - Text-based ASCII visualization with pseudocode fallback for inserts

### 🧠 Educational Features- [Usage](#usage)

- **Real-time Pseudocode Display** - ⚡ Animated collision visualization (linear, quadratic, double hashing)

  - Block-level highlighting (loops, conditions)- [Screenshots](#screenshots)

  - Variable tracking- [Demo Examples](#demo-examples)

  - Step-by-step execution - 🧠 Pseudocode panel with line highlighting and variable display

  - Auto-run mode with adjustable speed - 🧾 Collision Steps panel with copy/clear

  - [Contributing](#contributing)

- **Collision Visualization**

  - Detailed probe sequence tracking## 🎯 Overview

  - Formula display for each mode - 🪦 Tombstones support for open addressing deletes

  - Terminal-style execution log

  This project provides a complete simulation of hash table data structures with visual representations of:

- **Performance Monitoring**├── gui_simulator.py        # Graphical user interface (with pseudocode + steps)

  - Load factor tracking- How keys are hashed and stored in buckets

  - Collision counting- How collisions occur and are resolved

  - Automatic rehashing suggestions3. **Maximum Size:** Limited to 100 buckets for practical visualization

- Load factor monitoring and automatic rehashing

## 🚀 Quick Start

Perfect for:

### Prerequisites## � Future Enhancements

- Python 3.7 or higher

- tkinter (included with Python)- [ ] Cuckoo hashing implementation

- [ ] Performance benchmarking tools

### Installation- [ ] Export/import table states

- [ ] Step-by-step pseudocode for search/delete

1. Clone the repository:- [ ] More sophisticated hash functions

```bash- [ ] Theme customization for GUI

git clone https://github.com/yourusername/hash-table-simulator.git- **Three Collision Handling Modes:**

cd hash-table-simulator  - 🔗 **Chaining** - Uses linked lists in each bucket

```  - ➡️ **Linear Probing** - Open addressing with linear search

  - 📐 **Quadratic Probing** - Open addressing with quadratic search

2. Verify Python installation:

```bash- **Complete Operations:**

python --version### Demo 8: Double Hashing and Tombstones

python -c "import tkinter; print('tkinter ready!')"Demonstrates double hashing probe sequences and tombstone behavior after deletions.

```  - ➕ Insert keys (single or multiple)

  - 🔍 Search for keys

3. Run the simulator:  - 🗑️ Delete keys

```bash  - 📊 Display current state

# GUI Mode (Recommended)  - 🔄 Resize and rehash

python gui_simulator.py

- **Two Interface Options:**

# Console Mode  - 🖼️ **GUI Mode** - Beautiful tkinter-based graphical interface

python console_simulator.py  - 💻 **Console Mode** - Text-based ASCII visualization



# Run all demos### Advanced Features

python demo_examples.py- ⚡ Animated collision visualization

```### Hash Functions



## 📖 Usage GuideWe normalize keys using a polynomial rolling approach for strings, then compute:

- h1(key) = key % m

### GUI Interface- h2(key) = 1 + (key % (m-1)) for double hashing (never zero)



1. **Create a Hash Table:**These are exposed via `utils.normalize_key`, `utils.hash1`, and `utils.hash2` for explainable UI.

   - Set table size (1-100)- 📈 Real-time load factor monitoring

   - Choose collision mode- 🎨 Color-coded bucket states

   - Click "Create New Table"- 📝 Operation logging

- 🔄 Dynamic mode switching

2. **Insert Keys:**- 📊 Statistical information

   - Enter keys (comma-separated for multiple)- ⚠️ Automatic rehashing warnings

   - Click "➕ Insert"

   - Watch real-time visualization and pseudocode## 📁 Project Structure



3. **Operations:**```

   - **Search:** Find keys and highlight resultsHashing_Project/

   - **Delete:** Remove keys (tombstones for open addressing)│

   - **Show All Keys:** List all stored keys├── hash_table.py           # Core hash table implementation

   - **Resize:** Change table size with automatic rehashing├── gui_simulator.py        # Graphical user interface

├── console_simulator.py    # Console-based interface

4. **Pseudocode Panel:**├── demo_examples.py        # Demonstration scripts

   - Click "Step" to advance line-by-line├── README.md              # This file

   - Click "Auto Run" for automatic execution└── requirements.txt       # Python dependencies (if any)

   - Adjust animation speed with slider```

   - View variable values in real-time

## 🚀 Installation

### Console Interface

### Prerequisites

Simple menu-driven options:- Python 3.7 or higher

```- tkinter (usually included with Python)

1. Create New Hash Table

2. Insert Key(s)### Setup Steps

3. Search Key

4. Delete Key1. **Clone or Download the Project:**

5. Display Hash Table   ```bash

6. Show All Keys   cd Hashing_Project

7. Get Load Factor   ```

8. Resize & Rehash

9. Clear Table2. **Verify Python Installation:**

10. Change Collision Mode   ```bash

0. Exit   python --version

```   ```

   Should show Python 3.7 or higher

## 🔧 Collision Handling Explained

3. **Test tkinter (for GUI):**

### Chaining   ```bash

```   python -c "import tkinter; print('tkinter is installed')"

[0] → [ 10 ] → [ 20 ] → [ 30 ]   ```

[1] → [ EMPTY ]

[2] → [ 12 ]4. **No additional dependencies required!** The project uses only Python standard library.

```

- Each bucket holds a linked list## 📖 Usage

- No table size limit

- Simple implementation### Option 1: Graphical Interface (Recommended)



### Linear ProbingRun the GUI simulator:

``````bash

h(k, i) = (h(k) + i) mod mpython gui_simulator.py

``````

- Probe next sequential bucket

- Good cache performance#### GUI Controls:

- Can cause clustering

1. **Create New Table:**

### Quadratic Probing   - Enter table size (1-100)

```   - Select collision mode (chaining/linear/quadratic)

h(k, i) = (h(k) + i²) mod m   - Click "Create New Table"

```

- Probe with quadratic increments2. **Insert Keys:**

- Reduces primary clustering   - Enter one or more keys (comma-separated)

- Better distribution   - Click "➕ Insert"

   - Watch the visualization update

### Double Hashing

```3. **Search Keys:**

h(k, i) = (h1(k) + i * h2(k)) mod m   - Enter a key to search

h2(k) = 1 + (k mod (m-1))   - Click "🔍 Search"

```   - Found keys are highlighted in blue

- Uses secondary hash function

- Best distribution4. **Delete Keys:**

- Minimizes clustering   - Enter a key to delete

   - Click "🗑️ Delete"

## 📁 Project Structure   - Bucket is updated instantly



```5. **Other Operations:**

hash-table-simulator/   - "📊 Show All Keys" - Display all stored keys

├── hash_table.py          # Core hash table implementation   - "Clear Table" - Remove all elements

├── gui_simulator.py       # GUI with pseudocode & visualization   - "🔄 Resize & Rehash" - Change table size

├── console_simulator.py   # Console-based interface   - Adjust animation speed with slider

├── demo_examples.py       # Demonstration scripts

├── test_pseudocode.py     # Test pseudocode features### Option 2: Console Interface

├── utils.py              # Utility functions (hash functions)

├── requirements.txt      # Dependencies (none required!)Run the console simulator:

├── run.bat              # Windows batch launcher```bash

├── .gitignore           # Git ignore rulespython console_simulator.py

└── README.md            # This file```

```

#### Console Menu:

## 🎓 Learning Outcomes```

1.  Create New Hash Table

Using this simulator, you will understand:2.  Insert Key(s)

3.  Search Key

✅ How hash functions map keys to indices  4.  Delete Key

✅ Why collisions occur and how to handle them  5.  Display Hash Table

✅ Trade-offs between different collision strategies  6.  Show All Keys

✅ Impact of load factor on performance  7.  Get Load Factor

✅ When and why to resize hash tables  8.  Resize & Rehash

✅ Real-world hashing applications  9.  Clear Table

✅ Algorithm implementation with pseudocode  10. Change Collision Mode

0.  Exit

## 🎬 Demo Examples```



Run comprehensive demonstrations:### Option 3: Run Demo Examples

```bash

python demo_examples.pySee all features in action:

``````bash

python demo_examples.py

Includes:```

- Basic operations (insert, search, delete)

- Collision handling comparisonThis runs 7 comprehensive demonstrations showing:

- String key hashing- Basic operations

- Load factor and resizing- Collision handling comparison

- Mixed operations- String keys

- Quadratic probing details- Load factor and resizing

- Double hashing and tombstones- Mixed operations

- Edge case testing- Quadratic probing details

- Edge cases

## 📊 Technical Details

## 🔧 Collision Handling Techniques

### Time Complexity

| Operation | Average | Worst Case |### 1. Chaining (Separate Chaining)

|-----------|---------|------------|

| Insert    | O(1)    | O(n)      |**How it works:**

| Search    | O(1)    | O(n)      |- Each bucket contains a linked list

| Delete    | O(1)    | O(n)      |- Colliding keys are added to the list

- No limit on number of keys per bucket

### Space Complexity

- **Chaining:** O(n + m) where n = elements, m = buckets**Visualization:**

- **Open Addressing:** O(m) where m = buckets```

[0] -> [ 10 ] → [ 20 ] → [ 30 ]

### Load Factor Guidelines[1] -> [ EMPTY ]

- ✅ **< 0.5** - Optimal performance[2] -> [ 12 ]

- ⚠️ **0.5 - 0.75** - Acceptable```

- ❌ **> 0.75** - Consider resizing

**Advantages:**

## 🎨 GUI Features- Simple to implement

- No clustering issues

- **Color-Coded Visualization:**- Table never gets "full"

  - White: Empty buckets

  - Green: Filled buckets**Disadvantages:**

  - Orange: Collision occurred- Extra memory for pointers

  - Gray: Tombstone (deleted)- Cache performance

  - Blue: Search result

### 2. Linear Probing

- **Interactive Panels:**

  - Control panel with all operations**How it works:**

  - Canvas visualization with scrolling- Each bucket holds at most one key

  - Pseudocode panel with highlighting- On collision, check next bucket: `(hash + 1) % size`

  - Collision steps terminal- Continue until empty bucket found

  - Status bar with real-time stats

**Visualization:**

- **Animations:**```

  - Adjustable speed (200-2000ms)[0] -> [ 10 ]  ← Original position

  - Step-by-step execution[1] -> [ 20 ]  ← Moved due to collision

  - Auto-run mode[2] -> [ 12 ]

```

## 🤝 Contributing

**Advantages:**

Contributions welcome! Areas for improvement:- Good cache performance

- Additional collision strategies- Simple implementation

- More hash functions- No extra memory

- Performance benchmarking

- Unit tests**Disadvantages:**

- UI/UX enhancements- Primary clustering

- Documentation improvements- Table can fill up

- Slower with high load factor

## 📝 License

### 3. Quadratic Probing

MIT License - Feel free to use for educational purposes.

**How it works:**

## 🙏 Acknowledgments- On collision, check: `(hash + i²) % size` where i = 1, 2, 3...

- Reduces clustering compared to linear probing

Created for educational purposes to help students understand hash table data structures through interactive visualization.

**Visualization:**

## 📧 Contact```

[0] -> [ 10 ]  ← Original position

For questions or suggestions, please open an issue on GitHub.[1] -> [ 20 ]  ← Moved by 1² = 1

[4] -> [ 30 ]  ← Moved by 2² = 4

---```



**Happy Hashing! 🔐****Advantages:**

- Reduces primary clustering

*Made with ❤️ for Data Structures enthusiasts*- Better distribution

- Good cache performance

**Disadvantages:**
- Can fail to find empty slots
- Secondary clustering
- Table can fill up

## 📸 Screenshots

### GUI Interface Features:

**Control Panel:**
- Table size and mode selection
- Key input field (supports comma-separated values)
- Operation buttons with emoji icons
- Resize controls
- Animation speed slider

**Visualization Canvas:**
- Color-coded buckets:
  - White: Empty
  - Green: Filled
  - Orange: Collision
  - Red: Highlighted
  - Blue: Search result
- Chain visualization for chaining mode
- Clear bucket labels and indices

**Operation Log:**
- Timestamped entries
- Terminal-style display
- Success/failure indicators
- Detailed operation messages

**Status Bar:**
- Current operation status
- Real-time statistics (size, elements, load factor)

### Console Interface:

**ASCII Visualization:**
```
============================================================
HASH TABLE VISUALIZATION (CHAINING mode)
Size: 5 | Elements: 6 | Load Factor: 1.20
============================================================
[ 0] -> [ 10 ] → [ 15 ]
[ 1] -> [ EMPTY ]
[ 2] -> [ 12 ]
[ 3] -> [ 23 ] → [ 13 ]
[ 4] -> [ EMPTY ]
============================================================
```

## 🎬 Demo Examples

### Demo 1: Basic Operations
Shows insert, search, delete with chaining mode.

### Demo 2: Collision Handling Comparison
Compares all three modes with the same dataset.

### Demo 3: String Keys
Demonstrates hashing of string values.

### Demo 4: Load Factor and Resizing
Shows monitoring and automatic rehashing.

### Demo 5: Mixed Operations
Complete workflow with all operations.

### Demo 6: Quadratic Probing Detail
In-depth view of quadratic probing behavior.

### Demo 7: Edge Cases
Tests error handling and boundary conditions.

## 🔬 Technical Details

### Hash Function

Simple modulo-based hash function:
```python
def hash_function(key):
    if isinstance(key, str):
        key_value = abs(hash(key))
    else:
        key_value = abs(int(key))
    return key_value % size
```

### Load Factor

Calculated as: `load_factor = number_of_elements / table_size`

**Recommendations:**
- ✅ **< 0.5** - Optimal performance
- ⚠️ **0.5 - 0.7** - Acceptable
- ❌ **> 0.7** - Consider resizing

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Insert    | O(1)        | O(n)       |
| Search    | O(1)        | O(n)       |
| Delete    | O(1)        | O(n)       |

*Note: Worst case occurs with many collisions*

### Space Complexity

- **Chaining:** O(n + m) where n = elements, m = table size
- **Open Addressing:** O(m) where m = table size

## 📚 Code Structure

### Class: `HashTable`

**Attributes:**
- `size`: Number of buckets
- `mode`: Collision handling mode
- `table`: Actual storage
- `count`: Number of elements
- `collision_log`: List of collision events

**Methods:**
- `insert(key)`: Add a key
- `search(key)`: Find a key
- `delete(key)`: Remove a key
- `resize(new_size)`: Resize and rehash
- `get_load_factor()`: Calculate load factor
- `display_console()`: ASCII visualization

### Class: `Node` (for chaining)

Linked list node for chaining mode.

### Class: `HashTableGUI`

Complete GUI implementation with:
- Canvas-based visualization
- Event handlers for all operations
- Animation support
- Real-time updates

### Class: `ConsoleSimulator`

Menu-driven console interface with:
- Text-based visualization
- Interactive prompts
- Error handling
- Formatted output

## 🎓 Learning Outcomes

By using this simulator, you will understand:

1. ✅ How hash functions map keys to indices
2. ✅ Why collisions occur in hash tables
3. ✅ Different strategies for resolving collisions
4. ✅ Trade-offs between collision handling methods
5. ✅ Impact of load factor on performance
6. ✅ When and why to resize hash tables
7. ✅ Real-world applications of hashing

## 🐛 Known Limitations

1. **Simple Hash Function:** Uses basic modulo operation (good for learning, not production)
2. **Delete in Open Addressing:** Simple implementation without tombstones
3. **Quadratic Probing:** May not find empty slots in some cases with high load factors
4. **Maximum Size:** Limited to 100 buckets for practical visualization

## 🔮 Future Enhancements

- [ ] Double hashing support
- [ ] Cuckoo hashing implementation
- [ ] Performance benchmarking tools
- [ ] Export/import table states
- [ ] Step-by-step operation breakdown
- [ ] More sophisticated hash functions
- [ ] Tombstone handling for deletions
- [ ] Theme customization for GUI

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional collision resolution strategies
- Better hash functions
- Performance optimizations
- UI/UX enhancements
- More demonstration examples
- Unit tests

## 📝 License

This project is created for educational purposes. Feel free to use, modify, and distribute.

## 👨‍💻 Author

Hash Table Simulator
Created: October 25, 2025

## 🙏 Acknowledgments

- Python tkinter documentation
- Data Structures and Algorithms textbooks
- Computer Science education community

## 📧 Support

For questions, issues, or suggestions, please open an issue in the project repository.

---

**Happy Hashing! 🔐**

Made with ❤️ for Data Structures enthusiasts
