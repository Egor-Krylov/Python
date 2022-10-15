import random

n = int(input('Введите длину массива: '))

list = [i for i in range(n)]
print('Изначальный спсиок: ')
print(list)
for i in range(n):
    randomPosition = random.randint(i, n - 1)
    if (randomPosition > i):
        temp = list[randomPosition]
        list[randomPosition] = list[i]
        list[i] = temp

print('Перемешанный спсиок: ')
print(list)
