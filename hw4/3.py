# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [1,1,3,5,2,5,8,9,4,3,4]
resultList = []
for i in range(len(list)):
    duplicate = False
    for j in range(len(list)):
        if (i != j) and list[i] == list[j]:
            duplicate = True
    if not duplicate:
        resultList.append(list[i])
print(resultList)
