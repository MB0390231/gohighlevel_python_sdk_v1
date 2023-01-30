import requests, json, sys, time

from urllib.parse import urlencode


class ghlapi(object):
    API = "https://rest.gohighlevel.com"

    def get(self, route, headers, params=None, version="v1"):
        # defaults to version 1
        # TODO: explain why params must be encoded before reaching this function

        url = f"{self.API}/{version}/{route}"

        if params:
            url += f"?{urlencode(params)}"
        print(url)
        response = requests.get(url=url, headers=headers)
        body = response.json()
        # self.rate_limit_reached(response.headers)
        # self.verify_response(body)
        return body

    def post(self, route, headers, values=None):
        url = self.API + route
        if values is None:
            response = requests.post(url, headers)
        else:
            response = requests.post(url, headers, data=json.dumps(values))
        body = response.json()
        self.rate_limit_reached(response.headers)
        self.verify_response(body)
        return body

    def put(self, route, headers, values):
        url = self.API + route
        response = requests.put(url, headers, data=json.dumps(values))
        body = response.json()
        self.rate_limit_reached(response.headers)
        self.verify_response(body)
        return body

    # TODO: Because GHL doesn't document what error messages they will give, I will have to wait and see smh
    def rate_limit_reached(self, headers):
        try:
            if headers["RateLimit-Remaining"] == "0":
                seconds_till_reset = headers["RateLimit-Reset"]
                raise Exception(f"Rate Limit Reached. Seconds until reset: {seconds_till_reset}")
        except Exception as exc:
            print(exc)
        return False

    # TODO: change structure of error message to include the dict returned not just the "msg" value
    def verify_response(self, response):
        if "msg" in response.keys():
            raise ValueError(response["msg"])
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
