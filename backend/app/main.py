from fastapi import FastAPI
from app.routers.github_router import router as github_router

app = FastAPI(
    title="Proyecto IT Makita API",
    description="API para integración con servicios externos",
    version="1.0.0"
)

app.include_router(github_router)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Bienvenido a Proyecto IT Makita API"
    }