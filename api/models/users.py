from database.db_mongo import COLLECCION2
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# funcion para registrar usuarios 
def registrar_usuario(id: int, username: str, password: str):
    hashed_password = hash_password(password)

    nuevo_usuario = {
        "_id": id,
        "username": username,
        "password": hashed_password
    }

    COLLECCION2.insert_one(nuevo_usuario)
    return {
        "id": id,
        "username": username
    }



# funcion para validar usuarios
def validar_usuario(id: int, username: str) -> bool:
    return COLLECCION2.find_one({
        "$or": [
            {"_id": id},
            {"username": username}
        ]
    }) is not None

# funcion para iniciar sesion
def iniciar_sesion(id: int,username: str, password: str) -> bool:
    user = COLLECCION2.find_one({"_id": id}) and COLLECCION2.find_one({"username": username})

    if not user:
        return False

    if not verify_password(password, user["password"]):
        return False

    return True
