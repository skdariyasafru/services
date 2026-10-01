from flask import Flask

from routes.home_routes import home_bp
from routes.cooking_routes import cooking_bp
from routes.electrical_routes import electrical_bp
from routes.cart_routes import cart_bp


def create_app():

    app = Flask(__name__)

    # ==============================
    # CONFIG
    # ==============================

    app.config["SECRET_KEY"] = "service-project-development-key"

    # ==============================
    # REGISTER ROUTES
    # ==============================

    app.register_blueprint(home_bp)
    app.register_blueprint(cooking_bp)
    app.register_blueprint(electrical_bp)
    app.register_blueprint(cart_bp)

    # ==============================
    # HEALTH CHECK
    # ==============================

    @app.route("/ping")
    def ping():
        return "SERVICE PROJECT is running!"

    return app


app = create_app()


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000,
        debug=True
    )
