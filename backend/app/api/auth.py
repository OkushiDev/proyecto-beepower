from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.database import get_db
from app.db.models import User
from app.core.security import verify_password, create_access_token
from app.schemas.token import Token

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    # 1. Búsqueda y validación de la entidad de usuario
    query = select(User).where(User.email == form_data.username)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    # 2. Verificación criptográfica de la contraseña
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de acceso inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Generación del token JSON Web Token (JWT)
    # El claim 'sub' (Subject) almacena el identificador único del usuario
    access_token = create_access_token(data={"sub": str(user.id)})

    # 4. Emisión de la respuesta bajo el estándar OAuth2
    return {"access_token": access_token, "token_type": "bearer"}