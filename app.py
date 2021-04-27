from flask import Flask
from flask_selfdoc import Autodoc

app = Flask(__name__)
auto = Autodoc(app)


@app.route("/")
@auto.doc()
def index():
    """Returns "Hello, World!" and a 200 HTTP Code"""
    return "Hello, World!"


@app.route("/healthz")
@auto.doc()
def healthz():
    """Returns "OK" and a 200 HTTP Code"""
    return "OK"


@app.route("/unhealthz")
@auto.doc()
def unhealthz():
    """Returns "NOK!" and a 500 HTTP Code"""
    return "NOK!", 500


@app.route("/docs")
def documentation():
    return auto.html()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
