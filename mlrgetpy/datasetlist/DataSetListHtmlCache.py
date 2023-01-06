from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.FilterInput import FilterInput
from mlrgetpy.log.ConfigLog import ConfigLog
from bs4 import BeautifulSoup
import json
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.datasetlist.DataSetListHtml import DataSetListHTML
from datetime import date
import pickle


@dataclass
class DataSetListHTMLCache (DataSetListAbstract):
    __dataset_html = DataSetListHTML()
    __file_cache = 'response-html.pkl'

    def findAll(self) -> dict:
        current_date = date.today()
        cached_date = None

        [cached_response, cached_date] = self.getCache()

        if cached_date == None or (current_date - cached_date).days >= 100:
            datasets_json = self.__dataset_html.findAll()
            self.save_object([datasets_json, current_date], self.__file_cache)
        else:
            ConfigLog.log.write_caching(self.__file_cache)
            datasets_json = cached_response

        return datasets_json

    def getCache(self):
        list_response = []
        try:
            with open(self.__file_cache, 'rb') as inp:
                list_response = pickle.load(inp)
                response = list_response[0]
        except:
            list_response = [None, None]

        return list_response

    def save_object(self, obj, filename):
        with open(filename, 'wb') as outp:
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
