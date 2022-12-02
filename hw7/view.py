

def view_one_line(data):
    print(data)

def view_new_line(data):
    # result = []
    for i in data.split('\n'):
        print('')
        for j in i.split(' '):
            print(j)
    
    # print(data.join("\n"))