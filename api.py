from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

import json, uvicorn
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="./view/static"), name="static")
templates = Jinja2Templates(directory="./view")

with open("data.json", 'r', encoding="utf8") as f:
    data = {"data" : f.read()}

@app.get("/")
def root(request: Request):
    context = {"request" : request} | data
    return templates.TemplateResponse("index.html", context)

if __name__ == "__main__":
   uvicorn.run("api:app", port=8000, log_level="info", host="localhost", reload=True)
