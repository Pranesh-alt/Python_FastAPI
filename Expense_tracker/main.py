from fastapi import FastAPI, Request
from .database import Base, engine
from . import models
from .routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles
 
app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="Expense_tracker/templates")

app.mount("/static", StaticFiles(directory="Expense_tracker/static"), name="static")

@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/health")
def health_check():
    return {"status": "Healthy"}

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)

