from models import Task
from storage import StorageManager
from datetime import datetime

class TaskService:
    """Service untuk mengelola operasi Task"""
    
    def __init__(self, storage_manager=None):
        self.storage = storage_manager or StorageManager()
    
    def get_all_tasks(self):
        """Mendapatkan semua tasks"""
        data = self.storage.read()
        return [Task.from_dict(item) for item in data]
    
    def get_task_by_id(self, task_id):
        """Mendapatkan task berdasarkan ID"""
        tasks = self.get_all_tasks()
        return next((task for task in tasks if task.id == task_id), None)
    
    def create_task(self, title, description=''):
        """Membuat task baru"""
        tasks_data = self.storage.read()
        new_id = self._get_next_id(tasks_data)
        
        new_task = Task(
            id=new_id,
            title=title,
            description=description
        )
        
        tasks_data.append(new_task.to_dict())
        self.storage.write(tasks_data)
        
        return new_task
    
    def update_task(self, task_id, title=None, description=None):
        """Update task berdasarkan ID"""
        tasks_data = self.storage.read()
        task_index = next(
            (i for i, t in enumerate(tasks_data) if t['id'] == task_id),
            None
        )
        
        if task_index is None:
            return None
        
        if title is not None:
            tasks_data[task_index]['title'] = title
        if description is not None:
            tasks_data[task_index]['description'] = description
        
        tasks_data[task_index]['timestamp'] = datetime.now().isoformat()
        
        self.storage.write(tasks_data)
        return Task.from_dict(tasks_data[task_index])
    
    def delete_task(self, task_id):
        """Menghapus task berdasarkan ID"""
        tasks_data = self.storage.read()
        task = next((t for t in tasks_data if t['id'] == task_id), None)
        
        if task is None:
            return None
        
        tasks_data = [t for t in tasks_data if t['id'] != task_id]
        self.storage.write(tasks_data)
        
        return Task.from_dict(task)
    
    def _get_next_id(self, tasks_data):
        """Mendapatkan ID berikutnya"""
        if not tasks_data:
            return 1
        return max(task['id'] for task in tasks_data) + 1
