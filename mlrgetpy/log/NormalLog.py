from abc import abstractmethod
from dataclasses import dataclass

from requests import Response
from mlrgetpy.log.LogAbstract import LogAbstract


@dataclass
class NormalLog(LogAbstract):

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
