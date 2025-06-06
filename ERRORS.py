
class AccessDeniedError(Exception):
    def __init__(self, message="Доступ запрещен"):
        super().__init__(message)