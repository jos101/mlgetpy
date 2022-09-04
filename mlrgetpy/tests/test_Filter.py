from turtle import pd
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
        # TODO: important -> make characteristic tabular

        print("characteristic ")
        print(data.Name)
