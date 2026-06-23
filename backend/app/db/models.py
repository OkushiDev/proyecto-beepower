from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.database import Base

class User(Base):
    # __tablename__ define el nombre real que tendrá la tabla en PostgreSQL
    __tablename__ = "users"

    # Mapped[tipo] le dice a Python qué tipo de dato esperar.
    # mapped_column(...) le dice a PostgreSQL cómo configurar la columna físicamente.
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    # unique=True garantiza que la base de datos rechace correos duplicados.
    # index=True acelera dramáticamente las búsquedas por este campo.
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    
    # Aquí no guardaremos contraseñas reales, sino el "hash" generado por bcrypt en el futuro.
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # server_default=func.now() delega al motor de PostgreSQL la tarea de estampar la 
    # fecha y hora exacta en la que se crea el registro de forma automática.
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())