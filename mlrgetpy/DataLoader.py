from abc import abstractmethod
from dataclasses import dataclass

from typing import List


@dataclass
class DataLoader:

    @abstractmethod
    def load(self, datafile: str, attributes_list: List[str]):
        NotImplemented

    def __has_duplicated(self, list: List) -> bool:
        """Check if the list has duplicated items

        Args:
            list (List): the list with values

        Returns:
            bool: True is the list has duplicated itmes, false if every item is unique
        """
        return len(list) != len(set(list))
