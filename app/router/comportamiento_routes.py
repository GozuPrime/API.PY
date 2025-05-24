from flask import Blueprint, jsonify
from app.repositories import comportamiento_repository as repo

comportamiento_bp = Blueprint('comportamiento', __name__)

@comportamiento_bp.route('/comportamientos/<int:idPaciente>', methods=['GET'])
def historial_comportamientos(idPaciente):
    try:
        return jsonify({
            '_comportamiento':repo.comportamiento_getcomportamiento(idPaciente)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500