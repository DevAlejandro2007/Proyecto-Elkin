from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# ===================================
# CONFIGURACIÓN DE BASE DE DATOS
# ===================================
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "coofla")

# ===================================
# CONFIGURACIÓN DE API
# ===================================
API_PORT = int(os.getenv("API_PORT", 8000))
API_HOST = os.getenv("API_HOST", "localhost")

# ===================================
# AUTENTICACIÓN Y SEGURIDAD
# ===================================
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("⚠️ SECRET_KEY no está configurado en .env")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
TOKEN_EXPIRATION = int(os.getenv("TOKEN_EXPIRATION", 30))

# ===================================
# ENTORNO
# ===================================
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# ===================================
# PLANTILLAS HTML
# ===================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))