n = int(input("Введите число: "))

list = [round((1 + 1/i)**i, 3) for i in range(1, n + 1)]

print(list)
sum = 0
for i in range(len(list)):
    sum += list[i]
print(sum)