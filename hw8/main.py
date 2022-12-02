import easygui as eg
import importator as imp
import exportator as exp
regimes1 = ["Добавить/редактировать данные", "Вывести данные"]
regimes2 = ["Добавить данные", "Редактировать данные"]
buttons = ["Фамилия", "Имя", "Отчество", "Пол", "Должность", "Дата рождения", "Номер телефона", "Зарплата", "Без фильтра"]
fields = exp.fields

while 1:
    if eg.buttonbox("Что нужно сделать?", "Вопрос", regimes1) == regimes1[0]:
        if eg.buttonbox("Что нужно сделать?", "Вопрос", regimes2) == regimes2[0]:
            imp.import_new_account(eg.multenterbox("Введите данные нового работника", "Новый работник", exp.fields))
        else:
            id = eg.enterbox("Введите id работника", "Скорректировать данные", "id")
            imp.change_existing_account(id, eg.multenterbox("Введите данные работника", "Изменить работника", exp.fields, exp.get_account_in_list(id)))
    else:
        filterfield = eg.buttonbox("По какому полю создать фильтр?", "Фильтр", buttons)
        if filterfield == buttons[-1]:
            eg.textbox('', '', exp.get_all_data_in_string())
        else:
            eg.textbox('', '', exp.get_all_data_filtered(filterfield, eg.enterbox("Введите значение для поиска: ", "Фильтр")))
    if not eg.ccbox("Продолжить работу?", "Вопрос", ['Продолжить','Закончить']):
        break



