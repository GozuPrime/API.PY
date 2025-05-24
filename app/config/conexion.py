import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=GOZU\SQLEXPRESS;"  
    "DATABASE=IA_Esquizofrenia;"     
    "Trusted_Connection=yes;"        
)


def get_connection():
    return pyodbc.connect(conn_str)