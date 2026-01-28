from fastapi import APIRouter, HTTPException
from models import users
from pydantic import BaseModel, Field
from utils.jwt_handler import crear_jwt

class LoginRequest(BaseModel):
    id: int = Field(..., gt=0, description="ID del estudiante")
    username: str = Field(..., min_length=3, description="Nombre de usuario")
    password: str = Field(..., min_length=6, description="Contraseña")

router = APIRouter(
    prefix="/login",
    tags=["Login"],
    responses={404: {"message": "Página no encontrada"}}
)

@router.post("/", status_code=200)
async def login(data: LoginRequest):
    """
    Endpoint para iniciar sesión.
    Valida las credenciales y retorna un JWT si son correctas.
    """
    if users.iniciar_sesion(data.id, data.username, data.password):
        # Generar JWT para el usuario
        access_token = crear_jwt(data.id, data.username)
        return {
            "message": "Inicio de sesión exitoso",
            "status": 200,
            "access_token": access_token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(
            status_code=401, 
            detail="Usuario o contraseña incorrectos"
        )