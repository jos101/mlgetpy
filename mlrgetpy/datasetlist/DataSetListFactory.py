from dataclasses import dataclass
from mlrgetpy.datasetlist.DataSetList import DataSetList
from mlrgetpy.datasetlist.DataSetListCache import DataSetListCache
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.datasetlist.DataSetListHtml import DataSetListHTML
from mlrgetpy.datasetlist.DataSetListHtmlCache import DataSetListHTMLCache


@dataclass
class DataSetListFactory():

    @staticmethod
    def create(type: str = 'cache'):

        object: DataSetListAbstract = None

        if type == "cache":
            object = DataSetListCache()
        elif type == "server":
            object = DataSetList()
        elif type == "cache_html":
            object = DataSetListHTMLCache()
        elif type == "server_html":
            object = DataSetListHTML()
        else:
            raise Exception("DataSetList: Type not Valid")

        return object
