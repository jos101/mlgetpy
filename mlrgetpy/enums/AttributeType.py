from enum import Enum
from typing import List


class AttributeType(Enum):
    INTEGER: str = "Integer"
    REAL: str = "Real"
    CATEGORICAL: str = "Categorical"


class FilterAttributeType(Enum):
    NUMERICAL: List[AttributeType] = [
        AttributeType.INTEGER, AttributeType.REAL]
    CATEGORICAL: List[AttributeType] = [AttributeType.CATEGORICAL]
    MIXED: List[List[AttributeType]] = [CATEGORICAL, NUMERICAL]
