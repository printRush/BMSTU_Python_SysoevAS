from math import *


with open('input1.txt', 'r') as f:
    data = map(int, f.read().split())


with open('output1.txt', 'w+') as f:
    for a in data:
        z1 = cos(a) + cos(2*a) + cos(6*a) + cos(7*a)
        z2 = 4*cos(a/2) * cos(5/2*a) * cos(4*a)
        f.write(f'Результат программы для уравнения 1: {z1}\n'
                     f'Результат программы для уравнения 2: {z2}\n\n')

print("Done!")