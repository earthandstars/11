#uvicorn main:app --reload
from fastapi import FastAPI, Request, Form
from fastapi.templating import jinja2Templates

app = FastAPI()
templates = jinja2Templates(directory="/code")

@app.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('Form.html', context={'request': request})
