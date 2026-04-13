"""
Day 10, Lesson 3: Event Handling in Tkinter
Covers:
  - Button click events
  - Keyboard events
  - Mouse events
  - Entry field events
  - Binding custom events
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Events Demo")
root.geometry("500x600")

# Display event log
event_log = tk.Text(root, height=20, width=60, bg="lightyellow")
event_log.pack(padx=10, pady=10)

def log_event(message):
    """Log event to the text widget"""
    event_log.insert(tk.END, f"► {message}\n")
    event_log.see(tk.END)  # Scroll to bottom
    print(message)

# ============================================
# 1. Button Click Events
# ============================================

log_event("=== Button Click Events ===")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

def on_button1_click():
    log_event("Button 1 clicked!")
    messagebox.showinfo("Info", "Button 1 was clicked")

def on_button2_click(event):
    """Event handlers receive an event object"""
    log_event("Button 2 clicked!")

button1 = tk.Button(frame_buttons, text="Simple Click", command=on_button1_click, 
                    bg="lightblue", width=15)
button1.pack(side="left", padx=5)

button2 = tk.Button(frame_buttons, text="With Event Object", command=on_button2_click,
                    bg="lightgreen", width=15)
button2.pack(side="left", padx=5)

# ============================================
# 2. Entry Field Events
# ============================================

log_event("\n=== Entry Field Events ===")

entry_label = tk.Label(root, text="Type in the entry field:", font=("Arial", 10))
entry_label.pack()

entry = tk.Entry(root, width=40, font=("Arial", 10))
entry.pack(pady=5)

def on_entry_change():
    """Called when entry text changes"""
    text = entry.get()
    log_event(f"Entry changed: '{text}'")

def on_entry_key_press(event):
    """Called when any key is pressed in the entry"""
    log_event(f"Key pressed: {event.char!r} (ASCII: {ord(event.char) if event.char else 'N/A'})")

# Bind events
entry.bind('<KeyRelease>', lambda e: on_entry_change())
entry.bind('<KeyPress>', on_entry_key_press)

# ============================================
# 3. Mouse Events
# ============================================

log_event("\n=== Mouse Events ===")

canvas = tk.Canvas(root, width=400, height=100, bg="white", relief="sunken", borderwidth=2)
canvas.pack(pady=10)

def on_canvas_click(event):
    """Handle mouse click on canvas"""
    log_event(f"Canvas clicked at ({event.x}, {event.y})")
    canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="red")

def on_canvas_motion(event):
    """Handle mouse motion on canvas"""
    log_event(f"Mouse at ({event.x}, {event.y})")

def on_canvas_enter(event):
    log_event("Mouse entered canvas")
    canvas.config(bg="lightblue")

def on_canvas_leave(event):
    log_event("Mouse left canvas")
    canvas.config(bg="white")

# Bind mouse events
canvas.bind('<Button-1>', on_canvas_click)
canvas.bind('<Motion>', on_canvas_motion)
canvas.bind('<Enter>', on_canvas_enter)
canvas.bind('<Leave>', on_canvas_leave)

canvas.create_text(200, 50, text="Click here and move mouse", font=("Arial", 12))

# ============================================
# 4. Keyboard Events
# ============================================

log_event("\n=== Keyboard Events ===")

def on_key_press(event):
    """Handle key press anywhere in window"""
    key_name = event.keysym  # Key name like 'a', 'Return', 'Escape'
    log_event(f"Key pressed: {key_name}")

def on_return_key(event):
    """Specific handler for Return key"""
    log_event("Return/Enter key pressed!")

# Bind keyboard events to root window
root.bind('<Key>', on_key_press)
root.bind('<Return>', on_return_key)

# ============================================
# 5. Radiobutton/Checkbox Events
# ============================================

log_event("\n=== Selection Events ===")

var = tk.StringVar(value="option1")

def on_radio_change():
    selected = var.get()
    log_event(f"Radio selection changed to: {selected}")

radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="option1", command=on_radio_change)
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="option2", command=on_radio_change)

radio1.pack(anchor=tk.W, padx=50)
radio2.pack(anchor=tk.W, padx=50)

# ============================================
# 6. Spinbox Events
# ============================================

log_event("\n=== Spinbox Events ===")

spinvar = tk.IntVar(value=5)

def on_spinbox_change():
    value = spinvar.get()
    log_event(f"Spinbox value: {value}")

spinbox = tk.Spinbox(root, from_=0, to=10, textvariable=spinvar, 
                     command=on_spinbox_change, width=10)
spinbox.pack(pady=5)

# ============================================
# 7. Window Events
# ============================================

log_event("\n=== Window Events ===")

def on_window_close():
    log_event("Window is closing...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_window_close)

# ============================================
# 8. Clear Log Button
# ============================================

def clear_log():
    event_log.delete(1.0, tk.END)
    log_event("Log cleared!")

clear_button = tk.Button(root, text="Clear Log", command=clear_log, bg="red", fg="white")
clear_button.pack(pady=5)

log_event("✅ Lesson 3 Complete! Try interacting with all elements.")

root.mainloop()
