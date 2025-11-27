from fastapi import FastAPI, Request
from routers import login, forms, register, view_form
from fastapi.middleware.cors import CORSMiddleware

#variable fasapi
app = FastAPI()

# Configuracion CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

origins = [
    "http://localhost:5173"
]


#routers ( endpoints )
app.include_router(login.router)
app.include_router(forms.router)
app.include_router(register.router)
app.include_router(view_form.router)
# main ( raiz )
@app.get("/")
async def root(request: Request):
    return {"message": "API de autenticacion. Usa /login/ para iniciar sesion y /register/ para registrarte."}