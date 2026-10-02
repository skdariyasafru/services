from flask import Blueprint, render_template, redirect, url_for, request, session

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    total = sum(
        item["price"] * item["quantity"]
        for item in cart_items
    )

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


@cart_bp.route("/cart/add", methods=["POST"])
def add_to_cart():

    service_type = request.form.get("service_type")
    item_name = request.form.get("item_name")
    price = int(request.form.get("price"))

    cart = session.get("cart", [])

    # Check whether item already exists
    for item in cart:

        if (
            item["name"] == item_name
            and item["service_type"] == service_type
        ):

            item["quantity"] += 1
            break

    else:

        cart.append({
            "name": item_name,
            "price": price,
            "quantity": 1,
            "service_type": service_type
        })

    session["cart"] = cart
    session.modified = True

    # Return to the same menu
    return redirect(
        url_for(
            "cooking.cooking_menu",
            service_type=service_type
        )
    )
