# app/main.py

from fastapi import FastAPI
from app.config import config
from app.routers import pdf

app = FastAPI(title=config.APP_NAME, version=config.VERSION)

# Register routes
app.include_router(pdf.router, prefix="/pdf", tags=["PDF Operations"])

# Este es el archivo principal de entrada para ejecutar la app
