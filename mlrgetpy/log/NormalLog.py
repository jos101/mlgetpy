from abc import abstractmethod
from dataclasses import dataclass

from requests import Response
from mlrgetpy.log.ILog import ILog


@dataclass
class NormalLog(ILog):

    @abstractmethod
    def write_url(self, url: str):
        print(f'Opening {url}')

    @abstractmethod
    def write_id(self, id: str):
        print(f'id: {id}')

    @abstractmethod
    def write_use_cache(self):
        print(f'using cache')

    @abstractmethod
    def write_add_ids(self, IDs: list):
        print(f'adding IDs {IDs}')

    @abstractmethod
    def write_remove_indexes(self, IDs: list):
        print(f'removing indexes {IDs}')

    @abstractmethod
    def write_save_file(self, response: Response, url: str, directory="", last=False):
        print(f'[saving file] url: {url}')
        print(f'        directory: {directory}')
        print(f'            last?: {last}')

    @abstractmethod
    def write_create_link_path(self, parent_url, current_url, name_folder):
        print(f'[create link path] parent url: {parent_url}')
        print(f'                  current_url: {current_url}')
        print(f'                  name folder: {name_folder}')

    @abstractmethod
    def write_caching(self, file: str):
        print(f'[using caching] {file}')

    @abstractmethod
    def write_datafile(self, datafile: str, has_header: bool):
        print(f"reading datafile: {datafile}")
        if has_header:
            print(f"datafile contains headers")
        else:
            print(f"datafile without headers")

    @abstractmethod
    def write_attributes(self, attributes: str):
        print(f"adding attributes headers: {attributes}")
