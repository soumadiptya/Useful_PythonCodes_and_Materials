from flask import Flask, render_template

# Initiate a Flask app
flask_app = Flask(__name__)


@flask_app.route("/")
@flask_app.route("/home")
def hello():
    return render_template(template_name_or_list='home.html')


@flask_app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == "__main__":
    flask_app.run(debug=True)
