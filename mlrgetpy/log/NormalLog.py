from abc import abstractmethod
from dataclasses import dataclass
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
