import pandas as pd

class Solution():
    __artists_path = "data/lastfm_artist_list.csv"
    __scrobbles_path = "data/lastfm_user_scrobbles.csv"
    
    def __init__(self, n_items: int = 4) -> None:
        self.__target = None
        self.__n_items = n_items
        self.__artists_dict = None
        self.__scrobbles_df = None

    def load_data(self) -> bool:
        try:
            self.__artists_dict = pd.read_csv(self.__artists_path, index_col="artist_id")["artist_name"].to_dict()
        except:
            print("Ошибка загрузки данных об исполнителях!\n")
            return False
        try:
            self.__scrobbles_df = pd.read_csv(self.__scrobbles_path)
        except:
            print("Ошибка загрузки данных о прослушиваниях!\n")
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
            #TODO Добавить решение
            #Заглушка для тестирования
            import random
            return self.__get_names_from_indexes(random.sample(range(1, len(self.__artists_dict)), self.__n_items))
        except:
            return []
    
    def clear(self) -> None:
        self.__target = None
    
    def __get_id_by_name(self, name: str) -> int:
        return next((i for i, n in self.__artists_dict.items() if n == name), None)

    def __get_names_from_indexes(self, indexes: list) -> list:
        return [self.__artists_dict[i] for i in indexes]
