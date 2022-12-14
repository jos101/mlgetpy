from dataclasses import dataclass, field
import os
from typing import List
from urllib.parse import urljoin

from requests import Response
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from lxml import html


@dataclass
class DownloaderNewHref(DownloaderAbstract):
    href_url: str = field(default="")
    repo_name: str = field(default="")
    req: RequestHelper = RequestHelper()

    root_url = "https://archive-beta.ics.uci.edu"

    def initiateDownload(self):
        # print("New: Initiate download")
        url = urljoin(self.root_url, self.href_url)

        directory = os.path.join("repo_download")
        name_folder = os.path.join(directory, self.repo_name)
        self.__createDirPath(directory)
        self.__createDirPath(name_folder)

        response_headers = self.req.head(url)

        print("┌" + "─" * 90 + "┐")
        print(f"│{self.repo_name:90s}│")
        print("├" + "─" * 90 + "┤")
        self.download(response_headers, url, name_folder)
        print("└" + "─" * 90 + "┘")

    def download(self, response_headers, url, name_folder):
        print(f"│{self.href_url:90s}│")

        self.req.saveFile(response_headers, url, name_folder, True)

    def __createDirPath(self, directory):
        return super().createDirPath(directory)
