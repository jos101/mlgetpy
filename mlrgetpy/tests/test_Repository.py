from mlrgetpy.Repository import Repository
import unittest 
import pandas as pd

class TestRepository(unittest.TestCase):

    def test_find(self):
        repo = Repository() 

        data: pd.DataFrame = repo.find()

        print(data)

        #self.assertEqual(data["payload"]["rows"][0]["Name"], ": Simulated Data set of Iraqi tourism places")
        