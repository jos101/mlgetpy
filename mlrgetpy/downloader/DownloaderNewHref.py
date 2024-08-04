from dataclasses import dataclass, field
import os
from typing import List
from urllib.parse import urljoin

from requests import Response
from mlrgetpy.BoxDownload import BoxDownload
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from lxml import html
import re


@dataclass
class DownloaderNewHref(DownloaderAbstract):
    """
    A class used to download usually a zip file from the repository 

    Parameters
    ----------
    href_url : str
        The href taken from the object
        Should have the pattern ^https://archive-beta\.ics\.uci\.edu/static/ml/datasets/[0-9]+/.+
        i.e. https://archive.ics.uci.edu/static/ml/datasets/100/arhive.zip
    repo_name : str
        The name of the repository
        should have the pattern [0-9]+_\[.+\]
        i.e. 100_[Iris]

    Attributes
    ----------
    req : RequestHelper
        A RequestHelper object

    """
    href_url: str = field(default="")
    repo_name: str = field(default="")
    req: RequestHelper = field(default_factory=lambda: RequestHelper())

    root_url = "https://archive.ics.uci.edu"

    def __post_init__(self) -> None:
        pattern = "^https://archive\.ics\.uci\.edu/static/public/[0-9]+/.+"
        x = re.search(pattern, self.href_url)
        if x == None:
            msg = f"[DownloaderNewHref error]: Not valid href_url\n"
            msg += f"\texpected pattern: {pattern}\n"
            msg += f"\thref_url: {self.href_url}"
            raise ValueError(msg)

        pattern_repo_name = "[0-9]+_\[.+\]"
        x = re.search(pattern_repo_name, self.repo_name)
        if x == None:
            msg = f"[DownloaderNewHref error]: Not valid repo_name\n"
            msg += f"\texpected pattern: {pattern_repo_name}\n"
            msg += f"\repo_name: {self.repo_name}"
            raise ValueError(msg)

    def initiateDownload(self):
        bdo = BoxDownload()
        # print("New: Initiate download")
        url = urljoin(self.root_url, self.href_url)

        directory = os.path.join("repo_download")
        name_folder = os.path.join(directory, self.repo_name)
        self.__createDirPath(directory)
        self.__createDirPath(name_folder)

        response_headers = self.req.head(url)

        print(bdo.top())
        print(bdo.header(self.repo_name))
        print(bdo.row_sep())
        self.download(response_headers, url, name_folder)
        print(bdo.bottom())

    def download(self, response_headers, url, name_folder):
        bdo = BoxDownload()
        print(bdo.text_row(self.href_url))

        self.req.saveFile(response_headers, url, name_folder, True)

    def __createDirPath(self, directory):
        return super().createDirPath(directory)
