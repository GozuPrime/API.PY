from app.config.conexion import get_connection

# LISTA A TODOS LOS PACIENTES
def paciente_sellst():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT idPaciente, nombre, apellido, dni FROM pacientes")
            paciente_lst = cursor.fetchall()
            conn.close()
            return paciente_lst
    except Exception as e:
         return str(e)
    
# REGISTRA AL PACIENTE Y RETORNA SU ID
def paciente_inst(nombre,apellido,dni):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO pacientes (nombre, apellido, dni) VALUES (?, ?, ?)",
                (nombre, apellido, dni)
            )
            pacienteId = cursor.fetchone()[0]
            conn.close()
            return pacienteId
    except Exception as e:
         return str(e)