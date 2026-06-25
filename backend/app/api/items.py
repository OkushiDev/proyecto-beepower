from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.database import get_db
from app.db.models import GameItem
from app.schemas.item import GameItemCreate

router = APIRouter()

@router.post("/", response_model=GameItemCreate, status_code=status.HTTP_201_CREATED)
async def create_item(item_in: GameItemCreate, db: AsyncSession = Depends(get_db)):
    """Crea un nuevo ítem en la base de datos para el videojuego."""
    
    # 1. Verificamos si el ID ya existe para no chocar la llave primaria
    query = select(GameItem).where(GameItem.id == item_in.id)
    result = await db.execute(query)
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Un ítem con este ID ya existe en el juego.")
        
    # 2. Transformamos el esquema validado de Pydantic al modelo físico de SQLAlchemy
    nuevo_item = GameItem(**item_in.model_dump())
    
    # 3. Persistimos en PostgreSQL
    db.add(nuevo_item)
    await db.commit()
    await db.refresh(nuevo_item)
    
    return nuevo_item

@router.get("/", response_model=List[GameItemCreate])
async def get_all_items(db: AsyncSession = Depends(get_db)):
    """Obtiene la lista de todos los ítems (Este será el núcleo del futuro game_data.json)"""
    query = select(GameItem)
    result = await db.execute(query)
    return result.scalars().all()