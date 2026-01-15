from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from models import users
from passlib.context import CryptContext
# modelo de datos para el registro
class RegisterRequest(BaseModel):
    id: int = Field(..., gt=0)
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=6)


# configuracion del router
router = APIRouter(
    prefix="/register",
    tags=["register"],
    responses={404:{"message":"no encontrado"}}
)

# registra un nuevo usuario
def registrar_usuario(id: int, username: str, password: str):
    if users.validar_usuario(id,username):
        raise HTTPException(status_code=400, detail="El nombre de usuario o id ya existe")
    hashed_password = users.hash_password(password)
    return users.registrar_usuario(id, username,hashed_password)

#endpoint "/register"
@router.post("/", status_code=201)
def register(data: RegisterRequest):

    nuevo_usuario = registrar_usuario(
        data.id,
        data.username,
        data.password
    )       
    if not nuevo_usuario:
        raise HTTPException(status_code=500, 
                            detail="Error al registrar el usuario")

    return {
        "status": 201,
        "message": "Usuario registrado correctamente",
        "data": {"id":data.id, "username": data.username}
    }
