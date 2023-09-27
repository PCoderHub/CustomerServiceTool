import os
import sys

current = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import app
import json

class TestConcernPostGet(unittest.TestCase):               #verify in database
    def setUp(self):
        self.app = app.test_client()

    def test_concernpostget(self):
        query = {
            "userName" : "testuser",
            "email" : "testuser@gmail.com",
            "agent" : "agent1",
            "concernType" : "query",
            "subject" : "subject1",
            "description" : "description1"
        }

        complaint = {
            "userName" : "testuser1",
            "email" : "testuser@gmail.com",
            "agent" : "agent1",
            "concernType" : "complaint",
            "subject" : "subject1"
        }

        responsepost1 = self.app.post('/concerns', data=json.dumps(query), content_type='application/json')
        self.assertEqual(responsepost1.status_code, 200)

        responsepost2 = self.app.post('/concerns', data=json.dumps(complaint), content_type='application/json')
        self.assertEqual(responsepost2.status_code, 200)

        responseget1 = self.app.get('/concerns') 
        self.assertEqual(responseget1.status_code, 200)                 # to get all tickets

        responseget2 = self.app.get('/concerns?userName=testuser')
        self.assertEqual(responseget2.status_code, 200)
        data = json.loads(responseget2.data)
        self.assertEqual(len(data), 1)                                  # to get number of tickets created by a user

if __name__ == '__main__':
    unittest.main()