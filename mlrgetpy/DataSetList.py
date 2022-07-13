from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser 
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.CacheDataSetList import CacheDataSetList
import pickle
import datetime
from datetime import date

@dataclass
class DataSetList:
    
    request = RequestHelper()
    
    __count:int = field(init=False)

    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find" #?offset=0&limit=2
    url2 = "https://archive-beta.ics.uci.edu/api/datasets-donated/pk/"

    creator = "https://archive-beta.ics.uci.edu/api/creators/pk/722"
    
    def getCount(self) -> int:
        response = self.request.get(self.url)
        return JsonParser().encode( response.text )["payload"]["count"]


    def findAll(self) -> dict:

        cache:CacheDataSetList = CacheDataSetList()

        response = None
        current_date = date.today()
        cached_date = None

        [cached_response, cached_date] = cache.getCache()

        if cached_date == None or (current_date - cached_date).days >= 1 :

            count = self.getCount() 
            response = self.request.get(self.url + f'?limit={count}')
        else:
            response = cached_response

        cache.save_object([response, current_date], "response.pkl")

        return JsonParser().encode( response.content )
    
    def save_object(self, obj, filename):
        with open(filename, 'wb') as outp:  # Overwrites any existing file.
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)