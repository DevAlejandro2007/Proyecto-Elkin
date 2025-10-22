from database.db_mongo import MONGO_COLECCION

#funcion de guardar cuestionario en la base de datos 
def guardar_cuestionario(usuario: str, preguntas: list):
    nuevo = {
        "usuario": usuario,
        "preguntas":preguntas
    }
    MONGO_COLECCION.insert_one(nuevo)
    return nuevo

# busca y devuelve el cuestionario 
def obtener_cuestionarios(usuario: str):
    return list(MONGO_COLECCION.find({"usuario": usuario}, {"_id": 0}))
