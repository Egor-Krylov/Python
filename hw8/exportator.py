import json

fields = ["Фамилия", "Имя", "Отчество", "Пол", "Должность", "Дата рождения", "Номера телефонов (через пробел)", "Зарплата"]

def get_next_id():
    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw8\database.json", 'r') as file:
        # file.write(json.dump(get_dict_from_data(exp.get_next_id(), data), ))
        allData = json.load(file)
        if (len(allData.keys()) > 0):
            return max([int(i) for i in allData.keys()]) + 1
        else:
            return 0

def get_all_data():
    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw8\database.json", 'r') as file:
        return json.load(file)

def get_all_data_in_string():
    str = ''
    allData = get_all_data()
    for i in allData.keys():
        phones = ' '.join(allData[i]["phones"])
        str += f'\n{i}: \nФамилия: {allData[i]["1name"]} \nимя: {allData[i]["2name"]} \nотчество: {allData[i]["3name"]}  \nпол: {allData[i]["sex"]} \nдолжность: {allData[i]["position"]} \nдень рождения: {allData[i]["birthdate"]} \nтелефоны: {phones} \nзарплата: {allData[i]["salary"]} \n'
    
    return str
    
def get_all_data_filtered(filter_field, filter_value):
    filter_index = fields.index(filter_field)
    str = ''
    allData = get_all_data()
    for i in allData.keys():
        list = get_account_in_list(i)
        if (filter_value in list[filter_index]):
            phones = ' '.join(allData[i]["phones"])
            str += f'\n{i}: \nФамилия: {allData[i]["1name"]} \nимя: {allData[i]["2name"]} \nотчество: {allData[i]["3name"]}  \nпол: {allData[i]["sex"]} \nдолжность: {allData[i]["position"]} \nдень рождения: {allData[i]["birthdate"]} \nтелефоны: {phones} \nзарплата: {allData[i]["salary"]} \n'
        
    return str

def get_account_in_list(id):
    allData = get_all_data()
    account = allData[id]
    return [account["1name"], account["2name"], account["3name"], account["sex"], account["position"], account["birthdate"], ' '.join(account["phones"]), account["salary"]]