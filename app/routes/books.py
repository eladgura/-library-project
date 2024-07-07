# File: app/routes/books.py

import secrets
from flask import Blueprint, request, jsonify
from app import db
from app.models.book import Book

# Define the Blueprint for books
books_bp = Blueprint('books', __name__)

# GET all books
@books_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# GET a specific book by ID
@books_bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())


@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        name=data['name'],
        genre=data['genre'],
        author=data['author'],
        in_stock=data['in_stock'],
        token=secrets.token_urlsafe()  # Generate token here or assign as needed
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

# PUT update an existing book by ID
@books_bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    book.name = data.get('name', book.name)
    book.genre = data.get('genre', book.genre)
    book.author = data.get('author', book.author)
    book.in_stock = data.get('in_stock', book.in_stock)

    db.session.commit()
    return jsonify(book.to_dict())

# DELETE a book by ID
@books_bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204
