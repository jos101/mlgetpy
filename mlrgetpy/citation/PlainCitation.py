from dataclasses import dataclass
from datetime import datetime
from ..citation.Citation import Citation

from ..citation.FormatAbstract import FormatAbstract
from ..datasetlist.DataSetListAbstract import DataSetListAbstract
import dateutil.parser
import pandas as pd


@dataclass
class PlainCitation(FormatAbstract):

    def get(self, data_set_list: DataSetListAbstract, data: pd.DataFrame) -> list:
        citations = []
        cit = Citation()
        year = None
        DOI: str = None

        for repo_id, row in data.iterrows():

            if (row["DateDonated"] != None):
                year = dateutil.parser.isoparse(row["DateDonated"]).year

            if (row["DOI"] != None):
                DOI = row["DOI"]

            creators = data_set_list.getCreators(repo_id)

            citations.append(cit.getPlaintext(
                creators, row['Name'], year, DOI))

        return citations
