from registro_ig import app
from flask import render_template, request, redirect, url_for
from registro_ig.models import select_all, insert
from registro_ig.forms import MovementForm
from datetime import date

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", pageTitle="Todos", data=registros)

def validaFormulario(camposFormulario):
    errores = []
    hoy = date.today().isoformat()
    if camposFormulario["date"] > hoy:
        errores.append("La fecha introducida es el futuro.")

    if camposFormulario["concept"] == "":
        errores.append("Introduce un concepto para la transacción.")

    #La primera condicion es para que el numero sea distinto a 0
    #La segunda condicion es para que el campo no este vacio
    if camposFormulario["quantity"] == "" or float(camposFormulario["quantity"]) == 0.0:
        errores.append("Introduce una cantidad positiva o negativa")

    return errores


@app.route("/new", methods=["GET", "POST"])
def new():
    form = MovementForm()
    if request.method == "GET":
        return render_template("new.html", form=form, pageTitle="Nuevo", dataForm="")
    else:
        if form.validate():
            insert([form.date.data.isoformat(),
                    form.concept.data,
                    form.quantity.data])
            return redirect(url_for("index"))
        else:
            return render_template("new.html", form=form)

