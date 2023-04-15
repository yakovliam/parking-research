import requests
from apiutils import *

url = "https://identity.us-east-1.prod.passportlabs.io/token"
data = {
    "client_id": "udTkceHng5AwmugJ",
    "client_secret": "EG1hshKPklIRF5tiZSnWTdXPFzE0Y09/d6JFRcRVx8pbABvmHIfedUlMtSTHVfwbn5Vz9K2DsCwngEFu",
    "grant_type": "client_credentials",
    "scope": "offline_access mobile:parking",
}
headers = {
    # 'accept': '*/*',
    "content-type": "application/x-www-form-urlencoded",
    "accept-encoding": "gzip;q=1.0, compress;q=0.5",
    "user-agent": "Parking/9.2.3 (com.passportparking.mobile; build:207; iOS 16.0.0) Alamofire/9.2.3",
    "accept-language": "en-US;q=1.0",
    "content-length": "0",
}

# calculate the content-length
import urllib.parse

data = urllib.parse.urlencode(data)
headers["content-length"] = str(len(data))

def request_token() -> PassportMethodReturn:
    response = requests.post(url, headers=headers, data=data)
    # if error, return FAILED
    if response.status_code != 200:
        return PassportMethodReturn.failed

    # parse the response to get the access_token
    response_json = response.json()
    access_token = response_json["access_token"]

    return PassportMethodReturn.success(access_token)