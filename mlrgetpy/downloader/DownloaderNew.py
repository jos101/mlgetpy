from dataclasses import dataclass, field
import os
from typing import List
from urllib.parse import urljoin

from requests import Response
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from lxml import html
from mlrgetpy.URLManager import URLManager
from mlrgetpy.BoxDownload import BoxDownload


@dataclass
class DownloaderNew(DownloaderAbstract):
    current_url: str = field()
    repo_name: str = field(default="")
    req: RequestHelper = RequestHelper()

    root_url = "https://archive-beta.ics.uci.edu"
    url = "https://archive-beta.ics.uci.edu/static/ml/datasets/"
    sub_url = "/ml/datasets/"
    parent_url = "/static/ml/datasets"
    __bdo = BoxDownload()

    def initiateDownload(self):
        #print("New: Initiate download")

        directory = os.path.join("repo_download")
        name_folder = os.path.join(directory, self.repo_name)
        self.__createDirPath(directory)

        links_path = self.create_links_path(
            self.parent_url, self.current_url, name_folder)

        print(self.__bdo.top())
        print(self.__bdo.text_row(self.repo_name))
        print(self.__bdo.row_sep())

        if len(links_path):
            self.downloadLinks(links_path)
        else:
            left = "Not Found:"
            right = "There is no Links in the url "
            print(self.__bdo.text_row(f"{self.current_url}"))
            print(self.__bdo.download_row3(left, right, 10))

        print(self.__bdo.bottom())

    def create_links_path(self, parent_url, url, name_folder):
        list_urls = []
        response = self.req.head(url)
        #print(f"header: {response.headers['Content-Type'].rsplit(';')[0]}")
        if response.headers['Content-Type'].rsplit(';')[0] == 'text/html':
            list_urls = [{'url': url, 'name_folder': name_folder}]
            self.__createDirPath(name_folder)
            response = self.req.get(url, expecting_json=False)
            links = self.getLinks(response)

            for link in links:
                if link == parent_url:
                    continue
                new_name_folder = URLManager.create_name_folder(
                    name_folder, link)
                list_urls = list_urls + \
                    self.create_links_path(url.replace(
                        self.root_url, ""), urljoin(url, link), new_name_folder)
        return list_urls

    def downloadLinks(self, links_path):
        print('\033[?25l', end="")  # hide cursor
        for path in links_path:
            print(f"│{path['url']:90s}│")
            response = self.req.get(path['url'], expecting_json=False)
            links = self.getLinks(response)
            archives: List = []

            # find archives
            for link in links:
                if urljoin(self.root_url, link)+"/" == urljoin(path['url'], '.'):
                    continue

                res2 = self.req.head(urljoin(path['url'], link))
                if res2.headers['Content-Type'].rsplit(';')[0] != 'text/html':
                    #print(f"  arhive: {urljoin(i[0], link)}")
                    archives.append(link)

            count = 0
            for archive in archives:
                last = False
                if count == len(archives) - 1:
                    last = True
                self.req.saveFile(response, urljoin(
                    path['url'], archive), path['name_folder'], last)
                count += 1

        print('\033[?25h', end="")  # show cursor

    def getLinks(self, response: Response):
        webpage = html.fromstring(response.content)
        links = webpage.xpath('//ul[@class="view-tiles"]/li/a/@href')
        return links

    def __createDirPath(self, directory):
        return super().createDirPath(directory)
