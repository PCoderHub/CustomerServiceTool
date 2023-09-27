#query concern

from concern import Concern

class Query(Concern):
    def __init__(self):
        super().__init__()
        self.__subject = ""
        self.__description = ""

    def get_subject(self):
        return self.__subject
    
    def set_subject(self, subject):
        self.__subject = subject

    def get_description(self):
        return self.__description
    
    def set_description(self, description):
        self.__description = description

    def make_concern(self):
        self.__concerntype = "respond within 24 hours"                                 # specific to Query
        return self.__concerntype