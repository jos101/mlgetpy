from dataclasses import dataclass, field
import os
from typing import List
from urllib.parse import urljoin

from requests import Response
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from lxml import html
from mlrgetpy.log.ConfigLog import ConfigLog
from mlrgetpy.URLManager import URLManager


@dataclass
class DownloaderError(DownloaderAbstract):
    current_url: str = field()
    href: str = field(default="")
    url_folder: str = field(default="")
    repo_name: str = field(default="")

    req: RequestHelper = RequestHelper()

    def initiateDownload(self):
        text = "Not compatible URL"
        text_url_folder = f'URL Folder: {self.url_folder}'
        text_href = f'href: {self.href}'

        print("┌" + "─" * 90 + "┐")
        print(f"│{self.repo_name:90s}│")
        print("├" + "─" * 90 + "┤")
        print(f'│{text_url_folder:90}│')
        print(f'│{text_href:90}│')
        print(f"│{self.current_url:90s}│")
        print(f"│{text:90s}│")
        print("└" + "─" * 90 + "┘")
