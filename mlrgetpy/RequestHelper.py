from dataclasses import dataclass
import os
from urllib import response
import requests
from requests import Response
from requests.exceptions import RequestException
from urllib import request

import urllib3
import re
from urllib import parse

from mlrgetpy.MyProgressBar import MyProgressBar


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

    def saveFile(self, response: Response, url: str, folder=""):

        fname = self.getName(response, url)
        directory = os.path.join("repo_download", folder)
        os.mkdir(directory)
        file = os.path.join(directory, fname)

        response = request.urlretrieve(url, file, MyProgressBar())
