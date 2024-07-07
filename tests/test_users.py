import unittest
from app import app, db
from app.models.user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

        # Add a test user
        self.test_user = User(username='testuser', email='testuser@example.com', password='testpassword')
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

    def test_get_user(self):
        response = self.app.get(f'/users/{self.test_user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data))

    def test_add_user(self):
        response = self.app.post('/users', json={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('newuser', str(response.data))

    def test_update_user(self):
        response = self.app.put(f'/users/{self.test_user.id}', json={
            'username': 'updateduser',
            'email': 'updateduser@example.com',
            'password': 'updatedpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('updateduser', str(response.data))

    def test_delete_user(self):
        response = self.app.delete(f'/users/{self.test_user.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
