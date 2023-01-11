from flask import Blueprint, render_template

views = Blueprint('views', __name__)


# whenever you THAT url the function below will run
@views.route('/')
def home():
    return render_template("home.html")
