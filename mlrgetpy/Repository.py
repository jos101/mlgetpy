from dataclasses import dataclass, field

from sympy import Not
from mlrgetpy.DataFrameConverter import DataFrameConverter
from mlrgetpy.DataSetList import DataSetList
import pandas as pd


@dataclass
class Repository:
    
    __data : pd.DataFrame = field(init=False, repr=False)
    __data_set_list : DataSetList = field(init=False, repr=False)
    __dfc : DataFrameConverter = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__data_set_list = DataSetList()
        self.__dfc = DataFrameConverter()

    def load(self) -> None:
        d  : dict        = self.__data_set_list.findAll()
        data : pd.DataFrame = self.__dfc.convertFromList(d["payload"]["rows"])
        self.__data = data
    
    def getData(self) -> pd.DataFrame:
        return self.__data.copy()

    def addByID(self, ID:int) -> None:
        NotImplemented

    def removeByIndex(self, indexes: list) -> None:
        self.__data = self.__data.drop(indexes)

    def download() -> None :
        NotImplemented
    
    def remove():
        NotImplemented