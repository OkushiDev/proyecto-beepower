from fastapi import FastAPI
from app.api import users  # Importamos el módulo de rutas

app = FastAPI(title="BeePower API", version="0.1.0")

# Conectamos el enrutador de usuarios a la red. 
# Todas las rutas dentro de ese archivo tendrán el prefijo "/usuarios"
app.include_router(users.router, prefix="/usuarios", tags=["Usuarios"])


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "0.1.0",
        "python_version": "3.14"
    }