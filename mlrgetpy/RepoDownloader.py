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

from mlrgetpy.downloader.DownloaderOld import DownloaderOld


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    __old_sub_url = "../machine-learning-databases/"
    __old_parent_url = "/ml/machine-learning-databases/"

    __new_url = "https://archive-beta.ics.uci.edu/api/static/ml/datasets/"
    __new_sub_url = "/ml/datasets/"
    __new_parent_url = "/api/static/ml/datasets"
    pbar = None
    # TODO repodownloader

    def __removeFilePath(self, file):
        if os.path.exists(file):
            os.remove(file)

    def __createDirPath(self, directory):
        if os.path.exists(directory) == False:
            os.mkdir(directory)

    def __getLinks(self, response: Response, url_type="old"):
        webpage = html.fromstring(response.content)
        if url_type == "old":
            links = webpage.xpath('//a/@href')
        elif url_type == "new":
            links = webpage.xpath('//ul[@class="view-tiles"]/li/a/@href')

        return links

    def download(self, data: pd.DataFrame):
        req = RequestHelper()

        print()
        for index, row in data.iterrows():
            # req.get(row["URLFolder"])
            # join with ml/machine-learning-databases/<index_repo>/
            if row["URLFolder"][0:30] == self.__old_sub_url:
                temp = row["URLFolder"].replace(self.__old_sub_url, "")
                current_url = urljoin(self.__old_url, temp)

                downloader = DownloaderOld(
                    current_url, repo_name=f'{index}_[{row["Name"]}]')
                downloader.initiateDownload()

            elif row["URLFolder"][0:13] == self.__new_sub_url:
                temp = row["URLFolder"].replace(self.__new_sub_url, "")
                current_url = urljoin(self.__new_url, temp)

                downloader = DownloaderNew(
                    current_url, repo_name=f'{index}_[{row["Name"]}]')
                downloader.initiateDownload()
            else:
                print(f'rep {index}: Not compatible url ({row["URLFolder"]})')
                continue

    def __createNameFolder(self, nameFolder, link, parent_url, url_type="old"):
        newNamefolder = ""
        if url_type == "old":
            newNamefolder = os.path.join(nameFolder, link)
        elif url_type == "new":
            newNamefolder = os.path.join(
                nameFolder, link.rsplit('/', 1)[-1])

        print(f"--name folder    : {nameFolder}")
        print(f"--link           : {link}")
        print(f"--new name folder: {newNamefolder}")
        return newNamefolder

    # TODO: determine if the link is a folder or an archive

    def __downloadLinks(self, req: RequestHelper, links: List, parent_url, current_url, nameFolder="", url_type="old", recursion=1) -> None:
        if url_type == "old":
            root_url = "https://archive.ics.uci.edu"
        elif url_type == "new":
            root_url = "https://archive-beta.ics.uci.edu"
        else:
            raise Exception(f"there is no type {url_type}")

        #print(f"recursion: {recursion}")
        print(f"parent_url: {parent_url}")
        print(f"current_url: {current_url}")
        print(f"link: {links}")
        print(f"name_folder: {nameFolder}")

        for link in links:
            if link == parent_url:
                continue

            # TODO: Refactor
            url = urljoin(current_url, link)
            response = req.head(url)
            print(response.headers['Content-Type'])
            if response.headers['Content-Type'] == 'text/html;charset=ISO-8859-1' or response.headers['Content-Type'] == 'text/html; charset=UTF-8':
                response = req.get(url)
                self.__createDirPath(nameFolder)

                self.__downloadLinks(
                    req=req,
                    links=self.__getLinks(response, url_type=url_type),
                    # TODO: create variable
                    parent_url=current_url.replace(root_url, ""),
                    current_url=url,
                    nameFolder=self.__createNameFolder(
                        nameFolder, link, parent_url, url_type),
                    recursion=recursion+1)
            else:
                self.__createDirPath(nameFolder)
                req.saveFile(response, url, nameFolder)

    def downloadALl(self, rep):
        NotImplemented
