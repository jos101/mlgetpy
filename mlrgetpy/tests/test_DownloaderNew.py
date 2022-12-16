import unittest
from mlrgetpy.downloader.DownloaderNew import DownloaderNew


class Test_DownloaderNew(unittest.TestCase):

    def test_create_links_path(self):
        parent_url = "/static/ml/datasets"
        current_url = "https://archive-beta.ics.uci.edu/static/ml/datasets/713"
        folder_name = "repo_download\713_[Auction Verification]"
        download_new = DownloaderNew(current_url, folder_name)

        expected = [{'url': 'https://archive-beta.ics.uci.edu/static/ml/datasets/713',
                     'name_folder': 'repo_download\713_[Auction Verification]'},
                    {'url': 'https://archive-beta.ics.uci.edu/static/ml/datasets/713/Graphics',
                     'name_folder': 'repo_download\713_[Auction Verification]\Graphics'}]

        result = download_new.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)
