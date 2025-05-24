from app.config.conexion import get_connection

# LISTA A TODOS LOS COMPORTAMIENTO
def comportamiento_getcomportamiento(idPaciente):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT frame, detecciones, movimientos, clasificacion FROM comportamiento WHERE idPaciente = ?",(idPaciente))
            comportamiento_lst = cursor.fetchall()
            conn.close()
            return comportamiento_lst
    except Exception as e:
         return str(e)
    