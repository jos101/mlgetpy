from dataclasses import dataclass, field
from typing import List
from mlrgetpy.enums.Area import Area
import json


@dataclass
class FilterInput:
    area: List[str] = None
    keywords: List[str] = None
    order_by: str = "NumHits"
    sort: str = "desc"
    skip: str = 0
    take: int = 20

    def __post_init__(self) -> None:
        self.__check_area()
        self.__check_keywords()

        if self.area == None:
            self.area = []

        if self.keywords == None:
            self.keywords = []

    # TODO: class to json
    '''
    return a str json of the object
    {"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0, "take":700}}}'
    '''

    def str_json(self) -> str:
        json_string: str = ""

        dictionary: dict = {}
        dictionary['Area'] = self.area
        dictionary['Keywords'] = self.keywords
        dictionary['orderBy'] = self.order_by
        dictionary['sort'] = self.sort
        dictionary['skip'] = self.skip
        dictionary['take'] = self.take

        dict_parent = {}
        dict_parent['json'] = dictionary

        dict_parent_parent = {}
        dict_parent_parent['0'] = dict_parent

        json_string = json.dumps(dict_parent_parent, separators=[",", ":"])

        return json_string

    def __check_keywords(self):
        if self.keywords != None and type(self.keywords) is not list:
            raise ValueError("FilterInput class: keywords must be a list")

        if type(self.keywords) is list:
            i = 0
            for item in self.keywords:
                if type(item) is not str:
                    raise ValueError(
                        f"FilterInput class: element {i} must be type str")
                i += 1

    def __check_area(self):
        if self.area != None and type(self.area) is not list:
            raise ValueError("Filter class: area must be a list")

        # exception if any element in the list is not an Area Class
        if type(self.area) is list:
            i = 0
            for item in self.area:
                if type(item) is not str:
                    raise ValueError(
                        f"Filter class: element {i} must be an str")
                i += 1
