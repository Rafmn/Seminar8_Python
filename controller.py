import model
import view


def run():
    start = view.show_menu()
    if start == 1:
        res = model.csv_data_open()
        view.show_res(res)
    elif start == 2:
        # in_info = view.add_info()
        # model.add_info(in_info)
        add_again = 0   # Добавление повторного запроса на ввод информации
        while add_again != 1:
            in_info = view.add_info()
            model.add_info(in_info)
            add_again = view.add_info_again()
    elif start == 3:
        view.show_res(model.csv_data_open()) # Добавлен вывод списка
        index = view.delete()
        model.del_info(index)
    elif start == 4:
        view.show_res(model.csv_data_open()) # Добавлен вывод списка
        index, tel = view.change_tel()
        model.update_info(index, tel)
    elif start == 5:     # Добавлена возможность экспорта записей в txt формат
        model.import_into_csv()
        view.show_export_txt()
        


# run()
