from project import app, db
from flask import render_template, request, redirect, url_for
from project.list_movies import list_movies
from project.book import Book

contents = []
students_grades = []


# localhost:5000/
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("content"):
            contents.append(request.form.get("content"))
    return render_template("home.html", contents=contents)


@app.route("/grades", methods=["GET", "POST"])
def grades():
    if request.method == "POST":
        if request.form.get("name") and request.form.get("grade"):
            student_grade = {
                "name": request.form.get("name"),
                "grade": request.form.get("grade"),
            }
            students_grades.append(student_grade)
    return render_template("grades.html", grades=students_grades)


@app.route("/movies/<type>")
def movies(type):
    return render_template("movies.html", movies=list_movies(type))


@app.route("/books")
def books():
    page = request.args.get("page", 1, type=int)
    per_page = 2
    page_books = Book.query.paginate(page=page, per_page=per_page)
    return render_template("books.html", books=page_books, page=page)


@app.route("/books/new", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        price = request.form.get("price")

        book = Book(title, description, price)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("books"))

    return render_template("new_book.html")


@app.route("/books/<int:id>/edit", methods=["GET", "POST"])
def edit_book(id):
    book = Book.query.filter_by(id=id).first()

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        price = request.form.get("price")

        Book.query.filter_by(id=id).update(
            {
                "title": title,
                "description": description,
                "price": price,
            }
        )
        db.session.commit()

        return redirect(url_for("books"))

    return render_template("edit_book.html", book=book)


@app.route("/books/<int:id>/delete")
def delete_book(id):
    book = Book.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books"))
