from dataclasses import dataclass
import json


@dataclass
class JsonParser:

    def encode(self, text: str) -> dict:
        data = json.loads(text)

        return data
