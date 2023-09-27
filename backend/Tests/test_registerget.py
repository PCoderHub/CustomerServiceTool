import os
import sys

current = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import app
import json

class TestRegisterGet(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_registerget(self):
        response = self.app.get('/register/agent')         #fetching agent users only
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)                     #asserting only two agents should be present(only two agents registered)

if __name__ == '__main__':
    unittest.main()