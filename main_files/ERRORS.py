
class AccessDeniedError(Exception):
    def __init__(self, message="Доступ запрещен"):
        super().__init__(message)

class ExistenceError(Exception):
    def __init__(self, message="Такой объект уже существует"):
        super().__init__(message)