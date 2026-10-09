# Task Manager Console App

A pure Python console application for managing tasks, built for the Cognifyz Level 2 (Intermediate) Task 3.

## Features
- **Create**: Add tasks with titles, optional descriptions, priority levels, and due dates.
- **Read**: View all tasks in a formatted table, or view detailed information for a specific task.
- **Update**: Modify existing tasks or quickly mark them as completed.
- **Delete**: Safely remove tasks with a confirmation prompt.
- **Search/Filter**: Search by keyword or filter by status and priority.
- **Robust Validation**: Error handling prevents crashes on bad inputs (e.g., incorrect date formats, empty titles).

## How to Run
Ensure you have Python 3.10+ installed.
1. Open your terminal.
2. Navigate to the `task_manager` directory.
3. Run the app:
   ```bash
   python main.py
   ```

## How to Run Tests
The project includes a robust test suite using the built-in `unittest` framework.
To run the tests:
```bash
python -m unittest -v test_tasks.py
```

## How CRUD is implemented
- **Storage**: Tasks are stored in memory using a Python list of `Task` objects within the `TaskManager` class.
- **Create**: `TaskManager.add_task` validates inputs via `utils.py` and appends a new `Task` to the list.
- **Read**: `TaskManager.get_all_tasks` and `TaskManager.get_task(id)` iterate over the list to return requested tasks.
- **Update**: `TaskManager.update_task` retrieves a task by its ID and modifies its object attributes directly.
- **Delete**: `TaskManager.delete_task` finds the task by ID and removes it from the list via `list.remove()`.

## Sample Output
```
===== TASK MANAGER =====
1. Add task
2. View all tasks
3. View task by ID
4. Update task
5. Delete task
6. Search / filter tasks
7. Exit
Enter choice: 2

--- All Tasks ---
ID   | Title                | Priority   | Due Date     | Status
----------------------------------------------------------------------
1    | Buy groceries        | High       | 2026-12-31   | Pending
```
