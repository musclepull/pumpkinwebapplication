import http
from typing import Union


class HTTPException(Exception):
    """Base exception class for all HTTP exceptions

    Attributes:
        status_code (http.HTTPStatus): HTTP status code that should be associated with the raised
            exception
        message (str): Message providing further description about the source of the error and if
            possible how it can be fixed or what steps should be taken after the fact
    """

    def __init__(self, status_code: http.HTTPStatus, message: str):
        self.status_code: http.HTTPStatus = status_code
        self.message: str = message

    def __str__(self):
        return f"{{status_code: {self.status_code}, message: {self.message}}}"


class HTTPClientError(HTTPException):
    """Base class for all client errors with a status in the 4xx range"""

    def __init__(self, status_code: http.HTTPStatus, message: Union[str, None] = None):
        message = message or 'A client error occurred and the request could not be completed'
        super().__init__(status_code, message)


class HTTPResourceNotFound(HTTPClientError):
    """Base class for all 404 HTTP exceptions. This should include all errors triggered by the
    attempt to access resources that could not be found or where the request is not applicable.
    This exception should also be thrown if the server does not wish to provide details of why
    the resource could not be returned
    """

    def __init__(self, message: Union[str, None] = None):
        status_code = http.HTTPStatus.NOT_FOUND
        message = message or 'Not Found. No response is applicable for given response'
        super().__init__(status_code, message)