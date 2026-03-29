from flask import Blueprint, redirect, render_template, request, url_for

from flask_app.models.taco import Taco

tacos_bp = Blueprint("tacos", __name__)


def _precio_from_form(form_value, default=0.0):
    try:
        return float(form_value)
    except (TypeError, ValueError):
        return default


@tacos_bp.route("/")
def index():
    tacos = Taco.get_all()
    return render_template("index.html", tacos=tacos)


@tacos_bp.route("/tacos/<int:taco_id>")
def detalle(taco_id):
    taco = Taco.get_by_id(taco_id)
    return render_template("detalle.html", taco=taco)


@tacos_bp.route("/tacos/nuevo", methods=["GET", "POST"])
def nuevo():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        if nombre:
            precio = _precio_from_form(request.form.get("precio"))
            descripcion = request.form.get("descripcion", "").strip()
            taco_id = Taco.create(nombre=nombre, precio=precio, descripcion=descripcion)
            return redirect(url_for("tacos.detalle", taco_id=taco_id))
    return render_template("nuevo.html")


@tacos_bp.route("/tacos/<int:taco_id>/editar", methods=["GET", "POST"])
def editar(taco_id):
    taco = Taco.get_by_id(taco_id)
    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        precio = _precio_from_form(request.form.get("precio"))
        Taco.update(taco_id, nombre=nombre, precio=precio)
        return redirect(url_for("tacos.detalle", taco_id=taco_id))
    return render_template("editar.html", taco=taco)


@tacos_bp.route("/buscar")
def resultados():
    q = request.args.get("q", "").strip()
    tacos = Taco.search(q) if q else []
    return render_template("resultados.html", tacos=tacos, q=q)
