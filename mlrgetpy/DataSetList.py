from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser 
from mlrgetpy.RequestHelper import RequestHelper


@dataclass
class DataSetList:
    
    request = RequestHelper()
    
    __count:int = field(init=False)

    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find" #?offset=0&limit=2
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"
    
    def getCount(self) -> int:
        response = self.request.get(self.url)
        return JsonParser().encode( response.text )["payload"]["count"]


    def findAll(self) -> dict:
        count = self.getCount() 
        response = self.request.get(self.url + f'?limit={count}')

        return JsonParser().encode( response.text )