from abc import abstractmethod
from dataclasses import dataclass, field
from urllib import response
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.RequestHelper import RequestHelper
from datetime import date


@dataclass
class DataSetListAbstract:

    request = RequestHelper()

    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find"  # ?offset=0&limit=2
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"

    creator_url = "https://archive-beta.ics.uci.edu/api/creators/pk/"

    def getCount(self) -> int:
        response = self.request.get(self.url)
        json_response = JsonParser().encode(response.text)
        self.__check_response(json_response)

        return json_response["payload"]["count"]

    def findAll(self):
        NotImplemented

    def getCreators(self, id: int) -> list:
        response = self.request.get(self.creator_url + str(id))
        json_response = JsonParser().encode(response.text)
        if 'payload' not in json_response:
            raise Exception(
                f"Not valid response: Json without payload key in {self.url}")
        return json_response["payload"]

    def __check_response(self, json_response: dict):
        if 'payload' not in json_response or 'count' not in json_response['payload']:
            raise Exception(
                f"Not valid response: Json without key ('payload') in {self.url}")
