from enum import Enum
from typing import List


class Area(Enum):
    BUSINESS: List[str] = ["Business", "Financial"]
    COMPUTER_SCIENCE: List[str] = ["Computer", "Computer Science"]
    ENGINEERING: str = "Engineering"
    GAME: str = "Game"
    LAW: str = "Engineering"
    LIFE_SCIENCES: str = ["Life", "Life Sciences"]
    PHYSICAL_SCIENCES: str = "Physical"
    SOCIAl_SCIENCES: str = "Social"
    OTHER: str = "Other"
