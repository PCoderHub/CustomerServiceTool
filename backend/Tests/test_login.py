import os
import sys

current = os.path.dirname(os.path.abspath(__file__))                 #to refer 'app.py' file
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_loginvalid(self):
        user = {
            'userName': 'customer1',
            'password': '12345678'
        }

        response = self.app.post('/login', json=user)
        data = response.get_json()
        self.assertEqual(response.status_code, 200)                    # to test correct status code is returned
        self.assertIn('id', data)                                      # to test correct response is received
        self.assertIn('userName', data)
        self.assertIn('password', data)
        self.assertIn('userType', data)

    def test_logininvalid(self):
        user = {
            'userName': 'customer1',
            'password' : '1234'
        }

        response = self.app.post('/login', json=user)
        data = response.get_json()
        self.assertEqual(response.status_code, 400)                     # to test response code for invalid data
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid credentials')

if __name__ == '__main__':
    unittest.main()