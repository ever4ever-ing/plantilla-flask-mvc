# {{cookiecutter.repo_name}}

{{cookiecutter.proyect_short_description}}

## Base de datos (MySQL)

Crea una base vacía. Por defecto la app usa la base `db` (configurable con `MYSQL_DATABASE`).

```sql
CREATE DATABASE db;
```

Variables de entorno opcionales: `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`.

## Migraciones

En la raíz del proyecto generado:

**PowerShell**

```powershell
$env:FLASK_APP = "server:app"
python -m pip install -r requirements.txt
python -m flask db migrate -m "inicial"
python -m flask db upgrade
```

Si no trajera carpeta `migrations/`, primero: `python -m flask db init`.

## Arranque

```powershell
python server.py
```

O: `python -m flask run` con `FLASK_APP=server:app`.
