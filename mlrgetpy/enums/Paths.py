from enum import Enum
import os


class Paths(Enum):
    ROOT_FOLDER: str = os.path.join("repo_download")
