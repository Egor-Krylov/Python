n = int(input('Введите длину массива: '))

list = [int(input(f"Введите {i}-й элемент: ")) for i in range(n)]
sum = 0
for i in range(n // 2):
    sum += list[2 * i + 1]
print(f"Сумма элементов на нечетных позициях: {sum}")
