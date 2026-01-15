from database.db_mongo import COLLECCION


#funcion de guardar cuestionario en la base de datos 
def guardar_cuestionario(id: str, username: str, preguntas: dict):
    nuevo = {
        "_id": id,
        "usuario": username,
        "preguntas":preguntas
    }
    COLLECCION.insert_one(nuevo)
    return nuevo
# busca y devuelve el cuestionario 
def obtener_cuestionarios(id: int):
    return list(COLLECCION.find({"_id": id}))
