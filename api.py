from fastapi import FastAPI, Request
import json, uvicorn
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="./view")
app = FastAPI()

with open("data.json", 'r', encoding="utf8") as f:
    data = {"data" : json.loads(f.read())}

@app.get("/")
def root(request: Request):
    context = {"request" : request} | data
    print(context)
    return templates.TemplateResponse("index.html", context)

if __name__ == "__main__":
   uvicorn.run("api:app", port=8000, log_level="info", host="localhost", reload=True)
