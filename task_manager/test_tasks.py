import unittest
import datetime
from task import Task
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        Task._id_counter = 1
        self.tm = TaskManager()
        
    def test_add_valid_task(self):
        t = self.tm.add_task("Buy groceries", "Milk and eggs", "High", "2026-12-31")
        self.assertEqual(t.title, "Buy groceries")
        self.assertEqual(t.priority, "High")
        self.assertEqual(t.due_date, datetime.date(2026, 12, 31))
        self.assertEqual(len(self.tm.get_all_tasks()), 1)
        
    def test_add_empty_title(self):
        with self.assertRaises(ValueError):
            self.tm.add_task("", "desc", "Low", "")
            
    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            self.tm.add_task("Title", "desc", "Urgent", "")
            
    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            self.tm.add_task("Title", "desc", "Low", "12-31-2026")
            
    def test_view_empty_list(self):
        self.assertEqual(self.tm.get_all_tasks(), [])
        
    def test_update_existing_task(self):
        t = self.tm.add_task("Task 1", "desc", "Low", "")
        self.tm.update_task(t.id, title="Task 1 Updated", status="Completed")
        self.assertEqual(t.title, "Task 1 Updated")
        self.assertEqual(t.status, "Completed")
        
    def test_update_missing_id(self):
        with self.assertRaises(ValueError):
            self.tm.update_task(999, title="Not found")
            
    def test_delete_existing_task(self):
        t = self.tm.add_task("Task 1", "", "", "")
        self.tm.delete_task(t.id)
        self.assertEqual(len(self.tm.get_all_tasks()), 0)
        
    def test_delete_missing_id(self):
        with self.assertRaises(ValueError):
            self.tm.delete_task(999)
            
    def test_id_uniqueness_after_deletion(self):
        t1 = self.tm.add_task("Task 1", "", "", "")
        t2 = self.tm.add_task("Task 2", "", "", "")
        self.tm.delete_task(t1.id)
        t3 = self.tm.add_task("Task 3", "", "", "")
        self.assertNotEqual(t2.id, t3.id)
        self.assertNotEqual(t1.id, t3.id)

if __name__ == "__main__":
    unittest.main()
