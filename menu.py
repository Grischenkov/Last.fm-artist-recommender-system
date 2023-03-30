class Menu():
    def __init__(self, items: list) -> None:
        self.__items = items
        self.__selection = None

    @property
    def selection(self) -> str:
        return self.__selection

    def show(self) -> None:
        print("\n".join(f"{index + 1}: {value}" for index, value in enumerate(self.__items)))
        self.__get_selection()

    def clear(self) -> None:
        self.__selection = None

    def __get_selection(self) -> None:
        while True:
            try:
                self.__selection = self.__items[self.__get_input() - 1]
                return
            except:
                print(f"Некорректный ввод!")

    def __get_input(self) -> int:
        while True:
            try:
                return int(input(f"Выбор: "))
            except:
                print(f"Некорректный ввод!")
