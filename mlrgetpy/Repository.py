from dataclasses import dataclass, field
from mlrgetpy.Filter import Filter

from mlrgetpy.DataFrameConverter import DataFrameConverter
import pandas as pd
from mlrgetpy.citation.CitationFactory import CitationFactory
from mlrgetpy.citation.FormatAbstract import FormatAbstract

from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.datasetlist.DataSetListFactory import DataSetListFactory
from mlrgetpy.filehandler.FileHandlerFactory import FileHandlerFactory

from rich.console import Console
from rich.table import Table


@dataclass
class Repository:

    __data: pd.DataFrame = field(init=False, repr=False)
    __data_set_list: DataSetListAbstract = field(init=False, repr=False)
    __dfc: DataFrameConverter = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__data_set_list = DataSetListFactory.create("cache")
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

    def load(self, filter: Filter = Filter()) -> None:

        d: dict = self.__data_set_list.findAll()
        data: pd.DataFrame = self.__dfc.convertFromList(d["payload"]["rows"])

        data = filter.filter(data)
        self.__data = data

    def getData(self) -> pd.DataFrame:

        data: pd.DataFrame = self.__filter()
        return data
    '''
    show data
    limit: The maximun to display
    type: table to show a table with ID, Name an aditional column, line to show as boxes 
    '''

    def showData(self, limit: int = None, type="table", column="Abstract") -> None:
        # TODO: show data with the rich module
        table: Table = Table(title="Data Set", style="green4")

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Name", style="magenta")
        if column == "Characteristic":
            table.add_column("Data set Characteristic", style="magenta")
        if column == "Area":
            table.add_column("Subject Area", style="magenta")
        if column == "Task":
            table.add_column("Associated Task", style="magenta")
        if column == "DateDonated":
            table.add_column("Date Donated", style="magenta")
        if column == "numInstances":
            table.add_column("Instances", style="magenta")
        if column == "numAttributes":
            table.add_column("Attributes", style="magenta")
        if column == "Views":
            table.add_column("Views", style="magenta")
        if column == "Abstract":
            table.add_column("Abstract", style="magenta", no_wrap=True)

        if self.__data is None:
            print("Load data first")
            return

        data: pd.DataFrame = self.__filter()

        if type == "table":
            count: int = 0
            for index, row in data.iterrows():
                count += 1
                if limit != None and count > limit:
                    break

                if column == "Characteristic":
                    table.add_row(str(index), row['Name'], row['Types'])
                if column == "Area":
                    table.add_row(str(index), row['Name'], row['Area'])
                if column == "Task":
                    table.add_row(str(index), row['Name'], row['Task'])
                if column == "DateDonated":
                    table.add_row(str(index), row['Name'], row['DateDonated'])
                if column == "numInstances":
                    table.add_row(str(index), row['Name'], str(
                        row['numInstances']))
                if column == "numAttributes":
                    table.add_row(
                        str(index), row['Name'], str(row['numAttributes']))
                if column == "Views":
                    table.add_row(str(index), row['Name'], str(row['NumHits']))
                if column == "Abstract":
                    table.add_row(
                        str(index), row['Name'], row['Abstract'][0:50])
            console: Console = Console()
            console.print(table)

        if type == "box":
            count: int = 0
            for index, row in data.iterrows():
                count += 1
                if limit != None and count > limit:
                    break
                from rich import print
                from rich.panel import Panel

                content = ""
                content += f"[cyan]Name : [magenta]{row['Name']}\n"
                content += f"[cyan]DataSet Characteristic : [magenta]{row['Types']}\n"
                content += f"[cyan]Subject Area : [magenta]{row['Area']}\n"
                content += f"[cyan]Associated Task : [magenta]{row['Task']}\n"
                content += f"[cyan]Date Donated : [magenta]{row['DateDonated']}\n"
                content += f"[cyan]Instances : [magenta]{row['numInstances']}\n"
                content += f"[cyan]Attributes : [magenta]{row['numAttributes']}\n"
                content += f"[cyan]Views : [magenta]{row['NumHits']}\n"
                content += f"[cyan]Abstract: [magenta]{row['Abstract']}\n"
                print(
                    Panel(content, title=f"[cyan]ID: [magenta]{index}", expand=False, style="magenta"))

    def extractCitation(self, ids: list, type: str = "bibtext") -> str:

        citations_list: list = []
        bib: FormatAbstract = CitationFactory.create(type)

        data = self.__data.filter(items=ids, axis="index")
        citations_list = bib.get(self.__data_set_list, data)

        return citations_list

    def saveCitations(self, type: str = "bibtext", limit: int = None) -> list:

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
        self.__data = self.__drop_ids(IDs, self.__data)
        # adds the new data to __data
        self.__data = pd.concat([self.__data, data])

    def __drop_ids(self, IDs: list, data: pd.DataFrame):
        for id in IDs:
            if id in data.index:
                data.drop(id, axis="index", inplace=True)
        return data

    def removeByIndex(self, indexes: list) -> None:
        self.__data = self.__data.drop(indexes)

    ''' add data set using the filter class '''

    def add_data_set(self, filter: Filter):
        d: dict = self.__data_set_list.findAll()
        data: pd.DataFrame = self.__dfc.convertFromList(d["payload"]["rows"])
        data = filter.filter(data)

        self.__data = self.__drop_ids(data.index.tolist(), self.__data)
        self.__data = pd.concat([self.__data, data])

    def download(self) -> None:
        NotImplemented

    # TODO: Remove
    def remove(self):
        NotImplemented

    '''
    create add by ID script to share with colleagues
    '''
    # TODO: create add by ID script to share with colleagues

    def share(self) -> str:

        script: str = "rep = New Repository()\n"
        script += f"rep.addByIDs({self.__data.index.tolist()})"

        return script
