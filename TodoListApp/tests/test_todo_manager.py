# tests/test_todo_manager.py
import pytest
from todolistapp.todo_manager import TodoManager
from todolistapp.models import Task

@pytest.fixture
def todo_manager():
    return TodoManager()

def test_add_task(todo_manager):
    task = Task(id=1, title="Test Task")
    added_task = todo_manager.add_task(task)
    assert added_task == task
    assert len(todo_manager.get_tasks()) == 1

def test_get_task(todo_manager):
    task = Task(id=1, title="Test Task")
    todo_manager.add_task(task)
    fetched_task = todo_manager.get_task(1)
    assert fetched_task == task

def test_delete_task(todo_manager):
    task = Task(id=1, title="Test Task")
    todo_manager.add_task(task)
    todo_manager.delete_task(1)
    assert len(todo_manager.get_tasks()) == 0
