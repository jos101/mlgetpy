from dataclasses import dataclass
from urllib import response
import requests
from requests import Response
from requests.exceptions import RequestException


import urllib3
import re
from urllib import parse


class RequestHelper:

    def get(self, url) -> Response:

        urllib3.disable_warnings()
        response = requests.get(url, verify=False)

        return response

    def getName(self, response: Response, url) -> str:
        try:
            fname = ''
            if "Content-Disposition" in response.headers.keys():
                fname = re.findall(
                    "filename=(.+)", response.headers["Content-Disposition"])[0]
            else:
                fname = parse.unquote(url.split("/")[-1])

        except RequestException as e:
            print(e)

        return fname
