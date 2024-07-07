import unittest
from app import app, db
from app.models.book import Book

class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_book(self):
        response = self.app.post('/books', json={
            'name': 'Test Book',
            'genre': 'Fiction',
            'author': 'Test Author',
            'in_stock': True
        })
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
