import requests, json, sys, time
from gohighlevel_python_sdk.exceptions import GHLRequestError
from urllib.parse import urlencode

V1 = "https://rest.gohighlevel.com/v1/"
V2 = "https://services.leadconnectorhq.com/"


class ghlapi(object):
    API = "https://rest.gohighlevel.com"
    REQUESTS_REMAINING = None
    SECONDS_UNTIL_RATE_RESET = None

    def get(self, route, headers, params=None, version="v1"):
        # defaults to version 1
        # TODO: explain why params must be encoded before reaching this function

        url = f"{self.API}/{version}/{route}"

        if params:
            url += f"?{urlencode(params)}"
        response = requests.get(url=url, headers=headers)
        body = response.json()
        self.write_rate_remaining(response.headers)
        self.verify_response(response)
        return body

    def post(self, route, headers, values=None):
        url = self.API + route
        if values is None:
            response = requests.post(url, headers)
        else:
            response = requests.post(url, headers, data=json.dumps(values))
        body = response.json()
        self.write_rate_remaining(response.headers)
        self.verify_response(response)
        return body

    def put(self, route, headers, values):
        url = self.API + route
        response = requests.put(url, headers, data=json.dumps(values))
        body = response.json()
        self.write_rate_remaining(response.headers)
        self.verify_response(response)
        return body

    # TODO: Because GHL doesn't document what error messages they will give, I will have to wait and see smh
    def write_rate_remaining(self, headers):
        try:
            self.REQUESTS_REMAINING = headers["RateLimit-Remaining"]
            self.SECONDS_UNTIL_RATE_RESET = headers["RateLimit-Reset"]
        except Exception as exc:
            print(exc)
        return False

    # TODO: change structure of error message to include the dict returned not just the "msg" value
    def verify_response(self, response):
        if response.status_code != 200:
            message = response.json()["msg"]
            raise GHLRequestError(message)
        return True

    def beauty_sleep(t):
        """
        Just a pretty way to countdown in the terminal
        t is an interger
        """
        for i in range(t, 0, -1):
            sys.stdout.write(str(i) + " ")
            sys.stdout.flush()
            time.sleep(1)
        print("")
        return

    def construct_headers(self, token):
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Version": "2021-04-15",
        }
