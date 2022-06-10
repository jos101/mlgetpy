from mlgetpy.DataSetList import DataSetList
import unittest 

class TestJsonParser(unittest.TestCase):

    def test_findAll(self):
        dataSet = DataSetList() 

        data: dict = dataSet.findAll()

        self.assertEqual(data["payload"]["rows"][0]["Name"], ": Simulated Data set of Iraqi tourism places")
        self.assertEqual(data["payload"]["rows"][1]["Name"], "2.4 GHZ Indoor Channel Measurements")

    def test_findByName(self):
        dataSet = DataSetList()

        data: dict = dataSet.findByName("Iris")
