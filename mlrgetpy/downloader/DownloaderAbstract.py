from abc import abstractmethod
from dataclasses import dataclass
import os

from requests import Response

from mlrgetpy.RequestHelper import RequestHelper


@dataclass
class DownloaderAbstract:
    req = RequestHelper()
    current_url: str = ""

    def initiateDownload(self):
        NotImplemented

    def downloadLinks(self):
        NotImplemented

    def getLinks(self, response: Response):
        NotImplemented

    def __createNameFolder(self, nameFolder, link, parent_url, url_type="old"):
        NotImplemented

    def createDirPath(self, directory):
        if os.path.exists(directory) == False:
            os.makedirs(directory)
