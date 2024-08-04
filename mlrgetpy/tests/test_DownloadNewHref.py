import unittest
from mlrgetpy.downloader.DownloaderNewHref import DownloaderNewHref


class Test_DownloadNewHref(unittest.TestCase):

    def test_init(self):
        # valid values for the contructor
        href_url = "https://archive.ics.uci.edu/static/public/713/auction+verification.zip"
        DownloaderNewHref(href_url=href_url,
                          repo_name="713_[Auction Verification]")

        with self.assertRaises(ValueError, msg="Href not valid"):
            href_url = "https://archive-beta.ics.uci.edu"
            DownloaderNewHref(href_url=href_url,
                              repo_name="713_[Auction Verification]")

        with self.assertRaises(ValueError, msg="repo_name not valid"):
            href_url = "https://archive-beta.ics.uci.edu/static/ml/datasets/713/auction+verification.zip"
            DownloaderNewHref(href_url=href_url,
                              repo_name="Foo")
