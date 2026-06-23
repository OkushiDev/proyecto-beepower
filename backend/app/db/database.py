from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# 1. Crear el Motor Asíncrono
# echo=True imprime en la terminal cada consulta SQL que el ORM genera por debajo. 
# Es una herramienta de auditoría invaluable durante el desarrollo.
engine = create_async_engine(settings.database_url, echo=True)

# 2. Fábrica de Sesiones
# expire_on_commit=False asegura que podamos seguir usando las variables de Python 
# incluso después de haber guardado los datos en PostgreSQL.
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 3. Clase Base para los Modelos
# Todas las tablas de la base de datos que creemos en el futuro heredarán de esta clase.
Base = declarative_base()

# 4. Dependencia de Inyección de Sesión
# Esta función generadora le entregará una sesión fresca a FastAPI cada vez que un 
# usuario haga una petición web, y se asegurará de cerrarla al terminar para no saturar la RAM.
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()