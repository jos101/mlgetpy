from abc import abstractmethod
from dataclasses import dataclass, field
import json
from urllib import response
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.FilterInput import FilterInput
from datetime import date
from mlrgetpy.IDInput import IDInput


@dataclass
class DataSetListAbstract:

    request = RequestHelper()

    # ...&input={"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":700}}}
    __url = 'https://archive-beta.ics.uci.edu/trpc/donated_datasets.filter?batch=1&input='
    # {"0":{"json":53}}
    __url2 = "https://archive-beta.ics.uci.edu/trpc/donated_datasets.getById?batch=1&input="

    __creator_url = "https://archive-beta.ics.uci.edu/trpc/creators.findByDatasetId?batch=1&input="

    '''
    URL to get repositories with the input in a json object
    https://archiv...ilter?batch=1&input={"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":700}}}
    '''

    def get_url(self, filter_input: FilterInput = FilterInput()) -> str:
        return self.__url + filter_input.str_json()

    def getCount(self) -> int:
        filter_input = FilterInput()
        response = self.request.get(self.get_url(filter_input))
        json_response = JsonParser().encode(response.text)
        self.__check_count_response(json_response, response.url)

        return json_response[0]["result"]["data"]["json"]["count"]

    def findAll(self):
        NotImplemented

    def get_href_by_id(self, id: int):
        dictionary: dict = {0: {"json": id}}
        json_input = json.dumps(dictionary, separators=[",", ":"])
        response = self.request.get(self.__url2 + json_input)
        json_response = JsonParser().encode(response.text)

        return json_response[0]["result"]["data"]["json"]["href"]

    def getCreators(self, id: int) -> list:
        id_input_object = IDInput(id)
        id_input_str: str = id_input_object.str_json()

        response = self.request.get(self.__creator_url + id_input_str)

        json_response = JsonParser().encode(response.text)
        self.__check_creators_response(json_response, response.url)

        return json_response[0]["result"]["data"]["json"]

    '''
    expected json [{"id": null,"result": {"type": "data","data": {"json": {"datasets": [],"count": 612}}}}]
    '''

    def __check_count_response(self, json_response: dict, url: str):
        expected_json = '[{"id": null,"result": {"type": "data","data": {"json": {"datasets": [],"count": 612}}}}]'

        if json_response[0] == False:
            msg = f"Not valid response: Expected json in index 0 of the list in {url}"
            msg += f"\nexpected json: {expected_json}"
            raise Exception(msg)

        if 'result' not in json_response[0]:
            msg = f"Not valid response: Json without key ('result') in {url}"
            msg += f"\nexpected json: {expected_json}"
            raise Exception(msg)

        if 'data' not in json_response[0]["result"]:
            msg = f"Not valid response: Json without key ('data') in {url}"
            msg += f"\nexpected json: {expected_json}"
            raise Exception(msg)

        if 'json' not in json_response[0]["result"]["data"]:
            msg = f"Not valid response: Json without key ('json') in {url}"
            msg += f"\nexpected json: {expected_json}"
            raise Exception(msg)

    def __check_creators_response(self, json_response: dict, url: str):
        if json_response[0] == False:
            raise Exception(
                f"Not valid response: Expected json in index 0 of the list in {url}")

        if 'result' not in json_response[0]:
            raise Exception(
                f"Not valid response: Json without key ('result') in {url}")

        if 'data' not in json_response[0]["result"]:
            raise Exception(
                f"Not valid response: Json without key ('data') in {url}")

        if 'json' not in json_response[0]["result"]["data"]:
            raise Exception(
                f"Not valid response: Json without key ('json') in {url}")

    def check_find_all_response(self, json_response: dict, url: str):
        if json_response[0] == False:
            raise Exception(
                f"Not valid response: Expected json in index 0 of the list in {url}")

        if 'result' not in json_response[0]:
            raise Exception(
                f"Not valid response: Json without key ('result') in {url}")

        if 'data' not in json_response[0]["result"]:
            raise Exception(
                f"Not valid response: Json without key ('data') in {url}")

        if 'json' not in json_response[0]["result"]["data"]:
            raise Exception(
                f"Not valid response: Json without key ('json') in {url}")

        if 'datasets' not in json_response[0]["result"]["data"]["json"]:
            raise Exception(
                f"Not valid response: Json without key ('datasets') in {url}")
