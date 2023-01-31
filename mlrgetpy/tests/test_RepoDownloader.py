import unittest
from mlrgetpy.RepoDownloader import RepodDownloader
from mlrgetpy.DataFrameConverter import DataFrameConverter
from mlrgetpy.JsonParser import JsonParser
import pandas as pd


class test_RepoDownloader(unittest.TestCase):

    @unittest.skip("")
    def test_download(self):
        down = RepodDownloader()
        dataframe: pd.DataFrame = self.__dataframe()
        result = down.download(dataframe)

        expected = [{"id": 722,
                     "name": '722_[NATICUSdroid (Android Permissions) Dataset]'},
                    {"id": 719,
                        "name": '719_[Bengali Hate Speech Detection Dataset]'},
                    {"id": 53, "name": '53_[Iris]'}]

        self.assertListEqual(expected, result)

    # @unittest.skip("")
    def __dataframe(self) -> pd.DataFrame:
        dfc = DataFrameConverter()

        f = open('dataset.json', "r")
        json = f.read()
        f.close()

        jsp = JsonParser()
        data = jsp.encode(json)

        df = dfc.convertFromList(data[0]["result"]["data"]["json"]["datasets"])

        return df

    def test_attributes(self):
        downloader = RepodDownloader()

        result = downloader.attributes(53)
        expected = ['sepal length', 'sepal width',
                    'petal length', 'petal width', 'class']

        self.assertListEqual(expected, result)

        result = downloader.attributes(109)
        expected = ['class', 'Alcohol', 'Malicacid', 'Ash', 'Alcalinity_of_ash',
                    'Magnesium', 'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols',
                    'Proanthocyanins', 'Color_intensity', 'Hue',
                    '0D280_0D315_of_diluted_wines', 'Proline']
        self.assertListEqual(expected, result)

    def test_extract_attributes_tr(self):
        downloader = RepodDownloader()
        content = """
<html>
<head> </head>
<body>
<div class="overflow-x-auto">
    <table class="my-4 table w-full">
        <thead><tr><th>Attribute Name</th><th>Role</th><th>Type</th><th>Description</th><th>Units</th><th>Missing Values</th></tr></thead>
        <tbody>
            <tr><td>sepal length</td><td>Feature</td><td>Continuous</td><td></td><td>cm</td><td>false</td></tr>
            <tr><td>sepal width</td><td>Feature</td><td>Continuous</td><td></td><td>cm</td><td>false</td></tr>
            <tr><td>petal length</td><td>Feature</td><td>Continuous</td><td></td><td>cm</td><td>false</td></tr>
            <tr><td>petal width</td><td>Feature</td><td>Continuous</td><td></td><td>cm</td><td>false</td></tr>
            <tr><td>class</td><td>Target</td><td>Categorical</td><td>class of iris plant</td><td></td><td>false</td></tr>
        </tbody>
    </table>
</div>
</body>
</html>
        """
        result = downloader._RepodDownloader__extract_attributes_tr(content)
        expected = ['sepal length', 'sepal width',
                    'petal length', 'petal width', 'class']

        self.assertListEqual(expected, result)
