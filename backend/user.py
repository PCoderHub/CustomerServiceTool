#User interface

class User:
    def __init__(self):
        self.__username = ""
        self.__password = ""

    def get_username(self):
        return self.__username
    
    def set_username(self, name):
        self.__username = name
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password 