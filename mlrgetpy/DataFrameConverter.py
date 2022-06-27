from dataclasses import dataclass
from mlrgetpy.JsonParser import JsonParser 
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
        dict["numAttributes"] = []
        dict["user"] = []
        dict["user_user"] = []
        dict["user_firstName"] = []
        dict["user_lastName"] = []


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

            dict["user_user"].append(None)
            dict["user_firstName"].append(None)
            dict["user_lastName"].append(None)

            if i["user"] != None :

                if "user" in i["user"].keys():
                    dict["user_user"][-1] = i["user"]["user"]
                
                if "firstName" in i["user"].keys():
                    dict["user_firstName"][-1] = i["user"]["firstName"]

                if "lastName" in i ["user"].keys():
                    dict["user_lastName"][-1] = i["user"]["lastName"]

            if i["tabular"] != None and "numAttributes" in i["tabular"].keys():
                dict["numAttributes"].append( i["tabular"]["numAttributes"] )
            else:
                dict["numAttributes"].append(0)

        df = pd.DataFrame.from_dict(dict)
        df = df.set_index('ID')

        return df
