from tkinter import *
from tkinter.messagebox import *
from math import log, fabs


def arth_series(x):
    if fabs(x) <= 1:
        return None
    eps = 0.0001
    sign = 1
    x_abs = x
    if x < 0:
        sign = -1
        x_abs = -x
    an = 1.0 / x_abs
    s = an
    n = 1
    while fabs(an) > eps:
        an = an / ((2 * n + 1) * x_abs * x_abs) * (2 * n - 1)
        s += an
        n += 1
        if n > 1000:
            break
    return sign * 2.0 * s


def arth_function(x):
    if fabs(x) <= 1:
        return None
    return 0.5 * log((x + 1) / (x - 1)) + dY


def get_data():
    global Xmax, Xmin, Ymax, Ymin, dX, dY, Kx, Ky
    try:
        tmpXmax = float(ent3.get())
        tmpXmin = float(ent2.get())
        tmpYmax = float(ent5.get())
        tmpYmin = float(ent4.get())
        tmpDY = float(ent7.get())
        tmpDX = float(ent6.get())

        if tmpXmin >= tmpXmax:
            showwarning(title="Ошибка", message="Xmax > Xmin")
            return False
        if tmpYmin >= tmpYmax:
            showwarning(title="Ошибка", message="Ymax > Ymin")
            return False
        if tmpDX <= 0:
            showwarning(title="Ошибка", message="Шаг меток > 0")
            return False

        Xmax = tmpXmax
        Xmin = tmpXmin
        Ymax = tmpYmax
        Ymin = tmpYmin
        dX = tmpDX
        dY = tmpDY

        Kx = MaxX / (Xmax - Xmin)
        Ky = MaxY / (Ymax - Ymin)
        return True
    except ValueError:
        showwarning(title="Ошибка", message="Введите числа")
        return False


def set_mark(a, b, lr_bt=1):
    ax_xy = []
    if lr_bt:
        ax_xy.append((a, b))
        ax_xy.append((a + 10, b))
    else:
        ax_xy.append((a, b))
        ax_xy.append((a, b - 10))
    cv.create_line(ax_xy, fill='black', width=2)


def plot_xy():
    cv.delete("axes")
    ax_xy = [(5, 5), (MaxX - 5, MaxY - 5)]
    cv.create_rectangle(ax_xy, fill="white", outline="green", width=2, tags="axes")

    y = Ymin
    y_pix = MaxY
    flg = False
    while y <= Ymax:
        text_y = str(round(y, 2))
        set_mark(0, y_pix, 1)
        if flg:
            cv.create_text(15, y_pix, text=text_y, anchor=W, font=("Arial", 9), tags="axes")
        set_mark(MaxX - 10, y_pix, 1)
        if flg:
            cv.create_text(MaxX - 15, y_pix, text=text_y, anchor=E, font=("Arial", 9), tags="axes")
        y += dX
        y_pix -= dX * Ky
        flg = not flg

    x = Xmin
    x_pix = 0
    flg = False
    while x <= Xmax:
        text_x = str(round(x, 2))
        set_mark(x_pix, 0, 0)
        if flg:
            cv.create_text(x_pix, 15, text=text_x, anchor=N, font=("Arial", 9), tags="axes")
        set_mark(x_pix, MaxY, 0)
        if flg:
            cv.create_text(x_pix, MaxY - 15, text=text_x, anchor=S, font=("Arial", 9), tags="axes")
        x += dX
        x_pix += dX * Kx
        flg = not flg


def fdraw(func, color):
    lxy = []
    step = 1.0 / Kx
    x = Xmin
    while x <= Xmax:
        y = func(x)
        if y is not None:
            lxy.append((x, y))
        else:
            lxy.append((x, None))
        x += step

    lpix = []
    for xy in lxy:
        if xy[1] is not None:
            if Ymin <= xy[1] <= Ymax:
                x_pix = Kx * (xy[0] - Xmin)
                y_pix = MaxY - Ky * (xy[1] - Ymin)
                lpix.append((x_pix, y_pix))
            else:
                if len(lpix) >= 2:
                    cv.create_line(lpix, fill=color, width=2, smooth=True, tags="graph")
                lpix = []
        else:
            if len(lpix) >= 2:
                cv.create_line(lpix, fill=color, width=2, smooth=True, tags="graph")
            lpix = []
    if len(lpix) >= 2:
        cv.create_line(lpix, fill=color, width=2, smooth=True, tags="graph")


