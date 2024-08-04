import unittest
from mlrgetpy.datasetlist.DataSetListHtml import DataSetListHTML


class test_DataSetListHTML(unittest.TestCase):

    def test_findAll(self):
        dt = DataSetListHTML()
        dataset = dt.findAll()

        self.assertEqual('Iris', dataset['datasets'][0]['Name'])
        self.assertEqual('Dry Bean', dataset['datasets'][1]['Name'])

        self.assertIn('ID', dataset['datasets'][0])
        self.assertIn('Name', dataset['datasets'][0])
        self.assertIn('Abstract', dataset['datasets'][0])
        self.assertIn('Area', dataset['datasets'][0])
        self.assertIn('Task', dataset['datasets'][0])
        self.assertIn('Types', dataset['datasets'][0])
        self.assertIn('DateDonated', dataset['datasets'][0])
        self.assertIn('URLFolder', dataset['datasets'][0])
        # self.assertIn('URLReadMe', dataset['datasets'][0])
        self.assertIn('URLLink', dataset['datasets'][0])
        self.assertIn('users', dataset['datasets'][0])

    def test_dataset(self):
        dt = DataSetListHTML()
        f = open("mlrgetpy/tests/html/dataset.html", encoding="utf8")
        result = dt.dataset(f)
        f.close()

        self.assertEqual('Iris', result['datasets'][0]['Name'])
        self.assertEqual('Dry Bean Dataset', result['datasets'][1]['Name'])
        self.assertEqual('Wine', result['datasets'][2]['Name'])

    def test_count(self):
        dt = DataSetListHTML()
        f = open("mlrgetpy/tests/html/dataset.html", encoding="utf8")
        result = dt.count(f)
        f.close()

        self.assertEqual(612, result)
