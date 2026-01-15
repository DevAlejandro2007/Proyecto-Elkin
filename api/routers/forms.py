from fastapi import APIRouter, HTTPException    
from models import cuestionario

#configuracion del router
router = APIRouter(
    prefix="/forms",
    tags=["forms"],
    responses={404:{"message":"pagina no encontrada"}}
)


#/form, endpoint del formulario
@router.post("/")
async def form(data: dict):
    id = data["id"]
    usuario = data["usuario"]
    preguntas = data["preguntas"]

    cuestionario.guardar_cuestionario(id, usuario, preguntas)

    confirmacion = cuestionario.obtener_cuestionarios(id)

    if not confirmacion:
        raise HTTPException(408, "Error al guardar el cuestionario")

    return {
        "status": 201,
        "message": "Guardado correctamente",
        "data": confirmacion
    }
