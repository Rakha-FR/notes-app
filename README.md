# LAPORAN APLIKASI TODO LIST REST API

**Nama Aplikasi:** Todo List REST API (Modular)  
**Versi:** 2.0  
**Framework:** Flask (Python)  
**Tanggal:** Januari 2025

---

## BAB 1: PENDAHULUAN

### 1.1 Latar Belakang Masalah

Dalam era digital saat ini, pengelolaan tugas dan catatan menjadi kebutuhan penting bagi individu maupun organisasi. Banyak pengguna memerlukan sistem yang dapat menyimpan, mengubah, dan menghapus catatan dengan mudah dan terstruktur. Namun, sistem pencatatan tradisional sering kali tidak efisien dan sulit diintegrasikan dengan aplikasi lain.

Aplikasi Todo List REST API dikembangkan untuk menjawab tantangan tersebut dengan menyediakan antarmuka pemrograman aplikasi (API) yang memungkinkan operasi CRUD (_Create, Read, Update, Delete_) pada data tugas. Dengan arsitektur modular dan penggunaan format JSON, aplikasi ini memudahkan integrasi dengan berbagai platform dan perangkat.

### 1.2 Maksud dan Tujuan Dibuatnya Aplikasi

**Maksud:**
- Menyediakan sistem manajemen tugas berbasis REST API yang mudah digunakan
- Membangun aplikasi dengan arsitektur modular yang mudah dikembangkan dan dipelihara
- Mengimplementasikan prinsip pemisahan tanggung jawab (_separation of concerns_) dalam pengembangan perangkat lunak

**Tujuan:**
1. Memudahkan pengguna dalam mengelola daftar tugas melalui API
2. Menyediakan antarmuka yang konsisten untuk operasi CRUD
3. Memastikan data tersimpan secara persisten dalam format JSON
4. Memberikan respons yang terstruktur dan mudah dipahami
5. Mendukung integrasi dengan aplikasi klien berbasis web, mobile, atau desktop

### 1.3 Deskripsi Singkat Aplikasi

Todo List REST API adalah aplikasi berbasis Flask yang menyediakan layanan manajemen tugas melalui protokol HTTP. Aplikasi ini memiliki arsitektur modular dengan pemisahan yang jelas antara lapisan rute (_routes_), layanan (_services_), model (_models_), dan penyimpanan (_storage_).

**Fitur Utama:**
- Mendapatkan semua tugas (GET `/api/tasks`)
- Mendapatkan tugas berdasarkan ID (GET `/api/tasks/<id>`)
- Membuat tugas baru (POST `/api/tasks`)
- Memperbarui tugas (PUT `/api/tasks/<id>`)
- Menghapus tugas (DELETE `/api/tasks/<id>`)

**Teknologi yang Digunakan:**
- **Python 3.x** - Bahasa pemrograman utama
- **Flask** - Framework web untuk membangun REST API
- **JSON** - Format penyimpanan data
- **Threading Lock** - Untuk thread-safety pada operasi file

---

## BAB 2: DETAIL KEBUTUHAN APLIKASI

### 2.1 Struktur Proyek

Aplikasi menggunakan arsitektur modular dengan struktur sebagai berikut:

```
todo-api/
├── app.py           # Entry point aplikasi
├── config.py        # Konfigurasi aplikasi
├── models.py        # Model data Task
├── routes.py        # Definisi endpoint API
├── services.py      # Business logic
├── storage.py       # Pengelolaan penyimpanan data
└── tasks.json       # File penyimpanan data (dibuat otomatis)
```

### 2.2 Kebutuhan Variabel

#### 2.2.1 Kelas Config (config.py)
| Variabel | Tipe Data | Deskripsi | Nilai Default |
|----------|-----------|-----------|---------------|
| `DATA_FILE` | string | Lokasi file penyimpanan JSON | `tasks.json` |
| `DEBUG` | boolean | Mode debug Flask | `True` |
| `HOST` | string | Alamat host server | `0.0.0.0` |
| `PORT` | integer | Port server | `5000` |

