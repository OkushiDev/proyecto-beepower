# Utilizar la imagen oficial de uv con Python 3.14 sobre Alpine Linux
FROM ghcr.io/astral-sh/uv:python3.14-alpine

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Optimización de caché: Copiar primero solo los manifiestos de dependencias
COPY pyproject.toml uv.lock ./

# Instalar las dependencias del proyecto de forma determinista sin incluir paquetes de desarrollo
RUN uv sync --frozen --no-dev

# Copiar el resto del código fuente del backend al contenedor
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Ejecutar el servidor asíncrono apuntando al nuevo directorio
CMD ["uv", "run", "fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]