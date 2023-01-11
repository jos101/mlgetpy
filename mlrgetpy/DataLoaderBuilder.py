from mlrgetpy.DataLoader import DataLoader
from mlrgetpy.DataLoaderCSV import DataLoaderCSV
from mlrgetpy.DataLoaderError import DataLoaderError
from mlrgetpy.DataLoaderxls import DataLoaderxls


class DataLoaderBuilder:

    def create(data_file: str) -> DataLoader:
        dataloader: DataLoader = DataLoaderError()

        if data_file.lower().endswith(".data") or data_file.lower().endswith(".dat"):
            dataloader = DataLoaderCSV()
        elif data_file.lower().endswith(".xls") or data_file.lower().endswith(".xlsx"):
            dataloader = DataLoaderxls()

        return dataloader
