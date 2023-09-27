#Customer class

from user import User

class Customer(User):
    def __init__(self):
        super().__init__()
        self.__usertype = "customer"
        self.__servicetype = "raise concerns"                       # specific to Customer

    def get_usertype(self):
        return self.__usertype

    def get_servicetype(self):
        return self.__servicetype
    
    def set_servicetype(self, servicetype):
        self.__servicetype = servicetype