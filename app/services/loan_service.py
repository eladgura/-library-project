from app import db
from app.models.loan import Loan

class LoanService:
    @staticmethod
    def get_loans():
        loans = Loan.query.all()
        return [loan.to_dict() for loan in loans]

    @staticmethod
    def get_loan(id):
        loan = Loan.query.get_or_404(id)
        return loan.to_dict()

    @staticmethod
    def add_loan(data):
        new_loan = Loan(
            user_id=data['user_id'],
            book_id=data['book_id'],
            due_date=data['due_date']
        )
        db.session.add(new_loan)
        db.session.commit()
        return new_loan.to_dict(), 201

    @staticmethod
    def update_loan(id, data):
        loan = Loan.query.get_or_404(id)
        loan.due_date = data.get('due_date', loan.due_date)
        loan.returned_date = data.get('returned_date', loan.returned_date)
        loan.overdue = data.get('overdue', loan.overdue)
  
