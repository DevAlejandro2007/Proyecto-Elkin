from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from config import templates    
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./pagina_web/src")

@app.get("/", response_class= HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request}) 