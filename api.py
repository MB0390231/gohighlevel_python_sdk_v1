import requests, json
from gohighlevel_python_sdk.exceptions import GHLRequestError
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class ghlapi(object):
    API = "https://rest.gohighlevel.com/v1"
    REQUESTS_REMAINING = None
    SECONDS_UNTIL_RATE_RESET = None

    def make_request(self, token, method, route, params=None, values=None, file=None):
        headers = self.construct_headers(token=token)
        if not params:
            params = {}
        url = f"{self.API}/{route}"
        if method in ["GET", "DELETE"]:
            response = requests.request(
                url=url,
                method=method,
                headers=headers,
                params=params,
            )
        elif method == "POST":
            if file:
                response = requests.post(url, files=file, headers=headers)
                return
            elif values is None:
                response = requests.post(url, headers=headers)
            else:
                response = requests.post(url, data=json.dumps(values), headers=headers)
        elif method == "PUT":
            response = requests.put(url, data=json.dumps(values), headers=headers)
        else:
            raise ValueError("Invalid request method")
        try:
            body = response.json()
        except:
            raise GHLRequestError(response.text)
        self._update_rate_limits(response.headers)
        self._verify_response(response)
        return body

    # TODO: Because GHL doesn't document what error messages they will give, I will have to wait and see smh
    def _update_rate_limits(self, headers):
        try:
            self.REQUESTS_REMAINING = headers["RateLimit-Remaining"]
            self.SECONDS_UNTIL_RATE_RESET = headers["RateLimit-Reset"]
        except Exception as e:
            LOGGER.exception(f"Error updating rate limits: {e}", exc_info=True)
        return False

    # TODO: change structure of error message to include the dict returned not just the "msg" value
    def _verify_response(self, response):
        if response.status_code != 200:
            message = f"Request failed with status code {response.status_code}\n Request URL: {response.url}\n Request Headers: {response.headers}\n Request Body: {response.text}"
            raise GHLRequestError(message)
        return True

    def construct_headers(self, token):
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Version": "2021-04-15",
        }
