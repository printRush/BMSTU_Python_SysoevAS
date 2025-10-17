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


a_x = [-10, 10]
a_y = [-10, 10]
dx = 300
dy = dx / ((a_x[1] - a_x[0]) / (a_y[1] - a_y[0]))
tr.setup(dx, dy, 200, 200)
tr.reset()

n_max = 10000

tr.setworldcoordinates(a_x[0], a_y[0], a_x[1], a_y[1])

tr.title("Lab_7_work_02")
tr.width(2)
tr.ht()
tr.tracer(0, 0)


tr.up()
m_fun = 0

for n in range(n_max):
    x = uniform(a_x[0], a_x[1])
    y = uniform(a_y[0], a_y[1])
    tr.goto(x, y)
    if fun2_2(x, y) != 0:  # попала
        tr.dot(3, "green")
    m_fun += 1

tr.color("blue", "blue")

# Ось X
tr.up()
tr.goto(a_x[0], 0)
tr.down()
tr.goto(a_x[1], 0)

# Ось Y
tr.up()
tr.goto(0, a_y[1])
tr.down()
tr.goto(0, a_y[0])

tr.up()


for x in range(a_x[0], a_x[1]):
    tr.goto(x, 0.1)
    tr.down()
    tr.goto(x, 0)
    tr.up()
    tr.sety(-0.4)
    coords = str(x)
    tr.write(coords)


for y in range(a_y[0], a_y[1]):
    tr.goto(0, y)
    tr.down()
    tr.goto(0.1, y)
    tr.up()
    tr.setx(0.2)
    coords = str(y)
    tr.write(coords)


poli = [0, 0.1, 0, -0.1, 0]
arr_beg = int(a_x[1])
x_poli = [arr_beg, arr_beg - 0.1, arr_beg + 0.3,
          arr_beg - 0.1, arr_beg]
tr.goto(x_poli[0], poli[0])
tr.begin_fill()
tr.down()

for i in range(1, 5):
    tr.goto(x_poli[i], poli[i])

tr.end_fill()

tr.up()
tr.goto(arr_beg, -0.7)
tr.write("X", font=("Arial", 14, "bold"))

arr_beg = int(a_y[1])
y_poli = [arr_beg, arr_beg - 0.1, arr_beg + 0.3,
          arr_beg - 0.1, arr_beg]

tr.up()
tr.goto(poli[0], y_poli[0])
tr.begin_fill()
tr.down()


for i in range(1, 5):
    tr.goto(poli[i], y_poli[i])
tr.end_fill()

tr.up()
tr.goto(0.2, arr_beg)
tr.write("Y", font=("Arial", 14, "bold"))
sf = (a_x[1] - a_x[0]) * (a_y[1] - a_y[0]) * m_fun / n_max
tr.goto(1, 9)
fstr = "N = {0:8d}\nNf = {1:8d}\nSf = {2:8.2f}"
messeg = fstr.format(n_max, m_fun, sf)
tr.write(messeg, font=("Arial", 12, "bold"))

print(messeg)

tr.done()
