from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.database import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.security import get_password_hash
from app.core.security import verify_access_token

from typing import List
router = APIRouter()


# Define el endpoint donde FastAPI buscará el token en la interfaz de Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: AsyncSession = Depends(get_db)
) -> User:
    """
    Dependencia reutilizable que valida el token JWT e inyecta el objeto del usuario
    actual autenticado en los endpoints protegidos.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales de acceso",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # 1. Verificar y decodificar token
    user_id = verify_access_token(token)
    if user_id is None:
        raise credentials_exception
        
    # 2. Consultar la existencia del usuario en la base de datos
    query = select(User).where(User.id == int(user_id))
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if user is None:
        raise credentials_exception
        
    # 3. Validar si la cuenta no se encuentra deshabilitada
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
        
    return user

# response_model=UserResponse es nuestra aduana de salida (oculta la contraseña)
# status_code=201 es el estándar web para indicar que un recurso fue creado exitosamente
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    
    # 1. Búsqueda de duplicados: Consultamos si el email ya existe
    query = select(User).where(User.email == user_in.email)
    result = await db.execute(query)
    user_exists = result.scalar_one_or_none()

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado."
        )

    # 2. Capa de Seguridad: Hashear la contraseña en texto plano recibida de internet
    hashed_pwd = get_password_hash(user_in.password)

    # 3. Modelado: Crear la instancia física para la base de datos
    new_user = User(
        email=user_in.email,
        hashed_password=hashed_pwd
    )

    # 4. Transacción: Añadir, guardar (commit) y actualizar el objeto con el ID generado
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # 5. Retorno: Devolvemos el modelo de BD. FastAPI lo pasará por UserResponse automáticamente
    return new_user

# --- LEER TODOS LOS USUARIOS (READ) ---
@router.get("/", response_model=List[UserResponse])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """Obtiene una lista de todos los usuarios con paginación."""
    # offset(skip).limit(limit) evita que el servidor colapse si hay 1 millón de usuarios
    query = select(User).offset(skip).limit(limit)
    result = await db.execute(query)
    # scalars().all() extrae los objetos de la base de datos y los convierte en una lista
    return result.scalars().all()


# --- LEER UN USUARIO ESPECÍFICO (READ) ---
@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Obtiene los detalles de un solo usuario por su ID."""
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user


# --- ACTUALIZAR USUARIO (UPDATE) ---
@router.patch("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_db),current_user: User = Depends(get_current_user)):
    """Actualiza la contraseña o el estado de un usuario."""
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    # Extraemos los datos enviados ignorando los que vengan vacíos (None)
    update_data = user_in.model_dump(exclude_unset=True)
    
    # Si el usuario quiere cambiar la contraseña, debemos hashearla antes de guardar
    if "password" in update_data:
        user.hashed_password = get_password_hash(update_data["password"])
    
    if "is_active" in update_data:
        user.is_active = update_data["is_active"]

    await db.commit()
    await db.refresh(user)
    return user


# --- ELIMINAR USUARIO (DELETE) ---
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int, 
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user) # <-- Restricción inyectada
):
    """Elimina permanentemente un usuario. Requiere autenticación JWT."""
    query = select(User).where(User.id == user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    await db.delete(user)
    await db.commit()
    return None

