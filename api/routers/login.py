from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import sqlite3

# configuracion del router
router = APIRouter(
    prefix="/login",
    tags=["Login"],
    responses={404:{"message":"pagina no encontrada"}}
)

# valida si el usuario esta disponible 
def validar_usuario(username: str, password: str):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

#endpoint "/login/"
@router.post("/login/",response_class=HTMLResponse)
async def login(data: dict):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Faltan credenciales")

    if validar_usuario(username, password):
        return {"message": "✅ Login exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
