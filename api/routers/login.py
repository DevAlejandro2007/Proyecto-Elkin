from fastapi import APIRouter, HTTPException
import sqlite3

# configuracion del router
router = APIRouter(
    prefix="/login",
    tags=["Login"],
    responses={404:{"message":"pagina no encontrada"}}
)

# valida si el usuario esta disponible 
def validar_usuario(id: int ,username: str, password: str):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=? AND username=? AND password=?", (id, username, password))
    user = cursor.fetchone()
    conn.close()
    return user

#endpoint "/login/"
@router.post("/")
async def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    id = data.get("id")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Faltan credenciales")

    if await validar_usuario(id,username, password):
        return {"message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
