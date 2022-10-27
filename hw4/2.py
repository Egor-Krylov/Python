# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("Введите число: "))
list = []
for i in range(2, n):

    if n % i == 0:
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            list.append(i)

print(list)