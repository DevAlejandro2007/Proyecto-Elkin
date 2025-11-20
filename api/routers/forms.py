from fastapi import APIRouter
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
    usuario = data["usuario"]
    preguntas = data["preguntas"]
    cuestionario.guardar_cuestionario(usuario, preguntas)    
    return {"message": "✅ Cuestionario guardado exitosamente"}
     