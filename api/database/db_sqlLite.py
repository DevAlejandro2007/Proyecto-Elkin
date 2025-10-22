import sqlite3
import os

# Ruta absoluta al archivo de la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "usuarios.db")

# coneccion con sql lite 
def get_sql_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print("❌ Error al conectar a la base de datos SQLite:", e)
        return None
