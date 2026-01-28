from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, Field
from models import cuestionario
from utils.jwt_handler import verificar_token, extraer_token_del_header
from typing import Optional, Dict, Any

# Modelo para validar los datos del formulario
class FormRequest(BaseModel):
    id: str = Field(..., min_length=1, description="ID del formulario")
    usuario: str = Field(..., min_length=1, description="Nombre del usuario")
    preguntas: Dict[str, Any] = Field(..., description="Respuestas del formulario")

# Configuración del router
router = APIRouter(
    prefix="/forms",
    tags=["forms"],
    responses={404: {"message": "página no encontrada"}}
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

# Endpoint del formulario
@router.post("/")
async def form(data: FormRequest, usuario_autenticado: dict = Depends(obtener_usuario_autenticado)):
    """
    Guarda un nuevo formulario/cuestionario.
    ⚠️ REQUIERE AUTENTICACIÓN (JWT token válido)
    
    Headers requerido:
        Authorization: Bearer <token>
    """
    try:
        user_id = int(usuario_autenticado.get("sub"))  # Convertir a int
        
        # Guardar el cuestionario
        cuestionario.guardar_cuestionario(data.id, data.usuario, data.preguntas)
        
        # Confirmar que se guardó
        confirmacion = cuestionario.obtener_cuestionarios(data.id)

        if not confirmacion:
            raise HTTPException(
                status_code=408, 
                detail="Error al guardar el cuestionario"
            )

        return {
            "status": 201,
            "message": "Guardado correctamente",
            "user_id": user_id,  # ID del usuario autenticado
            "data": confirmacion
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al guardar el cuestionario: {str(e)}"
        )
