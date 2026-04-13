# 📝 Day 10: GUI Development with Tkinter - EXERCISES

## Exercise 1: Simple Label & Button App

**Scenario:** Create a basic app with a label and button.

**Task:**
1. Create a window (400x200)
2. Add a label with text "Welcome to Tkinter!"
3. Add a button that changes the label text when clicked
4. Add an "Exit" button

**Expected Output:**
- Window with greeting label
- Button that says "Change Text"
- Clicking button updates label to "Text Changed!"

---

## Exercise 2: Simple Calculator

**Scenario:** Create a calculator that adds two numbers.

**Task:**
1. Create a window with grid layout
2. Add two Entry fields for user input
3. Add labels ("Number 1:", "Number 2:")
4. Add buttons: "+", "-", "*", "/" (each performs operation)
5. Display result in a label

**Expected Output:**
```
Number 1: [input field]
Number 2: [input field]
[+] [-] [*] [/]
Result: [number]
```

---

## Exercise 3: To-Do List App

**Scenario:** Build a simple task manager.

**Task:**
1. Create window with grid layout
2. Add entry field for new tasks
3. Add "Add Task" button
4. Add listbox to show all tasks (using Listbox widget)
5. Add "Delete Selected" button to remove tasks
6. Add "Clear All" button

**Requirements:**
- Tasks display in listbox
- Can add new tasks
- Can delete selected task
- Can clear entire list

**Hint:** Use `listbox.insert()`, `listbox.get()`, `listbox.delete()`

---

## Exercise 4: Temperature Converter

**Scenario:** Create a converter for Celsius ↔ Fahrenheit.

**Task:**
1. Create two frames:
   - Left frame: Input Celsius
   - Right frame: Input Fahrenheit
2. Each frame has:
   - Label for title
   - Entry field for value
3. Add "Convert" button in the middle
4. Display results in labels below entries
5. Formula: F = (C × 9/5) + 32

**Example:**
- Input: 0°C → Output: 32°F
- Input: 100°C → Output: 212°F

---

## Exercise 5: Survey Form

**Scenario:** Create a form with multiple widget types.

**Task:**
1. Create a form with the following fields (use grid layout):
   - Name (Entry)
   - Age (Spinbox, range 1-120)
   - City (Combobox with options: Amman, Zarqa, Irbid)
   - Gender (Radiobutton: Male/Female)
   - Subscribe (Checkbox)
   - Comments (Text area)
2. Add "Submit" button
   - Show messagebox with submitted data
3. Add "Reset" button
   - Clear all fields

**Deliverable:** 
- Functional form with validation
- Formatted output dialog on submit

---

## Exercise 6: Event Logging Application

**Scenario:** Track user interactions.

**Task:**
1. Create window with:
   - Text widget (log display)
   - Button (Button click logging)
   - Entry field (Track input changes)
   - Checkbutton (Log state changes)
   - Canvas (Log mouse events)

2. Log all events to text widget:
   - Button clicks: "Button clicked at HH:MM:SS"
   - Entry changes: "Text entered: [value]"
   - Checkbox changes: "Checkbox [checked/unchecked]"
   - Mouse clicks on canvas: "Canvas clicked at (x, y)"

**Deliverable:**
- Real-time event log displayed in text widget
- Clean, readable log format

---

## Exercise 7: Color Picker App

**Scenario:** Interactive color selection tool.

**Task:**
1. Create window with:
   - Three sliders (Red, Green, Blue) range 0-255
   - Display hex color code
   - Canvas showing preview of selected color
   - Label showing RGB values

2. Features:
   - Real-time color update as you move sliders
   - Show hex value: #RRGGBB
   - Clickable buttons for preset colors (Red, Green, Blue, Black, White)

**Hint:** Use `tk.Scale()` widget, convert RGB to Hex: `hex((R<<16) + (G<<8) + B)`

---

## Exercise 8: Student Grade Manager (Challenge)

**Scenario:** Complete application for managing student grades.

**Task:**
1. Create a window with multiple frames:
   - **Input Frame:** 
     - Entry: Student name
     - Entry: Test score (0-100)
     - Button: Add student
   
   - **Display Frame:**
     - Listbox: Show all students with scores
     - Listbox: Display grade (A, B, C, D, F)
   
   - **Statistics Frame:**
     - Labels showing:
       - Average grade
       - Highest score
       - Lowest score
   
   - **Action Frame:**
     - Delete student
     - Clear all
     - Export to file

2. Grade calculation:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: < 60

3. Data persistence:
   - Save to `students.txt` when adding
   - Load from file on startup

**Deliverable:**
- Fully functional grade manager
- Data saved to file
- Statistics calculated and displayed

---

## Exercise 9: Timer/Stopwatch App

**Scenario:** Build a timer application.

**Task:**
1. Create window with:
   - Label showing time (MM:SS format)
   - Entry for input seconds
   - Buttons: Start, Pause, Reset
   - Canvas (optional): Visual progress indicator

2. Features:
   - Input seconds and start countdown
   - Pause/resume functionality
   - Reset to zero
   - Message when timer finishes
   - Disable input during countdown

**Hint:** Use `root.after(ms, function)` for timer updates

---

## Exercise 10: Class-Based GUI Application

**Scenario:** Refactor a simple app using OOP.

**Task:**
1. Create a class `BMICalculator`:
   - `__init__(self, root)`: Initialize window
   - `setup_ui(self)`: Create widgets
   - `calculate_bmi(self)`: Calculate BMI
   - `update_result(self)`: Display result
   - `reset(self)`: Clear inputs

2. Elements:
   - Entry: Height (cm)
   - Entry: Weight (kg)
   - Button: Calculate
   - Label: Display result with category
   - Label: Category (Underweight, Normal, Overweight, Obese)

3. BMI Formula: BMI = weight(kg) / (height(m))²

**Deliverable:**
- Well-organized class-based code
- Clean separation of concerns
- Reusable structure

---

## Submission Checklist

✅ All windows create and close properly  
✅ All buttons have working functions  
✅ All Entry fields capture input correctly  
✅ Grid or Pack layout is properly used  
✅ Error handling for invalid inputs  
✅ Code is well-organized and readable  
✅ Comments explain complex functions  
✅ No errors in console output  

---

## Tips

- Always use `root.mainloop()` to start the app
- Use `command=function` for button clicks (no parentheses!)
- Use `.get()` to retrieve Entry/Spinbox values
- Use `.config()` to update widget properties
- Use Try/Except for converting user input
- Use messagebox for alerts and confirmations
- Use grid() for organized, professional layouts
- Store frequently accessed widgets as `self.widget` attributes
