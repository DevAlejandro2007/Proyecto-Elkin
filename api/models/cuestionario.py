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
