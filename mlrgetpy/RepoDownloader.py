from dataclasses import dataclass
import re
from lxml import html
import pandas as pd
from mlrgetpy.MyProgressBar import MyProgressBar
from mlrgetpy.RequestHelper import RequestHelper
from requests.exceptions import RequestException
from requests import Response
import progressbar

from rich import print
from urllib.parse import urljoin
import requests
from urllib import parse


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/"
    __new_url = "https://archive-beta.ics.uci.edu/api/static/ml/datasets/"
    pbar = None
    # TODO repodownloader

    def __getLinks(self, response: Response):
        webpage = html.fromstring(response.content)
        links = webpage.xpath('//a/@href')

        return links

    def download(self, data: pd.DataFrame):
        req = RequestHelper()

        print()
        for index, row in data.iterrows():
            # req.get(row["URLFolder"])
            # join with machine-learning-databases/<index_repo>/
            parent_url = urljoin(
                self.__old_url, row["URLFolder"].replace("../", ""))

            response = req.get(parent_url)
            links = self.__getLinks(response)

            # TODO: create function downloadLinks
            print(parent_url)
            for link in links:
                if link == "/ml/machine-learning-databases/":
                    continue

                # TODO: Refactor
                print(parse.unquote(link))
                url = urljoin(parent_url, link)
                response2 = requests.get(url)

                req.saveFile(response2, url, row["Name"])

            print("---")

    # TODO repodownloader

    def downloadALl(self, rep):
        NotImplemented
