from dataclasses import dataclass

from mlrgetpy.citation.FormatAbstract import FormatAbstract
from ..datasetlist.DataSetListAbstract import DataSetListAbstract
import pandas as pd

@dataclass
class PlainCitation(FormatAbstract):

    def get(self, data_set_list: DataSetListAbstract, data: pd.DataFrame) -> list:

        NotImplemented