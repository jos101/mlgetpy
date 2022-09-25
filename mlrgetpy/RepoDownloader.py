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


@dataclass
class RepodDownloader:

    __old_url = "https://archive.ics.uci.edu/ml/"
    __new_url = "https://archive-beta.ics.uci.edu/api/static/ml/datasets/"
    pbar = None
    # TODO repodownloader

    def __removeFilePath(self, file):
        if os.path.exists(file):
            os.remove(file)

    def __createDirPath(self, directory):
        if os.path.exists(directory) == False:
            os.mkdir(directory)

    def __getLinks(self, response: Response):
        webpage = html.fromstring(response.content)
        links = webpage.xpath('//a/@href')

        return links

    def download(self, data: pd.DataFrame):
        req = RequestHelper()

        print()
        for index, row in data.iterrows():
            # req.get(row["URLFolder"])
            # join with ml/machine-learning-databases/<index_repo>/
            current_url = urljoin(
                self.__old_url, row["URLFolder"].replace("../", ""))

            response = req.get(current_url)
            links = self.__getLinks(response)

            # TODO: create function downloadLinks
            parent_url = "/ml/machine-learning-databases/"
            directory = os.path.join("repo_download")
            self.__createDirPath(directory)

            self.__downloadLinks(req, links, parent_url, current_url,
                                 nameFolder=os.path.join(directory, row["Name"]))

    # TODO: determine if the link is a folder or an archive

    def __downloadLinks(self, req: RequestHelper, links: List, parent_url, current_url, nameFolder="", recursion=1) -> None:
        #print(f"recursion: {recursion}")
        #print(f"parent_url: {parent_url}")
        print(f"current_url: {current_url}")
        #print(f"name_folder: {nameFolder}")

        for link in links:
            if link == parent_url:
                continue

            # TODO: Refactor
            url = urljoin(current_url, link)
            response = requests.head(url)

            if response.headers['Content-Type'] != 'text/html;charset=ISO-8859-1':
                self.__createDirPath(nameFolder)
                req.saveFile(response, url, nameFolder)
            else:
                response = requests.get(url)
                self.__createDirPath(nameFolder)
                self.__downloadLinks(
                    req=req,
                    links=self.__getLinks(response),
                    parent_url=current_url.replace(
                        "https://archive.ics.uci.edu", ""),
                    current_url=url,
                    nameFolder=os.path.join(nameFolder, link),
                    recursion=recursion+1)

    def downloadALl(self, rep):
        NotImplemented
