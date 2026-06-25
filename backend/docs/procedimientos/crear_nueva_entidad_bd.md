# Protocolo para Crear una Nueva Entidad (Ej: characters_stats)
Si necesitas crear una nueva tabla mañana, el flujo de trabajo arquitectónico siempre requerirá crear/modificar estos 5 elementos en orden estricto:

1. Definir la Estructura Física (db/models.py): Creas la clase class CharacterStat(Base): con sus columnas y tipos de SQLAlchemy.

2. Registrar la Migración (migrations/env.py): Importas CharacterStat en la línea app.db.models para que Alembic la detecte.

3. Ejecutar Alembic (Terminal): Corres revision --autogenerate y upgrade head para materializar la tabla en PostgreSQL.

Generar script de revision
```bash
docker compose exec backend uv run alembic revision --autogenerate -m "crear_tabla_character_stat"
```
Aplicar script a la base de datos PostgreSQL
```bash
docker compose exec backend uv run alembic upgrade head"
```

4. Definir el Contrato Lógico (schemas/character.py): Creas un nuevo archivo con las clases de Pydantic (CharacterStatCreate, CharacterStatResponse) para validar las estadísticas.

5. Crear el Controlador (api/characters.py): Creas el archivo con los endpoints POST y GET.

6. Ensamblar el Módulo (main.py): Importas el nuevo enrutador y ejecutas app.include_router(characters.router).