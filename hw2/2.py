def factorial(value):
    result = 1
    for i in range(1,value + 1):
        result = result * i
    return result

n = int(input("Введите число: "))
list = [factorial(i) for i in range(1, n + 1)]

print(list)
