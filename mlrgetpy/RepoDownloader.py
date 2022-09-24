from dataclasses import dataclass
import re
from lxml import html
import pandas as pd
from mlrgetpy.MyProgressBar import MyProgressBar
from mlrgetpy.RequestHelper import RequestHelper
from requests.exceptions import RequestException
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

    def download(self, data: pd.DataFrame):
        req = RequestHelper()

        print()
        for index, row in data.iterrows():
            # req.get(row["URLFolder"])
            # join with machine-learning-databases/<index_repo>/
            url = urljoin(self.__old_url, row["URLFolder"].replace("../", ""))

            response = req.get(url)
            webpage = html.fromstring(response.content)
            links = webpage.xpath('//a/@href')
            # TODO: download zip or csv
            # TODO: remove url /ml/machine-learning-databases/
            print(url)
            for link in links:
                if link == "/ml/machine-learning-databases/":
                    continue

                # TODO: Refactor
                print(parse.unquote(link))
                url3 = urljoin(url, link)
                response2 = requests.get(url3)

                from urllib import request
                fname = req.getName(response2, url3)
                response = request.urlretrieve(
                    url3, 'repo_download\\' + fname, MyProgressBar())

            print("---")

    # TODO repodownloader

    def downloadALl(self, rep):
        NotImplemented
