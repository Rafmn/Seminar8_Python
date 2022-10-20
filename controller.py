import model
import view


def run():
    start = view.show_menu()
    if start == 1:
        res = model.csv_data_open()
        view.show_res(res)
    elif start == 2:
        in_info = view.add_info()
        model.add_info(in_info)
    elif start == 3:
        index = view.delete()
        model.del_info(index)
    elif start == 4:
        index, tel = view.change_tel()
        model.update_info(index, tel)


# run()
