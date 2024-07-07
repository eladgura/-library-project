import unittest
from app import app, db
from app.models.loan import Loan

class LoanTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_loan(self):
        response = self.app.post('/loans', json={
            'user_id': 1,
            'book_id': 1,
            'due_date': '2023-07-01'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_loans(self):
        response = self.app.get('/loans')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
