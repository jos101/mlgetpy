from mlrgetpy.Filter import Filter
from mlrgetpy.Repository import Repository
import unittest
import pandas as pd
from mlrgetpy.enums.Area import Area

from mlrgetpy.enums.AttributeType import FilterAttributeType


class TestRepository(unittest.TestCase):

    # TODO: download
    def test_download(self):
        rep = Repository()
        #rep.addByIDs(IDs=[480, 296, 540, 307, 314])
        #rep.addByIDs(IDs=[296, 540, 307, 314])

        # uses folders in old_url (432, 442)
        # rep.addByIDs(IDs=[432])
        # rep.addByIDs(IDs=[442])
        # uses folders in old_url (516)
        #rep.addByIDs(IDs=[516, 296, 540, 307, 314])

        # 713 uses https://archive-beta.ics.uci.edu/api/static/ml/datasets/713
        # and subfolder
        # 480 uses url https://archive.ics.uci.edu/ml/machine-learning-databases/00480/
        # 692 uses url https://archive-beta.ics.uci.edu/api/static/ml/datasets/692
        rep.addByIDs(IDs=[713, 480, 692])

        rep.download()

    def test_load(self):
        repo = Repository()

        repo.load()
        repo.getData()

        # self.assertEqual(data["payload"]["rows"][0]["Name"], ": Simulated Data set of Iraqi tourism places")

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
        # print()

        # rep.showData(limit=10, type="box")

        # rep.showData(limit=10, type="table", column="Characteristic")
        # rep.showData(limit=10, type="table", column="Area")
        # rep.showData(limit=10, type="table", column="Task")
        # rep.showData(limit=10, type="table", column="DateDonated")
        # rep.showData(limit=10, type="table", column="numInstances")
        # rep.showData(limit=10, type="table", column="numAttributes")
        # rep.showData(limit=10, type="table", column="Views")
        # rep.showData(limit=10, type="table", column="Abstract")
#

    def test_add_data_set(self):
        rep = Repository()
        rep.add_data_set(Filter(area=[Area.BUSINESS]))
        rep.add_data_set(Filter(area=[Area.COMPUTER_SCIENCE]))

        data = rep.getData().sort_index()
        # print(f"\n{data.shape[0]}")
        pd.set_option('display.max_rows', None)
        # print(data[["Area", "Name"]])
        self.assertEqual(data.shape[0], 272)

    def test_share(self):
        rep = Repository()
        rep.addByIDs(IDs=[480, 296, 540, 307, 314])

        expected: str = "rep = New Repository()\n"
        expected += "rep.addByIDs([480, 296, 540, 307, 314])"

        self.assertEqual(
            rep.share(), expected)
