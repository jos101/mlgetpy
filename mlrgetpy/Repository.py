from dataclasses import dataclass, field

from mlrgetpy.Citation import Citation
from mlrgetpy.DataFrameConverter import DataFrameConverter
import pandas as pd

from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from mlrgetpy.datasetlist.DataSetListFactory import DataSetListFactory

from datetime  import datetime


@dataclass
class Repository:
    
    __data : pd.DataFrame = field(init=False, repr=False)
    __data_set_list : DataSetListAbstract = field(init=False, repr=False)
    __dfc : DataFrameConverter = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.__data_set_list = DataSetListFactory.create("CACHE")
        self.__dfc = DataFrameConverter()
        self.__data = pd.DataFrame()

    def __filter(self) -> pd.DataFrame:

        cols_to_remove:list = [ "userID", "introPaperID",
            "DOI", "isTabular", "URLFolder",
            "URLReadme", "URLLink", "Graphics", "Status",
             "slug", "tabular", "user"
        ]

        data:pd.DataFrame = pd.DataFrame()
        data = self.__data.drop(cols_to_remove, axis=1)

        return data


    def load(self) -> None:
        d  : dict        = self.__data_set_list.findAll()
        data : pd.DataFrame = self.__dfc.convertFromList(d["payload"]["rows"])
        self.__data = data
    
    def getData(self) -> pd.DataFrame:

        data:pd.DataFrame = self.__filter()
        return data
    
    def showData(self) -> None:

        if self.__data is None: 
            print("Load data first")
            return 

        data:pd.DataFrame = self.__filter()
        
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
        
    def extractCitation(self, ids:list, type:str = "bibtext") -> str :
        
        citations_str:str = ""
        cit = Citation()
        if type == "bibtext":
            data = self.__data.filter(items=ids, axis="index")

            for repo_id, row in data.iterrows():
                year = datetime.strptime(row["DateDonated"], '%Y-%m-%d').year
                
                creators = self.__data_set_list.getCreators(repo_id)
                citations_str = cit.getBibtext(creators, row['Name'], year, repo_id)

        return citations_str

    def addByIDs(self, IDs:list) -> None:
        d : dict = self.__data_set_list.findAll()
        data: pd.DataFrame = self.__dfc.convertFromList( d["payload"]["rows"])
        data = data.filter(items=IDs, axis="index")

        for id in IDs:
            if id in self.__data.index:
                self.__data.drop(IDs, axis="index", inplace=True)
            
        self.__data = pd.concat([self.__data, data])


    def removeByIndex(self, indexes: list) -> None:
        self.__data = self.__data.drop(indexes)

    def download() -> None :
        NotImplemented
    
    def remove():
        NotImplemented