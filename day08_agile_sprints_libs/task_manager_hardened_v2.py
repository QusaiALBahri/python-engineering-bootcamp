#!/usr/bin/env python3
"""Day 8, Lesson 2: Task Manager - Hardened Production Version

This is the PROFESSIONAL, HARDENED version with:
- Type hints and comprehensive docstrings
- Input validation on all user inputs
- Proper error handling and logging
- File persistence with error recovery
- Clean, testable code following PEP 8
"""

import json
import logging
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Task:
    """Represents a single task with validation."""
    
    def __init__(self, title: str, description: str = "") -> None:
        """Initialize a task with validation."""
        if not title or not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Task title cannot be empty")
        
        self.title = title.strip()
        self.description = description.strip()
        self.completed = False
        self.created_at = datetime.now().isoformat()
        logger.info(f"Created task: {self.title}")
    
    def mark_complete(self) -> None:
        """Mark task as completed."""
        if not self.completed:
            self.completed = True
            logger.info(f"Completed: {self.title}")
    
    def mark_incomplete(self) -> None:
        """Mark task as incomplete."""
        if self.completed:
            self.completed = False
            logger.info(f"Reopened: {self.title}")
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = Task(data['title'], data.get('description', ''))
        task.completed = data.get('completed', False)
        task.created_at = data.get('created_at', datetime.now().isoformat())
        return task
    
    def __str__(self) -> str:
        """String representation of task."""
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"


class TaskManager:
    """Professional task manager with file persistence."""
    
    def __init__(self, filepath: str = "tasks.json") -> None:
        """Initialize task manager."""
        self.filepath = Path(filepath)
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        """Load tasks from file with error recovery."""
        try:
            if self.filepath.exists():
                with open(self.filepath, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(t) for t in data]
                    logger.info(f"Loaded {len(self.tasks)} tasks")
            else:
                logger.info("No existing tasks file, starting fresh")
        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading tasks: {e}. Starting fresh.")
            self.tasks = []
    
    def save_tasks(self) -> bool:
        """Save tasks to file."""
        try:
            with open(self.filepath, 'w') as f:
                json.dump([t.to_dict() for t in self.tasks], f, indent=2)
            logger.info(f"Saved {len(self.tasks)} tasks")
            return True
        except IOError as e:
            logger.error(f"Error saving tasks: {e}")
            return False
    
    def add_task(self, title: str, description: str = "") -> Optional[Task]:
        """Add a new task."""
        try:
            task = Task(title, description)
            self.tasks.append(task)
            self.save_tasks()
            return task
        except ValueError as e:
            logger.error(f"Invalid task: {e}")
            return None
    
    def get_task(self, index: int) -> Optional[Task]:
        """Get task by index with bounds checking."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        logger.warning(f"Task index {index} out of range")
        return None
    
    def complete_task(self, index: int) -> bool:
        """Mark task as complete."""
        task = self.get_task(index)
        if task:
            task.mark_complete()
            self.save_tasks()
            return True
        return False
    
    def delete_task(self, index: int) -> bool:
        """Delete a task."""
        if 0 <= index < len(self.tasks):
            deleted = self.tasks.pop(index)
            self.save_tasks()
            logger.info(f"Deleted task: {deleted.title}")
            return True
        return False
    
    def get_completed_count(self) -> int:
        """Get correct count of completed tasks."""
        return sum(1 for t in self.tasks if t.completed)
    
    def list_tasks(self) -> None:
        """Display all tasks in formatted table."""
        if not self.tasks:
            print("\n📭 No tasks yet. Create one!")
            return
        
        print("\n" + "="*60)
        print(f"📋 Tasks ({len(self.tasks)} total, "
              f"{self.get_completed_count()} done)")
        print("="*60)
        
        for i, task in enumerate(self.tasks):
            status = "✅" if task.completed else "⏳"
            print(f"{i+1}. {status} {task.title}")
            if task.description:
                print(f"   └─ {task.description}")
        
        print("="*60 + "\n")


def main() -> None:
    """Main interactive loop."""
    manager = TaskManager("tasks_hardened.json")
    
    print("\n🚀 Task Manager Pro v2.0 (Hardened Edition)")
    print("Commands: add, list, done, delete, clear, quit")
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if command == "add":
                title = input("  Task title: ").strip()
                desc = input("  Description (optional): ").strip()
                if manager.add_task(title, desc):
                    print("✅ Task added!")
            
            elif command == "list":
                manager.list_tasks()
            
            elif command == "done":
                manager.list_tasks()
                try:
                    idx = int(input("  Task number: ")) - 1
                    if manager.complete_task(idx):
                        print("✅ Marked complete!")
                    else:
                        print("❌ Invalid task")
                except ValueError:
                    print("❌ Please enter a number")
            
            elif command == "delete":
                manager.list_tasks()
                try:
                    idx = int(input("  Task number: ")) - 1
                    if manager.delete_task(idx):
                        print("✅ Deleted!")
                    else:
                        print("❌ Invalid task")
                except ValueError:
                    print("❌ Please enter a number")
            
            elif command == "clear":
                if input("  Delete all tasks? (y/n): ").lower() == 'y':
                    manager.tasks = []
                    manager.save_tasks()
                    print("✅ All tasks cleared")
            
            elif command == "quit":
                print("\n👋 Goodbye!")
                break
            
            else:
                print("❌ Unknown command")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
