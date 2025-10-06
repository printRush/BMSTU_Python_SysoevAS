from math import *

print('Введите Xbeg, Xend и Dx')

xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))

print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("Dx={0: 7.2f}".format(dx))

xt = xb

print("+--------+--------+")
print("I   X    I    Y   I")
print("+--------+--------+")

while xt <= xe:
    if xt < -5:
        y = 1.0
    elif -5 <= xt < -3:
        y = 3/2*xt + 4.5
    elif -3 <= xt < 3:
        y = sqrt(3**2 - xt**2)
    elif 3 <= xt < 8:
        y = 3/5*xt - 9/5
    else:
        y = 3.0
    print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt += dx

print("+--------+--------+")