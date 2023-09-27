import os
import sys

current = os.path.dirname(os.path.abspath(__file__))         # to refer path of 'app.py' file
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import ConcernMaker, Query, Complaint

class TestConcernFacade(unittest.TestCase):
    def test_concernfacade(self):
        concern = ConcernMaker()
        complaint = Complaint()
        complaint.set_username('abc')
        complaint.set_email('abc@xyz.com')
        complaint.set_subject('complaint subject')

        self.assertEqual(complaint.get_username(), 'abc')
        self.assertEqual(complaint.get_email(), 'abc@xyz.com')
        self.assertEqual(complaint.get_subject(), 'complaint subject')

        query = Query()
        query.set_username('def')
        query.set_email('def@uvw.com')
        query.set_subject('query subject')
        query.set_description('query description')

        self.assertEqual(query.get_username(), 'def')
        self.assertEqual(query.get_email(), 'def@uvw.com')
        self.assertEqual(query.get_subject(), 'query subject')
        self.assertEqual(query.get_description(), 'query description')

        ctype = concern.make_complaint()                           # concerntype of complaint
        qtype = concern.make_query()                               # concerntype of query
        
        #to check the correct ticket structure is being created
        self.assertEqual(ctype, 'respond within 48 hours')              
        self.assertEqual(qtype, 'respond within 24 hours')

if __name__ == '__main__':
    unittest.main()