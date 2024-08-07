from dataclasses import dataclass
import os
from typing import List
from urllib import response
import requests
from requests import Response
from requests.exceptions import RequestException
from urllib import request
from sympy import false

import urllib3
import re
from urllib import parse

from mlrgetpy.MyProgressBar import MyProgressBar
from mlrgetpy.log.ConfigLog import ConfigLog


@dataclass
class RequestHelper:

    def __post_init__(self) -> None:
        urllib3.disable_warnings()

    def get(self, url, expecting_json=True) -> Response:
        urllib3.disable_warnings()
        response = requests.get(url, verify=False)

        if response.status_code == 404:
            raise ValueError(f"[request error] 404: Not found page ({url})")

        if response.status_code != 200:
            raise ValueError(
                f"[request error] code {response.status_code}: page ({url})")

        if expecting_json and response.headers.get('Content-Type').startswith('application/json') == false:
            raise ValueError(f"[request error] Not a json content: ({url})")

        return response

    def head(self, url) -> Response:
        urllib3.disable_warnings()
        response = requests.head(url, verify=False)
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

    def saveFile(self, response: Response, url: str, directory="", last=false):
        ConfigLog.log.write_save_file(response, url, directory, last)

        fname = self.getName(response, url)
        file = os.path.join(directory, fname)

        #print(f"filename: {fname}")
        response = request.urlretrieve(url, file, MyProgressBar(fname, last))
        print()

    def downloadLinks(self, links: List, parent_url) -> None:
        NotImplemented
