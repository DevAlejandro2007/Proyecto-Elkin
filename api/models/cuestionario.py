from database.db_mongo import COLLECCION


#funcion de guardar cuestionario en la base de datos 
def guardar_cuestionario(id: str, username: str, preguntas: dict):
    nuevo = {
        "_id": id,
        "usuario": username,
        "preguntas":preguntas
    }
    try:
        COLLECCION.insert_one(nuevo)
    except Exception as e:
        print("Error al guardar el cuestionario:", e)
        raise Exception(f"No se pudo guardar el cuestionario: {str(e)}")
    return nuevo
# busca y devuelve el cuestionario 
def obtener_cuestionarios(id: int):
    return list(COLLECCION.find({"_id": id}))

def obtener_nucleo(id: int):
    estudiante = COLLECCION.find_one({"_id": id})
    estudiante_preguntas = estudiante.get("preguntas", {})
    nucleo_familiar = estudiante_preguntas.get("tipo nucleo familiar")
    if nucleo_familiar is None:
        raise Exception("Núcleo familiar no encontrado en las respuestas del estudiante.")
    if nucleo_familiar < 3:
        return "poco apto para el credito, puede llegar a faltar a sus pagos"
    elif nucleo_familiar == 3:
        return "apto para el credito, tiene estabilidad familiar"
    elif nucleo_familiar > 5:
        return "muy apto para el credito, tiene una familia estable y con buenos ingresos"
    return nucleo_familiar

