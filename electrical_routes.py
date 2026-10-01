from flask import Blueprint, render_template


electrical_bp = Blueprint(
    "electrical",
    __name__
)


@electrical_bp.route("/services/electrical")
def electrical_services():

    return render_template(
        "electrical.html"
    )
