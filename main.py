from fastapi import FastAPI, Request

from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 1. CSS/Images files-kaga static folder-ai mount seiya
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. HTML files-kaga templates folder-ai set seiya
templates = Jinja2Templates(directory="templates")


class HTMLResponse(BaseModel):
    pass
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # 'templates.TemplateResponse' moolam HTML-ai tharuvom
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login/",response_class=HTMLResponse)
async def olduser(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})
