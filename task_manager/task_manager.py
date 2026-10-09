from task import Task
from utils import validate_title, validate_priority, validate_date, validate_status

class TaskManager:
    """Manages the in-memory list of tasks and handles CRUD operations."""

    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, due_date_str):
        t_title = validate_title(title)
        t_priority = validate_priority(priority)
        t_due = validate_date(due_date_str)
        
        task = Task(t_title, description.strip() if description else "", t_priority, t_due)
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None

    def update_task(self, task_id, title=None, description=None, priority=None, due_date_str=None, status=None):
        task = self.get_task(task_id)
        if not task:
            raise ValueError("Task not found.")
        
        if title is not None and title.strip():
            task.title = validate_title(title)
        if description is not None:
            task.description = description.strip()
        if priority is not None and priority.strip():
            task.priority = validate_priority(priority)
        if due_date_str is not None and due_date_str.strip():
            task.due_date = validate_date(due_date_str)
        if status is not None and status.strip():
            task.status = validate_status(status)
        return task
        
    def delete_task(self, task_id):
        task = self.get_task(task_id)
        if not task:
            raise ValueError("Task not found.")
        self.tasks.remove(task)
        return task

    def search_tasks(self, keyword=None, status=None, priority=None):
        results = self.tasks
        if keyword:
            results = [t for t in results if keyword.lower() in t.title.lower() or keyword.lower() in t.description.lower()]
        if status:
            results = [t for t in results if t.status.lower() == status.lower()]
        if priority:
            results = [t for t in results if t.priority.lower() == priority.lower()]
        return results
