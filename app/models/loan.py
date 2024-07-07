from app import db
from datetime import datetime

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrowed_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    returned_date = db.Column(db.DateTime)
    overdue = db.Column(db.Boolean, default=False)

    def check_overdue(self):
        if self.returned_date is None and datetime.utcnow() > self.due_date:
            self.overdue = True
        return self.overdue

    def __repr__(self):
        return f'<Loan {self.id}>'