#### 2.2.2 Kelas Task (models.py)
| Atribut | Tipe Data | Deskripsi |
|---------|-----------|-----------|
| `id` | integer | Identitas unik tugas |
| `title` | string | Judul tugas |
| `content` | string | Konten detail tugas |
| `timestamp` | string (ISO 8601) | Waktu pembuatan/pembaruan |

#### 2.2.3 Kelas TaskService (services.py)
| Atribut | Tipe Data | Deskripsi |
|---------|-----------|-----------|
| `storage` | StorageManager | Instance untuk operasi penyimpanan |

#### 2.2.4 Kelas StorageManager (storage.py)
| Atribut | Tipe Data | Deskripsi |
|---------|-----------|-----------|
| `data_file` | string | Path file JSON |
| `lock` | threading.Lock | Lock untuk thread-safety |

### 2.3 Prosedur dan Fungsi

#### 2.3.1 app.py - Fungsi Utama

**`create_app()`**
- **Deskripsi:** Factory function untuk membuat instance Flask
- **Return:** Object Flask app yang telah dikonfigurasi
- **Fungsi:** Menginisialisasi aplikasi, mendaftarkan blueprint, dan mendefinisikan endpoint home

**`home()`**
- **Deskripsi:** Endpoint root untuk informasi API
- **Method:** GET
- **Return:** JSON berisi informasi API dan daftar endpoint

#### 2.3.2 models.py - Model Data

**`__init__(self, id, title, content='', timestamp=None)`**
- **Deskripsi:** Konstruktor kelas Task
- **Parameter:**
  - `id`: ID unik tugas
  - `title`: Judul tugas
  - `content`: Deskripsi tugas (opsional)
  - `timestamp`: Waktu pembuatan (default: waktu sekarang)

**`to_dict(self)`**
- **Deskripsi:** Mengonversi object Task menjadi dictionary
- **Return:** Dictionary berisi data tugas

**`from_dict(data)` (static method)**
- **Deskripsi:** Membuat object Task dari dictionary
- **Parameter:** `data` - Dictionary berisi data tugas
- **Return:** Instance Task

#### 2.3.3 routes.py - Endpoint API

**`get_all_tasks()`**
- **Endpoint:** GET `/api/tasks`
- **Deskripsi:** Mengambil semua tugas
- **Response:** JSON berisi array tugas dan jumlah total

**`get_task(task_id)`**
- **Endpoint:** GET `/api/tasks/<int:task_id>`
- **Deskripsi:** Mengambil tugas berdasarkan ID
- **Parameter:** `task_id` - ID tugas
- **Response:** JSON berisi data tugas atau pesan error (404)

**`create_task()`**
- **Endpoint:** POST `/api/tasks`
- **Deskripsi:** Membuat tugas baru
- **Request Body:** JSON dengan field `title` (wajib) dan `content` (opsional)
- **Response:** JSON berisi tugas yang baru dibuat (201)

**`update_task(task_id)`**
- **Endpoint:** PUT `/api/tasks/<int:task_id>`
- **Deskripsi:** Memperbarui tugas berdasarkan ID
- **Parameter:** `task_id` - ID tugas
- **Request Body:** JSON dengan field `title` dan/atau `content`
- **Response:** JSON berisi tugas yang diperbarui atau error (404)

**`delete_task(task_id)`**
- **Endpoint:** DELETE `/api/tasks/<int:task_id>`
- **Deskripsi:** Menghapus tugas berdasarkan ID
- **Parameter:** `task_id` - ID tugas
- **Response:** JSON berisi tugas yang dihapus atau error (404)

#### 2.3.4 services.py - Business Logic

**`get_all_tasks(self)`**
- **Deskripsi:** Mengambil semua tugas dari storage
- **Return:** List object Task

**`get_task_by_id(self, task_id)`**
- **Deskripsi:** Mencari tugas berdasarkan ID
- **Parameter:** `task_id` - ID tugas
- **Return:** Object Task atau None

