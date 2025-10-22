from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from models import cuestionario

#configuracion del router
router = APIRouter(
    prefix="/form",
    tags=["form"],
    responses={404:{"message":"pagina no encontrada"}}
)


#/form, endpoint del formulario
@router.get("/form",response_class=HTMLResponse)
async def form(usuario:str,preguntas:list):
    return cuestionario.guardar_cuestionario(usuario, preguntas)
     