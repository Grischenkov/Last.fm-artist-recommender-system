from menu import Menu

end_menu = None
start_menu = None
restart_menu = None

def main():
    while start_menu.selection != "Выйти":
        end_menu.clear()
        start_menu.clear()
        start_menu.show()
        if start_menu.selection == "Начало работы":
            #TODO Получить имя группы
            #TODO Найти похожие
            #TODO Вывести похожие
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
    #TODO инициализация решения (загрузка данных)
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
