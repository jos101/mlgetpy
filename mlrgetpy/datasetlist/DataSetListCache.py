from dataclasses import dataclass, field
import pickle
from datetime import date

from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.JsonParser import JsonParser


@dataclass
class DataSetListCache(DataSetListAbstract):

    def save_object(self, obj, filename):
        with open(filename, 'wb') as outp:
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

    def getCache(self):
        list_response = []
        try:
            with open('response.pkl', 'rb') as inp:
                list_response = pickle.load(inp)
                response = list_response[0]
        except:
            list_response = [None, None]

        return list_response

    def findAll(self) -> dict:
        response = None
        current_date = date.today()
        cached_date = None

        [cached_response, cached_date] = self.getCache()

        if cached_date == None or (current_date - cached_date).days >= 1:

            count = self.getCount()
            response = self.request.get(self.url)
        else:
            response = cached_response

        self.save_object([response, current_date], "response.pkl")

        return JsonParser().encode(response.content)[0]["result"]["data"]["json"]
