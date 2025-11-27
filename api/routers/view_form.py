from fastapi import APIRouter, HTTPException
from models import cuestionario

router = APIRouter(
    prefix="/view_form",
    tags=["forms"],
    responses={404:{"message":"pagina no encontrada"}}
)


informacion = {}

@router.get("/")  
async def view_form(id: str):
    cuestionarios = cuestionario.obtener_cuestionarios(id)
    informacion = cuestionarios
    if not cuestionarios:
        raise HTTPException(status_code=404, detail="Cuestionario no encontrado")
    return {
        "status": 200,
        "data": cuestionarios
    }
import numpy as np
np.random.seed(42)
n_samples = 200

Id_estudiante = np.arange(1, n_samples+1)
Edad = np.random.randint(18, 40, n_samples)
Carrera = np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.6, 0.2, 0.10, 0.05, 0.05])
# 1=Veterinaria, 2=Ingeniería, 3=Administración, 4=Derecho, 5=Psicología
Semestre_actual = np.random.randint(2, 10, n_samples)
Promedio = np.round(np.random.uniform(3.5, 5.0, n_samples), 2)
Situacion_laboral_estudiante = np.random.choice([0, 1, 2], n_samples, p=[0.7, 0.25, 0.05])
Ingreso_propio_estudiante = np.random.randint(0, 2500000, n_samples)
Historial_crediticio = np.random.choice([1, 2, 3], n_samples, p=[0.7, 0.2, 0.1])
Estado_civil = np.random.choice([1, 2, 3, 4], n_samples, p=[0.6, 0.2, 0.15, 0.05])
Ingresos_mensuales_familia = np.random.randint(1600000, 5000000, n_samples)
Valor_credito_solicitado = np.random.randint(3000000, 30000000, n_samples)
Tasa_interés = np.round(np.random.uniform(0.8, 2.0, n_samples), 2)
Garantía = np.random.choice([1, 2], n_samples, p=[0.5, 0.5])
Plazo = np.random.randint(24, 60, n_samples)
Tipo_vivienda = np.random.choice(
    [1, 2, 3, 4], n_samples, p=[0.3, 0.4, 0.25, 0.05]
)
Estado_credito = np.random.choice([1, 2, 3, 4], n_samples, p=[0.7, 0.15, 0.1, 0.05])
Cuota_mensual = (Valor_credito_solicitado * (1 + (Tasa_interés/100)*Plazo)) // Plazo
Monto_pagado = np.random.randint(0, Valor_credito_solicitado//2, n_samples)
Saldo_pendiente = Valor_credito_solicitado - Monto_pagado
#precio por facultades
Ciencias_Administrativas_Agropecuarias = [admin_empresas:=3959700,veterianaria:=10700000,zootecnia:=8976000,admin_empresas_agro:=8174000]
Ciencias_Sociales_Educacion = [derecho:=6545000,psicologia:=6545000,periodismo:=7469000,Educaion_infantil:=4553000]
Ingenierias = [industrial:=660000,informatica:= 7770000, ambiental:=7552000,alimentos:=7415000]
# Variables adicionales
# 1 = sí, 0 = no
Retraso_pago = np.random.choice([0, 1], n_samples)  
Tiene_aval = np.random.choice([0, 1], n_samples)     
Satisfaccion = np.random.randint(1, 6, n_samples)    
