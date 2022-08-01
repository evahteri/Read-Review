from flask import render_template, request, redirect
from app import app
from services.author_service import author_service
from services.book_service import book_service


@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/new_review")
def new_review():
    return render_template("new_review.html")

@app.route("/create_review")
def create_review():
    #TODO
    pass

@app.route("/new_author")
def new_author():
    return render_template("new_author.html")

@app.route("/create_author", methods=["POST"])
def create_author():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    author_service.create_author(first_name, last_name)
    return  redirect("/new_author")

@app.route("/new_book")
def new_book():
    return render_template("new_book.html")

@app.route("/create_book", methods=["POST"])
def create_book():
    author_first_name = request.form["author_first_name"]
    author_last_name = request.form["author_last_name"]
    title = request.form["title"]
    book_service.create_new_book(author_first_name, author_last_name, title)
    return redirect("/new_book")

@app.route("/book_search_results")
def book_search_results():
    query = request.args["query"]
    results = book_service.search_books(query)
    return render_template("book_results.html", results=results)