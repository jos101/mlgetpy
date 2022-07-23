from dataclasses import dataclass, field
from mlrgetpy.Citation import Citation
import pandas as pd
from mlrgetpy.datasetlist.DataSetListAbstract import DataSetListAbstract
from datetime  import datetime

@dataclass
class Bibtext:


    def get(self, data_set_list: DataSetListAbstract, data: pd.DataFrame) -> list:
        citations = []
        cit = Citation()
        
        for repo_id, row in data.iterrows(): 

            if (row["DateDonated"] == None): continue
            
            year = datetime.strptime(row["DateDonated"], '%Y-%m-%d').year
            
            creators = data_set_list.getCreators(repo_id)
            citations.append(cit.getBibtext(creators, row['Name'], year, repo_id) )
        
        return citations