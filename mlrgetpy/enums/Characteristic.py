from enum import Enum


class Characteristic(Enum):
    IMAGE: str = "Image"
    TABULAR: str = "Tabular"
    SEQUENTIAL: str = "Sequential"
    TEXT: str = "Text"
    TIME_SERIES: str = "Time-Series"
    DOMAIN_THEORY: str = "Domain-Theory"
    MULTIVARIATE: str = "Multivariate"
    UNIVARIATE: str = "Univariate"
    DATA_GENERATOR: str = "Data-Generator"
    ENGLISH_WORDS: str = "English words"
