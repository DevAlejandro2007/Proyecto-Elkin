from fastapi import APIRouter, HTTPException
import sqlite3

# configuracion del router
router = APIRouter(
    prefix="/register",
    tags=["register"],
    responses={404:{"message":"hola no encontrado"}}
)

# registra un nuevo usuario
def registrar_usuario(username: str, password: str):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

#endpoint "/register"
@router.post("/")
async def register(data: dict):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Faltan credenciales")

    try:
        registrar_usuario(username, password)
        return {"message": " Registro exitoso"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="El usuario ya existe")
    