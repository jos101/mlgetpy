from abc import abstractmethod
from dataclasses import dataclass

from requests import Response


@dataclass
class ILog:

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

    @abstractmethod
    def write_save_file(self, response: Response, url: str, directory="", last=False):
        NotImplemented

    @abstractmethod
    def write_create_link_path(self, parent_url, current_url, name_folder):
        NotImplemented

    @abstractmethod
    def write_caching(self, file: str):
        NotImplemented

    @abstractmethod
    def write_datafile(self, datafile: str, has_header: bool):
        NotImplemented

    @abstractmethod
    def write_attributes(self, attributes: str):
        NotImplemented
