from fastapi import APIRouter, HTTPException
from models import users
from pydantic import BaseModel, Field

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
    Retorna un token si las credenciales son válidas.
    """
    # Pydantic ya validó los datos, no necesitas .get()
    if users.iniciar_sesion(data.id, data.username, data.password):    
        return {"message": "Inicio de sesión exitoso", "status": 200}
    else:
        raise HTTPException(
            status_code=401, 
            detail="Usuario o contraseña incorrectos"
        )