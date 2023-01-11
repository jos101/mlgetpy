import unittest
from mlrgetpy.DataLoaderxls import DataLoaderxls
import os


class test_DataLoaderxls(unittest.TestCase):

    def test_load(self):

        dl = DataLoaderxls()

        df = dl.load(os.path.join("mlrgetpy", "tests",
                                  "data", "file-with-headers.xlsx"), [])
        print()
        print(df)

        df = dl.load(os.path.join("mlrgetpy", "tests", "data", "file-no-headers.xlsx"),
                     ["sepal length", "sepal width", "petal length", "petal width", "class"])
        print()
        print(df)
