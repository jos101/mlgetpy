from mlrgetpy.Repository import Repository
import unittest
import pandas as pd


class TestRepository(unittest.TestCase):

    def test_load(self):
        repo = Repository()

        repo.load()
        repo.getData()

        #self.assertEqual(data["payload"]["rows"][0]["Name"], ": Simulated Data set of Iraqi tourism places")

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

    def test_showData(self):
        repo = Repository()

        repo.load()
        # repo.showData()

    def test_extractCitation(self):
        repo = Repository()
        repo.load()

        repo.extractCitation([722])

    def test_saveCitations(self):
        repo = Repository()
        repo.load()
        citations = repo.saveCitations("bibtext", 4)

        self.assertEqual(len(citations), 4, "saving bibtext")

        citations = repo.saveCitations("plaintext", 4)
        self.assertEqual(len(citations), 4, "saving plaintext")

    def test_show_data(self):
        rep = Repository()
        rep.addByIDs(IDs=[480, 296, 540, 307, 314])
        # rep.showData(limit=2)
