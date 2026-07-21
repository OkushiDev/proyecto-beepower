from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import users, auth, items

app = FastAPI(
    title="BeePower API",
    description="API para gestión de usuarios y catálogo dinámico de videojuegos",
    version="1.0.0"
)

# Configuración de Orígenes Permitidos (CORS)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Permite cabeceras como Authorization para JWT
)

# Inclusión de enrutadores
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Autenticación"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Usuarios"])
app.include_router(items.router, prefix="/api/v1/items", tags=["Game Items"])