from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "service-project-development-key"


@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# COOKING SERVICE
# ==============================

@app.route("/services/cooking")
def cooking():
    return render_template("cooking.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/services/cooking/menu/<service_type>")
def cooking_menu(service_type):

    if service_type not in ["home", "delivery"]:
        return redirect(url_for("cooking"))

    return render_template(
        "cooking_menu.html",
        service_type=service_type
    )


# ==============================
# ELECTRICAL SERVICE
# ==============================

@app.route("/services/electrical")
def electrical_services():
    return render_template("electrical.html")


# ==============================
# CART
# ==============================

@app.route("/cart")
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


@app.route("/cart/add/<service_type>/<item_name>/<int:price>")
def add_to_cart(service_type, item_name, price):

    cart = session.get("cart", [])

    # Check if item already exists
    found = False

    for item in cart:
        if (
            item["name"] == item_name
            and item["service_type"] == service_type
        ):
            item["quantity"] += 1
            found = True
            break

    if not found:
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
            "cooking_menu",
            service_type=service_type
        )
    )


# ==============================
# HEALTH CHECK
# ==============================

@app.route("/ping")
def ping():
    return "SERVICE PROJECT is running!"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000,
        debug=True
    )
