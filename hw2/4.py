import random
n = int(input('Введите длину массива: '))
list = [random.randrange(-n,n) for i in range(n)]

data = open('file.txt', 'r')
product = 1
for line in data:
    if int(line) < len(list):
        product *= list[int(line)]
data.close()
print(product)