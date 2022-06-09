from dataclasses import dataclass
import json

from numpy import array


@dataclass
class JsonParser:

    def encode(self, text: str) -> array:

        data = json.loads(text)

        return data
