from flask import render_template
from app import app

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/create_review")
def create_review():
    return render_template("create_review.html")
