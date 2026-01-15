from fastapi import APIRouter, HTTPException
from models import users
from passlib.context import CryptContext


# configuracion del router
router = APIRouter(
    prefix="/login",
    tags=["Login"],
    responses={404:{"message":"pagina no encontrada"}}
)

#endpoint "/login/"
@router.post("/")
async def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    id = data.get("id")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Faltan credenciales")

    if users.iniciar_sesion(id,username, password):    
        return {"message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
