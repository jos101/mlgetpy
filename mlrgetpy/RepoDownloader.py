from dataclasses import dataclass
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
from mlrgetpy.downloader.DownloaderNew import DownloaderNew
from mlrgetpy.downloader.DownloaderNewHref import DownloaderNewHref

from mlrgetpy.downloader.DownloaderOld import DownloaderOld
from mlrgetpy.enums.DataSetColumn import DataSetColumn as c
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    __old_sub_url = "../machine-learning-databases/"

    __new_url = "https://archive-beta.ics.uci.edu/static/ml/datasets/"
    __new_sub_url = "/ml/datasets/"

    def download(self, data: pd.DataFrame):
        req = RequestHelper()
        dataset: DataSetListAbstract = DataSetListAbstract()

        print()
        for index, row in data.iterrows():
            # print(row)
            href = urljoin(self.__new_url, dataset.get_href_by_id(index))
            response = req.head(href)
            is_zip = response.headers['Content-Type'] == "application/zip"

            # req.get(row["URLFolder"])
            # join with ml/machine-learning-databases/<index_repo>/
            if row["URLFolder"][0:30] == self.__old_sub_url:
                temp = row["URLFolder"].replace(self.__old_sub_url, "")
                current_url = urljoin(self.__old_url, temp)

                downloader = DownloaderOld(
                    current_url, repo_name=f'{index}_[{row["Name"]}]')
                downloader.initiateDownload()

            elif row["URLFolder"][0:13] == self.__new_sub_url and is_zip == False:
                temp = row["URLFolder"].replace(self.__new_sub_url, "")
                current_url = urljoin(self.__new_url, temp)

                downloader = DownloaderNew(
                    current_url, repo_name=f'{index}_[{row["Name"]}]')
                downloader.initiateDownload()
            elif row["URLFolder"][0:13] == self.__new_sub_url and is_zip == True:
                downloader = DownloaderNewHref(
                    href_url=href, repo_name=f'{index}_[{row["Name"]}]')
                downloader.initiateDownload()
            else:
                print(
                    f'rep {index}: Not compatible url ({row["URLFolder"]}), href: {href}')
                continue

    def downloadALl(self, rep):
        NotImplemented
