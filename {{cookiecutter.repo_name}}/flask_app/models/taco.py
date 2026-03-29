from flask_app.extensions import db


class Taco(db.Model):
    """Tabla `tacos` gestionada por migraciones (Flask-Migrate)."""

    __tablename__ = "tacos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)

    @staticmethod
    def get_all():
        try:
            return Taco.query.order_by(Taco.id).all()
        except Exception:
            return []

    @staticmethod
    def get_by_id(taco_id):
        try:
            return db.session.get(Taco, taco_id)
        except Exception:
            return None

    @staticmethod
    def update(taco_id, nombre, precio, descripcion):
        t = db.session.get(Taco, taco_id)
        if t:
            t.nombre = nombre
            t.precio = precio
            t.descripcion = descripcion
            db.session.commit()

    @staticmethod
    def create(nombre, precio, descripcion):
        t = Taco(nombre=nombre, precio=precio, descripcion=descripcion)
        db.session.add(t)
        db.session.commit()
        return t.id

    @staticmethod
    def search(q):
        try:
            return (
                Taco.query.filter(Taco.nombre.like(f"%{q}%"))
                .order_by(Taco.id)
                .all()
            )
        except Exception:
            return []
