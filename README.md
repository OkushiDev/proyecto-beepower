# BeePower API - Sistema de Gestión de Game Data, Seguridad y bases de datos

Este proyecto tiene como objetivo poner en practica el desarrollo de una infraestructura de backend de alto rendimiento orientada a la persistencia asíncrona de datos, control de acceso perimetral mediante OAuth2/JWT y aprovisionamiento de datos estructurados dinámicos (*Game Data*) para motores de videojuegos (Unity/Godot), entre otros, utilizando FastAPI y TypeScript. 

## 1. Arquitectura y Stack Tecnológico

El sistema opera bajo una topología modular contenerizada con aislamiento de dependencias:

* **Entorno de Ejecución:** Docker & Docker Compose para orquestar servicios aislados.
* **Gestor de Paquetes:** `uv` para garantizar instalaciones deterministas de dependencias.
* **Servidor de Aplicaciones:** FastAPI inyectado sobre un bucle de eventos asíncrono (*Event Loop*).
* **Motor Relacional:** PostgreSQL como única fuente de verdad (*Source of Truth*).
* **Abstracción de Datos:** SQLAlchemy 2.0 (Patrón *Data Mapper*) empleando el driver binario asíncrono `asyncpg`.
* **Control de Versiones de BD:** Migraciones e Infraestructura como Código mediante Alembic.
* **Seguridad y Criptografía:** Autenticación por portador (*Bearer Token*) con firmas simétricas `HS256` vía PyJWT y cifrado unidireccional de contraseñas mediante Passlib y Bcrypt.

## 2. Requisitos Previos para el Despliegue

Cualquier dispositivo anfitrión que requiera clonar e inicializar el entorno de desarrollo debe contar nativamente con:

* **Docker Engine** (v20.10.0 o superior)
* **Docker Compose** (v2.0.0 o superior)
* **Git**

```bash
sudo pacman -Syu git docker docker-compose github-cli nodejs npm
```
En caso de tener un error con el despliegue en Archlinux, usar estos comandos en:
```bash
# Iniciar y habilitar el servicio
sudo systemctl enable --now docker.service

# Añadir el usuario actual al grupo de Docker
sudo usermod -aG docker $USER
```

---

## 3. Instrucciones de Instalación y Despliegue

Siga estos pasos de forma secuencial en una terminal del sistema operativo anfitrión:

### Paso 1: Clonar el Repositorio e ingresar al directorio
```bash
git clone <url-de-tu-repositorio> beepower
cd beepower
```

## Paso 2: Configuración de Variables de Entorno
Cree un archivo de configuración `.env` en la raíz del proyecto para inicializar la memoria de los contenedores. Nota crítica de seguridad: Este archivo está excluido en el control de versiones vía `.gitignore`.

```
# Configuración del Motor PostgreSQL
POSTGRES_USER=bee_admin
POSTGRES_PASSWORD=tu_clave_secreta_postgres
POSTGRES_DB=beepower_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Parámetros de Autenticación Criptográfica JWT
# (Genere un secreto de alta entropía en su terminal vía: openssl rand -hex 32)
SECRET_KEY=tu_clave_secreta_jwt_generada
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
## Paso 3: Construcción e Inicialización de Contenedores
Para compilar las imágenes virtualizadas e iniciar los servicios en segundo plano (detached), ejecute:

```bash
sudo docker compose up -d --build
```

## Paso 4: Aplicar Ciclo de Migraciones Relacionales
Una vez que el contenedor de la base de datos PostgreSQL se encuentre en estado saludable, inyecte las instrucciones en caliente para sincronizar los esquemas físicos:

```bash
sudo docker compose exec backend uv run alembic upgrade head
```

