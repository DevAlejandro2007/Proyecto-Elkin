import pymongo
from config import MONGO_URI, DATABASE_NAME

# Conexión con MongoDB usando variables del .env
try: 
    cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    cliente.server_info()
    print("✅ CONECTADO A LA BASE DE DATOS MONGODB")
    
    base_datos = cliente[DATABASE_NAME]
    COLLECCION = base_datos["form"]
    COLLECCION2 = base_datos["users"]
    
except Exception as e:
    print(f"❌ Error en la base de datos: {e}")
    COLLECCION = None
    COLLECCION2 = None


