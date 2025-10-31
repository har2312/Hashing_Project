# Hash Table Simulator# 🚀 Quick Start Guide



A comprehensive educational tool for learning hash table data structures.## Get Started in 3 Steps!



## Quick Start### Step 1: Verify Python

Open Command Prompt and check Python version:

```bash```bash

# GUI Mode (Recommended)python --version

python gui_simulator.py```

You need Python 3.7 or higher.

# Console Mode

python console_simulator.py### Step 2: Test the Installation

Navigate to the project folder:

# Run Demos```bash

python demo_examples.pycd c:\Users\itsha\Hashing_Project

``````



## FeaturesTest if tkinter is available:

```bash

- 4 collision handling modes (Chaining, Linear, Quadratic, Double Hashing)python -c "import tkinter; print('Ready to go!')"

- Real-time pseudocode visualization```

- Step-by-step execution

- Interactive GUI and console interfaces### Step 3: Launch the Simulator



## Requirements#### For Graphical Interface (Recommended):

```bash

- Python 3.7+python gui_simulator.py

- tkinter (included with Python)```



See [README.md](README.md) for full documentation.#### For Console Interface:

```bash
python console_simulator.py
```

#### To See All Demo Examples:
```bash
python demo_examples.py
```

## 🎯 First Time Using?

### Try This Simple Workflow:

1. **Launch GUI:**
   ```bash
   python gui_simulator.py
   ```

2. **Create Your First Hash Table:**
   - Table Size: 10
   - Mode: chaining
   - Click "Create New Table"

3. **Insert Some Keys:**
   - Type: `15, 25, 35, 45`
   - Click "➕ Insert"
   - Watch the visualization!

4. **Try Searching:**
   - Type: `25`
   - Click "🔍 Search"
   - See it highlighted in blue!

5. **Experiment with Collisions:**
   - Insert: `5, 15, 25` (these will collide in size-10 table)
   - Watch how chaining handles it with linked lists!

6. **Switch to Linear Probing:**
   - Change mode to "linear"
   - Click "Create New Table"
   - Insert same keys and see the difference!

## 📊 Example Commands (Console Mode)

```
1. Create New Hash Table
   - Size: 10
   - Mode: 1 (Chaining)

2. Insert Key(s)
   - Keys: 10, 20, 30, 15, 25

5. Display Hash Table
   - See the current state

6. Show All Keys
   - List all stored keys

7. Get Load Factor
   - Check current load

3. Search Key
   - Key: 25

4. Delete Key
   - Key: 20
```

## 🎨 Visual Guide

### Understanding the Colors (GUI):
- **White** → Empty bucket
- **Green** → Bucket with data
- **Orange** → Collision occurred here
- **Red** → Currently highlighted
- **Blue** → Search result found

### Reading the Console Output:
```
[ 0] -> [ 10 ] → [ 20 ]   ← Chained items
[ 1] -> [ EMPTY ]          ← Empty bucket
[ 2] -> [ 12 ]            ← Single item
```

## 💡 Tips for Learning

1. **Start with Chaining:**
   - Easiest to understand
   - Visual linked lists

2. **Compare Modes:**
   - Insert same keys in different modes
   - Observe how collisions are handled differently

3. **Watch Load Factor:**
   - Try filling a small table (size 5)
   - See when it suggests resizing

4. **Use Demo Examples:**
   - Run `python demo_examples.py`
   - Learn from 7 different scenarios

5. **Experiment:**
   - Try string keys: "Alice", "Bob", "Charlie"
   - Test edge cases: duplicate keys, full tables
   - Resize and see rehashing in action

## 🐛 Troubleshooting

### Problem: "python is not recognized"
**Solution:** Add Python to your PATH or use full path:
```bash
C:\Python39\python.exe gui_simulator.py
```

### Problem: "No module named tkinter"
**Solution:** Reinstall Python with tkinter support:
- Download from python.org
- Check "tcl/tk and IDLE" during installation

### Problem: GUI window is too small
**Solution:** The window is resizable! Just drag the corners.

### Problem: Can't see all buckets
**Solution:** Use the scrollbar on the right side of the visualization canvas.

## 🎓 Learning Path

### Beginner:
1. Run demo_examples.py
2. Use GUI with chaining mode
3. Insert, search, delete operations

### Intermediate:
1. Compare all three collision modes
2. Monitor load factors
3. Experiment with resizing

### Advanced:
1. Use console mode for precise control
2. Test edge cases (full tables, duplicates)
3. Analyze collision patterns
4. Read and modify the source code

## 📞 Need Help?

- Read the full README.md
- Check the comments in the source code
- Run demo_examples.py for inspiration

---

**Happy Learning! 🎉**

Start with: `python gui_simulator.py`
