from flask import Blueprint, request, jsonify
from src.database import db
from src.models.author import Author

authors_bp = Blueprint("authors", __name__)

@authors_bp.route("/authors", methods=["POST"])
def add_author():
    data = request.get_json()
    new_author = Author(name=data["name"], nationality=data["nationality"], birth_year=data["birth_year"])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({"message": "Author added successfully!"}), 201

@authors_bp.route("/authors", methods=["GET"])
def get_authors():
    authors = Author.query.all()
    output = []
    for author in authors:
        output.append({"id": author.id, "name": author.name, "nationality": author.nationality, "birth_year": author.birth_year})
    return jsonify({"authors": output})

@authors_bp.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    data = request.get_json()
    author.name = data["name"]
    author.nationality = data["nationality"]
    author.birth_year = data["birth_year"]
    db.session.commit()
    return jsonify({"message": "Author updated successfully!"})

@authors_bp.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author deleted successfully!"})


