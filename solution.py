import pickle

import pandas as pd

class Solution():
    __model_path = "research/als.pkl"
    __artists_path = "data/lastfm_artist_list.csv"
    
    def __init__(self, n_items: int = 4) -> None:
        self.__model = None
        self.__target = None
        self.__n_items = n_items
        self.__artists_dict = None

    def load_data(self) -> bool:
        try:
            self.__artists_dict = pd.read_csv(self.__artists_path, index_col="artist_id")["artist_name"].to_dict()
        except:
            print("Ошибка загрузки данных об исполнителях!\n")
            return False
        try:
            with open(self.__model_path, "rb") as f:
                self.__model = pickle.load(f)
        except:
            print("Ошибка загрузки модели!\n")
            return False
        return True
    
    def get_name(self) -> bool:
        try:
            print()
            self.__target = int(self.__get_id_by_name(input(f"Имя исполнителя: ")))
            return True
        except:
            print(f"Исполнитель не найден!\n")
            return False

    def get_n_similar(self) -> list:
        try:
            indices, distances = self.__model.similar_items(self.__target-1, N=5, filter_items=[self.__target-1])
            return self.__get_names_from_indexes([x+1 for x in indices])
        except:
            return []
    
    def clear(self) -> None:
        self.__target = None

    def __get_id_by_name(self, name: str) -> int:
        return next((i for i, n in self.__artists_dict.items() if n == name), None)

    def __get_names_from_indexes(self, indexes: list) -> list:
        return [self.__artists_dict[i] for i in indexes]
