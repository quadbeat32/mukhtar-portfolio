from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Mukhtar — SME Software")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

WHATSAPP = "2349027899539"  
EMAIL = "arunamukhtar@gmail.com"

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "whatsapp": WHATSAPP,
        "email": EMAIL,
    })

@app.get("/health")
def health():
    return {"ok": True}
