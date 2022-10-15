from math import sqrt


print("Введите первую координату первой точки: ")
ax = float(input())
print("Введите вторую координату первой точки: ")
ay = float(input())
print("Введите первую координату второй точки: ")
bx = float(input())
print("Введите вторую координату второй точки: ")
by = float(input())

print(((ax - bx)**2 + (ay - by)**2)**0.5)