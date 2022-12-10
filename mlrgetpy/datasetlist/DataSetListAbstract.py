from abc import abstractmethod
from dataclasses import dataclass, field
from urllib import response
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.FilterInput import FilterInput
from datetime import date
from mlrgetpy.IDInput import IDInput


@dataclass
class DataSetListAbstract:

    # TODO: tests for the urls
    request = RequestHelper()

    # ...&input={"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":700}}}
    # TODO: private URLS
    url = 'https://archive-beta.ics.uci.edu/trpc/donated_datasets.filter?batch=1&input='
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"

    creator_url = "https://archive-beta.ics.uci.edu/trpc/creators.getByDatasetId?batch=1&input="

    '''
    URL to get repositories with the input in a json object
    https://archiv...ilter?batch=1&input={"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":700}}}
    '''

    def get_url(self, filter_input: FilterInput = FilterInput()) -> str:
        return self.url + filter_input.str_json()

    # TODO: check valid response
    def check_valid_response(self):
        NotImplemented

    def getCount(self) -> int:
        filter_input = FilterInput()
        response = self.request.get(self.get_url(filter_input))
        json_response = JsonParser().encode(response.text)
        #self.__check_count_response(json_response, response.url)

        return json_response[0]["result"]["data"]["json"]["count"]

    def findAll(self):
        NotImplemented

    def getCreators(self, id: int) -> list:
        id_input_object = IDInput(id)
        id_input_str: str = id_input_object.str_json()

        response = self.request.get(self.creator_url + id_input_str)
        json_response = JsonParser().encode(response.text)
        self.__check_creators_response(json_response, response.url)

        return json_response[0]["result"]["data"]["json"]

    def __check_count_response(self, json_response: dict, url: str):
        if 'data' not in json_response[0]:
            raise Exception(
                f"Not valid response: Json without key ('data') in {url}")

    def __check_creators_response(self, json_response: dict, url: str):
        if 'json' not in json_response[0]["result"]["data"]:
            raise Exception(
                f"Not valid response: Json without key ('json') in {url}")
