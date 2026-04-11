# Day 10: GUI Programming with Tkinter

## Learning Outcomes

- Create graphical user interfaces (GUI)
- Handle user interactions and events
- Build real desktop applications
- Understand event-driven programming

---

## Part 1: Window Basics

```python
import tkinter as tk

# Create window
root = tk.Tk()
root.title("My First App")
root.geometry("400x300")  # width x height

# Add content
label = tk.Label(root, text="Hello, World!", font=("Arial", 14))
label.pack()

# Run
root.mainloop()
```

---

## Part 2: Widgets

### Labels
```python
label = tk.Label(root, text="Name:", font=("Arial", 12))
label.pack()
```

### Entry (Text Input)
```python
entry = tk.Entry(root)
entry.pack()
value = entry.get()  # Get text
entry.insert(0, "Default")  # Set text
```

### Button
```python
def on_click():
    print("Clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
```

### Text Box (Multi-line)
```python
text = tk.Text(root, height=5, width=40)
text.pack()
```

### Listbox
```python
listbox = tk.Listbox(root)
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")
listbox.pack()
```

---

## Part 3: Layout

### Pack (Simple)
```python
label.pack()
button.pack()
```

### Grid (Advanced)
```python
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=0, columnspan=2)
```

---

## Part 4: Complete Example

```python
import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")
        self.root.geometry("400x500")
        
        self.tasks = []
        
        # Title
        title = tk.Label(root, text="Todo List", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Input
        self.entry = tk.Entry(root, width=40)
        self.entry.pack()
        
        # Add button
        add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        add_btn.pack()
        
        # List
        self.listbox = tk.Listbox(root, height=15)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        
        # Delete button
        del_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        del_btn.pack()
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
    
    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)
            self.tasks.pop(index)

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
```

---

## Key Concepts

| Widget | Use |
|--------|-----|
| **Label** | Static text |
| **Entry** | Single-line input |
| **Text** | Multi-line input |
| **Button** | Clickable action |
| **Listbox** | Select from list |
| **Canvas** | Draw graphics |

---

## Event Handling

```python
def on_key_press(event):
    print(f"Key pressed: {event.char}")

button.bind("<KeyPress>", on_key_press)
```

---

## Next Steps

- [ ] Create a simple calculator GUI
- [ ] Build a contact manager
- [ ] See EXERCISES.md for challenges
