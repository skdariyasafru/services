from flask import Flask, render_template
from config import Config
from db import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/ping")
def ping():
    return "Service Project is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
