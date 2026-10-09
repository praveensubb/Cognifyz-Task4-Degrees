import sys
from task_manager import TaskManager

def print_tasks_table(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print(f"{'ID':<4} | {'Title':<20} | {'Priority':<10} | {'Due Date':<12} | {'Status':<15}")
    print("-" * 70)
    for t in tasks:
        due = t.due_date.strftime("%Y-%m-%d") if t.due_date else "None"
        title = t.title[:17] + "..." if len(t.title) > 20 else t.title
        print(f"{t.id:<4} | {title:<20} | {t.priority:<10} | {due:<12} | {t.status:<15}")

def main():
    tm = TaskManager()
    
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View task by ID")
        print("4. Update task")
        print("5. Delete task")
        print("6. Search / filter tasks")
        print("7. Exit")
        
        try:
            choice = input("Enter choice: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break
            
        if choice == '1':
            print("\n--- Add Task ---")
            try:
                title = input("Title (required): ").strip()
                desc = input("Description: ").strip()
                prio = input("Priority (Low/Medium/High) [Low]: ").strip()
                due = input("Due Date (YYYY-MM-DD) [None]: ").strip()
                
                task = tm.add_task(title, desc, prio, due)
                print(f"Success! Task added with ID {task.id}.")
            except ValueError as e:
                print(f"Error: {e}")
            except (KeyboardInterrupt, EOFError):
                print("\nCancelled.")
                
        elif choice == '2':
            print("\n--- All Tasks ---")
            print_tasks_table(tm.get_all_tasks())
            
        elif choice == '3':
            print("\n--- View Task ---")
            try:
                t_id_str = input("Enter Task ID: ").strip()
                if not t_id_str:
                    continue
                t_id = int(t_id_str)
                task = tm.get_task(t_id)
                if task:
                    print("\nTask Details:")
                    print("-" * 20)
                    print(task)
                    print("-" * 20)
                else:
                    print("Error: Task not found.")
            except ValueError:
                print("Error: Invalid ID format.")
            except (KeyboardInterrupt, EOFError):
                pass
                
        elif choice == '4':
            print("\n--- Update Task ---")
            try:
                t_id_str = input("Enter Task ID to update: ").strip()
                if not t_id_str:
                    continue
                t_id = int(t_id_str)
                task = tm.get_task(t_id)
                if not task:
                    print("Error: Task not found.")
                    continue
                
                print("\nCurrent Details:")
                print(task)
                print("\nEnter new values (leave blank to keep current value):")
                
                title = input(f"Title [{task.title}]: ").strip()
                desc = input(f"Description [{task.description}]: ").strip()
                prio = input(f"Priority [{task.priority}]: ").strip()
                due_curr = task.due_date.strftime("%Y-%m-%d") if task.due_date else "None"
                due = input(f"Due Date [{due_curr}]: ").strip()
                status = input(f"Status [{task.status}]: ").strip()
                
                quick_complete = input("Mark as Completed? (y/n) [n]: ").strip().lower()
                if quick_complete == 'y':
                    status = "Completed"
                    
                tm.update_task(t_id, title, desc, prio, due, status)
                print("Task updated successfully!")
                
            except ValueError as e:
                if "invalid literal for int" in str(e):
                    print("Error: Invalid ID format.")
                else:
                    print(f"Error: {e}")
            except (KeyboardInterrupt, EOFError):
                pass
                
        elif choice == '5':
            print("\n--- Delete Task ---")
            if not tm.get_all_tasks():
                print("List is empty. Nothing to delete.")
                continue
                
            try:
                t_id_str = input("Enter Task ID to delete: ").strip()
                if not t_id_str:
                    continue
                t_id = int(t_id_str)
                task = tm.get_task(t_id)
                if not task:
                    print("Error: Task not found.")
                    continue
                
                print("\nTask Details:")
                print(task)
                confirm = input("Are you sure you want to delete this task? (y/n): ").strip().lower()
                if confirm == 'y':
                    tm.delete_task(t_id)
                    print("Task deleted successfully.")
                else:
                    print("Deletion cancelled.")
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Error: Invalid ID format.")
                else:
                    print(f"Error: {e}")
            except (KeyboardInterrupt, EOFError):
                pass
                
        elif choice == '6':
            print("\n--- Search / Filter ---")
            try:
                kw = input("Search keyword (leave blank to skip): ").strip()
                st = input("Filter by status (leave blank to skip): ").strip()
                pr = input("Filter by priority (leave blank to skip): ").strip()
                
                results = tm.search_tasks(keyword=kw, status=st, priority=pr)
                print("\nSearch Results:")
                print_tasks_table(results)
            except (KeyboardInterrupt, EOFError):
                pass
                
        elif choice == '7':
            print("Exiting Task Manager. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
