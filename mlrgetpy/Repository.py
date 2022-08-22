from dataclasses import dataclass, field
from mlrgetpy.citation.Bibtext import Bibtext

from mlrgetpy.citation.Citation import Citation
from mlrgetpy.DataFrameConverter import DataFrameConverter
import pandas as pd
from mlrgetpy.filehandler.BibFileHandler import BibFileHandler
from mlrgetpy.citation.CitationFactory import CitationFactory
from mlrgetpy.citation.FormatAbstract import FormatAbstract

from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.datasetlist.DataSetListFactory import DataSetListFactory
from mlrgetpy.filehandler.FileHandlerFactory import FileHandlerFactory


@dataclass
class Repository:

    __data: pd.DataFrame = field(init=False, repr=False)
    __data_set_list: DataSetListAbstract = field(init=False, repr=False)
    __dfc: DataFrameConverter = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__data_set_list = DataSetListFactory.create("CACHE")
        self.__dfc = DataFrameConverter()
        self.__data = pd.DataFrame()

    '''
    removes columns no needed in showdata
    '''

    def __filter(self) -> pd.DataFrame:

        cols_to_remove: list = ["userID", "introPaperID",
                                "DOI", "isTabular", "URLFolder",
                                "URLReadme", "URLLink", "Graphics", "Status",
                                "slug", "tabular", "user"
                                ]

        data: pd.DataFrame = pd.DataFrame()
        data = self.__data.drop(cols_to_remove, axis=1)

        return data

    def load(self, name: str = None, num_instances_less_than: int = None,
             num_instances_greater_than: int = None,
             contains_name: str = None,
             query: str = None) -> None:

        d: dict = self.__data_set_list.findAll()
        data: pd.DataFrame = self.__dfc.convertFromList(d["payload"]["rows"])

        # TODO: add more filters
        # TODO: create a class for the filters

        if query != None:
            data = data.query(query)
        if name != None:
            data = data.query(f"Name == '{name}'")
        if contains_name != None:
            data = data.query(
                f'Name.str.contains("{contains_name}")', engine='python')
        if num_instances_less_than != None:
            data = data.query(f"numInstances < {num_instances_less_than}")
        if num_instances_greater_than != None:
            data = data.query(f"numInstances > {num_instances_greater_than}")

        self.__data = data

    def getData(self) -> pd.DataFrame:

        data: pd.DataFrame = self.__filter()
        return data

    def showData(self) -> None:
        # TODO: show data with the rich module

        if self.__data is None:
            print("Load data first")
            return

        data: pd.DataFrame = self.__filter()

        for index, row in data.iterrows():
            print(f"Name : {row['Name']}")
            print(f"DataSet Characteristic : {row['Types']}")
            print(f"Subject Area : {row['Area']}")
            print(f"Associated Task : {row['Task']}")
            print(f"Date Donated : {row['DateDonated']}")
            print(f"Instances : {row['numInstances']}")
            print(f"Attributes : {row['numAttributes']}")
            print(f"Views : {row['NumHits']}")
            print(f"Abstract: {row['Abstract']}")
            print("-----------------------------")

    def extractCitation(self, ids: list, type: str = "bibtext") -> str:

        citations_list: list = []
        bib: FormatAbstract = CitationFactory.create(type)

        data = self.__data.filter(items=ids, axis="index")
        citations_list = bib.get(self.__data_set_list, data)

        return citations_list

    def saveCitations(self, limit: int = None, type: str = "bibtext") -> list:

        ids: list = self.__data.index.tolist()
        citations: list = self.extractCitation(ids[:limit], type)

        f = FileHandlerFactory.create(type)
        f.save(citations)

        return citations

    def addByIDs(self, IDs: list) -> None:
        # retrieves all data set list
        d: dict = self.__data_set_list.findAll()
        # converts dict to dataframe
        data: pd.DataFrame = self.__dfc.convertFromList(d["payload"]["rows"])
        # filters the dataFrame
        data = data.filter(items=IDs, axis="index")

        # to avoid duplicates ids, removes it from __data
        for id in IDs:
            if id in self.__data.index:
                self.__data.drop(IDs, axis="index", inplace=True)

        # adds the new data to __data
        self.__data = pd.concat([self.__data, data])

    def removeByIndex(self, indexes: list) -> None:
        self.__data = self.__data.drop(indexes)

    # TODO: add data set using the filter class
    def add_data_set(self):
        NotImplemented

    def download(self) -> None:
        NotImplemented

    def remove(self):
        NotImplemented
