from datetime import datetime

class Task:
    """Model untuk Task"""
    
    def __init__(self, id, title, description='', timestamp=None):
        self.id = id
        self.title = title
        self.description = description
        self.timestamp = timestamp or datetime.now().isoformat()
    
    def to_dict(self):
        """Konversi object ke dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'timestamp': self.timestamp
        }
    
    @staticmethod
    def from_dict(data):
        """Membuat Task object dari dictionary"""
        return Task(
            id=data['id'],
            title=data['title'],
            description=data.get('description', ''),
            timestamp=data.get('timestamp')
        )