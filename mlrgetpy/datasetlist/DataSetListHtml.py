from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.FilterInput import FilterInput
from mlrgetpy.log.ConfigLog import ConfigLog
from bs4 import BeautifulSoup
import json
from mlrgetpy.RequestHelper import RequestHelper


@dataclass
class DataSetListHTML (DataSetListAbstract):

    __request_url = 'https://archive-beta.ics.uci.edu/datasets?skip=0&take=700'

    def findAll(self) -> dict:
        req = RequestHelper()
        response = req.get(self.__request_url, expecting_json=False)

        return self.dataset(response.content)

    def dataset(self, content: str) -> dict:
        soup = BeautifulSoup(content, 'html.parser')

        datasets = soup.find_all('script', type="application/json")
        data = json.loads(datasets[0].text)
        json1 = json.loads(data["body"])

        datasets_json = json1[0]["result"]["data"]["json"]

        return datasets_json

    def count(self, content: str) -> dict:
        soup = BeautifulSoup(content, 'html.parser')

        datasets = soup.find_all('script', type="application/json")
        data = json.loads(datasets[0].text)
        json1 = json.loads(data["body"])
        count = json1[0]["result"]["data"]["json"]["count"]

        return count
