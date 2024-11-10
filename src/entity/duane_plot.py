from os import PathLike
import pandas as pd
import numpy as np


class PlotEntity:
    def __init__(self, data_path: PathLike, title: str):
        self.data_path = data_path
        self.title = title
        self.__columns_to_transform = ["i", "t_i"]
        self.data = self.get_data()

    def plot(self, ax):
        self.data.plot(x="log_t_i", y="log_i", kind="scatter", ax=ax)

    def __read_data(self) -> pd.DataFrame:
        return pd.read_csv(self.data_path)

    def __transform(self) -> pd.DataFrame:
        data = self.__read_data()
        for i in self.__columns_to_transform:
            data["log_" + i] = np.log(data[i])
        return data

    def get_data(self) -> pd.DataFrame:
        return self.__transform()
