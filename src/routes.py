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
        description=data.get('description', '')
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
        description=data.get('description')
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