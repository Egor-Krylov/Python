# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
n = int(input("Введите степень многочлена: "))
resultString = f"{random.randint(0, 100)}"
for i in range(1, n+1):
    randomCoef = random.randint(0, 100)
    if randomCoef > 1:
        resultString = f"{randomCoef}*x^{i} + " + resultString
    elif randomCoef == 1:
        resultString = f"x^{i} + " + resultString

f = open('file.txt','w')
f.write(resultString)
f.close()
# print(resultString)