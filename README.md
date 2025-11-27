# Proyecto COOFLA ( COOPERATIVA FINANCIERA UNILASALLISTA ) 

## CONTENIDOS 

* [Descripción](#descripción)
* [Características](#características)
* [Tecnologías](#tecnologías)
* [Arquitectura](#arquitectura)
* [Backend](#backend)

---

# Descripción

Este es un **proyecto de ingeniería informática especificamente de la materia: Estructura de datos**, este proyecto consiste en una cooperativa financiera para estudiantes, donde el estudiante pueda entrar a la pagina y solicitar su estudio crediticio dependeiendo de las variables solicitadas.

>Nota: Actualmente se esta estructurando la pagina web y el backend

---

# Caracteristicas 

* Frontend con **React/tailwind y postCSS** 
* Backend con **logica financiera estructurada** para las solicitudes de creditos
* Bases de datos **SQL y NO SQL** donde se puede guardar informacion tando de los deudores y sus creditos 
* Hecho 100% por estudiantes de Unilasallista

---

# Tecnologías 
* **FastApi**: Creación de una Api que conecta con las bases de datos y la logica del arbol de decisiones
* **SQL Lite**: Esta base de datos es la escogida para guardar los usuarios de la plataforma
* **MongoDB**: Esta base de datos es la escogida para guardar los formularios hechos en la plataforma

---

# Arquitectura

```
FastApi-Mongod/
├─ api/
│  ├─ main.py
│  ├─ config.py
│  ├─ templates/
│  │    └─ PAGINA WEB
│  ├─ routers/             # Rutas (endpoints)
│  │   ├─ forms.py
│  │   └─ login.py
│  ├─ models/
│  │     ├─ cuestionario.py
│  │     ├─ users.py
│  │     └─ variables.py
│  └─dabatse/
│       ├─ db_mongo.py
│       └─ db_sqlLite.py
├─ README.md               # Documentación del proyecto
└─ .gitignore
```
# Backend:

* Carpeta API: Contiene todas las subcarpetas, archivos y conecciones que crearemos durante todo el proyecto
* [main.py](#main)
* [config.py](#congif)
* [templates](#templates)
* [routers](#routers)
* [models](#models)
* [database](#database)


hola
hola
hpla

sdfs
g
adf
gs
dfg
sd
fg


# main
---
## Inicialización de la aplicación
```
app = FastAPI()
```
Crea una instancia principal de FastAPI.
Sobre este objeto se registran middleware, rutas y configuraciones, y es la base para ejecutar la API.

---
## Configuracion CORS
```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
Habilita CORS para permitir que otras aplicaciones (por ejemplo un frontend en React, Vue o Angular) puedan hacer solicitudes a esta API.

---
### PARAMETROS 

- allow_origins=["*"]: Permite solicitudes desde cualquier origen. (en producción es recomendable definir dominios específicos)
- allow_credentials=True: Permite el uso de cookies y tokens en solicitudes.
- allow_methods=["*"]: Se aceptan todos los métodos HTTP (GET, POST, PUT, DELETE etc).
- allow_headers=["*"]: Se aceptan todos los tipos de encabezados.

## Inclusión de routers (módulos con endpoints)

```
app.include_router(login.router)

app.include_router(forms.router)

app.include_router(register.router)

app.include_router(view_form.router)
```

Esto permite separar la API en módulos más ordenados.
Cada archivo dentro de /routers contiene endpoints específicos, por ejemplo:

---
### Routers

- **login**: Manejo de autenticación / inicio de sesión.
- **register**: Registro de usuarios.
- **forms**: Procesamiento o creación de formularios.
- **view_form**: Visualización de los formularios almacenados.

Favorece la escalabilidad y mantenimiento del código.

---
### Endpoint raíz 
```
@app.get("/")
async def root(request: Request):
    return {"message": "API de autenticacion..."}
```
Retorna un mensaje informativo cuando se accede a la raíz del servidor.
Sirve como pantalla de bienvenida para indicar cómo usar los primeros endpoints.

---
