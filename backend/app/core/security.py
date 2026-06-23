from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from app.core.config import settings

# Configuramos Bcrypt como nuestro algoritmo de seguridad estándar
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Toma una contraseña en texto plano y devuelve el hash unidireccional.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con el hash guardado.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Toma un diccionario de datos (payload) y devuelve un JWT firmado criptográficamente.
    """
    to_encode = data.copy()
    
    # Si no se define un tiempo personalizado, usamos los 30 minutos por defecto
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Inyectamos de forma obligatoria la fecha de muerte del token en la carga útil (exp)
    to_encode.update({"exp": expire})
    
    # Criptografía pura: Empaquetamos, firmamos con la clave secreta y devolvemos el string
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt