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
            'version': '1.0',
            'endpoints': {
                'GET /api/tasks': 'Mendapatkan semua tasks',
                'GET /api/tasks/<id>': 'Mendapatkan task berdasarkan ID',
                'POST /api/tasks': 'Membuat task baru (body: title, description)',
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