**`create_task(self, title, content='')`**
- **Deskripsi:** Membuat tugas baru dengan ID otomatis
- **Parameter:**
  - `title`: Judul tugas
  - `content`: Deskripsi tugas
- **Return:** Object Task yang baru dibuat

**`update_task(self, task_id, title=None, content=None)`**
- **Deskripsi:** Memperbarui data tugas
- **Parameter:**
  - `task_id`: ID tugas
  - `title`: Judul baru (opsional)
  - `content`: Deskripsi baru (opsional)
- **Return:** Object Task yang diperbarui atau None

**`delete_task(self, task_id)`**
- **Deskripsi:** Menghapus tugas berdasarkan ID
- **Parameter:** `task_id` - ID tugas
- **Return:** Object Task yang dihapus atau None

**`_get_next_id(self, tasks_data)`**
- **Deskripsi:** Menghitung ID berikutnya untuk tugas baru
- **Parameter:** `tasks_data` - List data tugas
- **Return:** Integer ID berikutnya

#### 2.3.5 storage.py - Manajemen Penyimpanan

**`_initialize_file(self)`**
- **Deskripsi:** Menginisialisasi file JSON jika belum ada
- **Fungsi:** Membuat direktori dan file dengan data kosong

**`read(self)`**
- **Deskripsi:** Membaca data dari file JSON dengan thread-safe
- **Return:** List dictionary berisi data tugas

**`write(self, data)`**
- **Deskripsi:** Menulis data ke file JSON dengan thread-safe
- **Parameter:** `data` - List data yang akan disimpan
- **Fungsi:** Menyimpan data dengan format indentasi yang rapi

### 2.4 Alur Kerja Aplikasi

1. **Inisialisasi:** Aplikasi dimulai dari `app.py`, membuat instance Flask dan mendaftarkan blueprint
2. **Request Handling:** Ketika client mengirim request HTTP, Flask mengarahkan ke fungsi handler di `routes.py`
3. **Business Logic:** Handler memanggil method di `TaskService` untuk memproses logika bisnis
4. **Data Access:** `TaskService` menggunakan `StorageManager` untuk membaca/menulis data
5. **Response:** Data dikembalikan dalam format JSON dengan status code yang sesuai

---

## BAB 3: IMPLEMENTASI

### 3.1 Source Code

#### 3.1.1 app.py - Entry Point Aplikasi

```python
from flask import Flask, jsonify
from routes import api_bp
from config import Config

def create_app():
    """Factory function untuk membuat Flask app"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Home endpoint
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            'message': 'Todo List REST API (Modular)',
            'version': '2.0',
            'endpoints': {
                'GET /api/tasks': 'Mendapatkan semua tasks',
                'GET /api/tasks/<id>': 'Mendapatkan task berdasarkan ID',
                'POST /api/tasks': 'Membuat task baru (body: title, content)',
                'PUT /api/tasks/<id>': 'Update task berdasarkan ID',
                'DELETE /api/tasks/<id>': 'Menghapus task berdasarkan ID'
            }
        }), 200
    
    return app

if __name__ == '__main__':
    app = create_app()
    print(f"Server berjalan di http://{Config.HOST}:{Config.PORT}")
    print("Tekan CTRL+C untuk menghentikan server")
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
```

#### 3.1.2 config.py - Konfigurasi Aplikasi

```python
import os

class Config:
    # Path data file dengan fallback ke direktori saat ini jika tidak ada
    _data_file = os.getenv("DATA_FILE", "tasks.json")
    DATA_FILE = os.path.abspath(_data_file) if not os.path.isabs(_data_file) else _data_file
    DEBUG = bool(os.getenv("DEBUG", "true").lower() == "true")
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
```

#### 3.1.3 models.py - Model Data

```python
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
```

#### 3.1.4 routes.py - Definisi Endpoint

