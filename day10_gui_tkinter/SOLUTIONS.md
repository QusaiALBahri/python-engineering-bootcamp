# ✅ Day 10: GUI Development with Tkinter - SOLUTIONS

## Solution 1: Simple Label & Button App

```python
import tkinter as tk

root = tk.Tk()
root.title("Simple App")
root.geometry("400x200")

# Label with initial text
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14), bg="lightblue")
label.pack(pady=20)

# Function to change text
def change_text():
    label.config(text="Text Changed!")
    label.config(bg="lightgreen")

change_button = tk.Button(root, text="Change Text", command=change_text, bg="green", fg="white")
change_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white")
exit_button.pack(pady=10)

root.mainloop()
```

---

## Solution 2: Simple Calculator

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

# Entry fields
tk.Label(root, text="Number 1:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", padx=20, pady=10)
num1_entry = tk.Entry(root, width=20)
num1_entry.grid(row=0, column=1, padx=20, pady=10)

tk.Label(root, text="Number 2:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", padx=20, pady=10)
num2_entry = tk.Entry(root, width=20)
num2_entry.grid(row=1, column=1, padx=20, pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.grid(row=3, column=0, columnspan=2, pady=20)

# Operation functions
def calculate(operation):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Buttons
button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=2, pady=20)

tk.Button(button_frame, text="+", width=5, command=lambda: calculate("+")).pack(side="left", padx=5)
tk.Button(button_frame, text="-", width=5, command=lambda: calculate("-")).pack(side="left", padx=5)
tk.Button(button_frame, text="*", width=5, command=lambda: calculate("*")).pack(side="left", padx=5)
tk.Button(button_frame, text="/", width=5, command=lambda: calculate("/")).pack(side="left", padx=5)

root.mainloop()
```

---

## Solution 3: To-Do List App

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x350")

tasks = []

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text="New Task:").pack(side="left", padx=5)
task_entry = tk.Entry(input_frame, width=30)
task_entry.pack(side="left", padx=5)

# List frame
list_frame = tk.Frame(root)
list_frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(list_frame, text="Tasks:", font=("Arial", 10, "bold")).pack(anchor="w")

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=12, width=50)
task_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=task_listbox.yview)

# Functions
def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append(task)
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        task_listbox.delete(0, tk.END)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

tk.Button(button_frame, text="Add Task", command=add_task, bg="green", fg="white").pack(side="left", padx=5)
tk.Button(button_frame, text="Delete Selected", command=delete_task, bg="orange", fg="white").pack(side="left", padx=5)
tk.Button(button_frame, text="Clear All", command=clear_all, bg="red", fg="white").pack(side="left", padx=5)

root.mainloop()
```

---

## Solution 4: Temperature Converter

```python
import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")

# Main frame structure
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Left frame (Celsius)
left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=20)

tk.Label(left_frame, text="Celsius", font=("Arial", 12, "bold")).pack()
celsius_entry = tk.Entry(left_frame, width=15, font=("Arial", 11))
celsius_entry.pack(pady=10)
celsius_label = tk.Label(left_frame, text="", font=("Arial", 10))
celsius_label.pack()

# Right frame (Fahrenheit)
right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", padx=20)

tk.Label(right_frame, text="Fahrenheit", font=("Arial", 12, "bold")).pack()
fahrenheit_entry = tk.Entry(right_frame, width=15, font=("Arial", 11))
fahrenheit_entry.pack(pady=10)
fahrenheit_label = tk.Label(right_frame, text="", font=("Arial", 10))
fahrenheit_label.pack()

# Conversion functions
def celsius_to_fahrenheit():
    try:
        c = float(celsius_entry.get())
        f = (c * 9/5) + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{f:.2f}")
        fahrenheit_label.config(text=f"{f:.2f}°F")
    except ValueError:
        celsius_label.config(text="Invalid input!")

def fahrenheit_to_celsius():
    try:
        f = float(fahrenheit_entry.get())
        c = (f - 32) * 5/9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{c:.2f}")
        celsius_label.config(text=f"{c:.2f}°C")
    except ValueError:
        fahrenheit_label.config(text="Invalid input!")

def reset():
    celsius_entry.delete(0, tk.END)
    fahrenheit_entry.delete(0, tk.END)
    celsius_label.config(text="")
    fahrenheit_label.config(text="")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="C → F", command=celsius_to_fahrenheit, bg="blue", fg="white").pack(side="left", padx=5)
tk.Button(button_frame, text="F → C", command=fahrenheit_to_celsius, bg="blue", fg="white").pack(side="left", padx=5)
tk.Button(button_frame, text="Reset", command=reset, bg="gray", fg="white").pack(side="left", padx=5)

root.mainloop()
```

---

## Solution 6: Event Logging Application

```python
import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Event Logger")
root.geometry("500x600")

# Log display
log_text = tk.Text(root, height=20, width=60, bg="lightyellow")
log_text.pack(padx=10, pady=10)

def log_event(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_text.insert(tk.END, f"[{timestamp}] {message}\n")
    log_text.see(tk.END)

# Button
def on_button_click():
    log_event("Button clicked!")

button = tk.Button(root, text="Click me", command=on_button_click, bg="green", fg="white")
button.pack(pady=5)

# Entry field
def on_entry_change(event):
    text = entry.get()
    log_event(f"Text entered: '{text}'")

entry = tk.Entry(root, width=40)
entry.bind('<KeyRelease>', on_entry_change)
entry.pack(pady=5)

# Checkbox
def on_check_change():
    state = "checked" if check_var.get() else "unchecked"
    log_event(f"Checkbox {state}")

check_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Agree", variable=check_var, command=on_check_change)
checkbox.pack(pady=5)

# Canvas
def on_canvas_click(event):
    log_event(f"Canvas clicked at ({event.x}, {event.y})")

canvas = tk.Canvas(root, width=400, height=100, bg="white")
canvas.bind('<Button-1>', on_canvas_click)
canvas.pack(pady=5)

log_event("✅ Application started!")

root.mainloop()
```

