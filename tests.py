import unittest
import json
from unittest.mock import MagicMock, patch
from server import app
from services.auth_service import AuthService

class TestAuth(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.auth_service = AuthService()

    def test_login_successful(self):
        mock_user = {'id': 1, 'name': 'admin', 'email': 'test@example.com', 'password': '$2b$12$Y/J3OGbA6gbWOx'}
        self.auth_service.login = MagicMock(return_value=mock_user)

        payload = {
            'email': 'admin@email.com',
            'password': '123Change@'
        }

        with patch('utils.bcrypt.verify_password', return_value=True):
            response = self.client.post('/auth/login', data=json.dumps(payload), content_type='application/json')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertIn('token', data)

    def test_login_invalid_credentials(self):
        self.auth_service.login = MagicMock(return_value=None)

        payload = {
            'email': 'test@example.com',
            'password': 'invalidpassword'
        }

        with patch('utils.bcrypt.verify_password', return_value=False):
            response = self.client.post('/auth/login', data=json.dumps(payload), content_type='application/json')
            data = json.loads(response.data)

            self.assertEqual(response.status_code, 404)
            self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
