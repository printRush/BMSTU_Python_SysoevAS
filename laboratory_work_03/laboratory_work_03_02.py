from random import *


flag = 0

print("   X     Y      Res")
print("-------------------")

for n in range(10):
    x = uniform(-1, 4)
    y = uniform(-1, 10)
    if (x < -1) or (x > 4):
        flag = 0 #False
    if (((x>=-1) and (x< 1) and (y>=2*x+2) and (y<= x**3-4*x**2+x+6)) or
            ((x>=1)and(x<=4)and(y>=x**3-4*x**2+x+6) and (y<= 2*x+2))):
        flag = 1
    else:
        flag = 0

    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=" ")

    if flag:
        print("Yes")
    else:
        print("No")
