from flask import render_template, request, redirect
from app import app
from services.author_service import author_service


@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/create_review")
def create_review():
    return render_template("create_review.html")

@app.route("/new_author")
def new_author():
    return render_template("new_author.html")

@app.route("/create_author", methods=["POST"])
def create_author():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    author_service.create_author(first_name, last_name)
    return  redirect("/new_author")

