import unittest
from app import app,db
from app.models.user import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.app.post('/auth/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/auth/login', json={
            'email': 'testuser@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()