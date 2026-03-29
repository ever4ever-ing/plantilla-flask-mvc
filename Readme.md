# {{cookiecutter.repo_name}}

{{cookiecutter.proyect_short_description}}

##

CREATE DATABASE tacos_db;

## Para aplicar migraciones
$env:FLASK_APP = "server:app"
python -m flask db init
python -m flask db migrate -m "descripcion del cambio"
python -m flask db upgrade