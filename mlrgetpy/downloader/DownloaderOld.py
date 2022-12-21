from dataclasses import dataclass, field
import os
from typing import List
from urllib.parse import urljoin

from requests import Response
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from lxml import html
from mlrgetpy.log.ConfigLog import ConfigLog


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
        #print("OLD: Initiate download")
        #print(f"OLD: current url ->{self.current_url}")

        #print(f"Links: {links}")
        directory = os.path.join("repo_download")
        name_folder = os.path.join(directory, self.repo_name)

        #print(f"repo_name2: {repo_name2}")
        self.__createDirPath(directory)

        links_path = self.create_links_path(
            self.parent_url, self.current_url, name_folder)

        print("┌" + "─" * 90 + "┐")
        print(f"│{self.repo_name:90s}│")
        print("├" + "─" * 90 + "┤")
        self.downloadLinks(links_path)
        print("└" + "─" * 90 + "┘")

    def downloadLinks(self, links_path):
        print('\033[?25l', end="")  # hide cursor
        for path in links_path:
            print(f"│{path['url']:90s}│")
            response = self.req.get(path['url'], expecting_json=False)
            links = self.getLinks(response)
            archives: List = []

            for link in links:
                res2 = self.req.head(urljoin(path['url'], link))
                if res2.headers['Content-Type'] != 'text/html;charset=ISO-8859-1' and res2.headers['Content-Type'] != 'text/html; charset=UTF-8':
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

    def create_links_path(self, parent_url, url, name_folder):
        ConfigLog.log.write_create_link_path(parent_url, url, name_folder)

        list_urls = []
        response = self.req.head(url)
        if response.headers['Content-Type'].rsplit(';')[0] != 'text/html':
            return list_urls

        list_urls = [{'url': url, 'name_folder': name_folder}]
        self.__createDirPath(name_folder)
        response = self.req.get(url, expecting_json=False)

        links = self.getLinks(response)
        for link in links:
            if link == parent_url:
                continue

            new_parent_url = url.replace(self.root_url, "")
            new_url = urljoin(url, link)
            new_name_folder = self.create_name_folder(name_folder, link)
            list_urls = list_urls + \
                self.create_links_path(
                    new_parent_url, new_url, new_name_folder)

        return list_urls

    def getLinks(self, response: Response):
        webpage = html.fromstring(response.content)
        links = webpage.xpath('//a/@href')
        return links

    def __createDirPath(self, directory):
        return super().createDirPath(directory)

    def create_name_folder(self, nameFolder: str, link: str):
        link = self.remove_last_forward_slash(link)

        newNamefolder = ""
        newNamefolder = os.path.join(nameFolder, self.folder_from_link(link))
        return newNamefolder

    def remove_last_forward_slash(self, link):
        if (link[-1] == "/"):
            link = link[:len(link)-1]
        return link

    def folder_from_link(self, link):
        link = self.remove_last_forward_slash(link)
        return link.rsplit('/', 1)[-1]
