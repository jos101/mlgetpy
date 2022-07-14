from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser 
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.CacheDataSetList import CacheDataSetList
from mlrgetpy.DataSetListAbstract import DataSetListAbstract
import pickle
import datetime
from datetime import date

@dataclass
class DataSetList (DataSetListAbstract):
    
    
    def getCount(self) -> int:
        response = self.request.get(self.url)
        return JsonParser().encode( response.text )["payload"]["count"]


    def findAll(self) -> dict:

        count = self.getCount() 
        response = self.request.get(self.url + f'?limit={count}')

        return JsonParser().encode( response.content )
    