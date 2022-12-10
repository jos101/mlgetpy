from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract


@dataclass
class DataSetList (DataSetListAbstract):

    def findAll(self) -> dict:

        count = super.getCount()
        response = self.request.get(self.url)

        return JsonParser().encode(response.content)
