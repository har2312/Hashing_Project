"""
Interactive Hash Table Simulator with GUI

This module provides a graphical user interface for visualizing hash table operations
including insertion, search, deletion, and collision handling.

Features:
- Visual representation of hash buckets
- Color-coded collision indicators
- Animated collision events
- Support for chaining and open addressing modes
- Real-time load factor monitoring
- Interactive controls for all operations

Author: Hash Table Simulator
Date: October 25, 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
from typing import Optional
from hash_table import HashTable
from utils import normalize_key, hash1 as h1_fn, hash2 as h2_fn


class HashTableGUI:
    """
    Graphical User Interface for Hash Table Simulation.
    
    Provides an interactive canvas-based visualization of hash table operations
    with support for multiple collision handling strategies.
    """
    
    # Color scheme
    COLOR_EMPTY = "#FFFFFF"
    COLOR_FILLED = "#4CAF50"
    COLOR_COLLISION = "#FF9800"
    COLOR_HIGHLIGHT = "#FF5722"
    COLOR_SEARCH_FOUND = "#2196F3"
    COLOR_BORDER = "#333333"
    COLOR_TEXT = "#000000"
    
    def __init__(self, root):
        """
        Initialize the GUI application.
        
        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("Hash Table Simulator - Interactive Visualization")
        self.root.geometry("1400x900")
        self.root.configure(bg="#f0f0f0")
        
        # Hash table instance
        self.hash_table: Optional[HashTable] = None
        self.animation_delay = 300  # milliseconds
        
        # Setup GUI components
        self.setup_ui()
        
        # Initialize with default hash table
        self.create_hash_table()
    
    def setup_ui(self):
        """Set up all UI components."""
        # Main container
        main_container = tk.Frame(self.root, bg="#f0f0f0")
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_container,
            text="🔐 Hash Table Simulator",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 10))
        
        # Control Panel (Top)
        self.setup_control_panel(main_container)
        
        # Main content area (Canvas + Log)
        content_frame = tk.Frame(main_container, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas for visualization (Left) — show table below control panel like before
        self.setup_canvas(content_frame)

        # Right side: Pseudocode and Collision Steps panels
        self.setup_right_panels(content_frame)
        
        # Status bar (Bottom)
        self.setup_status_bar(main_container)
    
    def setup_control_panel(self, parent):
        """Set up the control panel with input fields and buttons."""
        control_frame = tk.LabelFrame(
            parent,
            text="Control Panel",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            padx=8,
            pady=6
        )
        control_frame.pack(fill=tk.X, padx=5, pady=5)

        # Split control panel: left = controls, right = inline visualizer
        left_controls = tk.Frame(control_frame, bg="#ffffff")
        left_controls.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))

        right_viz = tk.Frame(control_frame, bg="#ffffff")
        right_viz.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
        
        # Row 1: Table Configuration
        config_frame = tk.Frame(left_controls, bg="#ffffff")
        config_frame.pack(fill=tk.X, pady=2)
        
        tk.Label(config_frame, text="Table Size:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=5)
        self.size_var = tk.StringVar(value="10")
        tk.Entry(config_frame, textvariable=self.size_var, width=10, font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Label(config_frame, text="Collision Mode:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=15)
        self.mode_var = tk.StringVar(value="chaining")
        mode_combo = ttk.Combobox(
            config_frame,
            textvariable=self.mode_var,
            values=["chaining", "linear", "quadratic", "double"],
            state="readonly",
            width=12,
            font=("Arial", 10)
        )
        mode_combo.pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            config_frame,
            text="Create New Table",
            command=self.create_hash_table,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        ).pack(side=tk.LEFT, padx=15)
        
        tk.Button(
            config_frame,
            text="Clear Table",
            command=self.clear_table,
            bg="#FF5722",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        # Row 2: Operations
        ops_frame = tk.Frame(left_controls, bg="#ffffff")
        ops_frame.pack(fill=tk.X, pady=2)
        
        tk.Label(ops_frame, text="Key(s):", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=5)
        self.key_var = tk.StringVar()
        tk.Entry(ops_frame, textvariable=self.key_var, width=30, font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Label(
            ops_frame,
            text="(comma-separated for multiple)",
            font=("Arial", 8, "italic"),
            bg="#ffffff",
            fg="#666666"
        ).pack(side=tk.LEFT, padx=5)
        
        # Operation buttons
        button_frame = tk.Frame(left_controls, bg="#ffffff")
        button_frame.pack(fill=tk.X, pady=2)
        
        tk.Button(
            button_frame,
            text="➕ Insert",
            command=self.insert_key,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            padx=5,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="🔍 Search",
            command=self.search_key,
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            padx=5,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="🗑️ Delete",
            command=self.delete_key,
            bg="#FF9800",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            padx=5,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="📊 Show All Keys",
            command=self.show_all_keys,
            bg="#9C27B0",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            padx=5,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        # Row 3: Advanced operations
        adv_frame = tk.Frame(left_controls, bg="#ffffff")
        adv_frame.pack(fill=tk.X, pady=2)
        
        tk.Label(adv_frame, text="New Size:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=5)
        self.new_size_var = tk.StringVar(value="15")
        tk.Entry(adv_frame, textvariable=self.new_size_var, width=10, font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            adv_frame,
            text="🔄 Resize & Rehash",
            command=self.resize_table,
            bg="#607D8B",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        # Animation speed control
        tk.Label(adv_frame, text="Animation Speed:", font=("Arial", 10), bg="#ffffff").pack(side=tk.LEFT, padx=15)
        self.speed_var = tk.IntVar(value=800)
        speed_scale = tk.Scale(
            adv_frame,
            from_=200,
            to=2000,
            orient=tk.HORIZONTAL,
            variable=self.speed_var,
            length=150,
            bg="#ffffff",
            font=("Arial", 8)
        )
        speed_scale.pack(side=tk.LEFT, padx=5)
        tk.Label(adv_frame, text="ms (slower = more detail)", font=("Arial", 8), bg="#ffffff").pack(side=tk.LEFT)

        # Inline Hash Table Visualizer placed on the RIGHT
        inline_viz = tk.LabelFrame(
            right_viz,
            text="Hash Table Visualization",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            padx=6,
            pady=6
        )
        inline_viz.pack(fill=tk.BOTH, expand=True)

        canvas_container = tk.Frame(inline_viz, bg="#ffffff")
        canvas_container.pack(fill=tk.BOTH, expand=True)

        # Inline summary canvas (header only)
        self.inline_canvas = tk.Canvas(
            canvas_container,
            bg="#ffffff",
            width=520,
            height=140,
            highlightthickness=0
        )
        self.inline_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(canvas_container, orient=tk.VERTICAL, command=self.inline_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.inline_canvas.configure(yscrollcommand=scrollbar.set)

        # Enable inline header mode so the main canvas skips header drawing
        self.inline_header_enabled = True
    
    def setup_canvas(self, parent):
        """Set up the canvas for hash table visualization."""
        canvas_frame = tk.LabelFrame(
            parent,
            text="Hash Table Visualization",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Canvas with scrollbar
        canvas_container = tk.Frame(canvas_frame, bg="#ffffff")
        canvas_container.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(
            canvas_container,
            bg="#ffffff",
            highlightthickness=0
        )
        
        scrollbar = tk.Scrollbar(canvas_container, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def setup_right_panels(self, parent):
        """Set up pseudocode panel and collision steps panel."""
        right_frame = tk.Frame(parent, bg="#fdfdfd")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5)

        # Pseudocode Panel
        pseudo_frame = tk.LabelFrame(
            right_frame,
            text="Pseudocode",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            padx=8,
            pady=8
        )
        pseudo_frame.pack(fill=tk.BOTH, expand=True)

        self.pseudo_text = tk.Text(
            pseudo_frame,
            width=40,
            height=12,
            font=("Courier New", 10),
            bg="#f8f8f8",
            fg="#000",
            wrap=tk.NONE,
            spacing1=2,
            spacing3=2
        )
        self.pseudo_text.pack(fill=tk.BOTH, expand=True)
        self.pseudo_text.tag_configure("hl", background="#FFD700", foreground="#000", font=("Courier New", 10, "bold"))
        self.pseudo_text.tag_configure("comment", foreground="#008000", font=("Courier New", 10, "italic"))

        # Variables display under pseudocode
        self.var_label = tk.Label(pseudo_frame, text="Variables: (waiting for operation...)", anchor=tk.W, justify=tk.LEFT, font=("Courier New", 9, "bold"), bg="#ffffff", fg="#00008B")
        self.var_label.pack(fill=tk.X, pady=(6, 0))

        # Controls for step/auto
        controls = tk.Frame(pseudo_frame, bg="#ffffff")
        controls.pack(fill=tk.X, pady=(6, 0))
        self.auto_running = False
        tk.Button(controls, text="Step", command=self.step_once, bg="#4CAF50", fg="white", width=10, font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=3)
        self.auto_btn = tk.Button(controls, text="Auto Run", command=self.toggle_auto_run, bg="#2196F3", fg="white", width=12, font=("Arial", 9, "bold"))
        self.auto_btn.pack(side=tk.LEFT, padx=3)
        tk.Button(controls, text="Reset Steps", command=self.clear_steps, bg="#FF9800", fg="white", width=12, font=("Arial", 9)).pack(side=tk.LEFT, padx=3)
        tk.Button(controls, text="Copy Log", command=self.copy_steps, bg="#607D8B", fg="white", width=10, font=("Arial", 9)).pack(side=tk.LEFT, padx=3)

        # Collision Steps Panel
        steps_frame = tk.LabelFrame(
            right_frame,
            text="Collision Steps",
            font=("Arial", 12, "bold"),
            bg="#ffffff",
            padx=8,
            pady=8
        )
        steps_frame.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

        self.steps_text = scrolledtext.ScrolledText(
            steps_frame,
            width=48,
            height=12,
            font=("Courier New", 10),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="white"
        )
        self.steps_text.pack(fill=tk.BOTH, expand=True)
        
        # Initial helpful message
        self.steps_text.insert(tk.END, "Execution steps will appear here...\n\n")
        self.steps_text.insert(tk.END, "• Insert a key to see step-by-step execution\n")
        self.steps_text.insert(tk.END, "• Use 'Step' button to advance manually\n")
        self.steps_text.insert(tk.END, "• Use 'Auto Run' for automatic stepping\n")
        self.steps_text.insert(tk.END, "• Adjust animation speed with the slider above\n")

        # Internal step state
        self._current_steps = []
        self._current_step_index = 0
    
    def setup_status_bar(self, parent):
        """Set up the status bar."""
        status_frame = tk.Frame(parent, bg="#333333", height=30)
        status_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready",
            font=("Arial", 10),
            bg="#333333",
            fg="#ffffff",
            anchor=tk.W,
            padx=10
        )
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.info_label = tk.Label(
            status_frame,
            text="Size: 0 | Elements: 0 | Load Factor: 0.00",
            font=("Arial", 10),
            bg="#333333",
            fg="#00ff00",
            anchor=tk.E,
            padx=10
        )
        self.info_label.pack(side=tk.RIGHT)

    def draw_inline_header(self):
        """Draw the compact header summary inside the inline canvas (in Control Panel)."""
        if not hasattr(self, 'inline_canvas'):
            return
        c = self.inline_canvas
        c.delete("all")
        width = int(c.winfo_width() or 520)
        height = int(c.winfo_height() or 260)
        # Clean white background with subtle border
        c.create_rectangle(0, 0, width, height, fill="#f8f9fa", outline="#e0e0e0", width=1)
        # If table not ready, show placeholder title
        if not self.hash_table:
            c.create_text(width//2, 30, text="🔐 HASH TABLE VISUALIZER", font=("Arial", 16, "bold"), fill="#000080")
            c.create_text(width//2, 70, text="Create a table to see summary here", font=("Arial", 11), fill="#333")
            return
        # Stats
        size = self.hash_table.size
        count = self.hash_table.count
        load = self.hash_table.get_load_factor()
        mode = self.hash_table.mode.upper()
        mode_icons = {"CHAINING":"🔗","LINEAR":"➡️","QUADRATIC":"📐","DOUBLE":"🔁"}
        icon = mode_icons.get(mode, "🔐")
        c.create_text(width//2, 30, text="🔐 HASH TABLE VISUALIZER", font=("Arial", 16, "bold"), fill="#000080")
        c.create_text(width//2, 60, text=f"{icon}  Mode: {mode}", font=("Arial", 13, "bold"), fill="#2c3e50")
        # Row
        stats_y = 90
        c.create_text(30, stats_y, text=f"🧮 Size: {size}", font=("Arial", 11, "bold"), fill="#0b5394", anchor="w")
        c.create_text(width//2 - 40, stats_y, text=f"⚙️ Elements: {count}", font=("Arial", 11, "bold"), fill="#0b5394", anchor="w")
        # Load factor bar
        gx, gy, gw, gh = width//2 + 80, stats_y-10, 150, 18
        c.create_rectangle(gx, gy, gx+gw, gy+gh, outline="#777", width=2, fill="#eee")
        fill_w = int(gw * load) if load <= 1 else gw
        lf_color = "#4CAF50" if load < 0.5 else ("#FFC107" if load < 0.75 else "#F44336")
        if fill_w > 0:
            c.create_rectangle(gx, gy, gx+fill_w, gy+gh, outline="", fill=lf_color)
        c.create_text(gx+gw-12, gy+gh/2, text=f"{load:.2f}", font=("Arial", 10, "bold"), fill="#000", anchor="e")
        # Footer row
        c.create_text(30, stats_y+25, text=f"✳️ Collisions: {getattr(self.hash_table, 'collision_count', 0) if hasattr(self.hash_table, 'collision_count') else 0}", font=("Arial", 11, "bold"), fill="#8e44ad", anchor="w")
        c.create_text(width//2, stats_y+25, text=f"🧩 Hash: h(k) = k mod {size}", font=("Arial", 11), fill="#2c3e50", anchor="w")
    
    def setup_stats_panel(self, parent):
        """Set up creative statistics and insights visualization panel."""
        stats_frame = tk.LabelFrame(
            parent,
            text="📊 Real-Time Statistics & Insights",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        stats_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Create canvas for custom visualizations
        self.stats_canvas = tk.Canvas(
            stats_frame,
            bg="#f8f9fa",
            height=180,
            highlightthickness=1,
            highlightbackground="#e0e0e0"
        )
        self.stats_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Initialize stats display
        self.update_stats_visualization()
    
    def update_stats_visualization(self):
        """Draw creative statistics visualization with gauges and charts."""
        self.stats_canvas.delete("all")
        
        if not self.hash_table:
            # Welcome state - show getting started message
            self.draw_stats_welcome()
            return
        
        # Get statistics
        size = self.hash_table.size
        count = self.hash_table.count
        load_factor = self.hash_table.get_load_factor()
        mode = self.hash_table.mode
        collisions = len(self.hash_table.collision_log) if hasattr(self.hash_table, 'collision_log') else 0
        
        # Background gradient
        for i in range(0, 180, 3):
            color_val = 248 - int(i * 0.1)
            color = f"#{color_val:02x}{color_val:02x}{253:02x}"
            self.stats_canvas.create_rectangle(0, i, 400, i+3, fill=color, outline="")
        
        # Title with mode icon
        mode_icons = {
            'chaining': '🔗',
            'linear': '➡️',
            'quadratic': '📐',
            'double': '🔁'
        }
        icon = mode_icons.get(mode, '🔐')
        self.stats_canvas.create_text(
            200, 20,
            text=f"{icon} {mode.upper()} MODE",
            font=("Arial", 14, "bold"),
            fill="#1a237e"
        )
        
        # Row 1: Load Factor Gauge (left) + Elements Counter (right)
        self.draw_circular_gauge(60, 80, 40, load_factor, "Load Factor")
        self.draw_element_counter(180, 60, count, size)
        
        # Row 2: Collision Meter (left) + Performance Indicator (right)
        self.draw_collision_meter(60, 145, collisions)
        self.draw_performance_indicator(200, 140, load_factor, collisions)
        
    def draw_stats_welcome(self):
        """Draw welcome message when no table exists."""
        # Gradient background
        for i in range(0, 180, 3):
            color_val = 250 - int(i * 0.15)
            self.stats_canvas.create_rectangle(0, i, 400, i+3, fill=f"#{color_val:02x}{250:02x}{color_val:02x}", outline="")
        
        # Welcome icon
        self.stats_canvas.create_text(
            200, 50,
            text="🎯",
            font=("Arial", 40)
        )
        
        # Message
        self.stats_canvas.create_text(
            200, 100,
            text="Create a hash table to see\nreal-time statistics here!",
            font=("Arial", 12, "bold"),
            fill="#424242",
            justify=tk.CENTER
        )
        
        # Tip
        self.stats_canvas.create_rectangle(30, 135, 370, 165, fill="#e3f2fd", outline="#2196F3", width=2)
        self.stats_canvas.create_text(
            200, 150,
            text="💡 Tip: Stats update automatically with every operation",
            font=("Arial", 9, "italic"),
            fill="#1565c0"
        )
    
    def draw_circular_gauge(self, cx, cy, radius, value, label):
        """Draw a circular gauge for load factor."""
        # Background circle
        self.stats_canvas.create_oval(
            cx - radius, cy - radius,
            cx + radius, cy + radius,
            fill="#e0e0e0",
            outline="#9e9e9e",
            width=2
        )
        
        # Filled arc based on value
        if value > 0:
            extent = -360 * value  # Negative for clockwise
            # Color based on value
            if value < 0.5:
                fill_color = "#4CAF50"  # Green
            elif value < 0.75:
                fill_color = "#FFC107"  # Yellow
            else:
                fill_color = "#F44336"  # Red
            
            self.stats_canvas.create_arc(
                cx - radius + 5, cy - radius + 5,
                cx + radius - 5, cy + radius - 5,
                start=90,
                extent=extent,
                fill=fill_color,
                outline=""
            )
        
        # Center circle (white)
        inner_r = radius - 12
        self.stats_canvas.create_oval(
            cx - inner_r, cy - inner_r,
            cx + inner_r, cy + inner_r,
            fill="#ffffff",
            outline=""
        )
        
        # Value text
        self.stats_canvas.create_text(
            cx, cy - 5,
            text=f"{value:.2f}",
            font=("Arial", 14, "bold"),
            fill="#212121"
        )
        
        # Label
        self.stats_canvas.create_text(
            cx, cy + 55,
            text=label,
            font=("Arial", 9, "bold"),
            fill="#424242"
        )
    
    def draw_element_counter(self, x, y, count, size):
        """Draw element counter with animated bars."""
        # Box background
        self.stats_canvas.create_rectangle(
            x - 80, y,
            x + 80, y + 60,
            fill="#ffffff",
            outline="#2196F3",
            width=2
        )
        
        # Icon
        self.stats_canvas.create_text(
            x - 50, y + 15,
            text="📦",
            font=("Arial", 20)
        )
        
        # Count
        self.stats_canvas.create_text(
            x + 20, y + 15,
            text=f"{count} / {size}",
            font=("Arial", 16, "bold"),
            fill="#1976d2"
        )
        
        # Progress bar
        bar_width = 140
        bar_x = x - 70
        bar_y = y + 38
        
        # Background bar
        self.stats_canvas.create_rectangle(
            bar_x, bar_y,
            bar_x + bar_width, bar_y + 12,
            fill="#e3f2fd",
            outline="#90caf9",
            width=1
        )
        
        # Filled bar
        if size > 0:
            fill_width = int((count / size) * bar_width)
            if fill_width > 0:
                fill_color = "#4CAF50" if count < size * 0.7 else "#FF9800"
                self.stats_canvas.create_rectangle(
                    bar_x, bar_y,
                    bar_x + fill_width, bar_y + 12,
                    fill=fill_color,
                    outline=""
                )
        
        # Percentage text
        percentage = (count / size * 100) if size > 0 else 0
        self.stats_canvas.create_text(
            x, bar_y + 6,
            text=f"{percentage:.0f}%",
            font=("Arial", 8, "bold"),
            fill="#ffffff" if percentage > 30 else "#424242"
        )
    
    def draw_collision_meter(self, x, y, collisions):
        """Draw collision counter with visual indicator."""
        # Label
        self.stats_canvas.create_text(
            x, y - 10,
            text="💥 Collisions",
            font=("Arial", 9, "bold"),
            fill="#424242"
        )
        
        # Meter background
        meter_width = 100
        meter_height = 20
        self.stats_canvas.create_rectangle(
            x - meter_width/2, y,
            x + meter_width/2, y + meter_height,
            fill="#fff3e0",
            outline="#ff9800",
            width=2
        )
        
        # Collision count
        self.stats_canvas.create_text(
            x, y + meter_height/2,
            text=f"{collisions}",
            font=("Arial", 12, "bold"),
            fill="#e65100"
        )
        
        # Visual bars
        bar_count = min(collisions, 5)
        for i in range(bar_count):
            bar_x = x - meter_width/2 + 10 + i * 18
            bar_height = 5 + i * 2
            self.stats_canvas.create_rectangle(
                bar_x, y - 25,
                bar_x + 8, y - 25 + bar_height,
                fill="#ff5722",
                outline=""
            )
    
    def draw_performance_indicator(self, x, y, load_factor, collisions):
        """Draw performance status indicator."""
        # Determine performance status
        if load_factor < 0.5 and collisions < 3:
            status = "EXCELLENT"
            color = "#4CAF50"
            emoji = "⚡"
        elif load_factor < 0.7 and collisions < 10:
            status = "GOOD"
            color = "#8BC34A"
            emoji = "✅"
        elif load_factor < 0.85:
            status = "MODERATE"
            color = "#FFC107"
            emoji = "⚠️"
        else:
            status = "CRITICAL"
            color = "#F44336"
            emoji = "🔥"
        
        # Box
        self.stats_canvas.create_rectangle(
            x - 90, y,
            x + 90, y + 35,
            fill=color,
            outline="",
            width=0
        )
        
        # Inner glow effect
        self.stats_canvas.create_rectangle(
            x - 88, y + 2,
            x + 88, y + 33,
            fill=color,
            outline="#ffffff",
            width=2
        )
        
        # Status text
        self.stats_canvas.create_text(
            x - 30, y + 17,
            text=f"{emoji} {status}",
            font=("Arial", 11, "bold"),
            fill="#ffffff"
        )
        
        # Animated pulse dots
        dot_y = y + 17
        for i in range(3):
            dot_x = x + 40 + i * 15
            dot_size = 4 - i
            self.stats_canvas.create_oval(
                dot_x - dot_size, dot_y - dot_size,
                dot_x + dot_size, dot_y + dot_size,
                fill="#ffffff",
                outline=""
            )
    
    def create_hash_table(self):
        """Create a new hash table with specified parameters."""
        try:
            size = int(self.size_var.get())
            if size < 1 or size > 100:
                messagebox.showerror("Invalid Size", "Table size must be between 1 and 100")
                return
            
            mode = self.mode_var.get()
            self.hash_table = HashTable(size=size, mode=mode)
            
            self.append_compact_log(f"Created new hash table: Size={size}, Mode={mode}")
            self.update_status(f"New hash table created with {size} buckets ({mode} mode)")
            self.draw_hash_table()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for table size")
    
    def clear_table(self):
        """Clear all elements from the hash table."""
        if self.hash_table:
            self.hash_table.clear()
            self.append_compact_log("Table cleared")
            self.update_status("Hash table cleared")
            self.draw_hash_table()
    
    def insert_key(self):
        """Insert key(s) into the hash table."""
        if not self.hash_table:
            messagebox.showwarning("No Table", "Please create a hash table first")
            return
        
        key_input = self.key_var.get().strip()
        if not key_input:
            messagebox.showwarning("Empty Input", "Please enter at least one key")
            return
        
        # Parse keys (comma-separated)
        keys = [k.strip() for k in key_input.split(',')]
        
        # Try to convert to integers if possible
        parsed_keys = []
        for k in keys:
            try:
                parsed_keys.append(int(k))
            except ValueError:
                parsed_keys.append(k)  # Keep as string
        
        # Insert each key with visualization, pseudocode, and steps
        for key in parsed_keys:
            self.run_insert_with_pseudocode(key)
        
        self.draw_hash_table()
        self.key_var.set("")
        self.update_status(f"Inserted {len(parsed_keys)} key(s)")
    
    def search_key(self):
        """Search for a key in the hash table."""
        if not self.hash_table:
            messagebox.showwarning("No Table", "Please create a hash table first")
            return
        
        key_input = self.key_var.get().strip()
        if not key_input:
            messagebox.showwarning("Empty Input", "Please enter a key to search")
            return
        
        # Try to convert to integer
        try:
            key = int(key_input)
        except ValueError:
            key = key_input
        
        found, index, message = self.hash_table.search(key)
        
        self.append_compact_log(f"🔍 {message}")
        
        if found:
            self.draw_hash_table()
            self.highlight_bucket(index, self.COLOR_SEARCH_FOUND)
            messagebox.showinfo("Search Result", message)
        else:
            messagebox.showinfo("Search Result", message)
        
        self.update_status(message)
    
    def delete_key(self):
        """Delete a key from the hash table."""
        if not self.hash_table:
            messagebox.showwarning("No Table", "Please create a hash table first")
            return
        
        key_input = self.key_var.get().strip()
        if not key_input:
            messagebox.showwarning("Empty Input", "Please enter a key to delete")
            return
        
        # Try to convert to integer
        try:
            key = int(key_input)
        except ValueError:
            key = key_input
        
        success, index, message = self.hash_table.delete(key)
        
        self.append_compact_log(f"🗑️ {message}")
        
        if success:
            self.draw_hash_table()
            if index >= 0:
                self.highlight_bucket(index, self.COLOR_HIGHLIGHT)
        
        messagebox.showinfo("Delete Result", message)
        self.key_var.set("")
        self.update_status(message)
    
    def show_all_keys(self):
        """Display all keys currently in the hash table."""
        if not self.hash_table:
            messagebox.showwarning("No Table", "Please create a hash table first")
            return
        
        keys = self.hash_table.get_all_keys()
        
        if keys:
            keys_str = ", ".join([str(k) for k in keys])
            self.append_compact_log(f"📊 All keys: {keys_str}")
            messagebox.showinfo("All Keys", f"Keys in table:\n{keys_str}")
        else:
            self.append_compact_log("📊 Hash table is empty")
            messagebox.showinfo("All Keys", "Hash table is empty")
    
    def resize_table(self):
        """Resize the hash table and rehash all elements."""
        if not self.hash_table:
            messagebox.showwarning("No Table", "Please create a hash table first")
            return
        
        try:
            new_size = int(self.new_size_var.get())
            if new_size < 1 or new_size > 100:
                messagebox.showerror("Invalid Size", "New size must be between 1 and 100")
                return
            
            message = self.hash_table.resize(new_size)
            self.append_compact_log(f"🔄 {message}")
            self.update_status(message)
            self.draw_hash_table()
            messagebox.showinfo("Resize Complete", message)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for new size")
    
    def draw_hash_table(self):
        """Draw the hash table visualization on canvas with creative decorative elements."""
        self.canvas.delete("all")
        # If we have an inline header, refresh it too
        if getattr(self, 'inline_header_enabled', False) and hasattr(self, 'inline_canvas'):
            self.draw_inline_header()
        
        if not self.hash_table:
            # Draw welcome screen when no table exists
            self.draw_welcome_screen()
            return
        
        # Calculate dimensions
        bucket_width = 120
        bucket_height = 60
        margin = 20
        x_offset = 50
        # If header is drawn inline, start near top; otherwise leave room for header
        y_start = 30 if getattr(self, 'inline_header_enabled', False) else 150
        
        # Get statistics
        size = self.hash_table.size
        count = self.hash_table.count
        load_factor = self.hash_table.get_load_factor()
        mode = self.hash_table.mode.upper()
        
        # ========== DECORATIVE HEADER ==========
        if not getattr(self, 'inline_header_enabled', False):
            header_height = 130
            for i in range(0, header_height, 2):
                shade = 250 - int(i * 0.3)
                color = f"#{shade:02x}{shade:02x}{255:02x}"
                self.canvas.create_rectangle(0, i, 1000, i+2, fill=color, outline=color)
            self.canvas.create_text(250, 25, text="🔐 HASH TABLE VISUALIZER", font=("Arial", 20, "bold"), fill="#000080", anchor="center")
            mode_icons = {"CHAINING":"🔗","LINEAR":"➡️","QUADRATIC":"📐","DOUBLE":"🔁"}
            icon = mode_icons.get(mode, "🔐")
            self.canvas.create_text(250, 55, text=f"{icon}  Mode: {mode}", font=("Arial", 16, "bold"), fill="#4B0082", anchor="center")
            stats_y = 90
            self.canvas.create_text(80, stats_y, text=f"🧮  Size: {size}", font=("Arial", 12, "bold"), fill="#0b5394", anchor="w")
            self.canvas.create_text(220, stats_y, text=f"⚙️  Elements: {count}", font=("Arial", 12, "bold"), fill="#0b5394", anchor="w")
            gauge_x, gauge_y, gauge_w, gauge_h = 330, stats_y-10, 150, 20
            self.canvas.create_rectangle(gauge_x, gauge_y, gauge_x+gauge_w, gauge_y+gauge_h, outline="#777", width=2, fill="#eee")
            fill_w = int(gauge_w * load_factor) if load_factor <= 1 else gauge_w
            lf_color = "#4CAF50" if load_factor < 0.5 else ("#FFC107" if load_factor < 0.75 else "#F44336")
            if fill_w > 0:
                self.canvas.create_rectangle(gauge_x, gauge_y, gauge_x+fill_w, gauge_y+gauge_h, outline="", fill=lf_color)
            self.canvas.create_text(gauge_x+gauge_w-15, gauge_y+gauge_h/2, text=f"{load_factor:.2f}", font=("Arial", 11, "bold"), fill="#000", anchor="e")
            self.canvas.create_text(80, stats_y+25, text=f"✳️  Collisions: {getattr(self.hash_table, 'collision_count', 0) if hasattr(self.hash_table, 'collision_count') else 0}", font=("Arial", 12, "bold"), fill="#6a1b9a", anchor="w")
            self.canvas.create_text(330, stats_y+25, text=f"🧩  Hash: h(k) = k mod {size}", font=("Arial", 12), fill="#333", anchor="w")
            
        
        
        
        # ========== BUCKET VISUALIZATION ==========
        max_chain_length = 1
        if self.hash_table.mode == 'chaining':
            for i in range(size):
                chain_length = len(self.hash_table.get_bucket_contents(i))
                max_chain_length = max(max_chain_length, chain_length)
        
        # Draw each bucket
        for i in range(size):
            y = y_start + i * (bucket_height + margin)
            
            # Decorative row background (alternating subtle colors)
            row_color = "#fafafa" if i % 2 == 0 else "#ffffff"
            self.canvas.create_rectangle(
                0, y - 5,
                520, y + bucket_height + 5,
                fill=row_color,
                outline=""
            )
            
            # Bucket index label with icon
            index_icon = "▶" if i < 10 else "⏩"
            self.canvas.create_text(
                x_offset - 35,
                y + bucket_height // 2,
                text=f"{index_icon}",
                font=("Arial", 10),
                fill="#4a90e2"
            )
            
            self.canvas.create_text(
                x_offset - 15,
                y + bucket_height // 2,
                text=f"{i}",
                font=("Arial", 12, "bold"),
                fill=self.COLOR_TEXT
            )
            
            # Get bucket contents
            contents = self.hash_table.get_bucket_contents(i)
            
            if not contents:
                # Empty bucket with creative styling
                self.canvas.create_rectangle(
                    x_offset, y,
                    x_offset + bucket_width, y + bucket_height,
                    fill=self.COLOR_EMPTY,
                    outline=self.COLOR_BORDER,
                    width=2,
                    tags=f"bucket_{i}"
                )
                
                # Draw dotted pattern for empty
                for dx in range(10, bucket_width, 20):
                    for dy in range(10, bucket_height, 20):
                        self.canvas.create_oval(
                            x_offset + dx - 1, y + dy - 1,
                            x_offset + dx + 1, y + dy + 1,
                            fill="#e0e0e0",
                            outline="",
                            tags=f"bucket_{i}"
                        )
                
                self.canvas.create_text(
                    x_offset + bucket_width // 2,
                    y + bucket_height // 2,
                    text="∅ EMPTY",
                    font=("Arial", 10, "italic"),
                    fill="#cccccc",
                    tags=f"bucket_{i}"
                )
            else:
                # Draw based on mode
                if self.hash_table.mode == 'chaining':
                    # Draw chain with arrows
                    for idx, key in enumerate(contents):
                        x = x_offset + idx * (bucket_width + 15)
                        
                        # Chain link number badge
                        if idx > 0:
                            self.canvas.create_oval(
                                x - 10, y + bucket_height//2 - 10,
                                x - 10 + 20, y + bucket_height//2 + 10,
                                fill="#ff9800",
                                outline="#f57c00",
                                width=2
                            )
                            self.canvas.create_text(
                                x, y + bucket_height//2,
                                text=str(idx),
                                font=("Arial", 9, "bold"),
                                fill="white"
                            )
                        
                        # Rectangle for key
                        color = self.COLOR_COLLISION if idx > 0 else self.COLOR_FILLED
                        self.canvas.create_rectangle(
                            x, y,
                            x + bucket_width, y + bucket_height,
                            fill=color,
                            outline=self.COLOR_BORDER,
                            width=2,
                            tags=f"bucket_{i}"
                        )
                        
                        # Key icon
                        self.canvas.create_text(
                            x + 20, y + bucket_height // 2,
                            text="🔑",
                            font=("Arial", 12),
                            tags=f"bucket_{i}"
                        )
                        
                        # Key text
                        self.canvas.create_text(
                            x + bucket_width // 2 + 10,
                            y + bucket_height // 2,
                            text=str(key),
                            font=("Arial", 12, "bold"),
                            fill="white",
                            tags=f"bucket_{i}"
                        )
                        
                        # Arrow to next
                        if idx < len(contents) - 1:
                            arrow_x = x + bucket_width + 7
                            self.canvas.create_text(
                                arrow_x,
                                y + bucket_height // 2,
                                text="⇨",
                                font=("Arial", 16, "bold"),
                                fill=self.COLOR_COLLISION
                            )
                else:
                    # Open addressing - single key with tombstone support
                    if contents[0] == "TOMBSTONE":
                        # Tombstone styling
                        self.canvas.create_rectangle(
                            x_offset, y,
                            x_offset + bucket_width, y + bucket_height,
                            fill="#9e9e9e",
                            outline=self.COLOR_BORDER,
                            width=2,
                            tags=f"bucket_{i}",
                            stipple="gray50"
                        )
                        self.canvas.create_text(
                            x_offset + bucket_width // 2,
                            y + bucket_height // 2,
                            text="🪦 TOMBSTONE",
                            font=("Arial", 10, "bold"),
                            fill="white",
                            tags=f"bucket_{i}"
                        )
                    else:
                        # Regular key
                        self.canvas.create_rectangle(
                            x_offset, y,
                            x_offset + bucket_width, y + bucket_height,
                            fill=self.COLOR_FILLED,
                            outline=self.COLOR_BORDER,
                            width=2,
                            tags=f"bucket_{i}"
                        )
                        
                        # Key icon
                        self.canvas.create_text(
                            x_offset + 20, y + bucket_height // 2,
                            text="🔑",
                            font=("Arial", 12),
                            tags=f"bucket_{i}"
                        )
                        
                        self.canvas.create_text(
                            x_offset + bucket_width // 2 + 10,
                            y + bucket_height // 2,
                            text=str(contents[0]),
                            font=("Arial", 12, "bold"),
                            fill="white",
                            tags=f"bucket_{i}"
                        )
        
        # ========== FOOTER INFO ==========
        footer_y = y_start + size * (bucket_height + margin) + 20
        
        # Tips box
        self.canvas.create_rectangle(
            20, footer_y,
            480, footer_y + 60,
            fill="#e3f2fd",
            outline="#2196f3",
            width=2
        )
        
        self.canvas.create_text(
            250, footer_y + 15,
            text="💡 Quick Tips",
            font=("Arial", 11, "bold"),
            fill="#1976d2"
        )
        
        tips = {
            "chaining": "Chains can grow indefinitely • No table full condition",
            "linear": "Sequential probing • Watch for primary clustering",
            "quadratic": "i² spacing reduces clustering • Best with prime m",
            "double": "Dual hash functions • Minimal clustering"
        }
        
        tip_text = tips.get(self.hash_table.mode, "Hash table operations")
        self.canvas.create_text(
            250, footer_y + 40,
            text=tip_text,
            font=("Arial", 10),
            fill="#424242"
        )
        
        # Update canvas scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        # Update info label
        self.update_info_label()
    
    def draw_welcome_screen(self):
        """Draw a creative welcome screen when no hash table exists."""
        # Gradient background
        for i in range(0, 400, 4):
            shade = 240 - int(i * 0.1)
            color = f"#{shade:02x}{shade:02x}{255:02x}"
            self.canvas.create_rectangle(
                0, i, 600, i+4,
                fill=color, outline=color
            )
        
        # Large title
        self.canvas.create_text(
            300, 100,
            text="🔐 HASH TABLE SIMULATOR",
            font=("Arial", 24, "bold"),
            fill="#1a237e"
        )
        
        self.canvas.create_text(
            300, 140,
            text="Educational Visualization Tool",
            font=("Arial", 14, "italic"),
            fill="#283593"
        )
        
        # Feature boxes
        features = [
            ("🔗", "Chaining", "Linked list collision resolution"),
            ("➡️", "Linear Probing", "Sequential open addressing"),
            ("📐", "Quadratic Probing", "i² offset probing"),
            ("🔁", "Double Hashing", "Dual hash functions")
        ]
        
        box_y = 200
        for i, (icon, title, desc) in enumerate(features):
            x = 80 + (i % 2) * 260
            y = box_y + (i // 2) * 100
            
            # Box
            self.canvas.create_rectangle(
                x, y, x + 220, y + 80,
                fill="#ffffff",
                outline="#5c6bc0",
                width=2
            )
            
            # Icon
            self.canvas.create_text(
                x + 30, y + 25,
                text=icon,
                font=("Arial", 20)
            )
            
            # Title
            self.canvas.create_text(
                x + 130, y + 20,
                text=title,
                font=("Arial", 12, "bold"),
                fill="#1a237e"
            )
            
            # Description
            self.canvas.create_text(
                x + 130, y + 50,
                text=desc,
                font=("Arial", 9),
                fill="#666666"
            )
        
        # Instructions
        self.canvas.create_text(
            300, 420,
            text="👆 Start by creating a hash table using the controls above",
            font=("Arial", 12),
            fill="#f57c00"
        )
        
        # Version/credits
        self.canvas.create_text(
            300, 460,
            text="v2.0 • Real-time Pseudocode Visualization • Interactive Learning",
            font=("Arial", 9, "italic"),
            fill="#9e9e9e"
        )
    
    def highlight_bucket(self, index, color):
        """Highlight a specific bucket with animation."""
        if not self.hash_table or index < 0:
            return
        
        # Get animation delay
        delay = self.speed_var.get()
        
        # Flash the bucket
        for _ in range(2):
            self.canvas.itemconfig(f"bucket_{index}", fill=color)
            self.root.update()
            self.root.after(delay // 2)
            
            contents = self.hash_table.get_bucket_contents(index)
            if contents:
                self.canvas.itemconfig(f"bucket_{index}", fill=self.COLOR_FILLED)
            else:
                self.canvas.itemconfig(f"bucket_{index}", fill=self.COLOR_EMPTY)
            
            self.root.update()
            self.root.after(delay // 2)
    
    def animate_collision(self, index, key):
        """Animate a collision event."""
        delay = self.speed_var.get()
        
        # Draw table
        self.draw_hash_table()
        
        # Highlight collision bucket
        self.highlight_bucket(index, self.COLOR_COLLISION)
        
        # Redraw to show final state
        self.draw_hash_table()

    def animate_open_addressing_collision(self, entry):
        """Animate probing path for open addressing collisions.

        Args:
            entry (dict): Collision log entry with fields:
                - key
                - original_index
                - final_index
                - probes
                - type: 'linear' or 'quadratic' or 'double'
        """
        if not entry:
            return

        # Ensure current mode is open addressing
        if self.hash_table and self.hash_table.mode == 'chaining':
            return

        mode = entry.get('type')
        original = entry.get('original_index')
        final_index = entry.get('final_index')
        probes = entry.get('probes', 0)
        size = self.hash_table.size if self.hash_table else 0

        # Build probe sequence including original and each subsequent probe
        sequence = []
        if size and original is not None:
            # k = 0..probes (k=0 is original position)
            for k in range(0, probes + 1):
                if mode == 'linear':
                    idx = (original + k) % size
                elif mode == 'quadratic':
                    idx = (original + (k * k)) % size
                else:  # double hashing
                    # Need h2 to compute sequence; recompute from key if missing
                    key = entry.get('key')
                    nk_val, _ = normalize_key(key)
                    _h1, _ = h1_fn(nk_val, size)
                    _h2, _ = h2_fn(nk_val, size)
                    idx = (_h1 + k * _h2) % size
                sequence.append(idx)

        # Animate highlighting each probed bucket
        for idx in sequence:
            self.highlight_bucket(idx, self.COLOR_COLLISION)

        # Finally, emphasize the final placement bucket
        self.highlight_bucket(final_index, self.COLOR_FILLED)
        self.draw_hash_table()
    
    def log(self, message):
        """Back-compat: route log messages to steps panel as compact log."""
        self.append_compact_log(message)
    
    def clear_log(self):
        """Clear the operation log."""
        self.clear_steps()
    
    def update_status(self, message):
        """Update the status bar message."""
        self.status_label.configure(text=message)
    
    def update_info_label(self):
        """Update the info label with current statistics."""
        if self.hash_table:
            size = self.hash_table.size
            count = self.hash_table.count
            load_factor = self.hash_table.get_load_factor()
            self.info_label.configure(
                text=f"Size: {size} | Elements: {count} | Load Factor: {load_factor:.2f}"
            )

    # ---------- Pseudocode and Steps Utilities ----------
    def append_compact_log(self, message: str):
        """Append a single-line message to the Collision Steps panel with timestamp."""
        if not hasattr(self, 'steps_text'):
            return
        timestamp = time.strftime("%H:%M:%S")
        self.steps_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.steps_text.see(tk.END)

    def clear_steps(self):
        """Reset the pseudocode execution state."""
        if hasattr(self, 'steps_text'):
            self.steps_text.delete(1.0, tk.END)
            self.steps_text.insert(tk.END, "Execution steps will appear here...\n")
        if hasattr(self, 'pseudo_text'):
            self.pseudo_text.tag_remove("hl", 1.0, tk.END)
        self.var_label.configure(text="Variables: (waiting for operation...)")
        self._current_steps = []
        self._current_step_index = 0
        self.auto_running = False
        if hasattr(self, 'auto_btn'):
            self.auto_btn.configure(text="Auto Run")
        self.update_status("Execution state reset")

    def copy_steps(self):
        try:
            text = self.steps_text.get(1.0, tk.END)
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.update_status("Steps copied to clipboard")
        except Exception:
            pass

    def set_pseudocode_for_insert(self, mode: str):
        """Display clean, proper pseudocode for insert operation."""
        lines = []
        if mode == 'chaining':
            lines = [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  bucket[h1].append(key)",
                "  RETURN success",
            ]
        elif mode == 'linear':
            lines = [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i) % m",
                "    IF bucket[idx] is EMPTY or TOMBSTONE:",
                "      bucket[idx] = key",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN table_full",
            ]
        elif mode == 'quadratic':
            lines = [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i²) % m",
                "    IF bucket[idx] is EMPTY or TOMBSTONE:",
                "      bucket[idx] = key",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN table_full",
            ]
        else:  # double
            lines = [
                "FUNCTION Insert(key, m):",
                "  h1 = hash(key) % m",
                "  h2 = 1 + (hash(key) % (m-1))",
                "  i = 0",
                "  WHILE i < m:",
                "    idx = (h1 + i*h2) % m",
                "    IF bucket[idx] is EMPTY or TOMBSTONE:",
                "      bucket[idx] = key",
                "      RETURN success",
                "    i = i + 1",
                "  RETURN table_full",
            ]
        
        self.pseudo_text.configure(state=tk.NORMAL)
        self.pseudo_text.delete(1.0, tk.END)
        self.pseudo_text.insert(tk.END, "\n".join(lines))
        self.pseudo_text.configure(state=tk.DISABLED)
        self.pseudo_text.tag_remove("hl", 1.0, tk.END)
        self.var_label.configure(text="Variables: (ready to execute...)")

    def highlight_pseudo_line(self, line_no: int):
        try:
            self.pseudo_text.configure(state=tk.NORMAL)
            self.pseudo_text.tag_remove("hl", 1.0, tk.END)
            start = f"{line_no}.0"
            end = f"{line_no}.end"
            self.pseudo_text.tag_add("hl", start, end)
            self.pseudo_text.see(start)
            self.pseudo_text.configure(state=tk.DISABLED)
        except Exception:
            pass

    def build_insert_steps(self, key):
        """Build detailed micro-steps for insert operation with proper line mapping."""
        steps = []
        mode = self.hash_table.mode
        m = self.hash_table.size
        nk_val, nk_exp = normalize_key(key)
        h1_val, h1_exp = h1_fn(nk_val, m)
        
        # Map pseudocode lines to actual execution steps
        if mode == 'chaining':
            # Line 1: Compute h1
            steps.append({
                "line": 2,
                "text": f"Computing h1: {h1_exp}",
                "idx": None,
                "vars": {"key": key, "key_int": nk_val, "m": m, "h1": h1_val},
                "highlight_bucket": None
            })
            steps.append({
                "line": 2,
                "text": f"h1 = {h1_val} (hash bucket)",
                "idx": h1_val,
                "vars": {"key": key, "m": m, "h1": h1_val},
                "highlight_bucket": h1_val
            })
            # Line 2: Insert into chain
            steps.append({
                "line": 3,
                "text": f"Inserting key {key} at bucket[{h1_val}]",
                "idx": h1_val,
                "vars": {"key": key, "h1": h1_val},
                "highlight_bucket": h1_val
            })
            steps.append({
                "line": 4,
                "text": f"✓ Successfully inserted {key}",
                "idx": h1_val,
                "vars": {"key": key, "h1": h1_val},
                "highlight_bucket": h1_val
            })
            return steps
        
        # Open addressing modes
        h2_val = None
        h2_exp = None
        if mode == 'double':
            h2_val, h2_exp = h2_fn(nk_val, m)
        
        # Get actual probe sequence from collision log
        probes = 0
        final_idx = None
        probe_sequence = []
        if self.hash_table.collision_log:
            entry = self.hash_table.collision_log[-1]
            if entry.get('key') == key and entry.get('final_index') is not None:
                probes = entry.get('probes', 0)
                final_idx = entry.get('final_index')
        
        # Step 1: Compute h1
        steps.append({
            "line": 2,
            "text": f"Computing h1: {h1_exp}",
            "idx": None,
            "vars": {"key": key, "key_int": nk_val, "m": m, "h1": h1_val},
            "highlight_bucket": None
        })
        steps.append({
            "line": 2,
            "text": f"h1 = {h1_val}",
            "idx": h1_val,
            "vars": {"key": key, "m": m, "h1": h1_val},
            "highlight_bucket": h1_val
        })
        
        # Step 2: Compute h2 (double hashing only)
        if mode == 'double':
            steps.append({
                "line": 3,
                "text": f"Computing h2: {h2_exp}",
                "idx": None,
                "vars": {"key": key, "m": m, "h1": h1_val, "h2": h2_val},
                "highlight_bucket": None
            })
            steps.append({
                "line": 3,
                "text": f"h2 = {h2_val} (step size)",
                "idx": None,
                "vars": {"key": key, "m": m, "h1": h1_val, "h2": h2_val},
                "highlight_bucket": None
            })
        
        # Step 3: Initialize i = 0
        init_line = 3 if mode != 'double' else 4
        steps.append({
            "line": init_line,
            "text": "Initializing probe counter i = 0",
            "idx": None,
            "vars": {"h1": h1_val, "h2": h2_val, "i": 0, "m": m},
            "highlight_bucket": None
        })
        
        # Step 4: WHILE loop iterations
        loop_line = 4 if mode != 'double' else 5
        compute_line = 5 if mode != 'double' else 6
        check_line = 6 if mode != 'double' else 7
        place_line = 7 if mode != 'double' else 8
        break_line = 8 if mode != 'double' else 9
        incr_line = 9 if mode != 'double' else 10
        
        for i in range(probes + 1):
            # Check loop condition
            steps.append({
                "line": loop_line,
                "text": f"Check: i={i} < m={m}? → True, entering loop",
                "idx": None,
                "vars": {"h1": h1_val, "h2": h2_val, "i": i, "m": m},
                "highlight_bucket": None
            })
            
            # Compute idx
            if mode == 'linear':
                idx = (h1_val + i) % m
                formula = f"({h1_val} + {i}) % {m}"
            elif mode == 'quadratic':
                idx = (h1_val + i * i) % m
                formula = f"({h1_val} + {i}²) % {m} = ({h1_val} + {i*i}) % {m}"
            else:  # double
                idx = (h1_val + i * (h2_val or 1)) % m
                formula = f"({h1_val} + {i}*{h2_val}) % {m} = ({h1_val} + {i*(h2_val or 1)}) % {m}"
            
            steps.append({
                "line": compute_line,
                "text": f"Computing idx = {formula}",
                "idx": None,
                "vars": {"h1": h1_val, "h2": h2_val, "i": i, "idx": idx, "m": m},
                "highlight_bucket": None
            })
            steps.append({
                "line": compute_line,
                "text": f"idx = {idx}",
                "idx": idx,
                "vars": {"h1": h1_val, "h2": h2_val, "i": i, "idx": idx},
                "highlight_bucket": idx
            })
            
            # Check if slot is empty/tombstone
            slot_status = self.hash_table.get_bucket_contents(idx)
            is_available = (not slot_status) or (slot_status and slot_status[0] == "TOMBSTONE")
            
            if is_available or i == probes:
                steps.append({
                    "line": check_line,
                    "text": f"Check slot[{idx}]: {'EMPTY/TOMBSTONE' if is_available else 'Available'} → Can insert!",
                    "idx": idx,
                    "vars": {"h1": h1_val, "h2": h2_val, "i": i, "idx": idx},
                    "highlight_bucket": idx
                })
                steps.append({
                    "line": place_line,
                    "text": f"Placing key {key} at slot[{idx}]",
                    "idx": idx,
                    "vars": {"key": key, "idx": idx},
                    "highlight_bucket": idx
                })
                steps.append({
                    "line": break_line,
                    "text": "Breaking out of loop",
                    "idx": idx,
                    "vars": {"key": key, "idx": idx},
                    "highlight_bucket": idx
                })
                break
            else:
                steps.append({
                    "line": check_line,
                    "text": f"Check slot[{idx}]: OCCUPIED → Collision!",
                    "idx": idx,
                    "vars": {"h1": h1_val, "h2": h2_val, "i": i, "idx": idx},
                    "highlight_bucket": idx
                })
                steps.append({
                    "line": incr_line,
                    "text": f"Incrementing i: {i} + 1 = {i+1}",
                    "idx": None,
                    "vars": {"h1": h1_val, "h2": h2_val, "i": i+1},
                    "highlight_bucket": None
                })
        
        # Final success
        done_line = 10 if mode != 'double' else 11
        final_pos = final_idx if final_idx is not None else (idx if 'idx' in locals() else h1_val)
        steps.append({
            "line": done_line,
            "text": f"✓ Insert complete! Key {key} stored at index {final_pos}",
            "idx": final_pos,
            "vars": {"key": key, "final_position": final_pos},
            "highlight_bucket": final_pos
        })
        
        return steps

    def highlight_pseudo_lines(self, start_line, end_line=None):
        """Highlight a range of pseudocode lines (e.g., entire loop block)."""
        self.pseudo_text.tag_remove("hl", 1.0, tk.END)
        if end_line is None:
            end_line = start_line
        
        start = f"{start_line}.0"
        end = f"{end_line}.end"
        self.pseudo_text.tag_add("hl", start, end)
        self.pseudo_text.see(start)
        self.root.update()

    def run_insert_with_realtime_pseudocode(self, key):
        """Execute insert WITH REAL-TIME pseudocode highlighting during insertion."""
        if not self.hash_table:
            messagebox.showerror("Error", "Please create a hash table first!")
            return
        
        mode = self.hash_table.mode
        m = self.hash_table.size
        delay = self.speed_var.get()
        
        # Set pseudocode display
        self.set_pseudocode_for_insert(mode)
        self.draw_hash_table()
        
        # Log start
        self.steps_text.insert(tk.END, f"\n{'='*50}\n")
        self.steps_text.insert(tk.END, f"INSERTING KEY: {key} (Mode: {mode}, Size: {m})\n")
        self.steps_text.insert(tk.END, f"{'='*50}\n")
        self.steps_text.see(tk.END)
        
        # Highlight FUNCTION header
        self.highlight_pseudo_lines(1)
        self.root.after(delay)
        
        # STEP 1: Compute h1
        self.highlight_pseudo_lines(2)
        key_int = int(key) if isinstance(key, (int, str)) and str(key).isdigit() else hash(str(key))
        h1 = key_int % m
        self.steps_text.insert(tk.END, f"→ Computing h1 = {key_int} % {m} = {h1}\n")
        self.steps_text.see(tk.END)
        self.var_label.configure(text=f"Variables: key={key}, h1={h1}, m={m}")
        
        # Highlight the bucket being checked
        if hasattr(self, 'canvas'):
            self.canvas.itemconfig(f"bucket_{h1}", fill=self.COLOR_HIGHLIGHT)
        self.root.update()
        self.root.after(delay)
        
        if mode == 'chaining':
            # CHAINING: Direct insert
            self.highlight_pseudo_lines(3)
            self.steps_text.insert(tk.END, f"→ Appending {key} to bucket[{h1}] chain\n")
            self.steps_text.see(tk.END)
            self.root.update()
            self.root.after(delay)
            
            # Perform actual insertion
            success, index, collision, message = self.hash_table.insert(key)
            self.draw_hash_table()
            
            # Highlight RETURN
            self.highlight_pseudo_lines(4)
            self.steps_text.insert(tk.END, f"→ {message}\n")
            self.steps_text.see(tk.END)
            self.var_label.configure(text=f"Variables: Success! key={key} at bucket[{h1}]")
            
        else:
            # OPEN ADDRESSING: Probing required
            # Compute h2 for double hashing
            h2 = None
            if mode == 'double':
                self.highlight_pseudo_lines(3)
                h2 = 1 + (key_int % (m - 1 if m > 1 else 1))
                self.steps_text.insert(tk.END, f"→ Computing h2 = 1 + ({key_int} % {m-1}) = {h2}\n")
                self.steps_text.see(tk.END)
                self.var_label.configure(text=f"Variables: key={key}, h1={h1}, h2={h2}, m={m}")
                self.root.update()
                self.root.after(delay)
                init_line = 4
                while_line = 5
                idx_line = 6
                if_line = 7
                assign_line = 8
                return_line = 9
                increment_line = 10
            else:
                init_line = 3
                while_line = 4
                idx_line = 5
                if_line = 6
                assign_line = 7
                return_line = 8
                increment_line = 9
            
            # Initialize i = 0
            self.highlight_pseudo_lines(init_line)
            i = 0
            self.steps_text.insert(tk.END, f"→ Initialize probe counter: i = {i}\n")
            self.steps_text.see(tk.END)
            var_text = f"Variables: key={key}, h1={h1}"
            if h2: var_text += f", h2={h2}"
            var_text += f", i={i}, m={m}"
            self.var_label.configure(text=var_text)
            self.root.update()
            self.root.after(delay)
            
            # WHILE LOOP - probe until empty slot found
            max_probes = m
            found_slot = False
            final_idx = None
            
            for probe_num in range(max_probes):
                # Highlight ENTIRE WHILE LOOP BLOCK (lines while through increment)
                self.highlight_pseudo_lines(while_line, increment_line)
                self.steps_text.insert(tk.END, f"\n--- Probe #{probe_num + 1} (i={i}) ---\n")
                self.steps_text.see(tk.END)
                self.root.update()
                self.root.after(delay // 2)
                
                # Compute idx
                self.highlight_pseudo_lines(idx_line)
                if mode == 'linear':
                    idx = (h1 + i) % m
                    formula = f"({h1}+{i})%{m}"
                elif mode == 'quadratic':
                    idx = (h1 + i*i) % m
                    formula = f"({h1}+{i}²)%{m} = ({h1}+{i*i})%{m}"
                else:  # double
                    h2_val = h2 if h2 is not None else 1
                    idx = (h1 + i*h2_val) % m
                    formula = f"({h1}+{i}*{h2_val})%{m}"
                
                self.steps_text.insert(tk.END, f"→ Compute idx = {formula} = {idx}\n")
                self.steps_text.see(tk.END)
                var_text = f"Variables: key={key}, h1={h1}"
                if h2: var_text += f", h2={h2}"
                var_text += f", i={i}, idx={idx}, m={m}"
                self.var_label.configure(text=var_text)
                
                # Highlight the bucket being checked
                if hasattr(self, 'canvas'):
                    self.canvas.itemconfig(f"bucket_{idx}", fill=self.COLOR_HIGHLIGHT)
                self.root.update()
                self.root.after(delay)
                
                # Check slot status
                slot = self.hash_table.get_bucket_contents(idx)
                is_available = (not slot) or (slot and slot[0] == "TOMBSTONE")
                
                # Highlight IF condition check
                self.highlight_pseudo_lines(if_line)
                if is_available:
                    self.steps_text.insert(tk.END, f"→ bucket[{idx}] is {'EMPTY' if not slot else 'TOMBSTONE'} ✓ Available!\n")
                    self.steps_text.see(tk.END)
                    if hasattr(self, 'canvas'):
                        self.canvas.itemconfig(f"bucket_{idx}", fill=self.COLOR_FILLED)
                    self.root.update()
                    self.root.after(delay)
                    
                    # Highlight assignment: bucket[idx] = key
                    self.highlight_pseudo_lines(assign_line)
                    self.steps_text.insert(tk.END, f"→ Inserting: bucket[{idx}] ← {key}\n")
                    self.steps_text.see(tk.END)
                    self.root.update()
                    self.root.after(delay)
                    
                    # Perform actual insertion (we've been checking, now insert for real)
                    # Since we're controlling the process, directly call insert
                    success, index, collision, message = self.hash_table.insert(key)
                    self.draw_hash_table()
                    
                    # Highlight RETURN success
                    self.highlight_pseudo_lines(return_line)
                    self.steps_text.insert(tk.END, f"→ SUCCESS: {message}\n")
                    self.steps_text.see(tk.END)
                    self.var_label.configure(text=f"Variables: Inserted! key={key} at bucket[{idx}] after {i+1} probe(s)")
                    found_slot = True
                    final_idx = idx
                    break
                else:
                    # COLLISION!
                    self.steps_text.insert(tk.END, f"→ bucket[{idx}] is OCCUPIED ✗ Collision!\n")
                    self.steps_text.see(tk.END)
                    if hasattr(self, 'canvas'):
                        self.canvas.itemconfig(f"bucket_{idx}", fill=self.COLOR_COLLISION)
                    self.root.update()
                    self.root.after(delay)
                    
                    # Highlight increment: i = i + 1
                    self.highlight_pseudo_lines(increment_line)
                    i += 1
                    self.steps_text.insert(tk.END, f"→ Increment probe counter: i = {i}\n")
                    self.steps_text.see(tk.END)
                    var_text = f"Variables: key={key}, h1={h1}"
                    if h2: var_text += f", h2={h2}"
                    var_text += f", i={i}, m={m}"
                    self.var_label.configure(text=var_text)
                    self.root.update()
                    self.root.after(delay)
            
            if not found_slot:
                # Table full
                self.highlight_pseudo_lines(while_line + increment_line - while_line + 1)  # Last line (RETURN table_full)
                self.steps_text.insert(tk.END, f"→ FAILED: Table is full after {max_probes} probes\n")
                self.steps_text.see(tk.END)
                messagebox.showwarning("Insert Failed", "Hash table is full!")
        
        # Clear highlight after completion
        self.root.after(delay * 2)
        self.pseudo_text.tag_remove("hl", 1.0, tk.END)
        self.update_status(f"Insert complete: {key}")

    def run_insert_with_pseudocode(self, key):
        """Execute insert WITH REAL-TIME pseudocode highlighting - use new method."""
        self.run_insert_with_realtime_pseudocode(key)

    def step_once(self):
        """Execute one step of the pseudocode with detailed visualization."""
        if self._current_step_index >= len(self._current_steps):
            self.auto_running = False
            if hasattr(self, 'auto_btn'):
                self.auto_btn.configure(text="Auto Run")
            self.var_label.configure(text="Variables: Execution complete!")
            return
        
        step = self._current_steps[self._current_step_index]
        self._current_step_index += 1
        
        # Update pseudocode highlight
        line_no = step.get("line", 1)
        self.highlight_pseudo_line(line_no)
        
        # Build detailed variable display
        vars_dict = step.get("vars", {})
        if vars_dict:
            var_parts = []
            for k, v in vars_dict.items():
                if v is not None:
                    if isinstance(v, str):
                        var_parts.append(f"{k}='{v}'")
                    else:
                        var_parts.append(f"{k}={v}")
            vars_text = "Variables: " + " | ".join(var_parts) if var_parts else "Variables: -"
        else:
            vars_text = "Variables: -"
        self.var_label.configure(text=vars_text)
        
        # Append detailed step text to collision steps panel
        step_num = self._current_step_index
        step_text = step.get('text', '')
        self.steps_text.insert(tk.END, f"[Step {step_num}] {step_text}\n")
        self.steps_text.see(tk.END)
        
        # Visual highlighting on canvas
        bucket_idx = step.get("highlight_bucket")
        if bucket_idx is not None and bucket_idx >= 0:
            self.draw_hash_table()
            # Use different colors based on context
            if "✓" in step_text or "complete" in step_text.lower():
                self.highlight_bucket(bucket_idx, self.COLOR_FILLED)
            elif "collision" in step_text.lower() or "occupied" in step_text.lower():
                self.highlight_bucket(bucket_idx, self.COLOR_COLLISION)
            else:
                self.highlight_bucket(bucket_idx, self.COLOR_HIGHLIGHT)

    def toggle_auto_run(self):
        self.auto_running = not self.auto_running
        self.auto_btn.configure(text=("Stop" if self.auto_running else "Auto Run"))
        if self.auto_running:
            self._auto_step_loop()

    def _auto_step_loop(self):
        """Automatically step through pseudocode execution."""
        if not self.auto_running:
            return
        if self._current_step_index >= len(self._current_steps):
            self.auto_running = False
            self.auto_btn.configure(text="Auto Run")
            return
        self.step_once()
        delay = self.speed_var.get()
        self.root.after(delay, self._auto_step_loop)


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = HashTableGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
