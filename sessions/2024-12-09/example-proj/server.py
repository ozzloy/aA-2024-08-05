from flask import Flask, request
import routes.cats

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Home Page</h1>"


@app.route("/landing-page")
def landing_page():
    pass


@app.route("/cat/<cat_id>")
def update_cat(cat_id):
    print(cat_id)
    return cat_id


@app.route("/cat/<int: cat_id>", methods=["POST"])
def update_cat2(cat_id):
    print(cat_id)
    return cat_id


@app.route("/beep")
def specify():
    response = Response("<h1>hi</h1>")
    response.headers["Content-Type"] = "application/json"
    return response

@app.route("/demo-guy")
def demo_guy():
    cat = {"name": "king", "age": 13}
    return jsonify(cat)

@app.route("/create-cat2", methods=["POST"])
