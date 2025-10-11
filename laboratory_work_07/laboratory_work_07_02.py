import turtle as tr
from random import uniform


def fun2_2(x, y):
    if (x < -10) or (x > 10):
        flag = 0
        if (x < -10) or (x > 10):
            flag = 0
        if (((x >= -1) and (x < 1) and (y >= 2 * x + 2) and (y <= x ** 3 - 4 * x ** 2 + x + 6)) or
                ((x >= 1) and (x <= 4) and (y >= x ** 3 - 4 * x ** 2 + x + 6) and (y <= 2 * x + 2))):
            flag = 1
        else:
            flag = 0
            return flag


aX = [-10, 10]
aY = [-10, 10]
Dx = 300
Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
tr.setup(Dx, Dy, 200, 200)
tr.reset()

Nmax = 10000


tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

tr.title("Lab_7_work_02")
tr.width(2)
tr.ht()
tr.tracer(0, 0)


tr.up()
mfun = 0

for n in range(Nmax):
    x = uniform(aX[0], aX[1])
    y = uniform(aY[0], aY[1])
    tr.goto(x, y)
    if fun2_2(x, y) != 0:  # попала
        tr.dot(3, "green")
    mfun += 1
tr.color("blue", "blue")


# Ось X
tr.up()
tr.goto(aX[0], 0)
tr.down()
tr.goto(aX[1], 0)
# Ось Y
tr.up()
tr.goto(0, aY[1])
tr.down()
tr.goto(0, aY[0])


tr.up()
for x in range(aX[0], aX[1]):
    tr.goto(x, 0.1)
tr.down()
tr.goto(x, 0)
tr.up()
tr.sety(-0.4)
coords = str(x)
tr.write(coords)


for y in range(aY[0], aY[1]):
    tr.goto(0, y)
tr.down()
tr.goto(0.1, y)
tr.up()
tr.setx(0.2)
coords = str(y)
tr.write(coords)

poli = [0, 0.1, 0, -0.1, 0]
Arrbeg = int(aX[1])
Xpoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3,
         Arrbeg - 0.1, Arrbeg]
tr.goto(Xpoli[0], poli[0])
tr.begin_fill()
tr.down()
for i in range(1, 5):
    tr.goto(Xpoli[i], poli[i])
tr.end_fill()

tr.up()
tr.goto(Arrbeg, -0.7)
tr.write("X", font=("Arial", 14, "bold"))


Arrbeg = int(aY[1])
Ypoli = [Arrbeg, Arrbeg - 0.1, Arrbeg + 0.3,
         Arrbeg - 0.1, Arrbeg]
tr.up()
tr.goto(poli[0], Ypoli[0])
tr.begin_fill()
tr.down()
for i in range(1, 5):
    tr.goto(poli[i], Ypoli[i])
tr.end_fill()

tr.up()
tr.goto(0.2, Arrbeg)
tr.write("Y", font=("Arial", 14, "bold"))
Sf = (aX[1] - aX[0]) * (aY[1] - aY[0]) * mfun / Nmax
tr.goto(1, 9)
fstr = "N = {0:8d}\nNf = {1:8d}\nSf = {2:8.2f}"
meseg = fstr.format(Nmax, mfun, Sf)
tr.write(meseg, font=("Arial", 12, "bold"))
print(meseg)
tr.done()
