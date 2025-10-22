from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from config import templates
from routers import login, forms

#variable fasapi
app = FastAPI()

#routers ( endpoints )
app.include_router(login.router)
app.include_router(forms.router)

# main ( raiz )
@app.get("/",response_class= HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Index.html",{"request":request})