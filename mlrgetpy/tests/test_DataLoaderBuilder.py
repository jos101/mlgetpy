from mlrgetpy.DataLoader import DataLoader
from mlrgetpy.DataLoaderCSV import DataLoaderCSV
from mlrgetpy.DataLoaderError import DataLoaderError
from mlrgetpy.DataLoaderxls import DataLoaderxls
from mlrgetpy.DataLoaderBuilder import DataLoaderBuilder
import unittest


class test_DataLoaderBuilder(unittest.TestCase):

    def test_create(self):

        dataloader = DataLoaderBuilder.create("iris.data")
        self.assertEqual(True, isinstance(dataloader, DataLoaderCSV))

        dataloader = DataLoaderBuilder.create("iris.DATA")
        self.assertEqual(True, isinstance(dataloader, DataLoaderCSV))

        dataloader = DataLoaderBuilder.create("iris.DAT")
        self.assertEqual(True, isinstance(dataloader, DataLoaderCSV))

        dataloader = DataLoaderBuilder.create("iris.xls")
        self.assertEqual(True, isinstance(dataloader, DataLoaderxls))

        dataloader = DataLoaderBuilder.create("iris.xlsx")
        self.assertEqual(True, isinstance(dataloader, DataLoaderxls))

        dataloader = DataLoaderBuilder.create("IRIS.XLSX")
        self.assertEqual(True, isinstance(dataloader, DataLoaderxls))

        dataloader = DataLoaderBuilder.create("IRIS.XLS")
        self.assertEqual(True, isinstance(dataloader, DataLoaderxls))

        dataloader = DataLoaderBuilder.create("IRIS.zip")
        self.assertEqual(True, isinstance(dataloader, DataLoaderError))
