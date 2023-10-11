from exception import Exception


class InvalidCoordinateException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
