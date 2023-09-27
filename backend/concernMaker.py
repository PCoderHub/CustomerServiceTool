#Facade class

from query import Query
from complaint import Complaint

class ConcernMaker:
    def __init__(self):
        self.__query = Query()
        self.__complaint = Complaint()
        
    def make_query(self):
        return self.__query.make_concern()
    
    def make_complaint(self):
        return self.__complaint.make_concern()