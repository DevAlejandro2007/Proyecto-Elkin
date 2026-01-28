# Proyecto COOFLA (COOPERATIVA FINANCIERA UNILASALLISTA)

## 📑 CONTENIDOS

* [Descripción](#descripción)
* [Características](#características)
* [Tecnologías](#tecnologías)
* [Estructura del Proyecto](#estructura-del-proyecto)
* [Backend](#backend)
* [Autenticación JWT](#autenticación-jwt)
* [Endpoints API](#endpoints-api)
* [Instalación](#instalación)

---

## 📖 Descripción

Este es un **proyecto de ingeniería informática** de la materia **Estructura de Datos**. 

**COOFLA** es una plataforma de cooperativa financiera para estudiantes de Unilasallista donde pueden:
- ✅ Registrarse de forma segura
- ✅ Solicitar evaluaciones crediticias
- ✅ Consultar sus formularios guardados
- ✅ Recibir evaluaciones personalizadas

> **Estado**: Backend completo con autenticación JWT | Frontend en desarrollo

---

## ✨ Características

* ✅ **Autenticación segura con JWT** - Tokens encriptados con validación
* ✅ **Frontend moderno** - React 19 + Tailwind CSS + Vite
* ✅ **Backend robusto** - FastAPI con validación Pydantic
* ✅ **Base de datos híbrida** - MongoDB (formularios) + SQLite (usuarios)
* ✅ **API RESTful** - Swagger integrado
* ✅ **Variables de entorno** - Seguridad con .env
* ✅ **Control de versiones** - Git configurado
* ✅ **100% estudiantes** de Unilasallista

---

## 🛠️ Tecnologías

### Backend
- **FastAPI** - Framework web asincrónico
- **PyJWT** - Generación y validación de tokens
- **Pydantic** - Validación de datos
- **MongoDB** - Base de datos NoSQL
- **SQLite** - Base de datos SQL
- **python-dotenv** - Gestión de variables de entorno
- **Passlib** - Hash de contraseñas

### Frontend
- **React 19** - Biblioteca de UI
- **Vite** - Bundler rápido
- **Tailwind CSS** - Framework de estilos
- **React Router v7** - Enrutamiento
- **Lucide React** - Iconos
- **ESLint** - Análisis de código

---

## 📁 Estructura del Proyecto

```
Proyecto-Elkin/
│
├── api/                          # Backend (FastAPI)
│   ├── main.py                   # Punto de entrada
│   ├── config.py                 # Configuración global
│   ├── .env                      # Variables de entorno
│   │
│   ├── routers/                  # Endpoints
│   │   ├── login.py              # POST /login
│   │   ├── register.py           # POST /register
│   │   ├── forms.py              # POST /forms
│   │   └── view_form.py          # GET /view_form
│   │
│   ├── models/                   # Lógica de negocio
│   │   ├── users.py              # Gestión de usuarios
│   │   └── cuestionario.py       # Gestión de formularios
│   │
│   ├── utils/                    # Utilidades
│   │   ├── __init__.py
│   │   └── jwt_handler.py        # Manejo de JWT
│   │
│   ├── database/                 # Conexiones
│   │   ├── db_mongo.py           # MongoDB
│   │   └── db_sqlLite.py         # SQLite
│   │
│   └── __pycache__/              # Cache
│
├── pagina_web/                   # Frontend (React + Vite)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── index.css
│   │   ├── pages/                # Páginas
│   │   ├── components/           # Componentes
│   │   └── utils/
│   │
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── eslint.config.js
│
├── README.md
├── .gitignore
└── .git/
```

---

## 🔐 Backend

### main.py - Punto de entrada

Crea la instancia de FastAPI, configura CORS y registra todos los routers:

```python
app = FastAPI()

# CORS - Permite requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Registrar routers
app.include_router(login.router)
app.include_router(register.router)
app.include_router(forms.router)
app.include_router(view_form.router)
```

### config.py - Configuración global

Lee variables del `.env`:

```python
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
TOKEN_EXPIRATION = int(os.getenv("TOKEN_EXPIRATION"))
```

### .env - Variables de entorno (NO SUBIR A GITHUB)

```bash
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=coofla
SECRET_KEY=tu_clave_secreta_aqui
ALGORITHM=HS256
TOKEN_EXPIRATION=30
API_PORT=8000
API_HOST=localhost
DEBUG=True
```

### Routers - Endpoints de la API

#### **login.py** - Autenticación
```
POST /login
{
  "id": 1020112352,
  "username": "alejo",
  "password": "ingenieroalejo"
}

Response 200:
{
  "message": "Inicio de sesión exitoso",
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

#### **register.py** - Registro
```
POST /register
{
  "id": 1020112352,
  "username": "alejo",
  "password": "ingenieroalejo"
}

Response 201:
{
  "message": "Usuario registrado correctamente",
  "data": {"id": 1020112352, "username": "alejo"}
}
```

#### **forms.py** - Guardar formularios (REQUIERE JWT)
```
POST /forms
Authorization: Bearer <token>

{
  "id": "form_001",
  "usuario": "alejo",
  "preguntas": {"edad": 22, "carrera": "Ingeniería"}
}

Response 201:
{
  "message": "Guardado correctamente",
  "data": [...]
}
```

#### **view_form.py** - Ver formularios (REQUIERE JWT)
```
GET /view_form/?id=form_001
Authorization: Bearer <token>

Response 200:
{
  "message": "Cuestionarios encontrados",
  "data": [...]
}
```

### Models

**users.py** - Gestión de usuarios

Funciones principales:
```python
# Hash de contraseña
hash_password(password: str) -> str
# Verifica contraseña contra hash
verify_password(plain_password: str, hashed_password: str) -> bool
# Registra nuevo usuario en MongoDB
registrar_usuario(id: int, username: str, password: str) -> dict
# Valida si usuario existe
validar_usuario(id: int, username: str) -> bool
# Valida credenciales de login
iniciar_sesion(id: int, username: str, password: str) -> bool
```

**Ejemplo:**
```python
from models import users

# Registrar usuario
users.registrar_usuario(1020112352, "alejo", "ingenieroalejo")

# Validar login
if users.iniciar_sesion(1020112352, "alejo", "ingenieroalejo"):
    # Login exitoso
```

**cuestionario.py** - Gestión de formularios

Funciones principales:
```python
# Guarda formulario en MongoDB
guardar_cuestionario(id: str, username: str, preguntas: dict) -> dict

# Obtiene formularios del usuario
obtener_cuestionarios(id: int) -> list
```

**Ejemplo:**
```python
from models import cuestionario

# Guardar formulario
cuestionario.guardar_cuestionario(
    id="form_001",
    username="alejo",
    preguntas={"edad": 22, "carrera": "Ingeniería"}
)

# Obtener formularios
formularios = cuestionario.obtener_cuestionarios("form_001")
```

### Utils

**jwt_handler.py** - Manejo de JWT

Funciones principales:

**1. crear_jwt(user_id: int, username: str) -> str**
- Genera JWT después de login exitoso
- Payload incluye: `sub` (user_id), `username`, `iat`, `exp`
- Expira en 30 minutos (configurable en .env)

```python
from utils.jwt_handler import crear_jwt

token = crear_jwt(1020112352, "alejo")
# Retorna: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI..."
```

**2. verificar_token(token: str) -> dict**
- Decodifica y valida el JWT
- Retorna payload si es válido
- Lanza HTTPException si está expirado o es inválido

```python
from utils.jwt_handler import verificar_token

try:
    payload = verificar_token("eyJhbGc...")
    user_id = payload["sub"]  # Obtiene ID del usuario
except HTTPException:
    # Token inválido o expirado
```

**3. extraer_token_del_header(authorization: str) -> str**
- Extrae el token del header `Authorization: Bearer <token>`
- Valida formato correcto
- Lanza error si formato es incorrecto

```python
from utils.jwt_handler import extraer_token_del_header

token = extraer_token_del_header("Bearer eyJhbGc...")
# Retorna: "eyJhbGc..." (sin "Bearer ")
```

---

## 🗄️ Database

Módulo para manejar conexiones a bases de datos

### db_mongo.py - MongoDB

**Conexión a MongoDB**

```python
import pymongo
from config import MONGO_URI, DATABASE_NAME

cliente = pymongo.MongoClient(MONGO_URI)
base_datos = cliente[DATABASE_NAME]

# Colecciones
COLLECCION = base_datos["form"]      # Formularios
COLLECCION2 = base_datos["users"]    # Usuarios
```

**Características:**
- ✅ Conexión automática al iniciar
- ✅ Manejo de errores con try/except
- ✅ Variables de entorno para configuración

**Colecciones:**
| Colección | Propósito |
|-----------|----------|
| `form` | Guarda cuestionarios/formularios |
| `users` | Guarda usuarios registrados |

**Estructura de documento (users):**
```json
{
  "_id": 1020112352,
  "username": "alejo",
  "password": "$2b$12$hashbcrypt..."  // Hash bcrypt
}
```

**Estructura de documento (form):**
```json
{
  "_id": "form_001",
  "usuario": "alejo",
  "preguntas": {
    "edad": 22,
    "carrera": "Ingeniería",
    "semestre": 5
  }
}
```

### db_sqlLite.py - SQLite

**Conexión a SQLite**

```python
import sqlite3
import os

DB_PATH = "api/database/usuarios.db"

def get_sql_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar: {e}")
        return None
```

**Características:**
- ✅ Base de datos local (archivo usuarios.db)
- ✅ Manejo de conexiones
- ✅ Row factory para obtener filas como diccionarios

---

## 🎨 Frontend

### Estructura

```
pagina_web/
├── src/
│   ├── App.jsx                 # Componente raíz
│   ├── main.jsx                # Entry point
│   ├── index.css               # Estilos globales
│   │
│   ├── pages/
│   │   ├── Main.jsx            # Página principal
│   │   ├── Login.jsx           # Página de login
│   │   ├── Register.jsx        # Página de registro
│   │   ├── Credits.jsx         # Página de créditos
│   │   └── Pruebas.jsx         # Página de pruebas
│   │
│   ├── components/
│   │   └── Banner.jsx          # Banner superior (cabecera)
│   │
│   └── utils/
│       └── (funciones auxiliares)
│
├── public/                     # Archivos estáticos
├── index.html                  # HTML principal
├── package.json                # Dependencias
├── vite.config.js              # Config de Vite
├── tailwind.config.js          # Config de Tailwind
├── eslint.config.js            # Config de ESLint
└── node_modules/               # Dependencias instaladas
```

### App.jsx - Componente raíz

Define las rutas principales de la aplicación:

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Main } from "./pages/Main";
import { Login } from "./pages/Login";
import { Register } from "./pages/Register";
import { Credits } from "./pages/Credits";
import { Banner } from "./components/Banner";

export default function App() {
  return (
    <BrowserRouter>
      <div className="flex flex-col h-screen">
        <Banner title="Coofla" />
        <main className="flex-1 overflow-y-auto">
          <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/Login" element={<Login />} />
            <Route path="/Register" element={<Register />} />
            <Route path="/Credits" element={<Credits />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}
```

### Páginas

**Main.jsx** - Página principal
- Bienvenida y descripción del proyecto
- Botones para acceder a login/registro

**Login.jsx** - Página de inicio de sesión
```jsx
// Ejemplo de estructura
- Formulario con: id, username, password
- POST /login
- Guarda token en localStorage
- Redirige a /Credits
```

**Register.jsx** - Página de registro
```jsx
// Ejemplo de estructura
- Formulario con: id, username, password
- POST /register
- Mensaje de éxito
- Redirige a /Login
```

**Credits.jsx** - Página de créditos/solicitudes
- Ver formularios guardados (GET /view_form con JWT)
- Crear nuevo formulario (POST /forms con JWT)
- Mostrar evaluación crediticia

### Components

**Banner.jsx** - Componente reutilizable
- Barra de navegación superior
- Logo/Título del proyecto
- Links de navegación

### Llamadas al Backend

**Con token JWT:**
```javascript
// En componentes que necesitan JWT
const token = localStorage.getItem("token");

// GET request
fetch("/view_form/?id=form_001", {
  headers: { "Authorization": `Bearer ${token}` }
})

// POST request
fetch("/forms", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${token}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    id: "form_001",
    usuario: "alejo",
    preguntas: { edad: 22 }
  })
})
```

---

## 🔧 Configuración de desarrollo

### Tailwind CSS
- Utilidades para estilos rápidos
- Configurado en `tailwind.config.js`
- Importado en `index.css`

### Vite
- Dev server rápido con hot reload
- Bundler optimizado
- Comando: `npm run dev`

### ESLint
- Análisis estático de código
- Detecta errores y malas prácticas
- Comando: `npm run lint`

---

## 📚 Flujo completo de uso

```
┌─────────────────────────────────────────────────────┐
│           Usuario abre pagina_web                   │
└────────────────┬────────────────────────────────────┘
                 │
                 ├─→ Si NO está registrado:
                 │   ├─ Click en "Registrar"
                 │   ├─ Completa: id, username, password
                 │   ├─ POST /register
                 │   └─ Guardado en MongoDB (usuarios)
                 │
                 ├─→ Si está registrado:
                 │   ├─ Click en "Login"
                 │   ├─ Completa: id, username, password
                 │   ├─ POST /login
                 │   ├─ Recibe JWT y lo guarda en localStorage
                 │   └─ Redirige a /Credits
                 │
                 └─→ En /Credits (Autenticado):
                     ├─ GET /view_form (con JWT)
                     │   └─ Ve formularios guardados
                     │
                     └─ POST /forms (con JWT)
                         ├─ Crea nuevo cuestionario
                         └─ Guardado en MongoDB (form)
```

---

---

## 🔑 Autenticación JWT

**¿Qué es?** Token encriptado que valida la identidad del usuario sin guardar sesión en servidor.

**Estructura:** `ENCABEZADO.PAYLOAD.FIRMA`

**Flujo:**
1. POST /login → Genera JWT
2. Frontend guarda en localStorage
3. En requests siguientes envía: `Authorization: Bearer <JWT>`
4. Servidor valida firma del JWT
5. Si es válido → Acceso permitido ✅

**Usar JWT en requests:**

JavaScript:
```javascript
const token = localStorage.getItem("token");
fetch("/view_form/?id=123", {
  headers: { "Authorization": `Bearer ${token}` }
})
```

curl:
```bash
curl -H "Authorization: Bearer eyJhbGc..." http://localhost:8000/view_form/?id=123
```

ThunderClient:
- Authorization: `Bearer <token>`

---

## 📡 Endpoints API

| Método | Endpoint | JWT | Descripción |
|--------|----------|-----|---|
| POST | `/login` | ❌ | Iniciar sesión |
| POST | `/register` | ❌ | Registrar usuario |
| POST | `/forms` | ✅ | Guardar formulario |
| GET | `/view_form` | ✅ | Ver formularios |

---

## 📦 Instalación

### Backend

```bash
cd api
pip install -r requirements.txt
echo "MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=coofla
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
TOKEN_EXPIRATION=30" > .env
uvicorn main:app --reload
```

### Frontend

```bash
cd pagina_web
npm install
npm run dev
```

---

## 👥 Autores

Estudiantes de Ingeniería Informática - Unilasallista 2026
