from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(100))
    genre = db.Column(db.String(100))
    author = db.Column(db.String(100))
    in_stock = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Book {self.name}>'
