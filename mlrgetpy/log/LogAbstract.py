from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class LogAbstract:

    @abstractmethod
    def write_url(self, url: str):
        NotImplemented

    @abstractmethod
    def write_id(self, id: str):
        NotImplemented

    @abstractmethod
    def write_use_cache(self):
        NotImplemented

    @abstractmethod
    def write_add_ids(self, IDs: list):
        NotImplemented

    @abstractmethod
    def write_remove_indexes(self, IDs: list):
        NotImplemented
