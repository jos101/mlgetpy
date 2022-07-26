from dataclasses import dataclass

from ..filehandler.FileHandlerAbstract import FileHandlerAbstract
from ..filehandler.BibFileHandler import BibFileHandler
from ..filehandler.PlaintextFileHandler import PlaintextFileHandler

@dataclass
class FileHandlerFactory:

    @staticmethod
    def create(type = "bibtext") -> FileHandlerAbstract:
        object:FileHandlerAbstract = None

        if type == "bibtext":
            object = BibFileHandler()
        elif type == "plaintext":
            object = PlaintextFileHandler()

        return object
