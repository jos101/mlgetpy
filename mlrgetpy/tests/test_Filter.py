from logging import exception
from mlrgetpy.enums.Area import Area
from mlrgetpy.Filter import Filter
from mlrgetpy.Repository import Repository
import pandas as pd
import unittest
from pandas import testing as tm

from mlrgetpy.enums.Characteristic import Characteristic


class TestFilter(unittest.TestCase):

    def test_area(self):

        # TODO: Business should search for Financial and Business
        rep = Repository()
        filter = Filter(area=[Area.BUSINESS])
        rep.load(filter)
        data: pd.DataFrame = rep.getData()

        expected = (data.Area == data.Area)
        expected[:] = True
        result = (data.Area == "Business") | (data.Area == "Financial")
        tm.assert_series_equal(result, expected)

        # TODO: test Computer science should search for Computer and Compute Science
        # TODO: test LIFE_SCIENCE should search for Life and Life Science
        # TODO: test other. false in none value

    def test_characteristic(self):
        rep = Repository()
        filter = Filter(characteristics=[Characteristic.TABULAR])
        rep.load(filter)
        data: pd.DataFrame = rep.getData()

        expected = pd.Series(
            data=True, index=data.index.tolist()).rename_axis('ID')

        result = pd.Series(
            data=False, index=data.index.tolist()).rename_axis('ID')

        for index, row in data.iterrows():
            # TODO: change to omit None values. go to and change in  Filter__find_rows_containing_type
            if row.Types == None:
                result[result.index == index] = True
                continue

            valid_items = Characteristic.TABULAR.value
            result[result.index == index] = all(
                item in valid_items for item in row.Types.split(","))

            if result[result.index == index].any() == False:
                error = f'index {index}:  Not all values in  {row.Types.split(",")} are in {valid_items}'
                raise Exception(error)

        tm.assert_series_equal(result, expected)
