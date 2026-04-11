"""
Day 8 Sprint 1: Task Manager (BUGGY VERSION)
Find and fix 5 bugs (#801-805)

Bugs intentionally left in:
- #801: Tasks never load from file
- #802: Completed task count is wrong  
- #803: No validation on task names
- #804: Can't delete completed tasks
- #805: File format inconsistent
"""
import json
import os
from typing import List, Dict, Optional


class Task:
    """A single task with title, description, and completion status."""
    
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False
    
    def mark_complete(self):
        """Mark task as completed."""
        self.completed = True
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON storage."""
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }


class TaskManager:
    """Manages a list of tasks with persistence."""
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()  # BUG #801: This doesn't work!
    
    def add_task(self, title: str, description: str = "") -> bool:
        """Add a new task.
        
        BUG #803: No validation!
        """
        # BUG: Should validate title!
        task = Task(title, description)
        self.tasks.append(task)
        return True
    
    def complete_task(self, title: str) -> bool:
        """Mark a task completed."""
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True
        return False
    
    def delete_task(self, title: str) -> bool:
        """Delete a task by title.
        
        BUG #804: Can't delete completed tasks!
        """
        for i, task in enumerate(self.tasks):
            if task.title == title:
                if task.completed:
                    return False  # BUG: Why is this here?
                self.tasks.pop(i)
                return True
        return False
    
    def get_completed_count(self) -> int:
        """Get number of completed tasks.
        
        BUG #802: Wrong calculation!
        """
        # BUG: This should count completed tasks
        count = len([t for t in self.tasks if t.completed])
        return count * 2  # BUG: Why multiply by 2?
    
    def get_pending_count(self) -> int:
        """Get number of pending tasks."""
        return len([t for t in self.tasks if not t.completed])
    
    def save_tasks(self) -> bool:
        """Save tasks to JSON file.
        
        BUG #805: Inconsistent format!
        """
        try:
            with open(self.filename, 'w') as f:
                # BUG: Should save as list of dicts
                data = {
                    "tasks": [t.to_dict() for t in self.tasks],
                    "metadata": {  # BUG: Extra metadata breaks loading
                        "count": len(self.tasks),
                        "version": "1.0"
                    }
                }
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving: {e}")
            return False
    
    def load_tasks(self) -> bool:
        """Load tasks from JSON file.
        
        BUG #801: Never actually loads!
        """
        if not os.path.exists(self.filename):
            print(f"No file {self.filename} found - starting fresh")
            return False
        
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
            
            # BUG #801: Loads data but never creates Task objects!
            if "tasks" in data:
                task_list = data["tasks"]
                # Should create Task objects here!
                # But code just stops - never adds to self.tasks!
                pass
            
            return True
        except Exception as e:
            print(f"Error loading: {e}")
            return False
    
    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks!")
            return
        
        print("\n=== Task List ===")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task.completed else "○"
            print(f"{i}. [{status}] {task.title}")
            if task.description:
                print(f"   {task.description}")
        
        print(f"\nPending: {self.get_pending_count()}")
        print(f"Completed: {self.get_completed_count()}")  # BUG: Shows wrong count
    
    def print_report(self):
        """Print task summary."""
        total = len(self.tasks)
        completed = self.get_completed_count()  # BUG: Wrong value
        pending = self.get_pending_count()
        
        print(f"\n=== Task Report ===")
        print(f"Total: {total}")
        print(f"Completed: {completed}")  # BUG: This will be double
        print(f"Pending: {pending}")
        print(f"Progress: {(completed/total*100) if total > 0 else 0:.1f}%")


# Test the system
if __name__ == "__main__":
    manager = TaskManager("tasks.json")
    
    # Add tasks
    manager.add_task("Buy groceries", "Milk, eggs, bread")
    manager.add_task("Write code", "Day 8 exercises")
    manager.add_task("Exercise", "30 minutes running")
    
    # Mark some complete
    manager.complete_task("Buy groceries")
    
    # Display
    manager.list_tasks()
    manager.print_report()
    
    # Try to delete
    print("\nDeleting 'Buy groceries'...")
    if manager.delete_task("Buy groceries"):
        print("Deleted!")
    else:
        print("Failed to delete (BUG #804!)")
    
    # Save
    print("\nSaving tasks...")
    manager.save_tasks()
    
    # Try to load
    print("Loading tasks...")
    manager2 = TaskManager("tasks.json")
    manager2.list_tasks()
    print(f"Loaded {len(manager2.tasks)} tasks (BUG #801: should be 2!)")
