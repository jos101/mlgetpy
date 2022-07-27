from abc import abstractmethod
from dataclasses import dataclass, field
from urllib import response
from mlrgetpy.JsonParser import JsonParser 
from mlrgetpy.RequestHelper import RequestHelper
from datetime import date

@dataclass
class DataSetListAbstract:
    
    request = RequestHelper()
    
    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find" #?offset=0&limit=2
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"

    creator_url = "https://archive-beta.ics.uci.edu/api/creators/pk/"
    
    def getCount(self) -> int:
        response = self.request.get(self.url)
        return JsonParser().encode( response.text )["payload"]["count"]

    def findAll(self):
        NotImplemented
    
    def getCreators(self, id:int) -> list:
        response = self.request.get(self.creator_url + str(id))
        return JsonParser().encode( response.text )["payload"]


