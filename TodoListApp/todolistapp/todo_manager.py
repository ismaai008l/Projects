# todolist/todo_manager.py
from typing import List, Optional
from .models import Task

class TodoManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        return task

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, updated_task: Task) -> Optional[Task]:
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks[index] = updated_task
                return updated_task
        return None

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False
