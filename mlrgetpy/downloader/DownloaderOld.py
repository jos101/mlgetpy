from dataclasses import dataclass, field
import os
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

        response = self.req.get(self.current_url)
        links = self.getLinks(response)
        print(f"Links: {links}")
        # TODO: create function downloadLinks
        directory = os.path.join("repo_download")
        repo_name2 = os.path.join(directory, self.repo_name)
        print(f"repo_name2: {repo_name2}")
        self.__createDirPath(directory)
        self.downloadLinks(links, self.parent_url,
                           self.current_url, name_folder=repo_name2)

    def downloadLinks(self, links, parent_url, current_url, name_folder):
        print("-----Download links--------")
        print(f"current_url: {current_url}")
        print(f"parent_url: {parent_url}")
        print(f"links: {links}")
        print(f"name_folder: {name_folder}")

        for link in links:
            if link == parent_url:
                continue
            url = urljoin(current_url, link)
            response = self.req.head(url)
            print(f"link: {link}")
            print(f"header: {response.headers['Content-Type']}")

            if response.headers['Content-Type'] == 'text/html;charset=ISO-8859-1' or response.headers['Content-Type'] == 'text/html; charset=UTF-8':
                response = self.req.get(url)
                self.__createDirPath(name_folder)

                self.downloadLinks(
                    links=self.getLinks(response),
                    # TODO: create variable
                    parent_url=current_url.replace(self.root_url, ""),
                    current_url=url,
                    name_folder=self.__createNameFolder(
                        name_folder, link, parent_url))
            else:
                self.__createDirPath(name_folder)
                self.req.saveFile(response, url, name_folder)

    def getLinks(self, response: Response):
        webpage = html.fromstring(response.content)
        links = webpage.xpath('//a/@href')
        return links

    def __createDirPath(self, directory):
        return super().createDirPath(directory)

    def __createNameFolder(self, nameFolder, link, parent_url, url_type="old"):
        newNamefolder = ""
        newNamefolder = os.path.join(nameFolder, link)

        print(f"--name folder    : {nameFolder}")
        print(f"--link           : {link}")
        print(f"--new name folder: {newNamefolder}")
        return newNamefolder