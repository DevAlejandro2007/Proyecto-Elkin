from database.db_mongo import COLLECCION

#funcion de guardar cuestionario en la base de datos 
def guardar_cuestionario(id: int, username: str, preguntas: list):
    nuevo = {
        "id": id,
        "usuario": username,
        "preguntas":preguntas
    }
    COLLECCION.insert_one(nuevo)
    return nuevo
# busca y devuelve el cuestionario 
def obtener_cuestionarios(id: int):
    return list(COLLECCION.find({"id": id}, {"_id": 0}))
