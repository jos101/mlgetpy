from abc import abstractmethod
from dataclasses import dataclass

@dataclass
class FileHandlerAbstract:

    @abstractmethod
    def save(self, citations:list):
        NotImplemented