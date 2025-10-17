from math import *
a = float(input('Введите параметр а: '))

z1 = cos(a) + cos(2*a) + cos(6*a) + cos(7*a)
z2 = 4*cos(a/2) * cos(5/2*a) * cos(4*a)

print(f'Результат программы для уравнения 1: {z1}')
print(f'Результат программы для уравнения 2: {z2}')
