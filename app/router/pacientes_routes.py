from flask import Blueprint, jsonify, request
from app.repositories import pacientes_repository as repo

paciente_bp = Blueprint('pacientes', __name__)

@paciente_bp.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    try:
        return jsonify({
            "_pacientes":repo.paciente_sellst()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@paciente_bp.route('/pacientes', methods=['POST'])
def agregar_paciente():
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    dni = data.get('dni')

    try:
        if not all([nombre, apellido, dni]):
            return jsonify({'error': 'Debes completar todos los datos del formulario'}), 400
       
        pacienteId=repo.paciente_inst(nombre,apellido,dni)

        return jsonify({'mensaje': 'Paciente registrado correctamente','_paciente':pacienteId}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
