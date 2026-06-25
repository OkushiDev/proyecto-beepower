from typing import Optional, Dict, Any
from pydantic import BaseModel, Field

class GameItemCreate(BaseModel):
    # Campos de la Raíz Universal
    id: str = Field(..., min_length=3, max_length=50, examples=["wpn_iron_sword_01"])
    nombre: str = Field(..., max_length=100)
    categoria: str = Field(..., max_length=50)
    descripcion: Optional[str] = None
    
    # Rutas de los Assets (Agnósticos)
    icon_path: str = Field(..., max_length=255)
    visual_asset_path: Optional[str] = Field(None, max_length=255)
    audio_asset_path: Optional[str] = Field(None, max_length=255)
    
    # Economía Básica
    stack_maximo: int = Field(default=1, ge=1)
    precio_compra: int = Field(default=0, ge=0)
    precio_venta: int = Field(default=0, ge=0)
    
    # El diccionario dinámico limpio para la columna JSONB
    # Pydantic asegura que al menos sea un JSON válido antes de guardarlo
    propiedades: Dict[str, Any] = Field(default_factory=dict)