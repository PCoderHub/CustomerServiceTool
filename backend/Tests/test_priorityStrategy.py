import os
import sys

current = os.path.dirname(os.path.abspath(__file__))              # to refer 'app.py' file path
parent = os.path.dirname(current)
sys.path.append(parent)

import unittest
from app import ComplaintPrio, QueryPrio, Priority

class TestPriorityStrategy(unittest.TestCase):
    def test_priority(self):
        complaint_prio = ComplaintPrio()
        query_prio = QueryPrio()
        priority = Priority(complaint_prio)
        self.assertEqual(priority.set_priority(), 'high')                 
        #test to set if priority is high for complaint

        priority = Priority(query_prio)
        self.assertEqual(priority.set_priority(), 'very high')            
        # test to set priority is very high for query

if __name__ == '__main__':
    unittest.main()