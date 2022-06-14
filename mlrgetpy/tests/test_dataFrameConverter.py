from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.DataFrameConverter import DataFrameConverter
import unittest 


class TestDataFrameCoverter(unittest.TestCase):

    def test_convertFromList(self):
        dfc = DataFrameConverter()

        f = open('dataset.json', "r")
        json = f.read()
        f.close() 

        jsp = JsonParser()
        data = jsp.encode(json)

        df = dfc.convertFromList(data["payload"]["rows"])

        self.assertEqual(df["Name"][0], "NATICUSdroid (Android Permissions) Dataset")
        self.assertEqual(df["Name"][1], "Bengali Hate Speech Detection Dataset")

