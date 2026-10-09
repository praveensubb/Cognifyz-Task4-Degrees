import datetime

class Task:
    """Represents a single task in the task manager."""
    
    _id_counter = 1

    def __init__(self, title, description, priority, due_date=None):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = "Pending"
        self.created_at = datetime.datetime.now()

    def __str__(self):
        due = self.due_date.strftime("%Y-%m-%d") if self.due_date else "None"
        return (f"ID: {self.id} | Title: {self.title}\n"
                f"Priority: {self.priority} | Status: {self.status}\n"
                f"Due Date: {due}\n"
                f"Description: {self.description}")
