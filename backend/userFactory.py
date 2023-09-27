#Factory class

from agent import Agent
from customer import Customer

class UserFactory:
    def __init__(self):
        self.__user = None
    
    def get_user(self, type):
        if type is not None:
            if type.lower() == "agent":
                self.__user = Agent()
            elif type.lower() == "customer":
                self.__user = Customer()
            else:
                self.__user = None
        return self.__user