def draw(event):
    if not get_data():
        return
    cv.delete("graph")
    plot_xy()
    fdraw(arth_series, 'blue')
    fdraw(arth_function, 'red')
    cv.create_text(MaxX - 120, 30, text="y(x) - ряд Тейлора", fill="blue", anchor=W, font=("Arial", 10), tags="graph")
    cv.create_text(MaxX - 120, 50, text=f"z(x) = Arth(x) + {dY:.2f}", fill="red", anchor=W, font=("Arial", 10), tags="graph")


def final(event):
    window_deleted()


def window_deleted():
    if askyesno("Выход", "Завершить работу?"):
        root.destroy()


def show_xy(event):
    global ID1, ID2
    x = event.x
    y = event.y
    ent0.delete(0, END)
    ent1.delete(0, END)
    ent0.insert(0, str(round(Xmin + x / Kx, 2)))
    ent1.insert(0, str(round(Ymin + (MaxY - y) / Ky, 2)))
    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y, MaxX, y, dash=(3, 5))
    ID2 = cv.create_line(x, 0, x, MaxY, dash=(3, 5))


if __name__ == "__main__":
    root = Tk()
    root.title("Графика - Вариант 6")

    root.protocol('WM_DELETE_WINDOW', window_deleted)
    root.resizable(False, False)

    Kp = 0.7
    MaxX = root.winfo_screenwidth() * Kp
    MaxY = root.winfo_screenheight() * Kp

    cv = Canvas(root, width=MaxX, height=MaxY, bg="white")
    cv.grid(row=0, columnspan=9)
    cv.bind("<Button-1>", show_xy)

    Xmin = -5.0
    Xmax = -1.1
    Ymin = -3.0
    Ymax = 3.0
    dY = 0.0
    dX = 1.0

    ID1 = 0
    ID2 = 0

    Kx = MaxX / (Xmax - Xmin)
    Ky = MaxY / (Ymax - Ymin)

    lba0 = Label(root, text="X:", width=10, fg="blue", font="Ubuntu, 12")
    lba0.grid(row=1, column=0, sticky='e')
    ent0 = Entry(root, width=5, font="Ubuntu, 12")
    ent0.grid(row=1, column=1, sticky='w')
    ent0.insert(0, 0)

    lba1 = Label(root, text="Y:", width=10, fg="blue", font="Ubuntu, 12")
    lba1.grid(row=2, column=0, sticky='e')
    ent1 = Entry(root, width=5, font="Ubuntu, 12")
    ent1.grid(row=2, column=1, sticky='w')
    ent1.insert(0, 0)

    lba2 = Label(root, text="Xmin:", width=10, fg="blue", font="Ubuntu, 12")
    lba2.grid(row=1, column=2, sticky='e')
    ent2 = Entry(root, width=5, font="Ubuntu, 12")
    ent2.grid(row=1, column=3)
    ent2.insert(0, Xmin)

    lba3 = Label(root, text="Xmax:", width=10, fg="blue", font="Ubuntu, 12")
    lba3.grid(row=1, column=4, sticky='e')
    ent3 = Entry(root, width=5, font="Ubuntu, 12")
    ent3.grid(row=1, column=5)
    ent3.insert(0, Xmax)

    lba4 = Label(root, text="Ymin:", width=10, fg="blue", font="Ubuntu, 12")
    lba4.grid(row=2, column=2, sticky='e')
    ent4 = Entry(root, width=5, font="Ubuntu, 12")
    ent4.grid(row=2, column=3)
    ent4.insert(0, Ymin)

    lba5 = Label(root, text="Ymax:", width=10, fg="blue", font="Ubuntu, 12")
    lba5.grid(row=2, column=4, sticky='e')
    ent5 = Entry(root, width=5, font="Ubuntu, 12")
    ent5.grid(row=2, column=5)
    ent5.insert(0, Ymax)

    lba6 = Label(root, text="Шаг меток:", width=10, fg="blue", font="Ubuntu, 12")
    lba6.grid(row=1, column=6, sticky='e')
    ent6 = Entry(root, width=5, font="Ubuntu, 12")
    ent6.grid(row=1, column=7)
    ent6.insert(0, dX)

    lba7 = Label(root, text="Смещение:", width=10, fg="blue", font="Ubuntu, 12")
    lba7.grid(row=2, column=6, sticky='e')
    ent7 = Entry(root, width=5, font="Ubuntu, 12")
    ent7.grid(row=2, column=7)
    ent7.insert(0, dY)

    btn1 = Button(root, width=20, bg="#ccc", text="Рисовать")
    btn1.grid(row=1, column=8)
    btn1.bind("<Button-1>", draw)

    btn2 = Button(root, width=20, bg="#ccc", text="Выход")
    btn2.grid(row=2, column=8)
    btn2.bind("<Button-1>", final)

    plot_xy()
    fdraw(arth_series, 'blue')
    fdraw(arth_function, 'red')

    root.mainloop()