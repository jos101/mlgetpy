from dataclasses import dataclass
from mlgetpy.JsonParser import JsonParser 
from mlgetpy.RequestHelper import RequestHelper


@dataclass
class DataSetList:
    
    request = RequestHelper()
    
    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find?offset=0&limit=2"
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/53"
    
    def findAll(self) -> dict:
        
        response = self.request.get(self.url)

        return JsonParser().encode( response.text )
    
    def findByName(self, name:str) -> dict:
        
        request = RequestHelper()
        response = self.request.get(self.url2)
        
        return JsonParser().encode( response.text )
        
    