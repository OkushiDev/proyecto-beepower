from fastapi import FastAPI
from app.api import users, auth 


app = FastAPI(title="BeePower API", version="0.1.0")

app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(users.router, prefix="/usuarios", tags=["Usuarios"])


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "0.1.0",
        "python_version": "3.14"
    }