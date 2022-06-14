from dataclasses import dataclass
import pandas as pd

@dataclass
class DataFrameConverter:
    
    def convertFromList(self, rows: list) -> pd.DataFrame:
        dict = {} 

        ID = []
        userID = []
        introPaperID  = []
        Name  = []
        Abstract  = []
        Area  = []
        Task  = []
        Types  = []
        DOI  = []
        DateDonated  = []
        isTabular  = []
        URLFolder  = []
        URLReadme  = []
        URLLink  = []
        Graphics  = []
        Status  = []
        NumHits  = []
        AttributeTypes  = []
        numInstances  = []
        slug  = []
        

        dict["ID"] = []
        dict["userID"] = []
        dict["introPaperID"] = []
        dict["Name"] = []
        dict["Abstract"] = []
        dict["Area"] = []
        dict["Task"] = []

        for i in rows:
            dict["ID"].append(i["ID"])
            dict["userID"].append(i["userID"])
            dict["introPaperID"].append(i["introPaperID"])
            dict["Name"].append(i["Name"])

            dict["Abstract"].append(i["Abstract"])
            dict["Area"].append(i["Area"])

            dict["Task"].append(i["Task"])


        

        df = pd.DataFrame.from_dict(dict)

        return df
