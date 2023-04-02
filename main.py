import os

from menu import Menu
from solution import Solution

solution = None
end_menu = None
start_menu = None
restart_menu = None

def main():
    while start_menu.selection != "Выйти":
        os.system('cls' if os.name == 'nt' else 'clear')
        solution.clear()
        end_menu.clear()
        start_menu.clear()
        start_menu.show()
        if start_menu.selection == "Начало работы":
            #Получить имя исполнителя от пользователя
            while True:
                if solution.get_name():
                    break
                else:
                    restart_menu.clear()
                    restart_menu.show()
                    if restart_menu.selection == "Повторить":
                        pass
                    elif restart_menu.selection == "Выйти":
                        return
            #Вывести похожие
            print("Похожие: " + ", ".join(solution.get_n_similar()) + "\n")
            while end_menu.selection != "Перезапустить":
                end_menu.show()
                if end_menu.selection == "Перезапустить":
                    pass
                elif end_menu.selection == "Выйти":
                    return
        elif start_menu.selection == "Выйти":
            return
    return

if __name__ == "__main__":
    solution = Solution()
    if solution.load_data():
        end_menu = Menu(
            items = [
                "Перезапустить",
                "Выйти"
            ]
        )
        start_menu = Menu(
            items = [
                "Начало работы",
                "Выйти"
            ]
        )
        restart_menu = Menu(
            items = [
                "Повторить",
                "Выйти"
            ]
        )
        main()
    else:
        input("Нажмите любую клавишу для выхода...")
