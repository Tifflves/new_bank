from .User_Class import User
from main_files.ERRORS import AccessDeniedError, ExistenceError
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#

class BusinessClient(User):
    def __init__(self, user_id, password, name, email, corporate_name):
        super().__init__(user_id, password, name, email)

        self._corporate_name = corporate_name.upper()
        self._accounts = {
            "CORPORATE": [],
            "CHECKING": []
        }

#──────────────────────────────────────────||──||
#──────────────────────────────────────────||──||
    @property
    def corporate_name(self):
        return self._corporate_name

    @corporate_name.setter
    def corporate_name(self, value):
        self._corporate_name = value
#──────────────────────────────────────────||──||
    @property
    def accounts(self):
        return self._accounts

    @accounts.setter
    def accounts(self, value: tuple[str, int]):
        match value[0]:
            case "CORPORATE":
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

#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#
########################################################################################################################
#──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────#