from database.db_mongo import MONGO_COLECCION

def guardar_cuestionario(usuario: str, preguntas: list):
    nuevo = {
        "usuario": usuario,
        "preguntas": preguntas
    }
    MONGO_COLECCION.insert_one(nuevo)
    return nuevo

def obtener_cuestionarios(usuario: str):
    return list(MONGO_COLECCION.find({"usuario": usuario}, {"_id": 0}))
