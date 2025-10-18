import pymongo

MONGO_URI = "mongodb://localhost:27017/"
NOMBRE_DATABASE = "coofla"
MONGO_COLECCION = "form"

try: 
    cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS = 2000)
    cliente.server_info()
    print("CONECTADO A LA BASE DE DATOS CONECTADO ")
    base_datos = cliente[NOMBRE_DATABASE]
    COLLECCION = base_datos[MONGO_COLECCION]
except Exception as e:
    print("error en la base de datos:", e)
    COLLECCION = None