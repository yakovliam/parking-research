from generatetoken import request_token
from apiutils import PassportApiResponseStatus

def main():

    token_return = request_token()

    if token_return.status != PassportApiResponseStatus.SUCCESS:
        print("Failed to get token")
        return
    
    token = token_return.text
    print("Found token: " + token)

if __name__ == "__main__":
    main()