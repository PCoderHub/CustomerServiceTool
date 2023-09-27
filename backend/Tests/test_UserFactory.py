import os
import sys

current = os.path.dirname(os.path.abspath(__file__))         # to refer the path of 'app.py' file
parent = os.path.dirname(current)
sys.path.append(parent)

#Factory pattern test

import unittest
from app import app
from userFactory import UserFactory
from agent import Agent
from customer import Customer

class TestUserFactory(unittest.TestCase):
    def test_FactoryReturnsUser(self):
        user = UserFactory()
        # get_user() method from UserFactory class to decide which user needs to be created
        customer = user.get_user('customer')        
        agent = user.get_user('agent')
        self.assertIsInstance(customer, Customer)
        self.assertIsInstance(agent, Agent)

if __name__ == '__main__':
    unittest.main()