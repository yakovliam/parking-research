import enum
import requests

class PassportApiResponseStatus(enum.Enum):
    SUCCESS = enum.auto()
    FAILED = enum.auto()

class PassportApiResponse:
    def __init__(self, status: PassportApiResponseStatus, response: requests.Response):
        self.status = status
        self.response = response

class PassportMethodReturn:

    def __init__(self, status: PassportApiResponseStatus, text: str):
        self.status = status
        self.text = text

    @classmethod
    def success(cls, text: str):
        return cls(PassportApiResponseStatus.SUCCESS, text)
    
    @classmethod
    def failed(cls):
        return cls(PassportApiResponseStatus.FAILED, "")