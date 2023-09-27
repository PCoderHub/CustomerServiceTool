#Agent class

from user import User

class Agent(User):
    def __init__(self):
        super().__init__()
        self.__usertype = "agent"
        self.__department = "customer service"                           # specific to Agent

    def get_usertype(self):
        return self.__usertype

    def get_department(self):
        return self.__department
    
    def set_department(self, department):
        self.__department = department