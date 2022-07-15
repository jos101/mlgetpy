from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser 
from mlrgetpy.RequestHelper import RequestHelper
from datetime import date

@dataclass
class DataSetListAbstract:
    
    request = RequestHelper()
    
    __count:int = field(init=False)

    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find" #?offset=0&limit=2
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"

    creator = "https://archive-beta.ics.uci.edu/api/creators/pk/722"
    
    def getCount(self) -> int:
        response = self.request.get(self.url)
        return JsonParser().encode( response.text )["payload"]["count"]

    def findAll(self):
        NotImplemented