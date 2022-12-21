from abc import abstractmethod
from dataclasses import dataclass
from mlrgetpy.log.LogAbstract import LogAbstract


@dataclass
class NoLog(LogAbstract):

    @abstractmethod
    def write_url(self, url: str):
        pass

    @abstractmethod
    def write_id(self, id: str):
        pass

    @abstractmethod
    def write_use_cache(self):
        pass

    @abstractmethod
    def write_add_ids(self, IDs: list):
        pass

    @abstractmethod
    def write_remove_indexes(self, IDs: list):
        pass

    @abstractmethod
    def write_create_link_path(self, parent_url, current_url, name_folder):
        pass
