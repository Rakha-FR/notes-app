from datetime import datetime

class Task:
    """Model untuk Task"""
    
    def __init__(self, id, title, content='', timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().isoformat()
    
    def to_dict(self):
        """Konversi object ke dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }
    
    @staticmethod
    def from_dict(data):
        """Membuat Task object dari dictionary"""
        return Task(
            id=data['id'],
            title=data['title'],
            content=data.get('content', ''),
            timestamp=data.get('timestamp')
        )