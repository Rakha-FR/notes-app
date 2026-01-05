import os

class Config:
    FILE_DATA  = os.getenv("FILE_DATA", "tasks.json")    
    DEBUG = bool(os.getenv("DEBUG", "true").lower() == "true")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))