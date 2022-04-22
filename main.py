from flask import Flask, render_template, flash
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "LoveMyWife"

#Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What is your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

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

#Create Name page
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()  
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successful")
    
    return render_template("name.html", name = name, form = form)