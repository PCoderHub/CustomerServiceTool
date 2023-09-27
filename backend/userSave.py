#factory class called here

from userFactory import UserFactory

class UserSave:
    def __init__(self):
        self.__factory = UserFactory()

    def user_save(self, user):
        if user['userType'] == 'agent':                                     # to save agents
            agent = self.__factory.get_user(user['userType'])
            agent.set_username(user['userName'])
            agent.set_password(user['password'])
            return agent

        elif user['userType'] == 'customer':                                 # to save customers
            customer = self.__factory.get_user(user['userType'])
            customer.set_username(user['userName'])
            customer.set_password(user['password'])
            return customer

