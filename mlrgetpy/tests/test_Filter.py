from logging import exception
from mlrgetpy.enums.Area import Area
from mlrgetpy.Filter import Filter
from mlrgetpy.Repository import Repository
import pandas as pd
import unittest
from pandas import testing as tm

from mlrgetpy.enums.Characteristic import Characteristic


class TestFilter(unittest.TestCase):

    def test_area_int(self):

        with self.assertRaises(ValueError, msg="Must be an Area Class"):
            filter = Filter(area="Science")

        with self.assertRaises(ValueError, msg="Must be a List"):
            filter = Filter(area=Area.COMPUTER_SCIENCE)

        with self.assertRaises(ValueError, msg="Must be an List of Area Class"):
            filter = Filter(area=["Science"])

        with self.assertRaises(ValueError, msg="Must be an List of Area Class"):
            filter = Filter(area=[Area.BUSINESS, "Game", Area.LAW])

        filter = Filter(area=[Area.BUSINESS])
        self.assertEqual(Filter, type(filter), msg="One element")

        filter = Filter(area=[Area.BUSINESS, Area.ENGINEERING])
        self.assertEqual(Filter, type(filter), msg="Two element")

        filter = Filter(area=[Area.BUSINESS, Area.ENGINEERING, Area.LAW])
        self.assertEqual(Filter, type(filter))

    def test_characteristic_int(self):

        with self.assertRaises(ValueError, msg="Must be an Characteristic Class"):
            filter = Filter(characteristics="Tabular")

        with self.assertRaises(ValueError, msg="Must be a List"):
            filter = Filter(characteristics=Characteristic.TABULAR)

        with self.assertRaises(ValueError, msg="Must be an List of Characteristic Class"):
            filter = Filter(characteristics=["Tabular"])

        with self.assertRaises(ValueError, msg="Must be an List of Characteristic Class"):
            filter = Filter(characteristics=[
                            Characteristic.TABULAR, "Image", Characteristic.SEQUENTIAL])

        filter = Filter(characteristics=[Characteristic.TABULAR])
        self.assertEqual(Filter, type(filter), msg="One element")

        filter = Filter(characteristics=[
                        Characteristic.TABULAR, Characteristic.SEQUENTIAL])
        self.assertEqual(Filter, type(filter), msg="Two element")

        filter = Filter(characteristics=[
                        Characteristic.TABULAR, Characteristic.SEQUENTIAL, Characteristic.TIME_SERIES])
        self.assertEqual(Filter, type(filter))

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

        # test Computer science should search for Computer and Compute Science
        rep = Repository()
        filter = Filter(area=[Area.COMPUTER_SCIENCE])
        rep.load(filter)

        data: pd.DataFrame = rep.getData()
        result: pd.Series = (data.Area == 'Computer') | (
            data.Area == 'Computer Science')

        expected: pd.Series = pd.Series(
            data=True, index=data.index.tolist(), name="Area").rename_axis("ID")

        tm.assert_series_equal(result, expected)

        # test LIFE_SCIENCES should search for Life and Life Sciences
        rep = Repository()
        filter = Filter(area=[Area.LIFE_SCIENCES])
        rep.load(filter)

        data: pd.DataFrame = rep.getData()
        result: pd.Series = data.Area.isin(['Life', 'Life Sciences'])

        expected: pd.Series = pd.Series(
            data=True, index=data.index.tolist(), name="Area").rename_axis("ID")

        tm.assert_series_equal(result, expected)

        # test other. false in none value
        rep = Repository()
        filter = Filter(area=[Area.OTHER])
        rep.load(filter)

        data: pd.DataFrame = rep.getData()
        result: pd.Series = (data.Area == 'Other')

        expected: pd.Series = pd.Series(
            data=True, index=data.index.tolist(), name="Area").rename_axis("ID")

        tm.assert_series_equal(result, expected)

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
