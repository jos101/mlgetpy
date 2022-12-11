from dataclasses import dataclass
from mlrgetpy.JsonParser import JsonParser
import pandas as pd
from mlrgetpy.enums.DataSetColumn import DataSetColumn as c


@dataclass
class DataFrameConverter:

    def convertFromList(self, rows: list) -> pd.DataFrame:
        dict = {}

        dict[c.ID.value] = []
        dict[c.USER_ID.value] = []
        dict[c.INTRO_PAPER_ID.value] = []
        dict[c.NAME.value] = []
        dict[c.ABSTRACT.value] = []
        dict[c.AREA.value] = []
        dict[c.TASK.value] = []
        dict[c.TYPES.value] = []

        dict[c.DOI.value] = []
        dict[c.DATE_DONATED.value] = []

        dict[c.IS_TABULAR.value] = []
        dict[c.URL_FOLDER.value] = []
        dict[c.URL_README.value] = []
        dict[c.URL_LINK.value] = []

        dict[c.GRAPHICS.value] = []
        dict[c.STATUS.value] = []
        dict[c.NUM_HITS.value] = []
        dict[c.ATTRIBUTE_TYPES.value] = []

        dict[c.NUM_INSTANCES.value] = []
        dict[c.SLUG.value] = []

        dict[c.NUM_ATTRIBUTES.value] = []
        dict[c.USER.value] = []
        dict[c.USER_USER.value] = []
        dict[c.USER_FIRSTNAME.value] = []
        dict[c.USER_LASTNAME.value] = []

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

            dict[c.NUM_INSTANCES.value].append(i[c.NUM_INSTANCES.value])
            dict[c.NUM_ATTRIBUTES.value].append(i[c.NUM_ATTRIBUTES.value])

            dict[c.SLUG.value].append(i[c.SLUG.value])

            dict[c.USER.value].append(i[c.USERS.value])

            dict[c.USER_USER.value].append(None)
            dict[c.USER_FIRSTNAME.value].append(None)
            dict[c.USER_LASTNAME.value].append(None)

            if i[c.USERS.value] != None:

                if c.USER.value in i[c.USERS.value].keys():
                    dict[c.USER_USER.value][-1] = i[c.USERS.value][c.USER.value]

                if c.FIRSTNAME.value in i[c.USERS.value].keys():
                    dict[c.USER_FIRSTNAME.value][-1] = i[c.USERS.value][c.FIRSTNAME.value]

                if c.LASTNAME.value in i[c.USERS.value].keys():
                    dict[c.USER_LASTNAME.value][-1] = i[c.USERS.value][c.LASTNAME.value]

        df = pd.DataFrame.from_dict(dict)
        df = df.set_index(c.ID.value)

        return df
