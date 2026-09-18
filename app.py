from flask import Flask, render_template, request, redirect, url_for, flash

from config import Config
from db import db

from models.user import User


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


# --------------------------------
# HOME
# --------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------
# REGISTER
# --------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        address = request.form.get("address", "").strip()

        # Basic validation
        if not username or not password or not phone or not email:
            flash("Please fill all required fields.", "error")
            return redirect(url_for("register"))

        # Check username
        existing_username = User.query.filter_by(
            username=username
        ).first()

        if existing_username:
            flash("Username already exists.", "error")
            return redirect(url_for("register"))

        # Check email
        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:
            flash("Email already registered.", "error")
            return redirect(url_for("register"))

        # Check phone
        existing_phone = User.query.filter_by(
            phone=phone
        ).first()

        if existing_phone:
            flash("Phone number already registered.", "error")
            return redirect(url_for("register"))

        # Create user
        user = User(
            username=username,
            password=password,
            phone=phone,
            email=email,
            address=address
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful. Please login.", "success")

        return redirect(url_for("login"))

    return render_template("register.html")


# --------------------------------
# LOGIN
# --------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(
            username=username
        ).first()

        if user and user.password == password:

            flash("Login successful.", "success")

            return redirect(url_for("home"))

        flash("Invalid username or password.", "error")

    return render_template("login.html")


# --------------------------------
# PING
# --------------------------------

@app.route("/ping")
def ping():
    return "SERVICE PROJECT is running!"


# --------------------------------
# CREATE DATABASE TABLES
# --------------------------------

with app.app_context():
    db.create_all()


# --------------------------------
# RUN
# --------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000,
        debug=True
    )