```python
from flask import Blueprint, jsonify, request
from services import TaskService

api_bp = Blueprint('api', __name__, url_prefix='/api')
task_service = TaskService()

@api_bp.route('/tasks', methods=['GET'])
def get_all_tasks():
    """Endpoint untuk mendapatkan semua tasks"""
    tasks = task_service.get_all_tasks()
    return jsonify({
        'success': True,
        'count': len(tasks),
        'data': [task.to_dict() for task in tasks]
    }), 200

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Endpoint untuk mendapatkan task berdasarkan ID"""
    task = task_service.get_task_by_id(task_id)
    
    if task:
        return jsonify({
            'success': True,
            'data': task.to_dict()
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': f'Task dengan ID {task_id} tidak ditemukan'
        }), 404

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    """Endpoint untuk membuat task baru"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({
            'success': False,
            'message': 'Title wajib diisi'
        }), 400
    
    task = task_service.create_task(
        title=data['title'],
        content=data.get('content', '')
    )
    
    return jsonify({
        'success': True,
        'message': 'Task berhasil dibuat',
        'data': task.to_dict()
    }), 201

@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Endpoint untuk update task berdasarkan ID"""
    data = request.get_json()
    
    task = task_service.update_task(
        task_id=task_id,
        title=data.get('title'),
        content=data.get('content')
    )
    
    if task:
        return jsonify({
            'success': True,
            'message': 'Task berhasil diupdate',
            'data': task.to_dict()
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': f'Task dengan ID {task_id} tidak ditemukan'
        }), 404

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Endpoint untuk menghapus task berdasarkan ID"""
    task = task_service.delete_task(task_id)
    
    if task:
        return jsonify({
            'success': True,
            'message': f'Task dengan ID {task_id} berhasil dihapus',
            'data': task.to_dict()
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': f'Task dengan ID {task_id} tidak ditemukan'
        }), 404
```

#### 3.1.5 services.py - Business Logic

```python
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
    
    def create_task(self, title, content=''):
        """Membuat task baru"""
        tasks_data = self.storage.read()
        new_id = self._get_next_id(tasks_data)
        
        new_task = Task(
            id=new_id,
            title=title,
            content=content
        )
        
        tasks_data.append(new_task.to_dict())
        self.storage.write(tasks_data)
        
        return new_task
    
    def update_task(self, task_id, title=None, content=None):
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
        if content is not None:
            tasks_data[task_index]['content'] = content
        
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
```

#### 3.1.6 storage.py - Manajemen Penyimpanan

```python
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
```

### 3.2 Cara Menjalankan Aplikasi

#### 3.2.1 Instalasi Dependencies

```bash
# Buat virtual environment (opsional tapi disarankan)
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install Flask
pip install flask
```

#### 3.2.2 Menjalankan Server

```bash
python app.py
```

Output yang diharapkan:
```
Server berjalan di http://0.0.0.0:5000
Tekan CTRL+C untuk menghentikan server
```

### 3.3 Screenshot Hasil Running dan Penjelasan

#### 3.3.1 Menjalankan Server

**Screenshot:** Terminal menampilkan pesan server berhasil dijalankan

**Penjelasan:** Server Flask berjalan pada port 5000 dan siap menerima request HTTP. Mode debug diaktifkan untuk memudahkan pengembangan.

#### 3.3.2 GET / - Endpoint Home

**Request:**
```
GET http://localhost:5000/
```

**Response (200 OK):**
```json
{
  "message": "Todo List REST API (Modular)",
  "version": "2.0",
  "endpoints": {
    "GET /api/tasks": "Mendapatkan semua tasks",
    "GET /api/tasks/<id>": "Mendapatkan task berdasarkan ID",
    "POST /api/tasks": "Membuat task baru (body: title, content)",
    "PUT /api/tasks/<id>": "Update task berdasarkan ID",
    "DELETE /api/tasks/<id>": "Menghapus task berdasarkan ID"
  }
}
```

**Penjelasan:** Endpoint root memberikan informasi tentang API dan daftar endpoint yang tersedia.

