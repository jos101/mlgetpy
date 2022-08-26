from ast import Import
from asyncio import tasks
from dataclasses import dataclass, field
from tempfile import TemporaryDirectory
from typing import List
import pandas as pd

from mlrgetpy.enums.Area import Area
from mlrgetpy.enums.Characteristic import Characteristic
from mlrgetpy.enums.Task import Task


@dataclass
class Filter:
    name: str = None
    num_instances_less_than: int = None

    num_instances_greater_than: int = None
    contains_name: str = None
    characteristics: List[Characteristic] = None
    area: Area = None
    task: Task = None
    num_attributes_less_than: int = None
    num_attributes_greater_than: int = None
    query: str = None

    def __find_rows_containing_type(self, remain: pd.DataFrame, type: Characteristic):
        return remain.query(
            f"Types.str.contains('{type.value}', na=False)", engine="python"
        )

    def __find_rows_containing_Area(self, remain: pd.DataFrame, area: Area):
        return remain.query(
            f'Area.str.contains("{area.value}", na=False)', engine='python'
        )

    def __get_remaining_data(self, data: pd.DataFrame, temp_data: pd.DataFrame):
        return data.drop(temp_data.index.values.tolist())

    def filter(self, data: pd.DataFrame) -> pd.DataFrame:

        if self.query != None:
            data = data.query(self.query)
        if self.name != None:
            data = data.query(f"Name == '{self.name}'")
        if self.contains_name != None:
            data = data.query(
                f'Name.str.contains("{self.contains_name}", na=False)', engine='python'
            )
        if self.num_instances_less_than != None:
            data = data.query(
                f"numInstances <= {self.num_instances_less_than}")
        if self.num_instances_greater_than != None:
            data = data.query(
                f"numInstances >= {self.num_instances_greater_than}")

        if self.characteristics != None:
            temp_data: pd.DataFrame = pd.DataFrame()

            # iterate every characteristic
            for type in self.characteristics:

                temp_data = pd.concat([temp_data, self.__find_rows_containing_type(
                    self.__get_remaining_data(data, temp_data), type)])

            data = temp_data.sort_index()

        # TODO: test area filter
        # TODO: create filter for other in AREA
        # TODO: change to List[Area]
        if self.area != None:
            data = self.__find_rows_containing_Area(data, self.area)

        # TODO:create enum to TASK
        if self.task != None:
            data = data.query(f"Task == '{self.task.value}'")

        # TODO: Attribute type
        # TODO: create enum attribute type

        if self.num_attributes_less_than != None:
            data = data.query(
                f"numAttributes < {self.num_attributes_less_than}")
        if self.num_attributes_greater_than != None:
            data = data.query(
                f"numAttributes > {self.num_attributes_greater_than}")

        return data
