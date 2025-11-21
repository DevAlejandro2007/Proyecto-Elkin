# Proyecto COOFLA ( COOPERATIVA FINANCIERA UNILASALLISTA ) 

## CONTENIDOS 

* [Descripción](#descripción)
* [Características](#características)
* [Tecnologías](#tecnologías)
* [Arquitectura](#arquitectura)

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

# Tecnologias 
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

---
