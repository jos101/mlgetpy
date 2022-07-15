from dataclasses import dataclass
from mlrgetpy.datasetlist.DataSetList import DataSetList 
from mlrgetpy.datasetlist.CacheDataSetList import CacheDataSetList
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract

@dataclass
class DataSetListFactory():
    
    @staticmethod
    def create(type:str = 'CACHE'):

        object:DataSetListAbstract = None

        if type == "CACHE":
            object = CacheDataSetList()
        elif type == "SERVER":
            object = DataSetList()
        else:
            raise Exception("DataSetList: Type not Valid")

        return object