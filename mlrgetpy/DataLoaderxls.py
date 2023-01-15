from abc import abstractmethod
from dataclasses import dataclass
from mlrgetpy.DataLoader import DataLoader
from typing import List
import pandas as pd

from mlrgetpy.util.ListUtil import ListUtil


@dataclass
class DataLoaderxls(DataLoader):

    @abstractmethod
    def load(self, data_file: str, attributes_list: List[str]):
        df: pd.DataFrame

        if (attributes_list and ListUtil.has_duplicated(attributes_list) == False):
            # TODO: log of this print
            #print(f"datafile: {data_file}")
            #print(f"attribute list: {attributes_list}")
            df = pd.read_excel(data_file, header=None, names=attributes_list)
        else:
            df = pd.read_excel(data_file)

        return df
