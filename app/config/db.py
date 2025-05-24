import sqlite3
def create_db():
    conn = sqlite3.connect('IA_Esquizofrenia.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE "pacientes" (
        "idPaciente"	INTEGER,
        "nombre"	TEXT,
        "apellido"	TEXT,
        "dni"	TEXT,
        PRIMARY KEY("idPaciente" AUTOINCREMENT)
    );
    ''')


    cursor.execute('''
    CREATE TABLE "comportamiento" (
        "idComportamiento"	INTEGER,
        "idPaciente"	INTEGER,
        "frame"	INTEGER,
        "detecciones"	REAL,
        "movimientos"	TEXT,
        "clasificacion"	TEXT,
        PRIMARY KEY("idComportamiento" AUTOINCREMENT),
        FOREIGN KEY("idPaciente") REFERENCES "pacientes"("idPaciente")
    );
    ''')

    conn.commit()  

