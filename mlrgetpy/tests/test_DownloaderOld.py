import unittest
import os
from mlrgetpy.downloader.DownloaderOld import DownloaderOld
from requests import Response


class Test_DownloaderOld(unittest.TestCase):

    def test_create_links_path(self):
        # Bach Choral Harmony database
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00298/"

        folder_name = os.path.join(
            'repo_download', '298_[Bach Choral Harmony]')
        download_old = DownloaderOld(current_url, folder_name)

        expected = [{'name_folder': os.path.join(
            'repo_download', '298_[Bach Choral Harmony]'),
            'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00298/'}]

        result = download_old.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)

        # Iris database
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"

        folder_name = os.path.join('repo_download', '53_[iris]')
        download_old = DownloaderOld(current_url, folder_name)

        expected = [{'name_folder': os.path.join(
            'repo_download', '53_[iris]'),
            'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'}]

        result = download_old.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)

    def test_get_links(self):
        # Iris
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"
        folder_name = os.path.join('repo_download', '53_[iris]')
        download_old = DownloaderOld(current_url, folder_name)

        response: Response = Response()
        response.status_code = 200
        string = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /ml/machine-learning-databases/iris</title>
 </head>
 <body>
<h1>Index of /ml/machine-learning-databases/iris</h1>
<ul><li><a href="/ml/machine-learning-databases/"> Parent Directory</a></li>
<li><a href="Index"> Index</a></li>
<li><a href="bezdekIris.data"> bezdekIris.data</a></li>
<li><a href="iris.data"> iris.data</a></li>
<li><a href="iris.names"> iris.names</a></li>
</ul>
<address>Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips SVN/1.7.14 Phusion_Passenger/4.0.53 mod_perl/2.0.11 Perl/v5.16.3 Server at archive.ics.uci.edu Port 443</address>
</body></html>
'''
        string_bytes = bytes(string, 'utf-8')
        response._content = string_bytes
        expected = ['/ml/machine-learning-databases/', 'Index',
                    'bezdekIris.data', 'iris.data', 'iris.names']
        result = download_old.getLinks(response)
        self.assertListEqual(expected, result)

    def test_create_links_path(self):
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"
        folder_name = os.path.join('repo_download', '53_[iris]')
        download_old = DownloaderOld(current_url, folder_name)

        expected = [{'name_folder': 'repo_download\\53_[iris]',
                     'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'}]

        result = download_old.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)

        # test with subfolders
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00432/"
        folder_name = os.path.join(
            'repo_download', '432_[News Popularity in Multiple Social Media Platforms]')
        download_old = DownloaderOld(current_url, folder_name)

        expected = [{'name_folder': folder_name,
                     'url': current_url},

                    {'name_folder': os.path.join(folder_name, 'Data'),
                     'url': 'https://archive.ics.uci.edu/ml/machine-learning-databases/00432/Data/'}
                    ]

        result = download_old.create_links_path(
            parent_url, current_url, folder_name)

        msg = "subfolders"
        self.assertListEqual(expected, result, msg)

    def test_remove_last_forward_slash(self):
        parent_url = "/ml/machine-learning-databases/"
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"
        folder_name = os.path.join('repo_download', '53_[iris]')
        download_old = DownloaderOld(current_url, folder_name)

        result = download_old.remove_last_forward_slash(
            'http://foo.com/bar/cat.txt/')
        expected = 'http://foo.com/bar/cat.txt'
        msg = 'Last Character is a forward slash. Should strip forward slash'
        self.assertEqual(expected, result, msg)

        result = download_old.remove_last_forward_slash(
            'http://foo.com/bar/cat.txt')
        expected = 'http://foo.com/bar/cat.txt'
        msg = 'The last character is not a forward slash'
        self.assertEqual(expected, result, msg)

    def test_folder_from_link(self):
        current_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/"
        folder_name = os.path.join('repo_download', '53_[iris]')
        download_old = DownloaderOld(current_url, folder_name)

        expected = 'cat'

        result = download_old.folder_from_link('http://foo.com/bar/cat/')
        msg = "Forward slash at the end of the link"
        self.assertEqual(expected, result, msg)

        result = download_old.folder_from_link('http://foo.com/bar/cat')
        msg = "There is not a forward slash at the end of the link"
        self.assertEqual(expected, result)