#### 3.3.3 POST /api/tasks - Membuat Task Baru

**Request:**
```
POST http://localhost:5000/api/tasks
Content-Type: application/json

{
  "title": "Belajar Flask",
  "content": "Mempelajari framework Flask untuk pengembangan REST API"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Task berhasil dibuat",
  "data": {
    "id": 1,
    "title": "Belajar Flask",
    "content": "Mempelajari framework Flask untuk pengembangan REST API",
    "timestamp": "2025-01-05T10:30:00.123456"
  }
}
```

**Penjelasan:** Task baru berhasil dibuat dengan ID otomatis (1) dan timestamp saat pembuatan.

#### 3.3.4 GET /api/tasks - Mendapatkan Semua Task

**Request:**
```
GET http://localhost:5000/api/tasks
```

**Response (200 OK):**
```json
{
  "success": true,
  "count": 3,
  "data": [
    {
      "id": 1,
      "title": "Belajar Flask",
      "content": "Mempelajari framework Flask untuk pengembangan REST API",
      "timestamp": "2025-01-05T10:30:00.123456"
    },
    {
      "id": 2,
      "title": "Membuat Dokumentasi",
      "content": "Menulis dokumentasi API yang lengkap",
      "timestamp": "2025-01-05T10:35:00.789012"
    },
    {
      "id": 3,
      "title": "Testing API",
      "content": "Melakukan pengujian pada semua endpoint",
      "timestamp": "2025-01-05T10:40:00.345678"
    }
  ]
}
```

**Penjelasan:** Menampilkan semua task yang tersimpan beserta jumlah totalnya.

#### 3.3.5 GET /api/tasks/1 - Mendapatkan Task Berdasarkan ID

**Request:**
```
GET http://localhost:5000/api/tasks/1
```

**Response (200 OK):**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "Belajar Flask",
    "content": "Mempelajari framework Flask untuk pengembangan REST API",
    "timestamp": "2025-01-05T10:30:00.123456"
  }
}
```

**Penjelasan:** Mengembalikan detail task dengan ID 1.

#### 3.3.6 PUT /api/tasks/1 - Update Task

**Request:**
```
PUT http://localhost:5000/api/tasks/1
Content-Type: application/json

{
  "title": "Belajar Flask - Updated",
  "content": "Mempelajari Flask dan mengimplementasikan REST API modular"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Task berhasil diupdate",
  "data": {
    "id": 1,
    "title": "Belajar Flask - Updated",
    "content": "Mempelajari Flask dan mengimplementasikan REST API modular",
    "timestamp": "2025-01-05T11:00:00.567890"
  }
}
```

**Penjelasan:** Task berhasil diperbarui dengan data baru dan timestamp diperbarui.

#### 3.3.7 DELETE /api/tasks/1 - Menghapus Task

**Request:**
```
DELETE http://localhost:5000/api/tasks/1
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Task dengan ID 1 berhasil dihapus",
  "data": {
    "id": 1,
    "title": "Belajar Flask - Updated",
    "content": "Mempelajari Flask dan mengimplementasikan REST API modular",
    "timestamp": "2025-01-05T11:00:00.567890"
  }
}
```

**Penjelasan:** Task dengan ID 1 berhasil dihapus dari sistem. Data task yang dihapus dikembalikan sebagai konfirmasi.

#### 3.3.8 Error Handling - Task Tidak Ditemukan

**Request:**
```
GET http://localhost:5000/api/tasks/999
```

**Response (404 Not Found):**
```json
{
  "success": false,
  "message": "Task dengan ID 999 tidak ditemukan"
}
```

**Penjelasan:** Sistem memberikan respons error yang jelas ketika task tidak ditemukan.

#### 3.3.9 Error Handling - Validasi Input

**Request:**
```
POST http://localhost:5000/api/tasks
Content-Type: application/json

