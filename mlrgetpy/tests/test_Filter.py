from logging import exception
from unittest import result
from mlrgetpy.enums.Area import Area
from mlrgetpy.Filter import Filter
from mlrgetpy.Repository import Repository
import pandas as pd
import unittest
from pandas import testing as tm
from mlrgetpy.enums.AttributeType import FilterAttributeType

from mlrgetpy.enums.Characteristic import Characteristic
from mlrgetpy.enums.Task import Task


class TestFilter(unittest.TestCase):

    def test_area_init(self):

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

    def test_characteristic_init(self):

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
        df = pd.DataFrame({'ID': [25, 78, 86,
                                  93, 102, 124,
                                  128, 132, 135],
                           'Name': ['data1', 'data2', 'data3',
                                    'data4', 'data5', 'data6',
                                    'data7', 'data8', 'data9'],
                           'Area': ['Financial', 'Computer', 'Business',
                                    'Computer Science', 'Life', 'Life Sciences',
                                    'Other', None, 'Area1']})
        df = df.set_index('ID')

        # Business should search for Financial and Business
        filter = Filter(area=[Area.BUSINESS])
        result = filter.filter(df)
        self.assertEqual([25, 86], result.index.tolist())

        # test Computer science should search for Computer and Compute Science
        # in the online repository mistakenly just search for
        # "Computer" and not for "Computer Science"
        filter = Filter(area=[Area.COMPUTER_SCIENCE])
        result = filter.filter(df)
        self.assertEqual([78, 93], result.index.tolist())

        # test LIFE_SCIENCES should search for Life and Life Sciences
        filter = Filter(area=[Area.LIFE_SCIENCES])
        result = filter.filter(df)
        self.assertEqual([102, 124], result.index.tolist())

        # test other. false in none value
        filter = Filter(area=[Area.OTHER])
        result = filter.filter(df)
        self.assertEqual([128], result.index.tolist())

    def test_characteristic(self):

        df = pd.DataFrame({'ID': [25, 78, 86,
                                  93, 102, 124,
                                  128, 132, 135,
                                  137, 139, 142,
                                  145, 147],
                           'Name': ['data1', 'data2', 'data3',
                                    'data4', 'data5', 'data6',
                                    'data7', 'data8', 'data9',
                                    'data10', 'data11', 'data12',
                                    'data13', 'data14'],
                           'Types': ['Tabular', 'Multivariate', 'Univariate',
                                     'Sequential', 'Time-Series', 'Sequential',
                                     'Other', None, 'Tabular,Multivariate',
                                     'Tabular,Univariate', 'Univariate, Multivariate', 'Univariate,Multivariate',
                                     'Tabular,Multivariate', 'Multivariate,Tabular']})
        df = df.set_index('ID')

        # TABULAR: str = ["Tabular", "Multivariate", "Univariate"]
        # The characteristic in id 139 is not valid due to a space
        filter = Filter(characteristics=[Characteristic.TABULAR])
        result = filter.filter(df)
        self.assertEqual([25, 78, 86, 135, 137, 142, 145, 147],
                         result.index.tolist())

    def test_task(self):
        # test data
        df = pd.DataFrame({'ID': [25, 78, 86, 93, 102],
                           'Name': ['data1', 'data2', 'data3', 'data4', 'data5'],
                           'Task': ['Classification', 'Classification', 'Regression', 'Clustering', 'Other']})
        df = df.set_index('ID')

        # test classification
        filter = Filter(task=Task.CLASSIFICATION)
        result = filter.filter(df)
        self.assertEqual([25, 78], result.index.tolist())

        # test Regression
        filter = Filter(task=Task.REGRESSION)
        result = filter.filter(df)
        self.assertEqual([86], result.index.tolist())

        # test clustering
        filter = Filter(task=Task.CLUSTERING)
        result = filter.filter(df)
        self.assertEqual([93], result.index.tolist())

        # test Other
        filter = Filter(task=Task.OTHER)
        result = filter.filter(df)
        self.assertEqual([102], result.index.tolist())

    def test_attribute_type(self):

        df = pd.DataFrame({'ID': [25, 78, 86,
                                  93, 102, 124,
                                  128, 132, 135,
                                  137, 139, 142,
                                  145, 147],
                           'Name': ['data1', 'data2', 'data3',
                                    'data4', 'data5', 'data6',
                                    'data7', 'data8', 'data9',
                                    'data10', 'data11', 'data12',
                                    'data13', 'data14'],
                           'AttributeTypes': ['Integer', 'Real', 'Integer,Real',
                                              'Categorical', 'Time-Series', 'Sequential',
                                              'Categorical', None, 'Integer,Real',
                                              'Integer,Categorical', 'Real,Categorical', 'Real, Categorical',
                                              'Tabular,Multivariate', 'Multivariate,Tabular']})
        df = df.set_index('ID')

        filter = Filter(attribute_type=FilterAttributeType.NUMERICAL)
        result = filter.filter(df)
        self.assertEqual([25, 78, 86, 135, 137, 139, 142],
                         result.index.tolist())

        filter = Filter(attribute_type=FilterAttributeType.CATEGORICAL)
        result = filter.filter(df)
        self.assertEqual([93, 128, 137, 139, 142], result.index.tolist())

        # There should be at least one attribute type Numerical and one Categorical
        # every attribute type is separated by comma and may contain space (id 142)
        filter = Filter(attribute_type=FilterAttributeType.MIXED)
        result = filter.filter(df)
        self.assertEqual([137, 139, 142],
                         result.index.tolist())
