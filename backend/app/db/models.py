from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func, Integer, Float, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB
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


class GameItem(Base):
    __tablename__ = "game_items"

    # Raíz Universal Agnóstica (Columnas Fijas)
    id: Mapped[str] = mapped_column(String(50), primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    categoria: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    descripcion: Mapped[str] = mapped_column(Text, nullable=True)
    
    # Identificadores de Recursos (Assets)
    icon_path: Mapped[str] = mapped_column(String(255), nullable=False)
    visual_asset_path: Mapped[str] = mapped_column(String(255), nullable=True)
    audio_asset_path: Mapped[str] = mapped_column(String(255), nullable=True)
    
    # Economía y Lógica Básica de Inventario
    stack_maximo: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    precio_compra: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    precio_venta: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    # Datos Asimétricos Específicos
    propiedades: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)