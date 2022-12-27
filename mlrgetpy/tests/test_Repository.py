from mlrgetpy.Filter import Filter
from mlrgetpy.Repository import Repository
import unittest
import pandas as pd
from mlrgetpy.enums.Area import Area

from mlrgetpy.enums.AttributeType import FilterAttributeType
import os


class TestRepository(unittest.TestCase):

    def test_load(self):
        repo = Repository()

        repo.load()
        repo.getData()

        # self.assertEqual(data["payload"]["rows"][0]["Name"], ": Simulated Data set of Iraqi tourism places")

    # @unittest.skip("")
    def test_addByIDs(self):
        repo = Repository()

        repo.addByIDs([556])
        repo.addByIDs([558])
        self.assertEqual(repo.getData().filter(items=[556], axis="index")[
                         "Name"].values[0], ": Simulated Data set of Iraqi tourism places")
        self.assertEqual(repo.getData().filter(items=[558], axis="index")[
                         "Name"].values[0], "Monolithic Columns in Troad and Mysia Region")
        self.assertEqual(repo.getData().shape[0], 2)

        repo.addByIDs([556])
        self.assertEqual(repo.getData(
        ).shape[0], 2, msg="Added a existed index must not change the shape of the dataframe")

        repo = Repository()
        repo.load()
        count = repo.getData().shape[0]
        repo.addByIDs([556])
        self.assertEqual(repo.getData(
        ).shape[0], count, msg="addByIds after load must not alter the row count")

    # @unittest.skip("")
    def test_extractCitation(self):
        repo = Repository()
        repo.load()

        repo.extractCitation([722])

    # @unittest.skip("")
    def test_saveCitations(self):
        repo = Repository()
        repo.load()
        citations = repo.saveCitations("bibtext", 4)

        self.assertEqual(len(citations), 4, "saving bibtext")

        citations = repo.saveCitations("plaintext", 4)
        self.assertEqual(len(citations), 4, "saving plaintext")

    # @unittest.skip("")
    def test_add_data_set(self):
        rep = Repository()
        rep.add_data_set(Filter(area=[Area.BUSINESS]))
        rep.add_data_set(Filter(area=[Area.COMPUTER_SCIENCE]))

        data = rep.getData().sort_index()
        # print(f"\n{data.shape[0]}")
        pd.set_option('display.max_rows', None)
        # print(data[["Area", "Name"]])
        self.assertEqual(data.shape[0], 272)

    # @unittest.skip("")
    def test_share(self):
        rep = Repository()
        rep.addByIDs(IDs=[480, 296, 540, 307, 314])

        expected: str = "rep = New Repository()\n"
        expected += "rep.addByIDs([480, 296, 540, 307, 314])"

        self.assertEqual(
            rep.share(), expected)

    def test_unzip(self):
        rep = Repository()
        extract_path = os.path.join('mlrgetpy', 'tests', 'zip')
        file = os.path.join(extract_path, 'hello.py')

        if os.path.exists(file):
            os.remove(file)

        zip_path = os.path.join(extract_path, 'hello.zip')
        rep.unzip(zip_path, extract_path)

        result = os.path.exists(file)
        self.assertTrue(result)

        if os.path.exists(file):
            os.remove(file)
