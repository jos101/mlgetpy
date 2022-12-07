from enum import Enum
import enum


class DataSetColumn(Enum):
    ID: str = "ID"
    USER_ID: str = "userID"
    INTRO_PAPER_ID: str = "introPaperID"
    NAME: str = "Name"
    ABSTRACT: str = "Abstract"
    AREA: str = "Area"
    TASK: str = "Task"
    TYPES: str = "Types"
    DOI: str = "DOI"
    DATE_DONATED: str = "DateDonated"
    IS_TABULAR: str = "isTabular"
    URL_FOLDER: str = "URLFolder"
    URL_README: str = "URLReadme"
    URL_LINK: str = "URLLink"
    GRAPHICS: str = "Graphics"
    STATUS: str = "Status"
    NUM_HITS: str = "NumHits"
    ATTRIBUTE_TYPES: str = "AttributeTypes"
    NUM_INSTANCES: str = "NumInstances"
    NUM_ATTRIBUTES: str = "NumAttributes"
    SLUG: str = "slug"
    TABULAR: str = "tabular"
    USERS: str = "users"
