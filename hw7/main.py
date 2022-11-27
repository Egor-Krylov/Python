import import_export as ie
import view

while True:
    regime = input("Введите 1, если хотите добавить данные, 2, если отобразить данные, другое, чтобы выйти: ")
    if regime == '1':
        ie.import_data(input("Введите ФИО абонента и номер телефона через пробел: "))
    elif regime == '2':
        if input("Введите 1, если хотите отобразить данные по абоненту в строке, 2, если нужно отобразить каждый пункт записи в отдельной строке: 78") == '1':
            view.view_one_line(ie.export_all())
        else:
            view.view_new_line(ie.export_all())
    else:
        break