# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input("Введите число: ")
# sum = 0
# for i in n:
#     if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
#         sum += int(i)
# print(f"Сумма цифр равна: {sum}")

from functools import reduce

digits = [int(i) for i in list(input("Введите число: ")) if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]

print(reduce(lambda sum, element: sum + element, digits))


