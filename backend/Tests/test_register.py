import os
import sys

current = os.path.dirname(os.path.abspath(__file__))                 # to refer 'app.py' file
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import app, db
import json

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_registerUser(self):
        customerData = {
            'userName': 'customeruser5',
            'password': '12345678',
            'userType': 'customer'
        }

        agentData = {
            'userName': 'agentuser2',
            'password': 'agentuser',
            'userType': 'agent'
        }

        cresponse = self.app.post('/register', data=json.dumps(customerData), content_type='application/json')
        aresponse = self.app.post('/register', data=json.dumps(agentData), content_type='application/json')

        self.assertEqual(cresponse.status_code, 200)                              # to check correct status code and response
        self.assertTrue('id' in cresponse.json)
        self.assertEqual(cresponse.json['userName'], 'customeruser5')
        self.assertEqual(cresponse.json['password'], '12345678')

        self.assertEqual(aresponse.status_code, 200)
        self.assertTrue('id' in aresponse.json)
        self.assertEqual(aresponse.json['userName'], 'agentuser2')
        self.assertEqual(aresponse.json['password'], 'agentuser')  

    def test_failDuplicateUser(self):
        data = {
            'userName': 'customer2',
            'password': '12345678',
            'userType': 'customer'
        }

        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)                              # to check correct status code returned for invalid data

    def tearDown(self):
        db['users'].delete_one({'userName': 'customeruser5'})
        db['users'].delete_one({'userName': 'agentuser2'})

if __name__ == '__main__':
    unittest.main()