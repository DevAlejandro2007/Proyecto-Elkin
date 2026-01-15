from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from models import cuestionario

# Modelo para validar el ID del formulario
class ViewFormRequest(BaseModel):
    id: str = Field(..., min_length=1, description="ID del formulario a buscar")

router = APIRouter(
    prefix="/view_form",
    tags=["forms"],
    responses={404: {"message": "Página no encontrada"}}
)

@router.get("/")  
async def view_form(id: str):
    """
    Obtiene un formulario específico por ID.
    
    Args:
        id: ID del formulario a buscar
    
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
            "data": cuestionarios
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener el cuestionario: {str(e)}"
        )
