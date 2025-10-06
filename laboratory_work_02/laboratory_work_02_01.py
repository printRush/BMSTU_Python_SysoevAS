from math import *

x = float(input('Enter x: '))

if x < -5:
    y = 1.0
    print((x, y))
elif -5 <= x < -3:
    y = 3/2*x + 4.5
    print((x, y))
elif -3 <= x < 3:
    y = sqrt(3**2 - x**2)
    print((x, y))
elif 3 <= x < 8:
    y = 3/5*x - 9/5
    print((x, y))
elif 8 <= x:
    y = 3.0
    print((x, y))