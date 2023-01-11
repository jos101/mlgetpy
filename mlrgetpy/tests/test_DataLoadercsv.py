import unittest
from mlrgetpy.DataLoaderCSV import DataLoaderCSV
import os


class test_DataLoaderCSV(unittest.TestCase):

    def test_load(self):

        dl = DataLoaderCSV()
        df = dl.load(os.path.join("mlrgetpy", "tests",
                     "data", "file-with-header.csv"), [])

        print()
        print(df)

        df = dl.load(os.path.join("mlrgetpy", "tests",
                     "data", "file.csv"), ["one", "two", "three", "four", "five", "six"])
        print()
        print(df)
