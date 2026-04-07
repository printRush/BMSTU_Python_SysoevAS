"""
    Задача лабораторной работы №7 задание 2.
"""


import turtle as tr
from random import uniform


class PointPlotter:
    def __init__(self):
        self.a_x = [-10, 10]
        self.a_y = [-10, 10]
        self.dx = 300
        self.dy = self.dx / ((self.a_x[1] - self.a_x[0]) / (self.a_y[1] - self.a_y[0]))
        self.n_max = 10000
        self.m_fun = 0

    def fun2_2(self, x, y):
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

    def setup_window(self):
        tr.setup(self.dx, self.dy, 200, 200)
        tr.reset()
        tr.setworldcoordinates(self.a_x[0], self.a_y[0], self.a_x[1], self.a_y[1])
        tr.title("Lab_7_work_02")
        tr.width(2)
        tr.ht()
        tr.tracer(0, 0)

    def draw_points(self):
        tr.up()
        for n in range(self.n_max):
            x = uniform(self.a_x[0], self.a_x[1])
            y = uniform(self.a_y[0], self.a_y[1])
            tr.goto(x, y)
            if self.fun2_2(x, y) != 0:
                tr.dot(3, "green")
            self.m_fun += 1

    def draw_axes(self):
        tr.color("blue", "blue")
        tr.up()
        tr.goto(self.a_x[0], 0)
        tr.down()
        tr.goto(self.a_x[1], 0)
        tr.up()
        tr.goto(0, self.a_y[1])
        tr.down()
        tr.goto(0, self.a_y[0])
        tr.up()

    def draw_x_marks(self):
        for x in range(self.a_x[0], self.a_x[1]):
            tr.goto(x, 0.1)
            tr.down()
            tr.goto(x, 0)
            tr.up()
            tr.sety(-0.4)
            coords = str(x)
            tr.write(coords)

    def draw_y_marks(self):
        for y in range(self.a_y[0], self.a_y[1]):
            tr.goto(0, y)
            tr.down()
            tr.goto(0.1, y)
            tr.up()
            tr.setx(0.2)
            coords = str(y)
            tr.write(coords)

    def draw_x_arrow(self):
        poli = [0, 0.1, 0, -0.1, 0]
        arr_beg = int(self.a_x[1])
        x_poli = [arr_beg, arr_beg - 0.1, arr_beg + 0.3, arr_beg - 0.1, arr_beg]
        tr.goto(x_poli[0], poli[0])
        tr.begin_fill()
        tr.down()
        for i in range(1, 5):
            tr.goto(x_poli[i], poli[i])
        tr.end_fill()
        tr.up()
        tr.goto(arr_beg, -0.7)
        tr.write("X", font=("Arial", 14, "bold"))

    def draw_y_arrow(self):
        poli = [0, 0.1, 0, -0.1, 0]
        arr_beg = int(self.a_y[1])
        y_poli = [arr_beg, arr_beg - 0.1, arr_beg + 0.3, arr_beg - 0.1, arr_beg]
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

    def draw_info(self):
        sf = (self.a_x[1] - self.a_x[0]) * (self.a_y[1] - self.a_y[0]) * self.m_fun / self.n_max
        tr.goto(1, 9)
        fstr = "N = {0:8d}\nNf = {1:8d}\nSf = {2:8.2f}"
        messeg = fstr.format(self.n_max, self.m_fun, sf)
        tr.write(messeg, font=("Arial", 12, "bold"))
        print(messeg)

    def run(self):
        self.setup_window()
        self.draw_points()
        self.draw_axes()
        self.draw_x_marks()
        self.draw_y_marks()
        self.draw_x_arrow()
        self.draw_y_arrow()
        self.draw_info()
        tr.done()


if __name__ == "__main__":
    plotter = PointPlotter()
    plotter.run()