from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

# 1. Esquema Base
# Contiene los campos que son comunes tanto cuando creamos un usuario
# como cuando lo leemos de la base de datos.
class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True

# 2. Esquema de Creación (Input)
# Hereda de UserBase. Representa el JSON exacto que esperamos recibir de internet
# cuando alguien llena un formulario de "Registrarse".
# Nota crítica: Exige una contraseña en texto plano.
class UserCreate(UserBase):
    password: str

# 3. Esquema de Respuesta (Output)
# Hereda de UserBase. Representa el JSON que nuestro servidor le enviará al navegador.
# Nota crítica: NUNCA incluye la contraseña. Añade el ID y la fecha de creación.
class UserResponse(UserBase):
    id: int
    created_at: datetime

    # Configuración de puente: Le dice a Pydantic que no intente leer un diccionario de Python regular,
    # sino que extraiga los datos directamente desde nuestra clase Modelo de SQLAlchemy.
    model_config = ConfigDict(from_attributes=True)

# 4. Esquema de Actualización
# Todos los campos son opcionales. El usuario puede enviar solo la contraseña, 
# solo el estado activo, o ambos.
class UserUpdate(BaseModel):
    password: Optional[str] = None
    is_active: Optional[bool] = None