import unittest
from mlrgetpy.URLManager import URLManager
import os


class test_URLManager(unittest.TestCase):

    def test_folder_from_link(self):
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"
        folder_name = os.path.join('repo_download', '53_[iris]')

        expected = 'cat'

        result = URLManager.folder_from_link('http://foo.com/bar/cat/')
        msg = "Forward slash at the end of the link"
        self.assertEqual(expected, result, msg)

        result = URLManager.folder_from_link('http://foo.com/bar/cat')
        msg = "There is not a forward slash at the end of the link"
        self.assertEqual(expected, result)

    def test_remove_last_forward_slash(self):
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"
        folder_name = os.path.join('repo_download', '53_[iris]')

        result = URLManager.remove_last_forward_slash(
            'http://foo.com/bar/cat.txt/')
        expected = 'http://foo.com/bar/cat.txt'
        msg = 'Last Character is a forward slash. Should strip forward slash'
        self.assertEqual(expected, result, msg)

        result = URLManager.remove_last_forward_slash(
            'http://foo.com/bar/cat.txt')
        expected = 'http://foo.com/bar/cat.txt'
        msg = 'The last character is not a forward slash'
        self.assertEqual(expected, result, msg)

    def test_create_name_folder(self):
        path = os.path.join('repo_download')
        result = URLManager.create_name_folder(path, 'http://foo/bar')
        expected = os.path.join('repo_download', 'bar')
        self.assertEqual(expected, result)

        path = os.path.join('repo_download', 'goo')
        result = URLManager.create_name_folder(path, 'http://foo/bar/')
        expected = os.path.join('repo_download', 'goo', 'bar')
        self.assertEqual(expected, result)

        path = os.path.join('repo_download', 'goo', 'zoo')
        result = URLManager.create_name_folder(path, 'http://foo/bar/cat.txt')
        expected = os.path.join('repo_download', 'goo', 'zoo', 'cat.txt')
        self.assertEqual(expected, result)
