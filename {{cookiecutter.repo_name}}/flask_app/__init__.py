from flask import Flask

from flask_app.config.mysqlconnection import get_sqlalchemy_uri
from flask_app.extensions import db, migrate


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config["SECRET_KEY"] = "dev-cambiar-en-produccion"
    app.config["SQLALCHEMY_DATABASE_URI"] = get_sqlalchemy_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    import flask_app.models  # noqa: F401 — registrar modelos en metadata

    from flask_app.controllers.tacos import tacos_bp

    app.register_blueprint(tacos_bp)

    return app
