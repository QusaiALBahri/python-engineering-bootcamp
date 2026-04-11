"""
Day 6 - GPA SYSTEM (FIXED VERSION - v2-hardened)
================================================

THIS IS THE PROFESSIONAL, BUG-FREE VERSION
All bugs fixed with:
- Proper validation
- Error handling
- Logging
- File persistence
- Correct calculations

Compare with gpa_buggy_v1.py to see the improvements
"""

import json
import os
import logging
from typing import List, Dict, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GPASystem:
    """Professional GPA calculation system with file persistence"""
    
    # GPA scale: 0-4 (typical US scale)
    GPA_SCALE = 4.0
    MAX_GRADE = 100
    
    def __init__(self, grade_file: str = "grades.json"):
        """Initialize GPA system with file storage"""
        self.students: List[Dict] = []  # FIX #703: Changed to list
        self.grade_file = grade_file
        logging.info(f"GPA System initialized")
        
    def add_student(self, name: str, grades: List[int]) -> bool:
        """Add a student with validation"""
        # FIX #704: Validate input
        if not name or not isinstance(name, str):
            logging.error(f"Invalid name: {name}")
            return False
            
        if not grades or not isinstance(grades, list):
            logging.error(f"Invalid grades for {name}")
            return False
            
        for grade in grades:
            if not isinstance(grade, (int, float)) or grade < 0 or grade > self.MAX_GRADE:
                logging.error(f"Grade {grade} out of range for {name}")
                return False
        
        # Check if student exists
        if any(s["name"] == name for s in self.students):
            logging.warning(f"Student {name} already exists, updating...")
            for student in self.students:
                if student["name"] == name:
                    student["grades"] = grades
                    return True
        
        self.students.append({"name": name, "grades": grades})
        logging.info(f"Added student: {name}")
        return True
        
    def calculate_gpa(self, name: str) -> Optional[float]:
        """Calculate GPA for a student (0-4 scale)"""
        for student in self.students:
            if student["name"] == name:
                grades = student["grades"]
                
                # FIX #701: Correct formula
                # Convert 0-100 scale to 0-4 scale
                gpa_points = [grade * self.GPA_SCALE / self.MAX_GRADE for grade in grades]
                gpa = sum(gpa_points) / len(gpa_points)
                
                logging.debug(f"Calculated GPA for {name}: {gpa:.2f}")
                return round(gpa, 2)
        
        logging.warning(f"Student {name} not found")
        return None
        
    def save_to_file(self) -> bool:
        """Save grades to JSON file with error handling"""
        try:
            # FIX #702: Proper JSON file writing
            with open(self.grade_file, 'w') as f:
                json.dump(self.students, f, indent=2)
            logging.info(f"Saved {len(self.students)} students to {self.grade_file}")
            return True
        except IOError as e:
            logging.error(f"Failed to save file: {e}")  # FIX #705: Clear error
            return False
            
    def load_from_file(self) -> bool:
        """Load grades from JSON file with error handling"""
        # FIX #702: Complete implementation
        try:
            if not os.path.exists(self.grade_file):
                logging.info(f"File {self.grade_file} not found - starting fresh")
                return False
                
            with open(self.grade_file, 'r') as f:
                self.students = json.load(f)
            logging.info(f"Loaded {len(self.students)} students from {self.grade_file}")
            return True
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON in {self.grade_file}: {e}")
            return False
        except IOError as e:
            logging.error(f"Failed to read file: {e}")
            return False
            
    def get_all_students(self) -> List[Dict]:
        """Return all students with their GPA"""
        result = []
        for student in self.students:
            gpa = self.calculate_gpa(student["name"])
            result.append({
                "name": student["name"],
                "grades": student["grades"],
                "gpa": gpa
            })
        return result
        
    def print_report(self):
        """Print a professional report"""
        print("\n" + "="*50)
        print("GPA REPORT")
        print("="*50)
        for student in self.get_all_students():
            print(f"{student['name']:15} | Grades: {student['grades']} | GPA: {student['gpa']:.2f}")
        print("="*50 + "\n")


# TEST CODE (Shows the fixes working)
if __name__ == "__main__":
    gpa_sys = GPASystem()
    
    # Load existing data if available
    gpa_sys.load_from_file()
    
    # Add students with validation
    gpa_sys.add_student("Alice", [85, 90, 92])
    gpa_sys.add_student("Bob", [78, 82, 80])
    gpa_sys.add_student("Invalid", ["not", "numbers"])  # Will be rejected
    
    # Calculate GPA (CORRECT - using right formula)
    alice_gpa = gpa_sys.calculate_gpa("Alice")
    print(f"Alice GPA: {alice_gpa:.2f}")  # Now correct!
    
    # Save to file (WORKS - with error handling)
    gpa_sys.save_to_file()
    
    # Print professional report
    gpa_sys.print_report()
