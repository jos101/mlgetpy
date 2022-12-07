from mlrgetpy.Repository import Repository
import unittest


class TestShowData(unittest.TestCase):

    @unittest.skip("prints too much")
    def test_showData(self):
        repo = Repository()

        repo.load()
        repo.showData()

    @unittest.skip("prints too much")
    def test_show_data_box(self):
        rep = Repository()
        rep.addByIDs(IDs=[480, 298, 540, 307, 314])

        print()
        rep.showData(limit=10, type="box")

        # rep.showData(limit=10, type="table", column="Characteristic")
        # rep.showData(limit=10, type="table", column="Area")
        # rep.showData(limit=10, type="table", column="Task")
        # rep.showData(limit=10, type="table", column="DateDonated")
        # rep.showData(limit=10, type="table", column="numInstances")
        # rep.showData(limit=10, type="table", column="numAttributes")
        # rep.showData(limit=10, type="table", column="Views")
        # rep.showData(limit=10, type="table", column="Abstract")

    @unittest.skip("prints too much")
    def test_show_data_box2(self):
        # TODO: test multiple task for repository 540
        rep = Repository()
        rep.addByIDs(IDs=[480, 298, 540, 307, 314])

        print()
        rep.showData(limit=10, type="box2")
