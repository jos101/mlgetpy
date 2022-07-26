from dataclasses import dataclass, field

@dataclass
class PlaintextFileHandler:
    
    __file:str = field(init=False)

    def __post_init__(self) -> None:
        self.__file = "citations.txt"
    
    def save(self, citations:list):

        f = open(self.__file, "w", encoding="utf-8")
        for i in citations:
            f.write(i + "\n\n")
        f.close()
