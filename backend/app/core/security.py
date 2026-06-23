from passlib.context import CryptContext

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