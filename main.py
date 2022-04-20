from flask import Flask, render_template
from wtforms import StringField, SubmitField
from flask_wtf 


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404