from dataclasses import dataclass
import pandas as pd

@dataclass
class DataFrameConverter:
    
    def convertFromList(self, rows: list) -> pd.DataFrame:
        dict = {} 

        dict["ID"] = []
        dict["userID"] = []
        dict["introPaperID"] = []
        dict["Name"] = []
        dict["Abstract"] = []
        dict["Area"] = []
        dict["Task"] = []
        dict["Types"] = []

        dict["DOI"] = []
        dict["DateDonated"] = []

        dict["isTabular"] = []
        dict["URLFolder"] = []
        dict["URLReadme"] = []
        dict["URLLink"] = []

        dict["Graphics"] = []
        dict["Status"]  = []
        dict["NumHits"] = []
        dict["AttributeTypes"] =  []
        dict["numInstances"] = []
        dict["slug"] = []

        dict["tabular"] = []
        dict["user"] = []

        for i in rows:
            dict["ID"].append( i["ID"] )
            dict["userID"].append( i["userID"] )
            dict["introPaperID"].append( i["introPaperID"] )
            dict["Name"].append( i["Name"] )

            dict["Abstract"].append( i["Abstract"] )
            dict["Area"].append( i["Area"] )

            dict["Task"].append( i["Task"] )
            dict["Types"].append( i["Types"] )
            dict["DOI"].append( i["DOI"] )
            dict["DateDonated"].append( i["DateDonated"] )

            dict["isTabular"].append( i["isTabular"] )
            dict["URLFolder"].append( i["URLFolder"] )
            dict["URLReadme"].append( i["URLReadme"] )
            dict["URLLink"].append( i["URLLink"] )

            dict["Graphics"].append( i["Graphics"] )
            dict["Status"].append( i["Status"] )
            dict["NumHits"].append( i["NumHits"] )
            dict["AttributeTypes"].append( i["AttributeTypes"] )
            dict["numInstances"].append( i["numInstances"] ) 
            dict["slug"].append( i["slug"] )    

            dict["tabular"].append( i["tabular"] )    
            dict["user"].append( i["user"] )    

        df = pd.DataFrame.from_dict(dict)
        df = df.set_index('ID')

        return df
