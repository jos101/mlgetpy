from dataclasses import dataclass, field
import os
from typing import List
from urllib.parse import urljoin

from requests import Response
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from lxml import html


@dataclass
class DownloaderOld(DownloaderAbstract):
    current_url: str = field()
    repo_name: str = field(default="")
    req: RequestHelper = RequestHelper()

    root_url = "https://archive.ics.uci.edu"
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    sub_url = "../machine-learning-databases/"
    parent_url = "/ml/machine-learning-databases/"

    def initiateDownload(self):
        print("OLD: Initiate download")
        print(f"OLD: current url ->{self.current_url}")

        #print(f"Links: {links}")
        directory = os.path.join("repo_download")
        name_folder = os.path.join(directory, self.repo_name)

        #print(f"repo_name2: {repo_name2}")
        self.__createDirPath(directory)

        links_path = self.create_links_path(
            self.parent_url, self.current_url, name_folder)
        for i in links_path:
            print(f"url: {i[0]}")
            response = self.req.get(i[0])
            links = self.getLinks(response)
            archives: List = []

            for link in links:
                res2 = self.req.head(urljoin(i[0], link))
                if res2.headers['Content-Type'] != 'text/html;charset=ISO-8859-1' and res2.headers['Content-Type'] != 'text/html; charset=UTF-8':
                    archives.append(link)

            count = 0
            for archive in archives:
                last = False
                if count == len(archives) - 1:
                    last = True
                self.req.saveFile(response, urljoin(
                    i[0], archive), i[1], last)
                count += 1

    # TODO: Refactor in class linksPaths
    def create_links_path(self, parent_url, url, name_folder):
        list_urls = []
        response = self.req.head(url)

        if response.headers['Content-Type'] == 'text/html;charset=ISO-8859-1' or response.headers['Content-Type'] == 'text/html; charset=UTF-8':
            list_urls = [(url, name_folder)]
            self.__createDirPath(name_folder)
            response = self.req.get(url)
            links = self.getLinks(response)
            for link in links:
                if link == parent_url:
                    continue
                list_urls = list_urls + \
                    self.create_links_path(url.replace(
                        self.root_url, ""), urljoin(url, link), os.path.join(name_folder, link))
        return list_urls

    def getLinks(self, response: Response):
        webpage = html.fromstring(response.content)
        links = webpage.xpath('//a/@href')
        return links

    def __createDirPath(self, directory):
        return super().createDirPath(directory)
