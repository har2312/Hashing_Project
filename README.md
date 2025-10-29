# 🔐 Hash Table Simulator - Interactive Visualization# 🔐 Hash Table Simulator - Interactive Visualization# 🔐 Hash Table Simulator - Interactive Visualization



A comprehensive educational tool for learning hash table data structures with beautiful visualizations, real-time pseudocode, and multiple collision resolution strategies.



![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)A comprehensive educational tool for learning hash table data structures with beautiful visualizations, real-time pseudocode, and multiple collision resolution strategies.**✨ NOW WITH ENHANCED PSEUDOCODE VISUALIZATION! ✨**

![License](https://img.shields.io/badge/license-MIT-green)

![Status](https://img.shields.io/badge/status-active-success)



## ✨ Features![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)---



### 🎯 Core Functionality![License](https://img.shields.io/badge/license-MIT-green)

- **Four Collision Handling Modes:**

  - 🔗 **Chaining** - Linked lists in each bucket![Status](https://img.shields.io/badge/status-active-success)## 🚀 Quick Links

  - ➡️ **Linear Probing** - Open addressing with linear search

  - 📐 **Quadratic Probing** - Open addressing with quadratic search

  - 🔁 **Double Hashing** - Secondary hash function for probe sequence

## ✨ Features**New to the project?** Start here:

- **Complete Operations:**

  - ➕ Insert keys (single or batch)- 👉 **[README_FIRST.md](README_FIRST.md)** - Start here for quick orientation!

  - 🔍 Search for keys

  - 🗑️ Delete keys (with tombstone support)### 🎯 Core Functionality- 📊 **[STATUS.md](STATUS.md)** - Quick project status overview

  - 📊 Display current state

  - 🔄 Resize and rehash dynamically- **Four Collision Handling Modes:**- ⭐ **[LATEST_UPDATE.md](LATEST_UPDATE.md)** - See what's new in this version



### 🖼️ Dual Interface Options  - 🔗 **Chaining** - Linked lists in each bucket- 📖 **[INDEX.md](INDEX.md)** - Master index to all documentation

1. **GUI Mode** (Recommended)

   - Beautiful tkinter-based interface  - ➡️ **Linear Probing** - Open addressing with linear search

   - Real-time canvas visualization

   - Color-coded bucket states  - 📐 **Quadratic Probing** - Open addressing with quadratic search**Want to try it right now?**

   - Step-by-step pseudocode panel

   - Collision steps viewer  - 🔁 **Double Hashing** - Secondary hash function for probe sequence```bash

   - Animated operations

python test_pseudocode.py

2. **Console Mode**

   - Text-based ASCII visualization- **Complete Operations:**```

   - Menu-driven interface

   - Perfect for terminals  - ➕ Insert keys (single or batch)



### 🧠 Educational Features  - 🔍 Search for keys**Want the pseudocode features?**

- **Real-time Pseudocode Display**

  - Block-level highlighting (loops, conditions)  - 🗑️ Delete keys (with tombstone support)- 📘 **[HOW_TO_USE_PSEUDOCODE.md](HOW_TO_USE_PSEUDOCODE.md)** - User guide

  - Variable tracking

  - Step-by-step execution  - 📊 Display current state- 📗 **[PSEUDOCODE_GUIDE.md](PSEUDOCODE_GUIDE.md)** - Complete feature documentation

  - Auto-run mode with adjustable speed

    - 🔄 Resize and rehash dynamically- 📙 **[VISUAL_EXAMPLES.md](VISUAL_EXAMPLES.md)** - Detailed execution examples

- **Collision Visualization**

  - Detailed probe sequence tracking

  - Formula display for each mode

  - Terminal-style execution log### 🖼️ Dual Interface Options---

  

- **Performance Monitoring**1. **GUI Mode** (Recommended)

  - Load factor tracking

  - Collision counting   - Beautiful tkinter-based interface## 📋 Table of Contents

  - Automatic rehashing suggestions

   - Real-time canvas visualization

## 🚀 Quick Start

   - Color-coded bucket states**Four Collision Handling Modes:**

### Option 1: Download Executable (Windows - No Python Required!)

   - Step-by-step pseudocode panel  - 🔗 **Chaining** - Uses linked lists in each bucket

1. Go to [Releases](https://github.com/har2312/Hashing_Project/releases)

2. Download `HashTableSimulator.exe`   - Collision steps viewer  - ➡️ **Linear Probing** - Open addressing with linear search

3. Run the executable - that's it!

   - Animated operations  - 📐 **Quadratic Probing** - Open addressing with quadratic search

### Option 2: Run from Source

  - 🔁 **Double Hashing** - Open addressing using a secondary hash step size

**Prerequisites:**

- Python 3.7 or higher2. **Console Mode**- [Overview](#overview)

- tkinter (included with Python)

   - Text-based ASCII visualization- [Project Structure](#project-structure)

**Installation:**

   - Menu-driven interface- [Installation](#installation)

```bash

# Clone the repository   - Perfect for terminals  - 🖼️ **GUI Mode** - Tkinter-based graphical interface with Pseudocode Panel and Collision Steps

git clone https://github.com/har2312/Hashing_Project.git

cd Hashing_Project  - 💻 **Console Mode** - Text-based ASCII visualization with pseudocode fallback for inserts



# Verify Python### 🧠 Educational Features- [Usage](#usage)

python --version

python -c "import tkinter; print('tkinter ready!')"- **Real-time Pseudocode Display** - ⚡ Animated collision visualization (linear, quadratic, double hashing)



# Run the simulator  - Block-level highlighting (loops, conditions)- [Screenshots](#screenshots)

python gui_simulator.py        # GUI Mode

python console_simulator.py    # Console Mode  - Variable tracking- [Demo Examples](#demo-examples)

python demo_examples.py        # Run all demos

```  - Step-by-step execution - 🧠 Pseudocode panel with line highlighting and variable display



## 📖 Usage Guide  - Auto-run mode with adjustable speed - 🧾 Collision Steps panel with copy/clear



### GUI Interface  - [Contributing](#contributing)



1. **Create a Hash Table:**- **Collision Visualization**

   - Set table size (1-100)

   - Choose collision mode  - Detailed probe sequence tracking## 🎯 Overview

   - Click "Create New Table"

  - Formula display for each mode - 🪦 Tombstones support for open addressing deletes

2. **Insert Keys:**

   - Enter keys (comma-separated for multiple)  - Terminal-style execution log

   - Click "➕ Insert"

   - Watch real-time visualization and pseudocode  This project provides a complete simulation of hash table data structures with visual representations of:



3. **Operations:**- **Performance Monitoring**├── gui_simulator.py        # Graphical user interface (with pseudocode + steps)

   - **Search:** Find keys and highlight results

   - **Delete:** Remove keys (tombstones for open addressing)  - Load factor tracking- How keys are hashed and stored in buckets

   - **Show All Keys:** List all stored keys

   - **Resize:** Change table size with automatic rehashing  - Collision counting- How collisions occur and are resolved



4. **Pseudocode Panel:**  - Automatic rehashing suggestions3. **Maximum Size:** Limited to 100 buckets for practical visualization

   - Click "Step" to advance line-by-line

   - Click "Auto Run" for automatic execution- Load factor monitoring and automatic rehashing

   - Adjust animation speed with slider

   - View variable values in real-time## 🚀 Quick Start



### Console InterfacePerfect for:



Simple menu-driven options:### Prerequisites## � Future Enhancements

```

1. Create New Hash Table- Python 3.7 or higher

2. Insert Key(s)

3. Search Key- tkinter (included with Python)- [ ] Cuckoo hashing implementation

4. Delete Key

5. Display Hash Table- [ ] Performance benchmarking tools

6. Show All Keys

7. Get Load Factor### Installation- [ ] Export/import table states

8. Resize & Rehash

9. Clear Table- [ ] Step-by-step pseudocode for search/delete

10. Change Collision Mode

0. Exit1. Clone the repository:- [ ] More sophisticated hash functions

```

```bash- [ ] Theme customization for GUI

## 🔧 Collision Handling Explained

git clone https://github.com/yourusername/hash-table-simulator.git- **Three Collision Handling Modes:**

### Chaining

```cd hash-table-simulator  - 🔗 **Chaining** - Uses linked lists in each bucket

[0] → [ 10 ] → [ 20 ] → [ 30 ]

[1] → [ EMPTY ]```  - ➡️ **Linear Probing** - Open addressing with linear search

[2] → [ 12 ]

```  - 📐 **Quadratic Probing** - Open addressing with quadratic search

- Each bucket holds a linked list

- No table size limit2. Verify Python installation:

- Simple implementation

```bash- **Complete Operations:**

### Linear Probing

```python --version### Demo 8: Double Hashing and Tombstones

h(k, i) = (h(k) + i) mod m

```python -c "import tkinter; print('tkinter ready!')"Demonstrates double hashing probe sequences and tombstone behavior after deletions.

- Probe next sequential bucket

- Good cache performance```  - ➕ Insert keys (single or multiple)

- Can cause clustering

  - 🔍 Search for keys

### Quadratic Probing

```3. Run the simulator:  - 🗑️ Delete keys

h(k, i) = (h(k) + i²) mod m

``````bash  - 📊 Display current state

- Probe with quadratic increments

- Reduces primary clustering# GUI Mode (Recommended)  - 🔄 Resize and rehash

- Better distribution

python gui_simulator.py

### Double Hashing

```- **Two Interface Options:**

h(k, i) = (h1(k) + i * h2(k)) mod m

h2(k) = 1 + (k mod (m-1))# Console Mode  - 🖼️ **GUI Mode** - Beautiful tkinter-based graphical interface

```

- Uses secondary hash functionpython console_simulator.py  - 💻 **Console Mode** - Text-based ASCII visualization

- Best distribution

- Minimizes clustering



## 📁 Project Structure# Run all demos### Advanced Features



```python demo_examples.py- ⚡ Animated collision visualization

Hashing_Project/

├── hash_table.py           # Core hash table implementation```### Hash Functions

├── gui_simulator.py        # GUI with pseudocode & visualization

├── console_simulator.py    # Console-based interface

├── demo_examples.py        # Demonstration scripts

├── test_pseudocode.py      # Test pseudocode features## 📖 Usage GuideWe normalize keys using a polynomial rolling approach for strings, then compute:

├── test_setup.py           # Setup verification tests

├── utils.py               # Utility functions (hash functions)- h1(key) = key % m

├── build.py               # Build script for executables

├── requirements.txt       # Dependencies (none required!)### GUI Interface- h2(key) = 1 + (key % (m-1)) for double hashing (never zero)

├── run.bat                # Windows batch launcher

├── .gitignore             # Git ignore rules

├── LICENSE                # MIT License

├── CHANGELOG.md           # Version history1. **Create a Hash Table:**These are exposed via `utils.normalize_key`, `utils.hash1`, and `utils.hash2` for explainable UI.

├── DEPLOYMENT.md          # Deployment guide

├── QUICKSTART.md          # Quick reference   - Set table size (1-100)- 📈 Real-time load factor monitoring

└── README.md              # This file

```   - Choose collision mode- 🎨 Color-coded bucket states



## 🎓 Learning Outcomes   - Click "Create New Table"- 📝 Operation logging



Using this simulator, you will understand:- 🔄 Dynamic mode switching



✅ How hash functions map keys to indices  2. **Insert Keys:**- 📊 Statistical information

✅ Why collisions occur and how to handle them  

✅ Trade-offs between different collision strategies     - Enter keys (comma-separated for multiple)- ⚠️ Automatic rehashing warnings

✅ Impact of load factor on performance  

✅ When and why to resize hash tables     - Click "➕ Insert"

✅ Real-world hashing applications  

✅ Algorithm implementation with pseudocode     - Watch real-time visualization and pseudocode## 📁 Project Structure



## 🎬 Demo Examples



Run comprehensive demonstrations:3. **Operations:**```

```bash

python demo_examples.py   - **Search:** Find keys and highlight resultsHashing_Project/

```

   - **Delete:** Remove keys (tombstones for open addressing)│

Includes:

- Basic operations (insert, search, delete)   - **Show All Keys:** List all stored keys├── hash_table.py           # Core hash table implementation

- Collision handling comparison

- String key hashing   - **Resize:** Change table size with automatic rehashing├── gui_simulator.py        # Graphical user interface

- Load factor and resizing

- Mixed operations├── console_simulator.py    # Console-based interface

- Quadratic probing details

- Double hashing and tombstones4. **Pseudocode Panel:**├── demo_examples.py        # Demonstration scripts

- Edge case testing

   - Click "Step" to advance line-by-line├── README.md              # This file

## 📊 Technical Details

   - Click "Auto Run" for automatic execution└── requirements.txt       # Python dependencies (if any)

### Time Complexity

| Operation | Average | Worst Case |   - Adjust animation speed with slider```

|-----------|---------|------------|

| Insert    | O(1)    | O(n)      |   - View variable values in real-time

| Search    | O(1)    | O(n)      |

| Delete    | O(1)    | O(n)      |## 🚀 Installation



### Space Complexity### Console Interface

- **Chaining:** O(n + m) where n = elements, m = buckets

- **Open Addressing:** O(m) where m = buckets### Prerequisites



### Load Factor GuidelinesSimple menu-driven options:- Python 3.7 or higher

- ✅ **< 0.5** - Optimal performance

- ⚠️ **0.5 - 0.75** - Acceptable```- tkinter (usually included with Python)

- ❌ **> 0.75** - Consider resizing

1. Create New Hash Table

## 🎨 GUI Features

2. Insert Key(s)### Setup Steps

- **Color-Coded Visualization:**

  - White: Empty buckets3. Search Key

  - Green: Filled buckets

  - Orange: Collision occurred4. Delete Key1. **Clone or Download the Project:**

  - Gray: Tombstone (deleted)

  - Blue: Search result5. Display Hash Table   ```bash



- **Interactive Panels:**6. Show All Keys   cd Hashing_Project

  - Control panel with all operations

  - Canvas visualization with scrolling7. Get Load Factor   ```

  - Pseudocode panel with highlighting

  - Collision steps terminal8. Resize & Rehash

  - Status bar with real-time stats

9. Clear Table2. **Verify Python Installation:**

- **Animations:**

  - Adjustable speed (200-2000ms)10. Change Collision Mode   ```bash

  - Step-by-step execution

  - Auto-run mode0. Exit   python --version



## 🚀 Deployment```   ```



### Create Your Own Executable   Should show Python 3.7 or higher



```bash## 🔧 Collision Handling Explained

# Install PyInstaller

pip install pyinstaller3. **Test tkinter (for GUI):**



# Build executable### Chaining   ```bash

python build.py

```   python -c "import tkinter; print('tkinter is installed')"

# Or manually:

pyinstaller --onefile --windowed --name HashTableSimulator gui_simulator.py[0] → [ 10 ] → [ 20 ] → [ 30 ]   ```

```

[1] → [ EMPTY ]

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

[2] → [ 12 ]4. **No additional dependencies required!** The project uses only Python standard library.

## 🤝 Contributing

```

Contributions welcome! Areas for improvement:

- Additional collision strategies- Each bucket holds a linked list## 📖 Usage

- More hash functions

- Performance benchmarking- No table size limit

- Unit tests

- UI/UX enhancements- Simple implementation### Option 1: Graphical Interface (Recommended)

- Documentation improvements



## 📝 License

### Linear ProbingRun the GUI simulator:

MIT License - See [LICENSE](LICENSE) file for details.

``````bash

## 🙏 Acknowledgments

h(k, i) = (h(k) + i) mod mpython gui_simulator.py

Created for educational purposes to help students understand hash table data structures through interactive visualization.

``````

## 📧 Contact

- Probe next sequential bucket

- **GitHub:** [@har2312](https://github.com/har2312)

- **Repository:** [Hashing_Project](https://github.com/har2312/Hashing_Project)- Good cache performance#### GUI Controls:

- **Issues:** [Report a bug](https://github.com/har2312/Hashing_Project/issues)

- Can cause clustering

## 📜 Changelog

1. **Create New Table:**

See [CHANGELOG.md](CHANGELOG.md) for version history.

### Quadratic Probing   - Enter table size (1-100)

---

```   - Select collision mode (chaining/linear/quadratic)

**Happy Hashing! 🔐**

h(k, i) = (h(k) + i²) mod m   - Click "Create New Table"

*Made with ❤️ for Data Structures enthusiasts*

```

**⭐ If you find this project helpful, please give it a star on GitHub!**

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
