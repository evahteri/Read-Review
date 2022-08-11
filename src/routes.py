from flask import render_template, request, redirect, session, abort, flash
from app import app
from services.author_service import author_service
from services.book_service import book_service
from services.user_service import user_service
from services.review_service import review_service


@app.route("/")
def index():
    results = review_service.get_recent_reviews()
    return render_template("homepage.html", results=results)


@app.route("/new_author")
def new_author():
    return render_template("new_author.html")


@app.route("/create_author", methods=["POST"])
def create_author():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    author_service.create_author(first_name, last_name)
    flash("Author created succesfully!")
    return redirect("/new_author")


@app.route("/new_book")
def new_book():
    return render_template("new_book.html")


@app.route("/create_book", methods=["POST"])
def create_book():
    author_first_name = request.form["author_first_name"]
    author_last_name = request.form["author_last_name"]
    title = request.form["title"]
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    book_service.create_new_book(author_first_name, author_last_name, title)
    flash("Book created succesfully!")
    return redirect("/new_book")


@app.route("/book_search_results")
def book_search_results():
    query = request.args["query"]
    results = book_service.search_books(query)
    return render_template("book_results.html", results=results)


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    role = request.form["role"]
    if user_service.create_user(username, password, role) == "username exists":
        flash("This username already exists")
        return redirect("/sign_up")
    if user_service.create_user(username, password, role) == "invalid password":
        flash("""Please provide a password that is more than 8 characters long, 
        includes at least one number, one special character , 
        one lower and one uppercase character.""")
        return redirect("/sign_up")
    if user_service.create_user(username, password, role):
        flash("User created successfully!")
        return redirect("/sign_in")


@app.route("/sign_out")
def sign_out():
    if session["username"]:
        del session["username"]
    if session["role"]:
        del session["role"]
    return redirect("/")


@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")


@app.route("/sign_user_in", methods=["POST"])
def sign_user_in():
    username = request.form["username"]
    password = request.form["password"]
    if user_service.sign_in(username, password):
        return redirect("/")
    if not user_service.sign_in(username, password):
        flash("Invalid username or password")
        return redirect("/sign_in")


@app.route("/books/<int:book_id>/new_review")
def new_review(book_id):
    book = book_service.get_book_by_id(book_id)
    author_first_name = book.first_name
    author_last_name = book.last_name
    title = book.title
    return render_template("new_review.html", book_id=book_id,
                           author_first_name=author_first_name,
                           author_last_name=author_last_name, title=title)


@app.route("/books/<int:book_id>/create_review", methods=["POST"])
def create_review(book_id):
    title = request.form["title"]
    review = request.form["review"]
    rating = request.form["rating"]
    book_id = book_id
    review_service.create_review(title, review, rating, book_id)
    flash("Review created successfully!")
    return redirect("/")

@app.route("/info")
def info():
    return render_template("/info.html")