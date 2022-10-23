n = int(input('Введите длину массива: '))

list = [1, 0, 1]
for i in range(n - 1):
    list.append(list[-1] + list[-2])
    if (i % 2):
        list.insert(0, list[-1])
    else :
        list.insert(0, -list[-1])
print(list)