from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session
)


cart_bp = Blueprint(
    "cart",
    __name__
)


# ==============================
# CART PAGE
# ==============================

@cart_bp.route("/cart")
def cart():

    cart_items = session.get(
        "cart",
        []
    )

    total = sum(
        item["price"] * item["quantity"]
        for item in cart_items
    )

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# ==============================
# ADD TO CART
# ==============================

@cart_bp.route(
    "/cart/add/<service_type>/<item_name>/<int:price>"
)
def add_to_cart(
    service_type,
    item_name,
    price
):

    cart = session.get(
        "cart",
        []
    )

    # Check whether item already exists
    for item in cart:

        if (
            item["name"] == item_name
            and
            item["service_type"] == service_type
        ):

            item["quantity"] += 1

            session["cart"] = cart
            session.modified = True

            return redirect(
                url_for(
                    "cooking.cooking_menu",
                    service_type=service_type
                )
            )

    # Add new item
    cart.append({

        "name": item_name,

        "price": price,

        "quantity": 1,

        "service_type": service_type
    })

    session["cart"] = cart
    session.modified = True

    return redirect(
        url_for(
            "cooking.cooking_menu",
            service_type=service_type
        )
    )
