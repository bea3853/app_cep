from flask import Blueprint, render_template, request
from app.viewmodels.cep_viewmodel import get_cep_data

cep_bp = Blueprint("cep", __name__)


@cep_bp.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        cep = request.form.get("cep")
        result = get_cep_data(cep)

    return render_template("index.html", result=result)