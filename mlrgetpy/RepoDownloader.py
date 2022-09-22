from dataclasses import dataclass
from lxml import html
import pandas as pd
from mlrgetpy.RequestHelper import RequestHelper


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/"
    __new_url = "https://archive-beta.ics.uci.edu/api/static/ml/datasets/"

    # TODO repodownloader

    def download(self, data: pd.DataFrame):
        req = RequestHelper()

        print()
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
                    print(link)

            print("---")

    # TODO repodownloader

    def downloadALl(self, rep):
        NotImplemented
