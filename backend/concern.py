# interface class

class Concern:
    def __init__(self):
        self.__username = ""
        self.__email = ""
        self.__agent = ""
        self.__concerntype = ""
    
    def get_username(self):
        return self.__username
    
    def set_username(self, username):
        self.__username = username

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_agent(self):
        return self.__agent
    
    def set_agent(self, agent):
        self.__agent = agent

    def make_concern(self):                  # method to set the concerntype
        pass