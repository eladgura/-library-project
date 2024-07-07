from app import db
from app.models.book import Book

class BookService:
    @staticmethod
    def get_books():
        books = Book.query.all()
        return [book.to_dict() for book in books]

    @staticmethod
    def get_book(id):
        book = Book.query.get_or_404(id)
        return book.to_dict()

    @staticmethod
    def add_book(data):
        new_book = Book(
            name=data['name'],
            genre=data['genre'],
            author=data['author'],
            in_stock=data['in_stock']
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book.to_dict(), 201

    @staticmethod
    def update_book(id, data):
        book = Book.query.get_or_404(id)
        book.name = data.get('name', book.name)
        book.genre = data.get('genre', book.genre)
        book.author = data.get('author', book.author)
        book.in_stock = data.get('in_stock', book.in_stock)
        db.session.commit()
        return book.to_dict()

    @staticmethod
    def delete_book(id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return '', 204
