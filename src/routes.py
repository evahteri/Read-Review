from flask import render_template, request, redirect, session, abort, flash
from app import app
from services.book_service import book_service
from services.user_service import user_service
from services.review_service import review_service
from services.read_list_service import read_list_service


@app.route("/")
def index():
    results = review_service.get_recent_reviews()
    return render_template("homepage.html", results=results)


@app.route("/new_book")
def new_book():
    if user_service.get_role(session["username"]) != 1:
        flash("Not authorised to do this action")
        return redirect("/")
    return render_template("new_book.html")


@app.route("/create_book", methods=["POST"])
def create_book():
    author_first_name = request.form["author_first_name"]
    author_last_name = request.form["author_last_name"]
    title = request.form["title"]
    if book_service.check_if_book_exists(author_first_name, author_last_name, title):
        flash("This book already exists.")
        return redirect("/new_book")
    if len(author_first_name) < 1:
        flash("Missing author first name")
        return redirect("/new_book")
    if len(author_first_name) > 40:
        flash("Author's first name too long")
        return redirect("/new_book")
    if len(author_last_name) < 1:
        flash("Missing author last name")
        return redirect("/new_book")
    if len(author_last_name) > 40:
        flash("Author's last name too long")
        return redirect("/new_book")
    if len(title) < 1:
        flash("Missing title")
        return redirect("/new_book")
    if len(title) > 150:
        flash("Title too long")
        return redirect("/new_book")
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    if user_service.get_role(session["username"]) != 1:
        flash("Not authorised to do this action")
        return redirect("/new_book")
    book_service.create_new_book(author_first_name, author_last_name, title)
    flash("Book created succesfully!")
    return redirect("/new_book")


@app.route("/book_search_results")
def book_search_results():
    query = request.args["query"]
    results = book_service.search_books(query)
    session["url_search_results"] = request.url
    return render_template("book_results.html", results=results)


@app.route("/review_search_results/<int:book_id>")
def review_search_results(book_id):
    session["url_search_results"] = request.url
    results = review_service.get_reviews(book_id)
    return render_template("review_results.html", results=results, book_id=book_id)


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    username = request.form["username"]
    password = request.form["password"]
    role = request.form["role"]
    if not user_service.check_username_validity(username):
        flash(
            "Username has to be longer than two characters and shorter than 50 characters.")
        return redirect("/sign_up")
    if not user_service.check_user_does_not_exist(username):
        flash("This username already exists")
        return redirect("/sign_up")
    if not user_service.check_password_validity(password):
        flash("""Please provide a password that is more than 8 characters long,
        includes at least one number, one special character,
        one lower and one uppercase character.""")
        return redirect("/sign_up")
    if user_service.create_user(username, password, role):
        flash("User created successfully!")
        user_service.sign_in(username, password)
        return redirect("/")
    flash("Something went wrong")
    return redirect("/sign_up")


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
    review_text = request.form["review"]
    rating = request.form["rating"]
    if not review_service.check_review_length(review_text):
        flash("Review has to be over two characters and under 10 0000 characters.")
        return redirect(f"/books/{book_id}/new_review")
    if not review_service.check_title_length(title):
        flash("Title has to be over two characters and under 100 characters.")
        return redirect(f"/books/{book_id}/new_review")
    if not review_service.check_rating(rating):
        flash("Invalid rating")
        return redirect(f"/books/{book_id}/new_review")
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    review_service.create_review(title, review_text, rating, book_id)
    flash("Review created successfully!")
    return redirect("/")


@app.route("/info")
def info():
    return render_template("/info.html")


@app.route("/reviews/<int:review_id>")
def review(review_id):
    result = review_service.get_review_by_id(review_id)
    book_title = result.book_title
    review_title = result.review_title
    user = result.username
    rating = result.rating
    review_text = result.review
    return render_template("review.html", book_title=book_title, review_title=review_title,
                           user=user, rating=rating, review=review_text)


@app.route("/delete_book/<int:book_id>", methods=["POST", "GET"])
def delete_book(book_id):
    if user_service.get_role(session["username"]) == 1:
        if book_service.delete_book(book_id):
            flash("Book deleted")
            return redirect(session["url_search_results"])
        flash("Something went wrong")
        return redirect(session["url_search_results"])
    flash("Not authorised to do this action")
    return redirect("/")


@app.route("/read_list")
def read_list():
    user_id = user_service.get_user_id()
    return redirect(f"/read_list/{user_id}")


@app.route("/read_list/<int:user_id>")
def read_list_page(user_id):
    if user_service.validate_user(user_id):
        results = read_list_service.get_read_list(user_id)
        return render_template("read_list.html", results=results, user_id=user_id)
    flash("Invalid user")
    return redirect("/")


@app.route("/add_read_list/<int:book_id>")
def add_read_list(book_id):
    user_id = user_service.get_user_id()
    if read_list_service.add_to_read_list(user_id, book_id):
        flash("Book added to your read list!")
        return redirect(session["url_search_results"])
    flash("Book already in your read list!")
    return redirect(session["url_search_results"])


@app.route("/read_list/<int:user_id>/delete/<int:book_id>")
def delete_from_read_list(user_id, book_id):
    if user_service.validate_user(user_id):
        read_list_service.delete_from_read_list(user_id, book_id)
        flash("Book deleted from your read list")
        return redirect(f"/read_list/{user_id}")
    return redirect("/sign_in")


@app.route("/user_results")
def user_results():
    query = request.args["query"]
    results = user_service.search_users(query)
    return render_template("user_results.html", results=results)


@app.route("/view_read_list/<int:user_id>")
def view_read_list(user_id):
    session["url_search_results"] = request.url
    username = user_service.get_username(user_id)
    results = read_list_service.get_read_list(user_id)
    return render_template("read_list_result.html", results=results, username=username)


@app.route("/delete_review/<int:review_id>", methods=["POST", "GET"])
def delete_review(review_id):
    if user_service.get_role(session["username"]) == 1 or review_service.validate_review(review_id):
        if review_service.delete_review(review_id):
            flash("Review deleted")
            return redirect(session["url_search_results"])
        flash("Something went wrong")
        return redirect(session["url_search_results"])
    flash("Not authorised to do this action")
    return redirect(session["url_search_results"])


@app.route("/profile")
def profile():
    user_id = user_service.get_user_id()
    if not user_service.validate_user(user_id):
        return redirect("/sign_in")
    username = user_service.get_username(user_id)
    role = user_service.get_role(username)
    return render_template("profile.html", user_id=user_id, username=username, role=role)


@app.route("/user_reviews/<int:user_id>")
def reviews(user_id):
    if not user_service.validate_user(user_id):
        flash("Invalid user")
        return redirect("/")
    session["url_search_results"] = request.url
    results = review_service.get_user_reviews(user_id)
    return render_template("user_reviews.html", results=results)
