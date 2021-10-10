from flask import Flask

# Initiate a Flask app
flask_app = Flask(__name__)


@flask_app.route("/")
@flask_app.route("/home")
def hello():
    return "<h1>Hello World. This is my Home page</h1>"


@flask_app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == "__main__":
    flask_app.run(debug=True)
