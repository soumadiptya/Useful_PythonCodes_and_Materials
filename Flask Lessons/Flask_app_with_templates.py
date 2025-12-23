from flask import Flask, render_template, url_for

# Initiate a Flask app
flask_app = Flask(__name__)
posts = [{'author': 'Corey Schafer',
          'title': 'Blog Post 1',
          'content': 'Flask Lessons',
          'date_posted': 'April 20, 2018'},
         {'author': 'Soumadiptya Chakraborty',
          'title': 'Blog Post 2',
          'content': 'Flask follow up Homework',
          'date_posted': 'October 10, 2021'}
         ]


@flask_app.route("/")
@flask_app.route("/home")
def hello():
    return render_template(template_name_or_list='home.html', posts=posts, title='Home')  # posts is a kwd argument not a normal one


@flask_app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    flask_app.run(debug=True)
