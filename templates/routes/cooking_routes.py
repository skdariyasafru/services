from flask import Blueprint, render_template, redirect, url_for


cooking_bp = Blueprint(
    "cooking",
    __name__
)


# ==============================
# COOKING HOME
# ==============================

@cooking_bp.route("/services/cooking")
def cooking():

    return render_template(
        "cooking.html"
    )


# ==============================
# COOKING MENU
# ==============================

@cooking_bp.route(
    "/services/cooking/menu/<service_type>"
)
def cooking_menu(service_type):

    # Only these two options are allowed
    if service_type not in ["home", "delivery"]:

        return redirect(
            url_for("cooking.cooking")
        )

    return render_template(
        "cooking_menu.html",
        service_type=service_type
    )
