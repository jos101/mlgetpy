from abc import abstractmethod
from dataclasses import dataclass
from mlrgetpy.DataLoader import DataLoader
from typing import List


@dataclass
class DataLoaderError(DataLoader):

    @abstractmethod
    def load(self, data_file: str, attributes_list: List[str]):
        print(f"File not supported to load in DataFrame: {data_file}")
