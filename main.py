from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from app.routers import auth, user, food_log, recommendations

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="votre_clé_secrète_sécurisée")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(auth, prefix="/auth", tags=["auth"])
app.include_router(user, prefix="/user", tags=["user"])
app.include_router(food_log, prefix="/food-log", tags=["food_log"])
app.include_router(recommendations, prefix="/recommendations", tags=["recommendations"])

@app.get("/")
async def root(request: Request):
    print("Route / atteinte, rendu de index.html")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup")
async def signup_page(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/dashboard")
async def dashboard_page(request: Request):
    message = request.query_params.get("message")
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/food_log")
async def food_log_page(request: Request):
    return templates.TemplateResponse("food_log.html", {"request": request})

@app.get("/profile")
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})


@app.get("/recommendations")
async def recommendations_page(request: Request):
    return templates.TemplateResponse("recommendations.html", {"request": request})

