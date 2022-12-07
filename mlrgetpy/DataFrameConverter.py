from dataclasses import dataclass
from mlrgetpy.JsonParser import JsonParser
import pandas as pd
from mlrgetpy.enums.DataSetColumn import DataSetColumn as c


@dataclass
class DataFrameConverter:

    def convertFromList(self, rows: list) -> pd.DataFrame:
        dict = {}

        # TODO: use enum
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
            dict[c.ID.value].append(i[c.ID.value])
            dict[c.USER_ID.value].append(i[c.USER_ID.value])
            dict[c.INTRO_PAPER_ID.value].append(i[c.INTRO_PAPER_ID.value])
            dict[c.NAME.value].append(i[c.NAME.value])

            dict[c.ABSTRACT.value].append(i[c.ABSTRACT.value])
            dict[c.AREA.value].append(i[c.AREA.value])

            dict[c.TASK.value].append(i[c.TASK.value])
            dict[c.TYPES.value].append(i[c.TYPES.value])
            dict[c.DOI.value].append(i[c.DOI.value])
            dict[c.DATE_DONATED.value].append(i[c.DATE_DONATED.value])

            dict[c.IS_TABULAR.value].append(i[c.IS_TABULAR.value])
            dict[c.URL_FOLDER.value].append(i[c.URL_FOLDER.value])

            if c.URL_README.value in i.keys():
                dict[c.URL_README.value].append(i[c.URL_README.value])
            else:
                dict[c.URL_README.value].append(None)

            dict[c.URL_LINK.value].append(i[c.URL_LINK.value])

            dict[c.GRAPHICS.value].append(i[c.GRAPHICS.value])
            dict[c.STATUS.value].append(i[c.STATUS.value])
            dict[c.NUM_HITS.value].append(i[c.NUM_HITS.value])
            dict[c.ATTRIBUTE_TYPES.value].append(i[c.ATTRIBUTE_TYPES.value])

            dict["numInstances"].append(i[c.NUM_INSTANCES.value])
            dict["numAttributes"].append(i[c.NUM_ATTRIBUTES.value])

            dict[c.SLUG.value].append(i[c.SLUG.value])

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
        df = df.set_index(c.ID.value)

        return df
