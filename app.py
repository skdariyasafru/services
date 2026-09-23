from flask import Flask, render_template

app = Flask(__name__)

app.config["SECRET_KEY"] = "service-project-development-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services/electrical")
def electrical_services():
    return render_template("electrical.html")


@app.route("/ping")
def ping():
    return "SERVICE PROJECT is running!"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000,
        debug=True
    )
