from user import time_now
from main_files.ERRORS import ExistenceError, AccessDeniedError


#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#

class User:
    def __init__(self, user_id: str, password: str, name: str, email: str):
        self._name = name.upper()
        self._email = email.upper()
        self._password = password.upper()
        self._accounts = {
            "SAVING": [],
            "CHECKING" : []
        }


        self.__user_id = user_id.upper()
        self.__creation_time = time_now()


#──────────────────────────────────────────||──||
#──────────────────────────────────────────||──||
    @property
    def user_id(self):
        return self.__user_id

    @property
    def creation_time(self):
        return self.__creation_time

#──────────────────────────────────────────||──||
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
#──────────────────────────────────────────||──||
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
#──────────────────────────────────────────||──||
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
#──────────────────────────────────────────||──||
    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, value: tuple[str, int]):
        match value[0]:
            case "SAVING":
                if any(value[1] in val for val in self._accounts.values()):
                    raise ExistenceError
                else:
                    self._accounts["SAVING"].append(value[1])
                    print(self._accounts.items())

            case "CHECKING":
                if any(value[1] in val for val in self._accounts.values()):
                    raise ExistenceError
                else:
                    self._accounts["CHECKING"].append(value[1])
#──────────────────────────────────────────||──||
#──────────────────────────────────────────||──||

#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#

class BusinessClient(User):
    def __init__(self, user_id, password, name, email, corporate_name, corporate_account = None):
        super().__init__(user_id, password, name, email)

#──────────────────────────────────────────||──||
#──────────────────────────────────────────||──||

        self._corporate_name = corporate_name
        self.corporate_account = corporate_account

#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#

a = User("ID0003", "qwerty", "edward", "edward@gmail.com")

print(a.name)
print(a.creation_time)

a.accounts = ("SAVING", 1234_5678)
a.accounts = ("SAVING", 1234_5678)
print(a.accounts)
