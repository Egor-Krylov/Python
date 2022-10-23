n = int(input('Введите длину массива: '))

list = [int(input(f"Введите {i}-й элемент: ")) for i in range(n)]
listProducts = []
for i in range((n+1) // 2):
    listProducts.append(list[i]*list[-i-1])
print(list)
print(listProducts)
