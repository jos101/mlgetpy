from dataclasses import dataclass, field
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.FilterInput import FilterInput
from mlrgetpy.log.ConfigLog import ConfigLog


@dataclass
class DataSetList (DataSetListAbstract):

    def findAll(self) -> dict:
        count = self.getCount()
        filter_input = FilterInput(take=count)

        ConfigLog.log.write_url(self.get_url(filter_input))
        response = self.request.get(self.get_url(filter_input))
        json_object = JsonParser().encode(response.content)

        self.check_find_all_response(
            json_object, self.get_url(filter_input))

        return json_object
