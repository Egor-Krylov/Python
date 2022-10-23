n = int(input('Введите число: '))

list = []
while n > 0:
    list.insert(0, str(n % 2))
    n = n // 2
print("".join(list))