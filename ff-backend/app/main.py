from fastapi import FastAPI, Request
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)


app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")
static = StaticFiles(directory=BASE_DIR / "static")
app.mount("/static", static)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html"
    )



