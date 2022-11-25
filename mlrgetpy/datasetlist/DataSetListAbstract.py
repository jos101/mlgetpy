from abc import abstractmethod
from dataclasses import dataclass, field
from urllib import response
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.RequestHelper import RequestHelper
from datetime import date


@dataclass
class DataSetListAbstract:

    # TODO: tests for the urls
    request = RequestHelper()

    # ?offset=0&limit=2
    # TODO: class for the input with method to serialize like json string
    url = 'https://archive-beta.ics.uci.edu/trpc/donated_datasets.filter?batch=1&input={"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":10}}}'
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"

    creator_url = "https://archive-beta.ics.uci.edu/api/creators/pk/"

    # TODO: check valid response
    def check_valid_response(self):
        NotImplemented

    def getCount(self) -> int:
        response = self.request.get(self.url)
        json_response = JsonParser().encode(response.text)
        #self.__check_count_response(json_response, response.url)

        return json_response[0]["result"]["data"]["json"]["count"]

    def findAll(self):
        NotImplemented

    def getCreators(self, id: int) -> list:

        response = self.request.get(self.creator_url + str(id))
        json_response = JsonParser().encode(response.text)
        self.__check_creators_response(json_response, response.url)

        return json_response["payload"]

    def __check_count_response(self, json_response: dict, url: str):
        if 'data' not in json_response[0]:
            raise Exception(
                f"Not valid response: Json without key ('data') in {url}")

    def __check_creators_response(self, json_response: dict, url: str):
        if 'payload' not in json_response:
            raise Exception(
                f"Not valid response: Json without key ('payload') in {url}")
