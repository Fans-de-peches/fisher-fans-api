from fastapi import Depends, FastAPI
from .routes.v1 import router as v1_router, auth_route
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(v1_router, prefix="/api/v1")
app.include_router(auth_route.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet toutes les origines
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes
    allow_headers=["*"],  # Permet tous les en-têtes
)

@app.get("/")
def home():
    return {"message": "Hello World"}