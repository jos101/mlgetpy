from mlrgetpy.datasetlist.DataSetList import DataSetList
import unittest


class TestDataSetList(unittest.TestCase):

    # @unittest.skip("no caching")
    def test_findAll(self):
        dataSet = DataSetList()

        data: dict = dataSet.findAll()

        self.assertEqual("Iris",
                         data[0]["result"]["data"]["json"]["datasets"][0]["Name"])
        self.assertEqual("Dry Bean Dataset",
                         data[0]["result"]["data"]["json"]["datasets"][1]["Name"])

    def test_findByID(self):
        NotImplemented
        #dataSet = DataSetList()

        #data: dict = dataSet.findByName("Iris")
