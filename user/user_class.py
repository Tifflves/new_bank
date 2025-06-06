from user import time_now
import ERRORS

########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################

class User:
    def __init__(self, user_id: str, password: str, name: str, email: str, account=None):
        self._name = name
        self._email = email
        self._password = password
        self.accounts = []


        self.__user_id = user_id
        self.__creation_time = time_now()


        self.protected_attr = ["__user_id", "__creation_time"]

####################################||--||
    def getter(self, attr_name):
        if attr_name in self.protected_attr:
            attr =  "_User" + attr_name
            return getattr(self, attr, None)
        return getattr(self, attr_name, None)

####################################||--||
    def setter(self, attr_name, value):
        if attr_name in self.protected_attr:
            raise ERRORS.AccessDeniedError()

        setattr(self, attr_name, value)
        print("Success")
        return True

####################################||--||

#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#

a = User("AB122222", "bb123", "EDWARD","EDWARD@GMAIL.COM")

print(a.getter("__user_id"))
print(a.getter("_email"))

a.setter("_email", "ded@gmail.com")
a.setter("__user_id", "new")
print(a.getter("__user_id"))
print(a.getter("_email"))