#complaint concern

from concern import Concern

class Complaint(Concern):
    def __init__(self):
        super().__init__()
        self.__subject = ""

    def get_subject(self):
        return self.__subject
    
    def set_subject(self, subject):
        self.__subject =subject

    def make_concern(self):
        self.__concerntype = "respond within 48 hours"                       # specific to Complaint
        return self.__concerntype