from dataclasses import dataclass, field

from mlrgetpy.citation.FormatAbstract import FormatAbstract
from mlrgetpy.citation.PlainCitation import PlainCitation

from .Bibtext import Bibtext

@dataclass
class CitationFactory:

    @staticmethod
    def create(type:str = "bibtext") -> FormatAbstract:
        
        object:FormatAbstract = None

        if type == "bibtext":
            object =  Bibtext()
        elif type == "plaintext":
            object = PlainCitation()
        
        return object