from enum import Enum
from typing import List


class AttributeType(Enum):
    NUMERICAL: List[str] = ["Integer", "Real"]
    CATEGORICAL: List[str] = ["Categorical"]
