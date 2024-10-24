# todolist/main.py
from .models import Task
from .todo_manager import TodoManager
from datetime import datetime

def main():
    todo_manager = TodoManager()

    # Example: Add a task
    task_1 = Task(id=1, title="Buy groceries", description="Milk, Eggs, Bread", due_date=datetime(2024, 10, 25))
    todo_manager.add_task(task_1)

    # Example: List all tasks
    tasks = todo_manager.get_tasks()
    print(f"Tasks: {tasks}")

    # Example: Get a task
    task = todo_manager.get_task(1)
    print(f"Task 1: {task}")

    # Example: Update a task
    task_1_updated = Task(id=1, title="Buy groceries and snacks", description="Milk, Eggs, Bread, Chips", completed=True)
    todo_manager.update_task(1, task_1_updated)

    # Example: Delete a task
    todo_manager.delete_task(1)

if __name__ == "__main__":
    main()
