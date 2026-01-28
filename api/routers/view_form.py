from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from models import cuestionario
from utils.jwt_handler import verificar_token, extraer_token_del_header
from typing import Optional

# Modelo para validar el ID del formulario
class ViewFormRequest(BaseModel):
    id: str = Field(..., min_length=1, description="ID del formulario a buscar")

router = APIRouter(
    prefix="/view_form",
    tags=["forms"],
    responses={404: {"message": "Página no encontrada"}}
)

# Dependencia para proteger el endpoint
async def obtener_usuario_autenticado(authorization: Optional[str] = Header(None)):
    """
    Valida que el usuario tenga un JWT válido.
    Debe enviar: Authorization: Bearer <token>
    """
    token = extraer_token_del_header(authorization)
    payload = verificar_token(token)
    return payload

@router.get("/")  
async def view_form(id: str, usuario_autenticado: dict = Depends(obtener_usuario_autenticado)):
    """
    Obtiene un formulario específico por ID.
    ⚠️ REQUIERE AUTENTICACIÓN (JWT token válido)
    
    Headers requerido:
        Authorization: Bearer <token>
    
    Args:
        id: ID del formulario a buscar
        usuario_autenticado: Usuario validado por el JWT
    
    Returns:
        Lista de cuestionarios encontrados
    """
    try:
        cuestionarios = cuestionario.obtener_cuestionarios(id)
        
        if not cuestionarios:
            raise HTTPException(
                status_code=404, 
                detail="Cuestionario no encontrado"
            )
        
        return {
            "status": 200,
            "message": "Cuestionarios encontrados",
            "user_id": int(usuario_autenticado.get("sub")),  # Convertir a int
            "data": cuestionarios
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener el cuestionario: {str(e)}"
        )
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener el cuestionario: {str(e)}"
        )
