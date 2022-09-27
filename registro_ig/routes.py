from registro_ig import app
from flask import render_template
from registro_ig.models import select_all

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html", pageTitle="Todos", data=registros)