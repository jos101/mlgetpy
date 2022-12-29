import unittest
from mlrgetpy.RepoDownloader import RepodDownloader
from mlrgetpy.DataFrameConverter import DataFrameConverter
from mlrgetpy.JsonParser import JsonParser
import pandas as pd


class test_RepoDownloader(unittest.TestCase):

    def test_download(self):
        down = RepodDownloader()
        dataframe: pd.DataFrame = self.__dataframe()
        result = down.download(dataframe)

        expected = ['722_[NATICUSdroid (Android Permissions) Dataset]',
                    '719_[Bengali Hate Speech Detection Dataset]',
                    '53_[Iris]']

        self.assertListEqual(expected, result)

    def __dataframe(self) -> pd.DataFrame:
        dfc = DataFrameConverter()

        f = open('dataset.json', "r")
        json = f.read()
        f.close()

        jsp = JsonParser()
        data = jsp.encode(json)

        df = dfc.convertFromList(data[0]["result"]["data"]["json"]["datasets"])

        return df
