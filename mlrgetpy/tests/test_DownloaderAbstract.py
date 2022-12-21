import unittest
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
import os


class test_DownloaderAbstract(unittest.TestCase):

    def test_make_dir_path(self):
        path = os.path.join("repo_download", "test", "sub_test")
        downloader = DownloaderAbstract("")

        # remove the path
        if os.path.exists(path):
            os.removedirs(path)

        msg = "Should create sub folders test and subtest"
        self.assertIsNone(downloader.createDirPath(path), msg)
        self.assertTrue(os.path.exists(path), msg)

        msg = "There should not be a error when the path already exist"
        self.assertIsNone(downloader.createDirPath(path), msg)
