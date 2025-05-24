# api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

# Configurar conexión con SQL Server
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=GOZU\SQLEXPRESS;"  
    "DATABASE=IA_Esquizofrenia;"     
    "Trusted_Connection=yes;"        
)

# Obtener pacientes
@app.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT idPaciente, nombre, apellido, dni FROM pacientes")
        pacientes = [
            {
                'id': row.idPaciente,
                'nombre': row.nombre,
                'apellido': row.apellido,
                'dni': row.dni
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return jsonify(pacientes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Agregar paciente
@app.route('/pacientes', methods=['POST'])
def agregar_paciente():
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    dni = data.get('dni')

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO pacientes (nombre, apellido, dni) VALUES (?, ?, ?)",
            (nombre, apellido, dni)
        )
        conn.commit()
        conn.close()
        return jsonify({'mensaje': 'Paciente registrado correctamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Historial de comportamiento de un paciente
@app.route('/comportamientos/<int:idPaciente>', methods=['GET'])
def historial_comportamientos(idPaciente):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT frame, detecciones, movimientos, clasificacion FROM comportamiento WHERE idPaciente = ?",
            (idPaciente,)
        )
        registros = [
            {
                'frame': row.frame,
                'detecciones': row.detecciones,
                'movimientos': row.movimientos,
                'clasificacion': row.clasificacion
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return jsonify(registros)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)