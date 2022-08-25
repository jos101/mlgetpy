from enum import Enum
import enum


class Task(Enum):
    CLASSIFICATION: str = "Classification"
    REGRESSION: str = "Regression"
    CLUSTERING: str = "Clustering"
    OTHER: str = "Other"
