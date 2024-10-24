from pydantic import BaseModel, Field
from typing import List, Optional
import sqlite3


# Pydantic model for the task
class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    completed: bool = False


# SQLite database handler
class ToDoListDB:
    def __init__(self, db_name="todo_list.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_task(self, task: Task):
        query = """
        INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (task.title, task.description, task.completed))
        self.connection.commit()
        task.id = cursor.lastrowid  # Set the ID after inserting
        return task

    def get_tasks(self) -> List[Task]:
        query = "SELECT id, title, description, completed FROM tasks"
        cursor = self.connection.execute(query)
        tasks = [
            Task(id=row[0], title=row[1], description=row[2], completed=bool(row[3]))
            for row in cursor.fetchall()
        ]
        return tasks

    def update_task(self, task: Task):
        query = """
        UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?
        """
        self.connection.execute(query, (task.title, task.description, task.completed, task.id))
        self.connection.commit()

    def delete_task(self, task_id: int):
        query = "DELETE FROM tasks WHERE id = ?"
        self.connection.execute(query, (task_id,))
        self.connection.commit()


# To-Do list class that interacts with the database
class ToDoList:
    def __init__(self, db_name="todo_list.db"):
        self.db = ToDoListDB(db_name)

    def create_task(self, title: str, description: Optional[str] = None):
        task = Task(title=title, description=description)
        return self.db.add_task(task)

    def get_all_tasks(self) -> List[Task]:
        return self.db.get_tasks()

    def mark_task_complete(self, task_id: int):
        tasks = self.db.get_tasks()
        task = next((t for t in tasks if t.id == task_id), None)
        if task:
            task.completed = True
            self.db.update_task(task)

    def delete_task(self, task_id: int):
        self.db.delete_task(task_id)


# Example of interacting with the ToDoList app
if __name__ == "__main__":
    todo_app = ToDoList()

    # Add tasks
    todo_app.create_task("Buy groceries", "Milk, Bread, Eggs")
    todo_app.create_task("Finish the report")

    # List all tasks
    tasks = todo_app.get_all_tasks()
    for task in tasks:
        print(task)

    # Mark a task as complete
    todo_app.mark_task_complete(task_id=1)

    # Delete a task
    todo_app.delete_task(task_id=2)