{
  "content": "Task tanpa title"
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "Title wajib diisi"
}
```

**Penjelasan:** Sistem melakukan validasi input dan memberikan pesan error yang informatif.

### 3.4 Penjelasan Fitur Aplikasi

#### 3.4.1 Arsitektur Modular

Aplikasi menggunakan arsitektur berlapis yang memisahkan tanggung jawab:
- **Routes Layer:** Menangani HTTP request dan response
- **Service Layer:** Mengimplementasikan business logic
- **Model Layer:** Mendefinisikan struktur data
- **Storage Layer:** Mengelola persistensi data

Keuntungan arsitektur ini:
- Kode lebih mudah dipelihara dan dikembangkan
- Memudahkan pengujian unit (unit testing)
- Memungkinkan penggantian komponen tanpa mengubah keseluruhan sistem
- Meningkatkan reusabilitas kode

#### 3.4.2 Thread-Safe Storage

Penggunaan `threading.Lock` pada `StorageManager` memastikan bahwa operasi baca/tulis file aman untuk digunakan dalam lingkungan multi-threaded. Hal ini mencegah kondisi _race condition_ yang dapat menyebabkan data korup.

#### 3.4.3 Auto-Increment ID

Sistem secara otomatis menghasilkan ID unik untuk setiap task baru dengan mencari nilai maksimum dari ID yang sudah ada, kemudian menambahkannya dengan 1. Pendekatan ini sederhana namun efektif untuk aplikasi skala kecil hingga menengah.

#### 3.4.4 ISO 8601 Timestamp

Penggunaan format ISO 8601 untuk timestamp memastikan kompatibilitas dengan berbagai sistem dan bahasa pemrograman. Format ini juga mudah dibaca manusia dan dapat di-parse dengan mudah.

#### 3.4.5 RESTful Design

Aplikasi mengikuti prinsip REST dengan:
- Menggunakan HTTP methods yang sesuai (GET, POST, PUT, DELETE)
- URL yang deskriptif dan konsisten
- Status code HTTP yang tepat (200, 201, 400, 404)
- Response dalam format JSON yang terstruktur

#### 3.4.6 Environment Variables

Konfigurasi dapat disesuaikan melalui environment variables tanpa mengubah kode, memudahkan deployment di berbagai lingkungan (development, staging, production).

---

## BAB 4: KESIMPULAN DAN SARAN

### 4.1 Kesimpulan

Berdasarkan implementasi dan pengujian yang telah dilakukan, dapat disimpulkan bahwa:

1. **Aplikasi Berhasil Dikembangkan:** Todo List REST API versi 2.0 berhasil dibangun dengan arsitektur modular yang memisahkan tanggung jawab antara routing, business logic, model data, dan storage management.

2. **Fungsionalitas Lengkap:** Semua operasi CRUD (Create, Read, Update, Delete) telah diimplementasikan dengan baik dan berfungsi sesuai harapan. Setiap endpoint memberikan respons yang konsisten dan informatif.

3. **Desain yang Baik:** Implementasi mengikuti prinsip-prinsip pengembangan perangkat lunak yang baik, seperti:
   - Separation of Concerns (pemisahan tanggung jawab)
   - Single Responsibility Principle (setiap kelas memiliki satu tanggung jawab)
   - RESTful API design patterns
   - Thread-safe operations untuk concurrent access

4. **Keamanan Data:** Penggunaan threading lock pada operasi file I/O memastikan integritas data dalam lingkungan multi-threaded. Data disimpan dalam format JSON yang mudah dibaca dan di-backup.

5. **Skalabilitas Terbatas:** Meskipun efektif untuk aplikasi skala kecil hingga menengah, penggunaan file JSON sebagai penyimpanan memiliki keterbatasan dalam hal performa dan skalabilitas untuk data berskala besar.

6. **Error Handling yang Baik:** Aplikasi memberikan respons error yang informatif dengan HTTP status code yang tepat, memudahkan debugging dan integrasi dengan sistem lain.

7. **Mudah Dikembangkan:** Arsitektur modular memungkinkan pengembangan fitur baru atau modifikasi tanpa mengubah keseluruhan sistem. Misalnya, storage layer dapat dengan mudah diganti dari file JSON ke database tanpa mengubah layer lainnya.

### 4.2 Saran

#### 4.2.1 Untuk Pengembangan Lebih Lanjut

**1. Migrasi ke Database**

Untuk meningkatkan performa dan skalabilitas, disarankan untuk:
- Menggunakan database relasional seperti PostgreSQL atau MySQL
- Implementasi ORM seperti SQLAlchemy untuk abstraksi database
- Menambahkan connection pooling untuk optimasi koneksi database

**2. Implementasi Autentikasi dan Otorisasi**

Menambahkan keamanan dengan:
- JWT (JSON Web Token) untuk autentikasi
- Role-based access control (RBAC)
- Rate limiting untuk mencegah abuse
- HTTPS untuk enkripsi data transmisi

**3. Penambahan Fitur**

Fitur-fitur yang dapat ditambahkan:
- Kategori atau tag untuk task
- Status completion (completed/pending)
- Priority level (high/medium/low)
- Due date dan reminder
- Pencarian dan filter
- Pagination untuk daftar task yang panjang
- Soft delete (tidak menghapus permanen)

**4. Validasi Input yang Lebih Ketat**

Meningkatkan validasi dengan:
- Menggunakan library seperti marshmallow atau pydantic
- Validasi panjang maksimal title dan content
- Sanitasi input untuk mencegah injection attacks
- Type checking yang lebih ketat

**5. Logging dan Monitoring**

Implementasi sistem logging untuk:
- Tracking request dan response
- Monitoring error dan exception
- Analisis performa aplikasi
- Audit trail untuk perubahan data

**6. Unit Testing dan Integration Testing**

Menambahkan test coverage dengan:
- Unit test untuk setiap function
- Integration test untuk endpoint
- Test automation menggunakan pytest atau unittest
- Continuous Integration/Continuous Deployment (CI/CD)

**7. Dokumentasi API**

Meningkatkan dokumentasi dengan:
- Swagger/OpenAPI specification
- Interactive API documentation
- Example requests dan responses
- Error codes dan handling guide

**8. Containerization**

Memudahkan deployment dengan:
- Docker containerization
- Docker Compose untuk orchestration
- Kubernetes untuk production scaling

#### 4.2.2 Untuk Penggunaan

**1. Backup Data Berkala**

Karena menggunakan file JSON, sangat disarankan untuk:
- Melakukan backup rutin file `tasks.json`
- Implementasi automated backup script
- Menyimpan backup di lokasi terpisah

**2. Environment Configuration**

Untuk deployment:
- Gunakan environment variables untuk konfigurasi sensitif
- Jangan commit file konfigurasi dengan data sensitif
- Gunakan `.env` file untuk local development

**3. Monitoring Resource Usage**

Pantau penggunaan:
- CPU dan memory usage
- Disk space untuk file JSON
- Response time endpoint
- Request rate

**4. Security Best Practices**

Terapkan praktik keamanan:
- Jangan expose server ke public tanpa firewall
- Gunakan reverse proxy seperti Nginx
- Implementasi SSL/TLS certificate
- Regular security updates

#### 4.2.3 Untuk Pembelajaran

**1. Eksplorasi Framework Lain**

Untuk memperluas pengetahuan:
- FastAPI untuk async support dan automatic documentation
- Django REST Framework untuk aplikasi yang lebih kompleks
- Express.js (Node.js) untuk perbandingan ekosistem

**2. Studi Database Design**

Pelajari tentang:
- Normalisasi database
- Indexing untuk optimasi query
- Transaction management
- Database migration strategies

**3. Microservices Architecture**

Eksplorasi konsep:
- Service decomposition
- API Gateway pattern
- Event-driven architecture
- Message queues (RabbitMQ, Kafka)

**4. Cloud Deployment**

Pelajari deployment ke cloud:
- AWS (EC2, Lambda, RDS)
- Google Cloud Platform
- Microsoft Azure
- Heroku untuk quick deployment

### 4.3 Penutup

Todo List REST API yang telah dikembangkan merupakan fondasi yang solid untuk aplikasi manajemen tugas. Dengan arsitektur modular yang baik, aplikasi ini mudah untuk dikembangkan dan dipelihara. Implementasi prinsip-prinsip REST dan pemisahan tanggung jawab membuat kode lebih terstruktur dan profesional.

Meskipun masih terdapat ruang untuk perbaikan, terutama dalam hal skalabilitas dan keamanan, aplikasi ini telah berhasil memenuhi tujuan awal untuk menyediakan API yang fungsional dan mudah digunakan. Dengan mengikuti saran-saran yang telah diuraikan, aplikasi ini dapat dikembangkan menjadi solusi enterprise-grade yang robust dan scalable.

Pengembangan aplikasi ini juga memberikan pembelajaran berharga tentang best practices dalam pengembangan REST API, arsitektur software, dan pengelolaan data. Pengetahuan ini dapat menjadi dasar untuk proyek-proyek yang lebih kompleks di masa mendatang.

---

## REFERENSI

1. **Flask Documentation** - Official Flask framework documentation
   - URL: https://flask.palletsprojects.com/
   - Diakses: Januari 2025

2. **REST API Design Best Practices** - RESTful API design guidelines
   - Source: Mozilla Developer Network (MDN)
   - URL: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

3. **Python Official Documentation** - Python 3 standard library
   - URL: https://docs.python.org/3/
   - Diakses: Januari 2025

4. **PEP 8 - Style Guide for Python Code**
   - URL: https://peps.python.org/pep-0008/
   - Style guidelines yang diikuti dalam penulisan kode

5. **Threading - Python Threading Module**
   - URL: https://docs.python.org/3/library/threading.html
   - Referensi untuk implementasi thread-safe operations

6. **JSON Format Specification** - RFC 8259
   - URL: https://datatracker.ietf.org/doc/html/rfc8259
   - Spesifikasi format JSON yang digunakan

7. **HTTP Status Codes** - RFC 7231
   - URL: https://datatracker.ietf.org/doc/html/rfc7231
   - Referensi untuk penggunaan HTTP status codes

8. **ISO 8601 - Date and Time Format**
   - URL: https://www.iso.org/iso-8601-date-and-time-format.html
   - Format timestamp yang digunakan dalam aplikasi

---

## LAMPIRAN

### A. Cara Instalasi Dependencies

```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi virtual environment (Windows)
venv\Scripts\activate

