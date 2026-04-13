"""
Day 10, Lesson 2: Layout Managers in Tkinter
Covers:
  - pack() layout manager
  - grid() layout manager  
  - place() layout manager - absolute positioning
  - Comparison and best practices
"""

import tkinter as tk

# ============================================
# 1. PACK Layout Manager
# ============================================

print("Pack Layout Manager Demo")

root1 = tk.Tk()
root1.title("Pack Layout")
root1.geometry("300x250")

label_pack = tk.Label(root1, text="Pack Layout Manager", font=("Arial", 12, "bold"), bg="lightblue")
label_pack.pack(pady=10)

# Pack fills sequentially (top to bottom by default)
button1 = tk.Button(root1, text="Button 1 (top)", bg="red", fg="white", width=20)
button1.pack(pady=5)

button2 = tk.Button(root1, text="Button 2 (middle)", bg="green", fg="white", width=20)
button2.pack(pady=5)

button3 = tk.Button(root1, text="Button 3 (bottom)", bg="blue", fg="white", width=20)
button3.pack(pady=5)

# pack with side parameter
frame_pack = tk.Frame(root1, bg="lightyellow", height=50)
frame_pack.pack(fill="x", pady=10)

b1 = tk.Button(frame_pack, text="Left", width=10)
b1.pack(side="left", padx=5)

b2 = tk.Button(frame_pack, text="Center", width=10)
b2.pack(side="left", padx=5)

b3 = tk.Button(frame_pack, text="Right", width=10)
b3.pack(side="left", padx=5)

label_pack_note = tk.Label(root1, text="Note: Good for simple, linear layouts", font=("Arial", 9, "italic"))
label_pack_note.pack()

# ============================================
# 2. GRID Layout Manager
# ============================================

print("Grid Layout Manager Demo")

root2 = tk.Tk()
root2.title("Grid Layout")
root2.geometry("400x300")

label_grid = tk.Label(root2, text="Grid Layout Manager", font=("Arial", 12, "bold"), bg="lightgreen")
label_grid.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="ew")

# Grid creates a table-like structure
tk.Label(root2, text="Name:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root2, width=30).grid(row=1, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root2, text="Email:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Entry(root2, width=30).grid(row=2, column=1, columnspan=2, padx=10, pady=5)

tk.Label(root2, text="Message:", font=("Arial", 10)).grid(row=3, column=0, sticky="nw", padx=10, pady=5)
tk.Text(root2, height=4, width=30).grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# Buttons
tk.Button(root2, text="Submit", bg="green", fg="white").grid(row=4, column=1, padx=5, pady=10)
tk.Button(root2, text="Reset", bg="red", fg="white").grid(row=4, column=2, padx=5, pady=10)

label_grid_note = tk.Label(root2, text="Note: Excellent for forms and organized layouts", font=("Arial", 9, "italic"))
label_grid_note.grid(row=5, column=0, columnspan=3, padx=10)

# ============================================
# 3. PLACE Layout Manager
# ============================================

print("Place Layout Manager Demo")

root3 = tk.Tk()
root3.title("Place Layout")
root3.geometry("500x350")

label_place = tk.Label(root3, text="Place Layout Manager (Absolute Positioning)", 
                       font=("Arial", 12, "bold"), bg="lightyellow")
label_place.place(x=10, y=10, width=480, height=30)

canvas = tk.Canvas(root3, bg="white", highlightthickness=1)
canvas.place(x=10, y=50, width=480, height=250)

# Draw grid on canvas
for i in range(0, 500, 50):
    canvas.create_line(i, 0, i, 250, fill="lightgray", dash=(2, 2))
for i in range(0, 300, 50):
    canvas.create_line(0, i, 480, i, fill="lightgray", dash=(2, 2))

# Place buttons at specific (x, y) coordinates
btn1 = tk.Button(root3, text="Button at (50, 70)", bg="red", fg="white")
btn1.place(x=50, y=70, width=120, height=30)

btn2 = tk.Button(root3, text="Button at (200, 150)", bg="green", fg="white")
btn2.place(x=200, y=150, width=120, height=30)

btn3 = tk.Button(root3, text="Button at (350, 100)", bg="blue", fg="white")
btn3.place(x=350, y=100, width=120, height=30)

label_place_note = tk.Label(root3, text="Note: Use for pixel-perfect control (not recommended for responsive design)", 
                            font=("Arial", 9, "italic"))
label_place_note.place(x=10, y=310, width=480, height=30)

# ============================================
# 4. Comparison Window
# ============================================

print("Comparison of Layout Managers")

root4 = tk.Tk()
root4.title("Comparison")
root4.geometry("500x400")

comparison_text = """
LAYOUT MANAGER COMPARISON:

PACK:
  ✓ Simple and intuitive
  ✓ Good for linear layouts
  ✗ Limited for complex designs
  ✗ Hard to align items precisely
  
GRID:
  ✓ Perfect for forms and tables
  ✓ Excellent for organized layouts
  ✓ Good for responsive designs
  ✓ Most flexible for complex UIs
  ✗ Slightly more complex syntax
  
PLACE:
  ✓ Pixel-perfect positioning
  ✓ Absolute control
  ✗ Not responsive
  ✗ Hard to maintain
  ✗ Not recommended for modern UIs

RECOMMENDATION: Use grid() for most applications!
"""

text_widget = tk.Text(root4, font=("Courier", 10), bg="lightyellow")
text_widget.pack(fill="both", expand=True, padx=10, pady=10)
text_widget.insert(1.0, comparison_text)
text_widget.config(state="disabled")  # Read-only

# ============================================
# 5. Run all demonstrations
# ============================================

print("✅ Lesson 2 Complete! Close all windows to continue.")
print("\nPress Ctrl+C in console if windows don't close automatically.")

# Start event loops
root1.mainloop()
