import os
from urllib.parse import quote_plus

import pymysql
from pymysql.cursors import DictCursor


def get_sqlalchemy_uri():
    """URI para Flask-SQLAlchemy (misma configuración que `get_connection`)."""
    user = os.environ.get("MYSQL_USER", "root")
    password = quote_plus(os.environ.get("MYSQL_PASSWORD", "password"))
    host = os.environ.get("MYSQL_HOST", "localhost")
    port = os.environ.get("MYSQL_PORT", "3306")
    database = os.environ.get("MYSQL_DATABASE", "db")
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"


def get_connection():
    """Conexión MySQL (valores por defecto; sobrescribir con variables de entorno)."""
    return pymysql.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "password"),
        database=os.environ.get("MYSQL_DATABASE", "db"),
        cursorclass=DictCursor,
    )
