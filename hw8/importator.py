import json
import exportator as exp

def import_new_account(data):
    allData = dict()
    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw8\database.json", 'r') as file:        
        allData = json.load(file)

    allData[exp.get_next_id()] = get_dict_from_data(data)

    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw8\database.json", 'w') as file:
        json.dump(allData, file)


def get_dict_from_data(data):
    return {"1name": data[0], "2name":data[1],  "3name":data[2], "sex": data[3], "position": data[4], "birthdate": data[5], "phones": data[6].split(), "salary": data[7]}

def change_existing_account(id, data):
    allData = exp.get_all_data()
    allData[id] = get_dict_from_data(data)
    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw8\database.json", 'w') as file:
        json.dump(allData, file)