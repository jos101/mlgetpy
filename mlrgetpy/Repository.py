from dataclasses import dataclass, field
from mlrgetpy.Filter import Filter

from mlrgetpy.util.Strutil import Strutil
from mlrgetpy.DataFrameConverter import DataFrameConverter
import pandas as pd
from mlrgetpy.RepoDownloader import RepodDownloader
from mlrgetpy.citation.CitationFactory import CitationFactory
from mlrgetpy.citation.FormatAbstract import FormatAbstract

from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.datasetlist.DataSetListFactory import DataSetListFactory
from mlrgetpy.filehandler.FileHandlerFactory import FileHandlerFactory
from mlrgetpy.enums.DataSetColumn import DataSetColumn as c

from rich.console import Console
from rich.table import Table
import rich

from mlrgetpy.log.ConfigLog import ConfigLog
from zipfile import ZipFile
import os
from mlrgetpy.enums.Paths import Paths
from pathlib import Path


@dataclass
class Repository:

    __data: pd.DataFrame = field(init=False, repr=False)
    __data_set_list: DataSetListAbstract = field(init=False, repr=False)
    __dfc: DataFrameConverter = field(init=False, repr=False)
    __structure: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__data_set_list = DataSetListFactory.create("cache_html")
        self.__dfc = DataFrameConverter()
        self.__data = pd.DataFrame()

    '''
    removes columns no needed in showdata
    '''

    def __filter(self) -> pd.DataFrame:

        cols_to_remove: list = ["userID", "introPaperID",
                                "DOI", "isTabular", "URLFolder",
                                "URLReadme", "URLLink", "Graphics", "Status",
                                "slug", "user"
                                ]

        data: pd.DataFrame = pd.DataFrame()
        data = self.__data.drop(cols_to_remove, axis=1)

        return data

    def load(self, filter: Filter = Filter()) -> None:

        d: dict = self.__data_set_list.findAll()

        data: pd.DataFrame = self.__dfc.convertFromList(d["datasets"])

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
                        str(index), row['Name'], row['Abstract'][0:100])
            console: Console = Console()
            console.print(table)

        if type == "box":
            count: int = 0
            for index, row in data.iterrows():
                count += 1
                if limit != None and count > limit:
                    break

                content = ""
                content += f"[cyan]Name : [magenta]{row[c.NAME.value]}\n"
                content += f"[cyan]DataSet Characteristic : [magenta]{row[c.TYPES.value]}\n"
                content += f"[cyan]Subject Area : [magenta]{row[c.AREA.value]}\n"
                content += f"[cyan]Associated Task : [magenta]{row[c.TASK.value]}\n"
                content += f"[cyan]Date Donated : [magenta]{row[c.DATE_DONATED.value]}\n"
                content += f"[cyan]Instances : [magenta]{row[c.NUM_INSTANCES.value]}\n"
                content += f"[cyan]Attributes : [magenta]{row[c.NUM_ATTRIBUTES.value]}\n"
                content += f"[cyan]Views : [magenta]{row[c.NUM_HITS.value]}\n"
                content += f"[cyan]Abstract: [magenta]{row[c.ABSTRACT.value]}\n"
                rich.print(
                    rich.panel.Panel(content, title=f"[cyan]ID: [magenta]{index}", expand=False, style="magenta"))

                answer = input("Next? yes(enter)/No(q):")
                if (answer == 'q'):
                    break

        if type == "box2":
            count: int = 0
            for index, row in data.iterrows():
                count += 1
                if limit != None and count > limit:
                    break

                print("┌" + "─"*100 + "┐")

                print("│"
                      + f"{str(index)[0:5]:5s}" + ": "
                      + f"{row['Name'][0:93]:93s}"
                      + "│")

                print("├"
                      + "─"*19 + "┬"
                      + "─"*19 + "┬"
                      + "─"*19 + "┬"
                      + "─"*19 + "┬"
                      + "─"*19 + "─"
                      + "┤")

                print("│"
                      + f"{'Instances'[0:19]:19s}" + "│"
                      + f"{'Attributes'[0:19]:19s}" + "│"
                      + f"{'Views'[0:19]:19s}" + "│"
                      + f'{"Associated Task"[0:19]:19s}' + "│"
                      + f"{('Subject Area')[0:19]:19s}" + " "
                      + "│")

                task: str = ""
                area: str = ""
                num_hits: int = 0
                num_instances: int = 0
                num_attr:  int = 0
                if row[c.TASK.value] != None:
                    task = row[c.TASK.value]
                if row[c.AREA.value] != None:
                    area = row[c.AREA.value]
                if row[c.NUM_HITS.value] != None:
                    num_hits = row[c.NUM_HITS.value]
                if row[c.NUM_INSTANCES.value] != None:
                    num_instances = row[c.NUM_INSTANCES.value]
                if row[c.NUM_ATTRIBUTES.value] != None:
                    num_attr = row[c.NUM_ATTRIBUTES.value]

                # print every task in a new line when there is no space (ID 540)
                task_list = Strutil.get_list(task, ",", 19)
                area_list = Strutil.get_list(area, ",", 19)
                for i in range(Strutil.get_max_length(task_list, area_list)):
                    num_instances_str = str(num_instances)
                    num_attr_str = str(num_attr)
                    num_hits_str = str(num_hits)
                    if i > 0:
                        num_instances_str = ""
                        num_attr_str = ""
                        num_hits_str = ""
                    print("│"
                          + f"{num_instances_str[0:19]:19s}" + "│"
                          + f"{num_attr_str[0:19]:19s}" + "│"
                          + f"{num_hits_str[0:19]:19s}" + "│"
                          + f"{Strutil.get_value(task_list, i):19s}" + "│"
                          + f"{Strutil.get_value(area_list, i):19s}" + " "
                          + "│")

                print("├"
                      + "─" * 19 + "┴"
                      + "─" * 19 + "┴"
                      + "─" * 19 + "┴"
                      + "─" * 19 + "┴"
                      + "─" * 19 + "─"
                      + "┤")

                abstract: str = row['Abstract'].replace("\n", " ")
                buffer: str = ""
                for word in abstract.split(" "):
                    prev_buffer = buffer
                    if buffer == "":
                        buffer = word
                    else:
                        buffer += " " + word

                    if len(buffer) > 98:
                        print("│" + f"{prev_buffer[0:100]:100s}" + "│")
                        buffer = word
                print("│" + f"{buffer[0:100]:100s}" + "│")

                print("└"+"─"*100+"┘")

            # ┌────┬───────────┬────────┬───────────┐
            # │    │   old url │ new url│ subfolders│
            # ├────┼───────────┼────────┼───────────┤
            # │ 713│           │     x  │     x     │
            # ├────┼───────────┼────────┼───────────┤
            # │ 299│     x     │        │           │
            # ├────┼───────────┼────────┼───────────┤
            # │ 432│     x     │        │     x     │
            # ├────┼───────────┼────────┼───────────┤
            # │ 692│     x     │        │           │
            # └────┴───────────┴────────┴───────────┘
                question = "Next? yes(enter)/No(q): "
                answer = input(question)
                if (answer == 'q'):
                    print("\033[A", end="")
                    print("\r", end="")
                    print(" " * (len(question) + len(answer)), end="\r")
                    break
                else:
                    print("\033[A", end="")
                    print("\r", end="")
                    print(" " * (len(question) + len(answer)), end="\r")

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
        ConfigLog.log.write_add_ids(IDs)

        # retrieves all data set list
        d: dict = self.__data_set_list.findAll()
        # converts dict to dataframe
        data: pd.DataFrame = self.__dfc.convertFromList(d["datasets"])
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
        ConfigLog.log.write_remove_indexes(indexes)
        self.__data = self.__data.drop(indexes)

    ''' add data set using the filter class '''

    def add_data_set(self, filter: Filter):
        d: dict = self.__data_set_list.findAll()
        data: pd.DataFrame = self.__dfc.convertFromList(d["datasets"])
        data = filter.filter(data)

        self.__data = self.__drop_ids(data.index.tolist(), self.__data)
        self.__data = pd.concat([self.__data, data])

    # TODO
    def download(self) -> None:
        # repodoenloader.py
        repDownloader = RepodDownloader()
        repo_names: list = repDownloader.download(self.__data)

        # search zip files
        zip_files = []
        for repo_name in repo_names:
            directory = os.path.join(
                Paths.ROOT_FOLDER.value, repo_name["name"])
            zip_files = zip_files + self.find_zip_files(directory)

        # unzip files
        for zip_file in zip_files:
            self.unzip(zip_file["zip"], zip_file["root"])

        # load in dataframe
        data_frames = {}
        self.__structure = ""
        for repo_name in repo_names:
            data_frames[repo_name["id"]] = {}
            data_files = []
            self.__structure += f"{repo_name['name']}\n"

            directory = os.path.join(
                Paths.ROOT_FOLDER.value, repo_name["name"])
            data_files = self.find_data_files(directory)

            pos = -1
            for data_file in data_files:
                pos += 1
                p = Path(data_file)

                sep = "├──"
                if pos == len(data_files) - 1:
                    sep = "└──"

                self.__structure += f"{sep}{p.name}\n"
                data_frames[repo_name["id"]][p.name] = pd.read_csv(data_file)

        return data_frames

    def unzip(self, zip_path: str, extract_path: str):
        with ZipFile(zip_path, 'r') as zObject:
            zObject.extractall(extract_path)

    def structure(self) -> str:
        return self.__structure

    # TODO
    def find_zip_files(self, path: str):
        zip_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".zip"):
                    zip_path = os.path.join(root, file)
                    zip_files.append({"root": root, "zip": zip_path})

        return zip_files

    def find_data_files(self, path: str):
        data_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".data") or file.endswith(".csv"):
                    path = os.path.join(root, file)
                    data_files.append(path)

        return data_files

    # TODO
    def explore(self) -> None:
        """Shows the files in the repositories
        """
        NotImplemented

    def share(self) -> str:
        """Create add by ID script to share with colleagues

        Returns:
            str: scripts to share with colleagues
        """

        script: str = "rep = New Repository()\n"
        script += f"rep.addByIDs({self.__data.index.tolist()})"

        return script
