from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from config import templates
from routers import *

app = FastAPI()

#routers ( endpoints)
#
#
#

@app.get("/",response_class= HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Index.html",{"request":request})