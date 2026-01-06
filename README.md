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

### Struktur Proyek

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

### Kebutuhan Variabel

#### config.py
| Variabel | Tipe Data | Deskripsi | Nilai Default |
|----------|-----------|-----------|---------------|
| `DATA_FILE` | string | Lokasi file penyimpanan JSON | `tasks.json` |
| `DEBUG` | boolean | Mode debug Flask | `True` |
| `HOST` | string | Alamat host server | `0.0.0.0` |
| `PORT` | integer | Port server | `5000` |

#### models.py
| Atribut | Tipe Data | Deskripsi |
|---------|-----------|-----------|
| `id` | integer | Identitas unik tugas |
| `title` | string | Judul tugas |
| `content` | string | Konten detail tugas |
| `timestamp` | string (ISO 8601) | Waktu pembuatan/pembaruan |

#### services.py
| Atribut | Tipe Data | Deskripsi |
|---------|-----------|-----------|
| `storage` | StorageManager | Instance untuk operasi penyimpanan |

#### storage.py
| Atribut | Tipe Data | Deskripsi |
|---------|-----------|-----------|
| `data_file` | string | Path file JSON |
| `lock` | threading.Lock | Lock untuk thread-safety |

### Prosedur dan Fungsi

#### app.py - Fungsi Utama

**`create_app()`**
- **Deskripsi:** Factory function untuk membuat instance Flask
- **Return:** Object Flask app yang telah dikonfigurasi
- **Fungsi:** Menginisialisasi aplikasi, mendaftarkan blueprint, dan mendefinisikan endpoint home

**`home()`**
- **Deskripsi:** Endpoint root untuk informasi API
- **Method:** GET
- **Return:** JSON berisi informasi API dan daftar endpoint

#### models.py - Model Data

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

#### routes.py - Endpoint API

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

#### services.py - Business Logic

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

#### storage.py - Manajemen Penyimpanan

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

### Alur Kerja Aplikasi

1. **Inisialisasi:** Aplikasi dimulai dari `app.py`, membuat instance Flask dan mendaftarkan blueprint
2. **Request Handling:** Ketika client mengirim request HTTP, Flask mengarahkan ke fungsi handler di `routes.py`
3. **Business Logic:** Handler memanggil method di `TaskService` untuk memproses logika bisnis
4. **Data Access:** `TaskService` menggunakan `StorageManager` untuk membaca/menulis data
5. **Response:** Data dikembalikan dalam format JSON dengan status code yang sesuai

---

### 3.2 Cara Menjalankan Aplikasi

#### 3.2.1 Instalasi Dependencies

```bash
# Buat virtual environment (opsional tapi disarankan)
python -m venv venv

# Aktifkan virtual environment
# Linux/Mac:
source venv/bin/activate

# Install Flask
pip install flask

export DATA_FILE=
export DEBUG=
export HOST=
export PORT=
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
flask-cors==4.0.0
```

### C. Contoh File .env

```
DATA_FILE=tasks.json
DEBUG=true
HOST=0.0.0.0
PORT=5000
```

### D. Contoh Request menggunakan curl

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