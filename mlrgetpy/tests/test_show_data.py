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
        rep = Repository()
        rep.addByIDs(IDs=[480, 298, 540, 307, 314])

        print()
        rep.showData(limit=10, type="box2")

    '''
    test a repository with multiple tasks in the box2. 
    The task should print below when there is no space 
    in the cell
    '''
    @unittest.skip("prints too much")
    def test_show_data_multiple_task_box2(self):
        rep = Repository()
        rep.addByIDs(IDs=[540])
        print()
        rep.showData(limit=10, type="box2")