---

## Solution 8: Student Grade Manager (Challenge)

```python
import tkinter as tk
from tkinter import messagebox
import os

class GradeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Grade Manager")
        self.root.geometry("600x500")
        self.students = {}
        self.filename = "students.txt"
        
        self.load_data()
        self.setup_ui()
    
    def setup_ui(self):
        # Input frame
        input_frame = tk.LabelFrame(self.root, text="Add Student", padx=10, pady=10)
        input_frame.pack(padx=10, pady=10, fill="x")
        
        tk.Label(input_frame, text="Name:").pack(side="left", padx=5)
        self.name_entry = tk.Entry(input_frame, width=20)
        self.name_entry.pack(side="left", padx=5)
        
        tk.Label(input_frame, text="Score:").pack(side="left", padx=5)
        self.score_entry = tk.Entry(input_frame, width=10)
        self.score_entry.pack(side="left", padx=5)
        
        tk.Button(input_frame, text="Add", command=self.add_student, bg="green", fg="white").pack(side="left", padx=5)
        
        # Display frame
        display_frame = tk.LabelFrame(self.root, text="Students", padx=10, pady=10)
        display_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.listbox = tk.Listbox(display_frame, height=12, width=70)
        self.listbox.pack(fill="both", expand=True)
        
        self.update_list()
        
        # Statistics frame
        stats_frame = tk.LabelFrame(self.root, text="Statistics", padx=10, pady=10)
        stats_frame.pack(padx=10, pady=5, fill="x")
        
        self.stats_label = tk.Label(stats_frame, text="", font=("Arial", 10))
        self.stats_label.pack()
        self.update_stats()
        
        # Action buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Delete Selected", command=self.delete_student, bg="orange", fg="white").pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear All", command=self.clear_all, bg="red", fg="white").pack(side="left", padx=5)
    
    def get_grade(self, score):
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"
    
    def add_student(self):
        try:
            name = self.name_entry.get().strip()
            score = float(self.score_entry.get())
            
            if not name:
                messagebox.showwarning("Warning", "Enter a name!")
                return
            
            self.students[name] = score
            self.save_data()
            self.update_list()
            self.update_stats()
            
            self.name_entry.delete(0, tk.END)
            self.score_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid score!")
    
    def delete_student(self):
        try:
            index = self.listbox.curselection()[0]
            name = list(self.students.keys())[index]
            del self.students[name]
            self.save_data()
            self.update_list()
            self.update_stats()
        except IndexError:
            messagebox.showwarning("Warning", "Select a student!")
    
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Clear all students?"):
            self.students.clear()
            self.save_data()
            self.update_list()
            self.update_stats()
    
    def update_list(self):
        self.listbox.delete(0, tk.END)
        for name, score in self.students.items():
            grade = self.get_grade(score)
            self.listbox.insert(tk.END, f"{name:20} Score: {score:6.1f}  Grade: {grade}")
    
    def update_stats(self):
        if not self.students:
            self.stats_label.config(text="No students yet")
            return
        
        scores = list(self.students.values())
        avg = sum(scores) / len(scores)
        max_score = max(scores)
        min_score = min(scores)
        
        stats_text = f"Average: {avg:.2f}  |  Highest: {max_score:.1f}  |  Lowest: {min_score:.1f}  |  Count: {len(self.students)}"
        self.stats_label.config(text=stats_text)
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            for name, score in self.students.items():
                f.write(f"{name},{score}\n")
    
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        self.students[parts[0]] = float(parts[1])

root = tk.Tk()
app = GradeManager(root)
root.mainloop()
```

---

## Common Patterns

### **Command with Parameters**
```python
# Wrong: button = tk.Button(command=my_function(arg))  # Runs immediately!
# Right: button = tk.Button(command=lambda: my_function(arg))
```

### **Get/Set Widget Values**
```python
# Entry
value = entry.get()  # Get text
entry.delete(0, tk.END)  # Clear
entry.insert(0, "New text")  # Set

# Label
label.config(text="New text")

# Listbox
listbox.insert(tk.END, "item")  # Add
listbox.delete(0)  # Delete first item
items = listbox.get(0, tk.END)  # Get all
```

### **Grid Layout Best Practice**
```python
for i, (label_text, var) in enumerate(fields):
    tk.Label(root, text=label_text).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    tk.Entry(root, textvariable=var).grid(row=i, column=1, padx=10, pady=5)
```

---

## Key Takeaways

✅ Always use `root.mainloop()` at the end  
✅ Use `command=` (not `command()`) for buttons  
✅ Use `lambda:` for passing arguments to command functions  
✅ Use grid() for organized, professional layouts  
✅ Bind events with `.bind('<event>', function)`  
✅ Save application state to files  
✅ Use classes for larger applications  
