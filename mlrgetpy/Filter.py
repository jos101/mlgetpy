from dataclasses import dataclass, field
from inspect import Attribute
from os import rename
from typing import List
import pandas as pd

from mlrgetpy.enums.Area import Area
from mlrgetpy.enums.AttributeType import AttributeType, FilterAttributeType
from mlrgetpy.enums.Characteristic import Characteristic
from mlrgetpy.enums.Task import Task


@dataclass
class Filter:
    name: str = None
    num_instances_less_than: int = None

    num_instances_greater_than: int = None
    contains_name: str = None
    characteristics: List[Characteristic] = None
    attribute_type: FilterAttributeType = None
    area: List[Area] = None
    task: Task = None
    num_attributes_less_than: int = None
    num_attributes_greater_than: int = None
    query: str = None

    def __check_area(self):
        if self.area != None and type(self.area) is not list:
            raise ValueError("Filter class: area must be a list")

        # exception if any element in the list is not an Area Class
        if type(self.area) is list:
            i = 0
            for item in self.area:
                if type(item) is not Area:
                    raise ValueError(
                        f"Filter class: element {i} must be an Area Class")
                i += 1

    def __check_characteristics(self):

        if self.characteristics != None and type(self.characteristics) is not list:
            raise ValueError("Filter class: characteristic must be a list")

        # exception if any element in the list is not an Characteristic Class
        if type(self.characteristics) is list:
            i = 0
            for item in self.characteristics:
                if type(item) is not Characteristic:
                    raise ValueError(
                        f"Filter class: element {i} must be an Characteristic Class")
                i += 1

    def __post_init__(self) -> None:

        self.__check_area()
        self.__check_characteristics()

    '''
    Type is equal to Characteristic
    search for multivariate, tabular, Time-series when type is Characteristic.TABULAR
    all items in the row.Types must be a item in Characteristic or row.Types is None
    '''

    def __find_rows_containing_type(self, remain: pd.DataFrame, type: Characteristic):
        filter: pd.Series = pd.Series(
            data=False, index=remain.index.tolist()).rename_axis('ID')

        for index, row in remain.iterrows():
            if row.Types == None:
                filter[filter.index == index] = False
                continue

            filter[filter.index == index] = all(
                item in type.value for item in row.Types.split(','))

        return remain[filter]

    def __get_filter_attr_type(self, data: pd.DataFrame, attrType: AttributeType):
        return data.AttributeTypes.str.contains(attrType.value, na=False)

    def __find_element_with_OR(self, data, listAttr: List[attribute_type]) -> pd.DataFrame:
        # false series filter
        filter: pd.Series = pd.Series(data=False, index=data.index.tolist())

        for at in listAttr:
            filter = filter | self.__get_filter_attr_type(data, at)

        return data[filter]

    # attribute type is related with characteristics (Type)
    def __search_attr_type(self, data: pd.DataFrame, filterAttrType: FilterAttributeType):
        temp_data: pd.DataFrame = pd.DataFrame()

        # these FilterAttrTypes have a List[AttributeType]
        if filterAttrType != FilterAttributeType.MIXED:
            temp_data = self.__find_element_with_OR(data, filterAttrType.value)

        # MIXED has List[List[AttributeType]]
        # the result must have a least one element of categorical and numerical
        # TODO: test filter
        if filterAttrType == FilterAttributeType.MIXED:
            temp_data: pd.DataFrame = data
            # List of list of Attributes
            for attrType in filterAttrType.value:
                temp_data = self.__find_element_with_OR(temp_data, attrType)

        return temp_data.sort_index()

    def __find_rows_containing_Area(self, remain: pd.DataFrame, area: Area):
        filter: pd.DataFrame = pd.DataFrame()
        if type(area.value) == list:
            # false series
            filter: pd.Series = pd.Series(
                data=False, index=remain.index.tolist())

            for area_val in area.value:
                filter = filter | (remain.Area == area_val)
        else:
            filter = remain.Area == area.value

        return remain[filter]

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

        if self.attribute_type != None:
            data = self.__search_attr_type(
                data, self.attribute_type)

        if self.area != None:

            temp_data: pd.DataFrame = pd.DataFrame()

            for item_area in self.area:
                temp_data = pd.concat([temp_data, self.__find_rows_containing_Area(
                    self.__get_remaining_data(data, temp_data), item_area)])

            data = temp_data.sort_index()

        if self.task != None:

            if self.task != Task.OTHER:
                data = data.query(
                    f'Task.str.contains("{self.task.value}", na=False)', engine='python')

            if self.task == Task.OTHER:
                data = self.__filter_task_other(data)

        if self.num_attributes_less_than != None:
            data = data.query(
                f"numAttributes < {self.num_attributes_less_than}")
        if self.num_attributes_greater_than != None:
            data = data.query(
                f"numAttributes > {self.num_attributes_greater_than}")

        return data

    '''
        find those row which not nontains Classification, Regression or Clustering.
        None tasks are include

    '''

    def __filter_task_other(self, data: pd.DataFrame):
        filter = pd.Series(
            data=False, index=data.index.tolist()).rename_axis('ID')

        for t in Task:
            if t == Task.OTHER:
                continue

            filter = filter | data.Task.str.contains(t.value, na=False)

        # negate the boolean series
        filter = ~filter

        return data[filter]
