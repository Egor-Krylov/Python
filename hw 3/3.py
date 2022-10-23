import random

list = [round(random.uniform(0,100), 3) for i in range(0,10)]
print(list)
list = [round(i % 1, 3) for i in list]
print(list)
print(round(max(list) - min(list), 3))