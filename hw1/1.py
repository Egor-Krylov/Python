print("Введите число: ")
number = int(input());
if number in range (1, 6):
    print("нет")
elif number in range(6,8):
    print("да")
else:
    print("некорректное число")