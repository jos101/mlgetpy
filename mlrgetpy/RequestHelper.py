from dataclasses import dataclass
from urllib import response
import requests
from requests import Response

import urllib3


class RequestHelper:

    def get(self, url) -> Response:

        urllib3.disable_warnings()
        response = requests.get(url, verify=False)

        return response
