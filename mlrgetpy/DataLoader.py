from abc import abstractmethod
from dataclasses import dataclass

from typing import List


@dataclass
class DataLoader:

    @abstractmethod
    def load(self, datafile: str, attributes_list: List[str]):
        NotImplemented
