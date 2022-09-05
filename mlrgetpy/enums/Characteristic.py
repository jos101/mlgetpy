from enum import Enum


class Characteristic(Enum):
    TABULAR: str = ["Tabular", "Multivariate", "Univariate"]
    SEQUENTIAL: str = ["Sequential"]
    TIME_SERIES: str = ["Time-Series"]
    TEXT: str = ["Text"]
    IMAGE: str = ["Image"]

    OTHER: str = ["Other"]
    DOMAIN_THEORY: str = ["Domain-Theory"]
    DATA_GENERATOR: str = ["Data-Generator"]
    ENGLISH_WORDS: str = ["English words"]
