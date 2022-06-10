from dataclasses import dataclass
import pandas as pd

@dataclass
class DataFrameConverter:
    
    def convertFromList(self, rows: list) -> pd.DataFrame:
        dict = {}
        names = []
        for i in rows:
            names.append(i["Name"])

        dict["Names"] = names

        df = pd.DataFrame.from_dict(dict)

        return df
