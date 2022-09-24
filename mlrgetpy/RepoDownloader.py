from dataclasses import dataclass
import re
from lxml import html
import pandas as pd
from mlrgetpy.MyProgressBar import MyProgressBar
from mlrgetpy.RequestHelper import RequestHelper
from requests.exceptions import RequestException
import progressbar

from rich import print


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/"
    __new_url = "https://archive-beta.ics.uci.edu/api/static/ml/datasets/"
    pbar = None
    # TODO repodownloader

    def download(self, data: pd.DataFrame):
        req = RequestHelper()

        print()
        i = 0
        for index, row in data.iterrows():
            # req.get(row["URLFolder"])
            url = self.__old_url + row["URLFolder"].replace("../", "")

            response = req.get(url)
            webpage = html.fromstring(response.content)
            links = webpage.xpath('//a/@href')
            # TODO: download zip or csv
            # TODO: remove url /ml/machine-learning-databases/
            print(url)
            for link in links:
                if self.__old_url+"machine-learning-databases/" != "https://archive.ics.uci.edu"+link:

                    # TODO: Refactor
                    print(link)
                    req2 = RequestHelper()
                    import requests
                    url3 = url+link
                    print(url3)
                    response2 = requests.get(url3)

                    try:
                        r = response

                        fname = ''
                        if "Content-Disposition" in r.headers.keys():
                            fname = re.findall(
                                "filename=(.+)", r.headers["Content-Disposition"])[0]
                        else:
                            from urllib import parse
                            fname = parse.unquote(url3.split("/")[-1])

                        print(fname)
                        from urllib import request

                        response = request.urlretrieve(
                            url3, 'repo_download\\' + fname, MyProgressBar())

                    except RequestException as e:
                        print(e)

                    # print(d)
                    # print(r.headers['content-disposition'])

            print("---")

    # TODO repodownloader

    def downloadALl(self, rep):
        NotImplemented
