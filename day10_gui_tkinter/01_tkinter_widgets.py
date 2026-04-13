"""
Day 10, Lesson 1: Tkinter Basics and Widgets
Covers:
  - Creating a Tkinter window
  - Basic widgets: Label, Button, Entry, Text
  - Widget properties (text, bg, fg, font, width, height)
"""

import tkinter as tk
from tkinter import messagebox

# ============================================
# 1. Creating a Basic Window
# ============================================

print("Creating a Tkinter window...")

root = tk.Tk()
root.title("Tkinter Basics Demo")
root.geometry("600x500")

# ============================================
# 2. Label Widget
# ============================================

label_section = tk.Label(root, text="Labels", font=("Arial", 12, "bold"))
label_section.pack(pady=(10, 5))

label1 = tk.Label(root, text="Simple Label", bg="lightblue", fg="darkblue", padx=10, pady=10)
label1.pack(padx=5, pady=5)

label2 = tk.Label(root, text="Styled Label", font=("Times", 14), bg="yellow", fg="red")
label2.pack(padx=5, pady=5)

# ============================================
# 3. Button Widget
# ============================================

button_section = tk.Label(root, text="Buttons", font=("Arial", 12, "bold"))
button_section.pack(pady=(15, 5))

def on_simple_click():
    print("Simple button clicked!")
    label1.config(text="Button was clicked!")

button1 = tk.Button(root, text="Simple Button", command=on_simple_click, bg="green", fg="white")
button1.pack(padx=5, pady=5)

def on_message_click():
    messagebox.showinfo("Information", "Hello from Tkinter!")

button2 = tk.Button(root, text="Show Message", command=on_message_click, bg="blue", fg="white")
button2.pack(padx=5, pady=5)

# ============================================
# 4. Entry Widget
# ============================================

entry_section = tk.Label(root, text="Entry Field", font=("Arial", 12, "bold"))
entry_section.pack(pady=(15, 5))

entry = tk.Entry(root, width=30, font=("Arial", 11))
entry.insert(0, "Type something here...")
entry.pack(padx=5, pady=5)

def get_entry_value():
    value = entry.get()
    print(f"Entry value: {value}")
    label1.config(text=f"You entered: {value}")

button_get = tk.Button(root, text="Get Entry Value", command=get_entry_value, bg="orange")
button_get.pack(padx=5, pady=5)

# ============================================
# 5. Text Widget (Multi-line)
# ============================================

text_section = tk.Label(root, text="Text Area", font=("Arial", 12, "bold"))
text_section.pack(pady=(15, 5))

text = tk.Text(root, height=6, width=50, font=("Arial", 10))
text.pack(padx=5, pady=5)

# ============================================
# 6. Frame Widget (Container)
# ============================================

frame = tk.Frame(root, bg="lightgray", relief="sunken", borderwidth=2)
frame.pack(padx=5, pady=5, fill="x")

frame_label = tk.Label(frame, text="Frame Container", bg="lightgray", font=("Arial", 10))
frame_label.pack()

frame_button1 = tk.Button(frame, text="Button in Frame 1")
frame_button1.pack(side="left", padx=5, pady=5)

frame_button2 = tk.Button(frame, text="Button in Frame 2")
frame_button2.pack(side="left", padx=5, pady=5)

# ============================================
# 7. Checkbutton Widget
# ============================================

check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Agree to terms", variable=check_var)
checkbutton.pack(padx=5, pady=5)

# ============================================
# 8. Radiobutton Widget
# ============================================

radio_var = tk.StringVar(value="option1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="option1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="option2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="option3")

radio1.pack(anchor=tk.W, padx=30)
radio2.pack(anchor=tk.W, padx=30)
radio3.pack(anchor=tk.W, padx=30)

# ============================================
# 9. Exit Button
# ============================================

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white", width=10)
exit_button.pack(padx=5, pady=10)

# ============================================
# 10. Start the Event Loop
# ============================================

print("✅ Lesson 1 Complete! Close the window to continue.")
root.mainloop()
