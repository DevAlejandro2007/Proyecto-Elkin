from database.db_sqlLite import get_sql_connection

#funcion de la tabla de usuarios ( formato )
def crear_tabla_usuarios():
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# funcion para registrar usuarios 
def registrar_usuario(username: str, password: str):
    conn = get_sql_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

