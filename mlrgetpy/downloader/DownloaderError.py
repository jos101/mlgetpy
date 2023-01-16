from dataclasses import dataclass, field
from urllib.parse import urljoin
from mlrgetpy.RequestHelper import RequestHelper
from mlrgetpy.downloader.DownloaderAbstract import DownloaderAbstract
from mlrgetpy.BoxDownload import BoxDownload


@dataclass
class DownloaderError(DownloaderAbstract):
    current_url: str = field()
    href: str = field(default="")
    url_folder: str = field(default="")
    repo_name: str = field(default="")

    def initiateDownload(self):
        bdo = BoxDownload()
        text = "Not compatible URL"
        text_url_folder = f'URL Folder: {self.url_folder}'
        text_href = f'href: {self.href}'

        print(bdo.top())
        print(bdo.text_row(self.repo_name))
        print(bdo.row_sep())
        print(bdo.text_row(text_url_folder))
        print(bdo.text_row(text_href))
        if self.current_url != "":
            print(bdo.text_row(self.current_url))
        print(bdo.text_row(text))
        print(bdo.bottom())
