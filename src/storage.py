import json
from threading import Lock
from config import Config
import os

class StorageManager:
    """Manager untuk operasi baca/tulis file JSON"""
    
    def __init__(self, data_file=None):
        self.data_file = data_file or Config.DATA_FILE
        self.lock = Lock()
        self._initialize_file()
    
    def _initialize_file(self):
        """Inisialisasi file jika belum ada"""
        # Pastikan direktori parent ada
        data_dir = os.path.dirname(self.data_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
        
        # Buat file jika tidak ada
        if not os.path.exists(self.data_file):
            self.write([])
    
    def read(self):
        """Membaca data dari file JSON"""
        with self.lock:
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                return []
    
    def write(self, data):
        """Menulis data ke file JSON"""
        with self.lock:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)