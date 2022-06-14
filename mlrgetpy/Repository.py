from dataclasses import dataclass

from mlrgetpy.DataFrameConverter import DataFrameConverter
from mlrgetpy.DataSetList import DataSetList
import pandas as pd


@dataclass
class Repository:
    
    def load(self) -> pd.DataFrame:
        ds : DataSetList = DataSetList()
        df : DataFrameConverter = DataFrameConverter()

        d  : dict        = ds.findAll()
        data : pd.DataFrame = df.convertFromList(d["payload"]["rows"])
        return data
    
    def download():
        NotImplemented
    
    def remove():
        NotImplemented