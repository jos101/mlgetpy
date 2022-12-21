import unittest
import os
from mlrgetpy.downloader.DownloaderNew import DownloaderNew
from requests import Response


class Test_DownloaderNew(unittest.TestCase):

    def test_create_links_path(self):
        parent_url = "/static/ml/datasets"
        current_url = "https://archive-beta.ics.uci.edu/static/ml/datasets/713"
        folder_name = os.path.join(
            'repo_download', '713_[Auction Verification]')
        download_new = DownloaderNew(current_url, folder_name)

        expected = [{'url': 'https://archive-beta.ics.uci.edu/static/ml/datasets/713',
                     'name_folder': os.path.join(
                         'repo_download', '713_[Auction Verification]')},
                    {'url': 'https://archive-beta.ics.uci.edu/static/ml/datasets/713/Graphics',
                     'name_folder': os.path.join(
                         'repo_download', '713_[Auction Verification]', 'Graphics')}]

        result = download_new.create_links_path(
            parent_url, current_url, folder_name)

        self.assertListEqual(expected, result)

    def test_create_name_folder(self):
        parent_url = "/static/ml/datasets"
        current_url = "https://archive-beta.ics.uci.edu/static/ml/datasets/713"
        folder_name = os.path.join(
            'repo_download', '713_[Auction Verification]')
        download_new = DownloaderNew(current_url, folder_name)

        link = 'https://archive-beta.ics.uci.edu/static/ml/datasets/713/data.csv'
        parent_url = 'https://archive-beta.ics.uci.edu/static/ml/datasets/713'
        result = download_new.create_name_folder(folder_name, link)

        expected = os.path.join(
            'repo_download', '713_[Auction Verification]', 'data.csv')
        self.assertEqual(expected, result)

    def test_get_links(self):
        current_url = "https://archive-beta.ics.uci.edu/static/ml/datasets/713"
        folder_name = os.path.join(
            'repo_download', '713_[Auction Verification]')
        download_new = DownloaderNew(current_url, folder_name)

        response: Response = Response()
        response.status_code = 200
        string = '''
<!DOCTYPE html>
<html>
<head><title>listing directory /static/ml/datasets/713/</title> </head>
<body class="directory">
    <input id="search" type="text" placeholder="Search" autocomplete="off" />
    <div id="wrapper">
        <h1><a href="/">~</a> / <a href="/static">static</a> / <a href="/static/ml">ml</a> / <a href="/static/ml/datasets">datasets</a> / <a href="/static/ml/datasets/713">713</a> / </h1>
        <ul id="files" class="view-tiles">
            <li>
                <a href="/static/ml/datasets" class="icon icon-directory" title=".."> 
                </a>
            </li>
            <li>
                <a href="/static/ml/datasets/713/Graphics" class="icon icon-directory" title="Graphics"> 
                </a>
            </li>
            <li>
                <a href="/static/ml/datasets/713/auction%2Bverification.zip" class="icon icon icon-zip icon-application-zip" title="auction+verification.zip">
                </a>
            </li>
            <li>
                <a href="/static/ml/datasets/713/data.csv" class="icon icon icon-csv icon-text" title="data.csv">
                </a>
            </li>
        </ul>
    </div>
</body>
</html>'''
        string_bytes = bytes(string, 'utf-8')

        response._content = string_bytes

        result = download_new.getLinks(response)
        expected = ['/static/ml/datasets',
                    '/static/ml/datasets/713/Graphics',
                    '/static/ml/datasets/713/auction%2Bverification.zip',
                    '/static/ml/datasets/713/data.csv']
        self.assertListEqual(expected, result)
