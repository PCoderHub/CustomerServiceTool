import os
import sys

current = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import app

class TestConcernPutDelete(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_concernputdelete(self):
        updatedquery = {
            "userName" : "testuser",
            "email" : "testuser@gmail.com",
            "agent" : "agent1",
            "concern" : "query",
            "subject" : "subject1",
            "description" : "description1 updated"
        }
        response = self.app.put('/concerns/6436cb9f24ca3421ed104e96', json=updatedquery)

        self.assertEqual(response.status_code, 200)

        updatedcomplaint = {
            "userName" : "testuser1",
            "email" : "testuser@gmail.com",
            "agent" : "agent1",
            "concern" : "complaint",
            "subject" : "subject1 updated"
        }

        res = self.app.put('/concerns/6436cba024ca3421ed104e97', json=updatedcomplaint)
        self.assertEqual(res.status_code, 200) 

        resp = self.app.delete('/concerns/6436cb9f24ca3421ed104e96')   #verify in database
        self.assertEqual(resp.status_code, 200)

        respdel = self.app.delete('/concerns/6436cba024ca3421ed104e97')    #verify in database
        self.assertEqual(respdel.status_code, 200)

if __name__ == '__main__':
    unittest.main()