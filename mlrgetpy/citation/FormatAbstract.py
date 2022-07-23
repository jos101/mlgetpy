from dataclasses import dataclass
from ..datasetlist.DataSetListAbstract import DataSetListAbstract
import pandas as pd

@dataclass
class FormatAbstract:

    def get(self, data_set_list: DataSetListAbstract, data: pd.DataFrame) -> list:
        NotImplemented