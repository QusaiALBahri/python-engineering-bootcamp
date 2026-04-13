# 🎯 Day 10: GUI Development with Tkinter (3 hours)

## 📚 Topics Covered

| Topic | File | Duration | What You'll Learn |
|-------|------|----------|-------------------|
| **Tkinter Basics & Widgets** | `01_tkinter_widgets.py` | 30min | Window, Label, Button, Entry widgets |
| **Layouts: Pack, Grid, Place** | `02_tkinter_layout.py` | 45min | Geometry managers for positioning widgets |
| **Events & Callbacks** | `03_tkinter_events.py` | 30min | Handling button clicks, text input, events |
| **Building a Mini Dashboard** | `04_mini_dashboard.py` | 30min | Complete app with multiple widgets |
| **Exercises & Solutions** | `EXERCISES.md`, `SOLUTIONS.md` | 45min | Hands-on GUI projects |

---

## 🎓 Learning Outcomes

By the end of Day 10, you should understand:

✅ How to create a window and add widgets  
✅ The difference between pack(), grid(), and place() layouts  
✅ How to handle button clicks and user input  
✅ How to create an event-driven application  
✅ How to build a simple but functional GUI application  
✅ How to update widgets dynamically  

---

## 🚀 Quick Start

### Run the examples:
```bash
python 01_tkinter_widgets.py
python 02_tkinter_layout.py
python 03_tkinter_events.py
python 04_mini_dashboard.py
```

### Try the exercises:
```bash
# Read EXERCISES.md and solve them
# Check your solutions against SOLUTIONS.md
```

---

## 🧠 Key Concepts at a Glance

### **Creating a Basic Window**
```python
import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")

label = tk.Label(root, text="Hello!")
label.pack()

root.mainloop()  # Start the event loop
```

### **Common Widgets**
```python
label = tk.Label(root, text="Hello")
button = tk.Button(root, text="Click me", command=on_click)
entry = tk.Entry(root)
text = tk.Text(root, height=10, width=30)
canvas = tk.Canvas(root, width=400, height=300)
```

### **Layout Managers**
```python
# Pack: Simple, linear layout
widget.pack(padx=10, pady=10, fill='both', expand=True)

# Grid: Table-like layout
widget.grid(row=0, column=0, padx=10, pady=10)

# Place: Absolute positioning
widget.place(x=100, y=50, width=200, height=30)
```

### **Handling Events**
```python
def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click", command=on_button_click)
button.pack()
```

---

## 📊 Mini Project: Calculator UI

**Scenario:** Build a simple calculator with a display and buttons.

**Features:**
1. Display field to show numbers
2. Number buttons (0-9)
3. Operation buttons (+, -, *, /)
4. Equals and Clear buttons
5. Working calculation logic

---

## 🎯 Focus Areas

- **Responsive Layout:** Use grid() for organized, responsive designs
- **Event Handling:** Connect buttons to functions
- **Data Binding:** Keep widgets and variables in sync
- **User Experience:** Provide visual feedback for interactions
