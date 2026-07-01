# Instrucciones de construccion y despliegue en Windows 11

Una vez instalado todo lo necesario y visto en `documentation/installation/windows11.md`, se debe dar inicio al proyecto. Para ello, debemos ubicarnos en la carpeta raiz del proyecto y seguir las siguientes indicaciones

## PASO 1: Construccion e Inicializacion de dontenedores

- El primer paso de todos es abrir la aplicacion **Docker Desktop**. Una vez abierta, deja que termine de cargar y luego cierrala, puesto que esto la mantendra oculta en segundo plano. Puedes verlo activo en el panel de abajo a la derecha de tu barra de tareas.

## PASO 2: Configuración de Variables de Entorno
Cree un archivo de configuración  `.env` en la raíz del proyecto para inicializar la memoria de los contenedores. Nota crítica de seguridad: Este archivo está excluido en el control de versiones vía `.gitignore`.

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

## PASO 3: Construccion e Inicializacion de dontenedores

Para compilar las imágenes virtualizadas e iniciar los servicios en segundo plano (detached), ejecute:

```powershell
docker compose up -d --build
```

## PASO 4: Aplicar Ciclo de Migraciones Relacionales
Una vez que el contenedor de la base de datos PostgreSQL se encuentre en estado saludable, inyecte las instrucciones en caliente para sincronizar los esquemas físicos:

```powershell
docker compose exec backend uv run alembic upgrade head
```


# Esto mantendra el proyecto y el backend funcionando. Se agregaran mas instrucciones a medida que se desarrolle la aplicacion