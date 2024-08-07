from dataclasses import dataclass
import json
from msilib.schema import Directory
import os
import re
from turtle import back
from typing import List
from lxml import html
import pandas as pd
from mlrgetpy.MyProgressBar import MyProgressBar
from mlrgetpy.RequestHelper import RequestHelper
from requests.exceptions import RequestException
from requests import Response
import progressbar

from rich import print
from urllib.parse import urljoin
import requests
from urllib import parse
from mlrgetpy.downloader.DownloaderError import DownloaderError
from mlrgetpy.downloader.DownloaderNew import DownloaderNew
from mlrgetpy.downloader.DownloaderNewHref import DownloaderNewHref

from mlrgetpy.downloader.DownloaderOld import DownloaderOld
from mlrgetpy.enums.DataSetColumn import DataSetColumn as c
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
import urllib.parse
from bs4 import BeautifulSoup


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    __old_sub_url = "../machine-learning-databases/"

    __new_url = "https://archive.ics.uci.edu/static/ml/datasets/"
    __new_sub_url = "/ml/datasets/"

    def download(self, data: pd.DataFrame):
        req = RequestHelper()
        dataset: DataSetListAbstract = DataSetListAbstract()
        repo_names = []

        print()
        for index, row in data.iterrows():
            repo_name = f'{index}_[{row["Name"]}]'

            # print(row)
            href = urljoin(self.__new_url, dataset.get_href_by_id(index))
            # print(href)
            response = req.head(href)
            # print (response.headers)
            # is_zip = response.headers['Content-Type'] == "application/zip"
            is_zip = href[ len(href) -4 ] == ".zip"


            downloader = DownloaderNewHref(
                href_url=href, repo_name=repo_name)
            downloader.initiateDownload()
            repo_names.append({"id": index, "name": repo_name})

            # req.get(row["URLFolder"])
            # join with ml/machine-learning-databases/<index_repo>/

            # old url (../machine-learning-databases/Iris/)
            # if row["URLFolder"][0:30] == self.__old_sub_url:
            #     temp = row["URLFolder"].replace(self.__old_sub_url, "")
            #     current_url = urljoin(self.__old_url, temp)
            #
            #     downloader = DownloaderOld(current_url, repo_name)
            #     downloader.initiateDownload()
            #     repo_names.append({"id": index, "name": repo_name})
            #
            # # new url no zip
            # elif row["URLFolder"][0:13] == self.__new_sub_url and is_zip == False:
            #     temp = row["URLFolder"].replace(self.__new_sub_url, "")
            #     current_url = urljoin(self.__new_url, temp)
            #
            #     downloader = DownloaderNew(current_url, repo_name)
            #     downloader.initiateDownload()
            #     repo_names.append({"id": index, "name": repo_name})
            #
            # # zip in new url
            # elif row["URLFolder"][0:13] == self.__new_sub_url and is_zip == True:
            #     downloader = DownloaderNewHref(
            #         href_url=href, repo_name=repo_name)
            #     downloader.initiateDownload()
            #     repo_names.append({"id": index, "name": repo_name})
            #
            # else:
            #     url_folder = self.data_folder(row["Name"])
            #
            #     if url_folder == None:
            #         current_url = ""
            #         downloader = DownloaderError(
            #             current_url, href, row["URLFolder"], repo_name)
            #         downloader.initiateDownload()
            #         continue
            #
            #     # data folder from old url
            #     temp = url_folder.replace(self.__old_sub_url, "")
            #     current_url = urljoin(self.__old_url, temp)
            #
            #     downloader = DownloaderOld(current_url, repo_name)
            #     downloader.initiateDownload()
            #     repo_names.append({"id": index, "name": repo_name})

        return repo_names

    def downloadALl(self, rep):
        NotImplemented

    def data_folder(self, repo_name):
        url_folder = None
        root_url = 'https://archive.ics.uci.edu/ml/datasets/'
        name = urllib.parse.quote_plus(repo_name)
        url = urljoin(root_url, name)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.find_all('a', href=True)
        for link in links:
            if link.text == 'Data Folder':
                url_folder = link['href']

        return url_folder

    def attributes(self, id: int) -> List[str]:
        attrs = []
        req = RequestHelper()
        url = 'https://archive.ics.uci.edu/dataset/'
        new_url = urljoin(url, str(id))

        # extracts attributes from json
        dt = DataSetListAbstract()
        attrs = dt.get_attributes(id)

        # extracts attributes from the script tag
        if attrs == []:
            response = req.get(new_url, expecting_json=False)
            attrs = self.__extract_attributes(response.content)

        # extracts attributes from the table tag
        if attrs == []:
            response = req.get(new_url, expecting_json=False)
            attrs = self.__extract_attributes_tr(response.content)

        return attrs

    def __extract_attributes(self, content: str) -> List[str]:
        attrs = []
        soup = BeautifulSoup(content, 'html.parser')
        datasets = soup.find_all('script', type="application/json")

        if datasets == None or len(datasets) < 2:
            return []

        # attrs=['data-sveltekit-fetched'])
        data = json.loads(datasets[1].text)
        json1 = json.loads(data["body"])

        for item in json1[0]["result"]["data"]["json"]["attributes"]:
            attrs.append(item["name"])

        return attrs

    def __extract_attributes_tr(self, content: str) -> List[str]:
        attrs = []
        soup = BeautifulSoup(content, 'html.parser')

        table = soup.find('table', class_='my-4 table w-full')

        if table == None:
            return []

        trs = table.tbody.find_all('tr')
        for tr in trs:
            attrs.append(tr.td.text)

        return attrs
