from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Estas variables deben coincidir exactamente con los nombres en tu archivo .env
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    
    # Valores por defecto para la red interna de Docker
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: str = "5432"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()