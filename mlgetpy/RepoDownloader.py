from dataclasses import dataclass
from mlgetpy.Repository import Repository


@dataclass
class RepodDownloader:

    def download(rep: Repository):
        NotImplemented

    def downloadALl(rep: Repository):
        NotImplemented