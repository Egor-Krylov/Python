print("Введите первую координату: ")
x = float(input())
print("Введите вторую координату: ")
y = float(input())

if (x > 0 and y > 0):
    print("первая четверть")
if (x < 0 and y > 0):
    print("вторая четверть")
if (x < 0 and y < 0):
    print("третья четверть")
if (x > 0 and y < 0):
    print("четвертая четверть")
