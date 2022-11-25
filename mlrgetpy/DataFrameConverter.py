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
        dict["Status"] = []
        dict["NumHits"] = []
        dict["AttributeTypes"] = []
        dict["numInstances"] = []
        dict["slug"] = []

        dict["tabular"] = []
        dict["numAttributes"] = []
        dict["user"] = []
        dict["user_user"] = []
        dict["user_firstName"] = []
        dict["user_lastName"] = []

        for i in rows:
            dict["ID"].append(i["ID"])
            dict["userID"].append(i["userID"])
            dict["introPaperID"].append(i["introPaperID"])
            dict["Name"].append(i["Name"])

            dict["Abstract"].append(i["Abstract"])
            dict["Area"].append(i["Area"])

            dict["Task"].append(i["Task"])
            dict["Types"].append(i["Types"])
            dict["DOI"].append(i["DOI"])
            dict["DateDonated"].append(i["DateDonated"])

            dict["isTabular"].append(i["isTabular"])
            dict["URLFolder"].append(i["URLFolder"])

            if "URLReadme" in i.keys():
                dict["URLReadme"].append(i["URLReadme"])
            else:
                dict["URLReadme"].append(None)

            dict["URLLink"].append(i["URLLink"])

            dict["Graphics"].append(i["Graphics"])
            dict["Status"].append(i["Status"])
            dict["NumHits"].append(i["NumHits"])
            dict["AttributeTypes"].append(i["AttributeTypes"])

            dict["numInstances"].append(i["NumInstances"])
            dict["numAttributes"].append(i["NumAttributes"])

            dict["slug"].append(i["slug"])

            dict["tabular"].append(i["isTabular"])
            dict["user"].append(i["users"])

            dict["user_user"].append(None)
            dict["user_firstName"].append(None)
            dict["user_lastName"].append(None)

            if i["users"] != None:

                if "user" in i["users"].keys():
                    dict["user_user"][-1] = i["users"]["user"]

                if "firstName" in i["users"].keys():
                    dict["user_firstName"][-1] = i["users"]["firstName"]

                if "lastName" in i["users"].keys():
                    dict["user_lastName"][-1] = i["users"]["lastName"]

        df = pd.DataFrame.from_dict(dict)
        df = df.set_index('ID')

        return df
