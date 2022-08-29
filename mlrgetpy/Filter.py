from dataclasses import dataclass, field
from inspect import Attribute
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

    def __post_init__(self) -> None:
        if self.area != None and type(self.area) is not list:
            raise ValueError("Filter class: area must be a list")

        # TODO: test filter with wrong Area
        # exception if any element in the list is not an Area Class
        if type(self.area) is list:
            i = 0
            for item in self.area:
                if type(item) is not Area:
                    raise ValueError(
                        f"Filter class: element {i} must be an Area Class")
                i += 1

        if self.characteristics != None and type(self.characteristics) is not list:
            raise ValueError("Filter class: area must be a list")

        # TODO: test filter with wrong Characteristic
        # exception if any element in the list is not an Area Class
        if type(self.characteristics) is list:
            i = 0
            for item in self.characteristics:
                if type(item) is not Characteristic:
                    raise ValueError(
                        f"Filter class: element {i} must be an Characteristic Class")
                i += 1

    '''
    Type is equal to Characteristic
    '''

    def __find_rows_containing_type(self, remain: pd.DataFrame, type: Characteristic):
        return remain.query(
            f"Types.str.contains('{type.value}', na=False)", engine="python"
        )

    def __find_rows_containing_attr_type(self, remain: pd.DataFrame, attrType: AttributeType):
        return remain.query(
            f"AttributeTypes.str.contains('{attrType.value}', na=False)", engine="python"
        )

    def __find_with_elements(self, data, listAttr: List[attribute_type]) -> pd.DataFrame:
        temp_data: pd.DataFrame = pd.DataFrame()
        # List of Attributes
        print(listAttr)
        for at in listAttr:
            remain_data = self.__get_remaining_data(data, temp_data)
            temp_data = pd.concat(
                [temp_data, self.__find_rows_containing_attr_type(remain_data, at)])

        return temp_data

    # attribute type is related with characteristics (Type)
    def __search_attr_type(self, data: pd.DataFrame, filterAttrType: FilterAttributeType):
        temp_data: pd.DataFrame = pd.DataFrame()

        # these FilterAttrTypes have a List[AttributeType]
        if filterAttrType == FilterAttributeType.CATEGORICAL or filterAttrType == FilterAttributeType.NUMERICAL:
            temp_data = self.__find_with_elements(data, filterAttrType.value)

        # MIXED has List[List[AttributeType]]
        # the result must have a least one element of categorical and numerical
        # TODO: test filter
        if filterAttrType == FilterAttributeType.MIXED:
            temp_data: pd.DataFrame = data
            # List of list of Attributes
            for attrType in filterAttrType.value:
                temp_data = self.__find_with_elements(temp_data, attrType)

        return temp_data.sort_index()

    def __find_rows_containing_Area(self, remain: pd.DataFrame, area: Area):
        # TODO: Business should search for Financial and Business
        # TODO: Computer science should search for Computer and Compute Science
        # TODO: LIFE_SCIENCE should search for Life and Life Science
        return remain[remain.Area == area.value]

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

        # TODO: Attribute type
        # TODO: create enum attribute type
        if self.attribute_type != None:
            data = self.__search_attr_type(
                data, self.attribute_type)

        # TODO: test area filter
        if self.area != None:

            temp_data: pd.DataFrame = pd.DataFrame()

            for item_area in self.area:
                temp_data = pd.concat([temp_data, self.__find_rows_containing_Area(
                    self.__get_remaining_data(data, temp_data), item_area)])

            data = temp_data.sort_index()

        # TODO: other task
        if self.task != None:
            data = data.query(f"Task == '{self.task.value}'")

        if self.num_attributes_less_than != None:
            data = data.query(
                f"numAttributes < {self.num_attributes_less_than}")
        if self.num_attributes_greater_than != None:
            data = data.query(
                f"numAttributes > {self.num_attributes_greater_than}")

        return data