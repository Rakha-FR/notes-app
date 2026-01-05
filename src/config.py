import os

class Config:
    # Path data file dengan fallback ke direktori saat ini jika tidak ada
    _data_file = os.getenv("DATA_FILE", "tasks.json")
    DATA_FILE = os.path.abspath(_data_file) if not os.path.isabs(_data_file) else _data_file
    DEBUG = bool(os.getenv("DEBUG", "true").lower() == "true")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))