import csv


def csv_data_open():      # 1 - показать все
    with open("010_Seminar10/csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res


def add_info(list):  # 2- добавление информации
    with open("010_Seminar10/csv_data.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)

# list=['Мама', 'папа',  '25544']
# add_info(list)



def del_info(index):  # удаление информации
    list_csv = csv_data_open()
    print(list_csv)
    del list_csv[index]
    with open("010_Seminar10/csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


# add_info(2)
def update_info(index, tel):  # обнавление информации
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("010_Seminar10/csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)

# update_info(0, '+7(495)469476')