# Aktivasi virtual environment (Linux/Mac)
source venv/bin/activate

# Install Flask
pip install flask

# Menyimpan dependencies ke file
pip freeze > requirements.txt
```

### B. File requirements.txt

```
Flask==3.0.0
Werkzeug==3.0.1
click==8.1.7
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
```

### C. Contoh File .env

```
DATA_FILE=tasks.json
DEBUG=true
HOST=0.0.0.0
PORT=5000
```

### D. Contoh Request menggunakan cURL

```bash
# GET semua tasks
curl -X GET http://localhost:5000/api/tasks

# GET task berdasarkan ID
curl -X GET http://localhost:5000/api/tasks/1

# POST task baru
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Task Baru","content":"Konten task"}'

# PUT update task
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Task Updated","content":"Konten baru"}'

# DELETE task
curl -X DELETE http://localhost:5000/api/tasks/1
```

### E. Struktur File tasks.json

```json
[
  {
    "id": 1,
    "title": "Belajar Flask",
    "content": "Mempelajari framework Flask",
    "timestamp": "2025-01-05T10:30:00.123456"
  },
  {
    "id": 2,
    "title": "Membuat API",
    "content": "Implementasi REST API",
    "timestamp": "2025-01-05T10:35:00.789012"
  }
]
```

---

**Dokumen ini dibuat pada:** Januari 2025  
**Versi Dokumen:** 1.0  
**Status:** Final