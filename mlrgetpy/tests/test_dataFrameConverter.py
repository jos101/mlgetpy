from cmath import nan
from mlrgetpy.JsonParser import JsonParser
from mlrgetpy.DataFrameConverter import DataFrameConverter
import unittest 
import pandas as pd
import numpy as np

class TestDataFrameCoverter(unittest.TestCase):

    def test_convertFromList(self):
        dfc = DataFrameConverter()

        f = open('dataset.json', "r")
        json = f.read()
        f.close() 

        jsp = JsonParser()
        data = jsp.encode(json)

        df = dfc.convertFromList(data["payload"]["rows"])

        self.assertEqual(df["Name"][722], "NATICUSdroid (Android Permissions) Dataset")
        self.assertEqual(df["Name"][719], "Bengali Hate Speech Detection Dataset")

        self.assertEqual(df["user_user"][722], "akshay.mathur@rockets.utoledo.edu")
        self.assertEqual(df["user_firstName"][722], "Akshay")
        self.assertEqual(df["user_lastName"][722], "Mathur")
        
        self.assertEqual(df["tabular"][719], None)
        self.assertEqual(df["numAttributes"][719], 0)



