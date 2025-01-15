class BaseException(Exception):
    def __init__(self, status_code: int, message: str, detail: str = None):
        self.status_code = status_code
        self.message = message
        self.detail = detail

    def __str__(self):
        return self.message


class DynamoDBException(BaseException):
    status_code = 500
    message = "Internal Server Error"

    def __init__(self, detail: str):
        super().__init__(self.status_code, self.message, detail)


class ResourceNotFoundException(BaseException):
    status_code = 404
    message = "Resource not found"

    def __init__(self, detail: str):
        super().__init__(self.status_code, self.message, detail)
