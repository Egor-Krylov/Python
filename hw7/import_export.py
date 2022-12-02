
def export_all():
    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw7\database.txt", 'r') as file:
        data = ''
        for i in file:
            data += i
        return data
    
def import_data(data):
    with open(r"C:\Users\Егор\Desktop\GeekBrains\Python\hw7\database.txt", 'a') as file:
        print(data + " added to database")
        file.write(data + '\n')
    
    