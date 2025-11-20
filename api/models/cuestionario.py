from database.db_mongo import COLLECCION

#funcion de guardar cuestionario en la base de datos 
def guardar_cuestionario(usuario: str, preguntas: list):
    nuevo = {
        "usuario": usuario,
        "preguntas":preguntas
    }
    COLLECCION.insert_one(nuevo)
    return nuevo
# busca y devuelve el cuestionario 
def obtener_cuestionarios(usuario: str):
    return list(COLLECCION.find({"usuario": usuario}, {"_id": 0}))
