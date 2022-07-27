from dataclasses import dataclass
from mlrgetpy.datasetlist.DataSetList import DataSetList 
from mlrgetpy.datasetlist.DataSetListCache import DataSetListCache
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract

@dataclass
class DataSetListFactory():
    
    @staticmethod
    def create(type:str = 'cache'):

        object:DataSetListAbstract = None

        if type == "cache":
            object = DataSetListCache()
        elif type == "server":
            object = DataSetList()
        else:
            raise Exception("DataSetList: Type not Valid")

        return object