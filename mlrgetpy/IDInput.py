from dataclasses import dataclass, field
from typing import List
from mlrgetpy.enums.Area import Area
import json


@dataclass
class IDInput:
    id: int = None

    def str_json(self) -> str:
        json_string: str = ""

        dictionary: dict = {}
        dictionary['json'] = self.id

        dict_parent = {}
        dict_parent['0'] = dictionary

        json_string = json.dumps(dict_parent, separators=[",", ":"])

        return json_string
