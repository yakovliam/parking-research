import enum
import requests

class PassportApiResponseStatus(enum.Enum):
    SUCCESS = enum.auto()
    FAILED = enum.auto()

class PassportApiResponse:
    def __init__(self, status: PassportApiResponseStatus, response: requests.Response):
        self.status = status
        self.response = response