import unittest
import os
from mlrgetpy.downloader.DownloaderOld import DownloaderOld
from requests import Response


class Test_DownloaderOld(unittest.TestCase):

    def test_create_links_path(self):
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00298/"

        folder_name = os.path.join(
            'repo_download', '298_[Bach Choral Harmony]')
        download_new = DownloaderOld(current_url, folder_name)

        expected = [{'name_folder': os.path.join(
            'repo_download', '298_[Bach Choral Harmony]'),
            'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00298/'}]

        result = download_new.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)

        # Iris database
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"

        folder_name = os.path.join(
            'repo_download', '788_[iris]')
        download_new = DownloaderOld(current_url, folder_name)

        expected = [{'name_folder': os.path.join(
            'repo_download', '788_[iris]'),
            'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'}]

        result = download_new.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)
