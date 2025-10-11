from math import sqrt
from turtle import *


def function(xt):
    if xt < -5:
        y = 1.0
    elif -5 <= xt < -3:
        y = 3 / 2 * xt + 4.5
    elif -3 <= xt < 3:
        y = sqrt(3 ** 2 - xt ** 2)
    elif 3 <= xt < 8:
        y = 3 / 5 * xt - 9 / 5
    else:
        y = 3.0
    return y


def plot_axis(min_value, max_value, ax="X"):
    up()
    if ax == "X":
        begin = (min_value, 0)
        end = (max_value, 0)
    else:
        begin = (0, min_value)
        end = (0, max_value)
    goto(begin)
    down()
    goto(end)


def plot_mark(min_value, max_value, ax="X"):
    up()
    for t in range(min_value, max_value):
        if ax == "X":
            point_begin = (t, 0)
            point_end = (t, 0.2)
            point_width = (t, -0.5)
        else:
            point_begin = (0, t)
            point_end = (0.2, t)
            point_width = (-0.5, t)
        goto(point_begin)
        down()
        goto(point_end)
        up()
        goto(point_width)
        write(str(t))


def plot_arrow(max_value, ax="X"):
    triangle = [(0.1, -0.1), (0, 0.3), (-0.1, -0.1)]
    up()
    goto(0, 0)
    begin_poly()
    for couple in triangle:
        goto(couple)
    end_poly()
    arrow = get_poly()
    register_shape("myArrow", arrow)
    resizemode("myArrow")
    shapesize(1, 2, 1)
    if ax == "X":
        tiltangle(0)
        goto(max_value + 0.2, 0)
        point_width = (int(max_value), -1.0)
    else:
        tiltangle(90)
        goto(0, max_value + 0.2)
        point_width = (0.2, int(max_value))
    stamp()
    goto(point_width)
    write(ax, font=("Arial", 14, "bold"))


def plot_function(min_value, max_value, n_max=1000):
    color("green")
    width(3)
    dx = (max_value - min_value) / n_max

    x = min_value
    y = function(x)
    if y is None:
        up()
        goto(x, y)
    else:
        goto(x, y)
        down()
    while x <= max_value:
        x = x + dx
        y = function(x)
        if y is None:
            up()
            continue
        else:
            goto(x, y)
            down()


if __name__ == "__main__":
    aX = (-12, 12)
    aY = (-5, 5)

    Dx = 800
    Dy = int(Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0])))
    setup(Dx, Dy)
    reset()

    setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    title("lab_work_7_1")
    width(2)
    color("blue", "blue")

    ht()
    tracer(0, 0)

    plot_axis(aX[0], aX[1], "X")
    plot_mark(aX[0], aX[1], "X")
    plot_arrow(aX[1], "X")

    plot_axis(aY[0], aY[1], "Y")
    plot_mark(aY[0], aY[1], "Y")
    plot_arrow(aY[1], "Y")

    plot_function(aX[0], aX[1], 1000)

    mainloop()