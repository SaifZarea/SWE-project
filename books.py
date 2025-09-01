from flask import Blueprint, request, jsonify
from src.database import db
from src.models.book import Book

books_bp = Blueprint("books", __name__)

@books_bp.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = Book(title=data["title"], author=data["author"], year_published=data["year_published"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Book added successfully!"}), 201

@books_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        output.append({"id": book.id, "title": book.title, "author": book.author, "year_published": book.year_published})
    return jsonify({"books": output})

@books_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data["title"]
    book.author = data["author"]
    book.year_published = data["year_published"]
    db.session.commit()
    return jsonify({"message": "Book updated successfully!"})

@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully!"})


