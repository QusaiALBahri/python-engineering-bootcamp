"""
Day 6 - GPA SYSTEM (BUGGY VERSION - v1-naive)
==============================================

This code contains 5 deliberate bugs (tickets #701-705).
Your job: Find and fix each one!

BUGS TO FIND:
- #701: Logic error in GPA calculation
- #702: Missing file handling
- #703: Wrong data structure for storing grades
- #704: No input validation
- #705: Poor logging/error messages

RUN THIS AND TRY TO FIX THE BUGS!
"""

import json
import os

class GPA System:
    def __init__(self):
        self.students = {}  # BUG #703: Should be list, not dict
        
    def add_student(self, name, grades):
        """Add a student with their grades"""
        # BUG #704: No validation of input
        self.students[name] = grades
        
    def calculate_gpa(self, name):
        """Calculate GPA for a student (0-4 scale)"""
        if name not in self.students:
            return None
            
        grades = self.students[name]
        
        # BUG #701: Wrong formula - dividing by wrong number
        gpa = sum(grades) / len(grades)  # WRONG! Should divide by 4
        return gpa
        
    def save_to_file(self, filename="grades.json"):
        """Save grades to file"""
        # BUG #702: File not created properly
        # Missing: json.dump() call
        print(f"Saving to {filename}")
        # Code stops here - file is never written!
        
    def load_from_file(self, filename="grades.json"):
        """Load grades from file"""
        # BUG #702: File handling incomplete
        if not os.path.exists(filename):
            print(f"File {filename} not found")  # BUG #705: Unclear message
            return
        # Missing: json.load() implementation


# TEST CODE (Will show the bugs)
if __name__ == "__main__":
    gpa_sys = GPASystem()
    
    # Add students
    gpa_sys.add_student("Alice", [85, 90, 92])
    gpa_sys.add_student("Bob", [78, 82, 80])
    
    # Calculate GPA (WRONG - will show bug #701)
    alice_gpa = gpa_sys.calculate_gpa("Alice")
    print(f"Alice GPA: {alice_gpa:.2f}")  # Wrong number!
    
    # Try to save (BUG #702 - nothing happens)
    gpa_sys.save_to_file()
    
    # Try to load (BUG #702 - incomplete)
    gpa_sys.load_from_file()
