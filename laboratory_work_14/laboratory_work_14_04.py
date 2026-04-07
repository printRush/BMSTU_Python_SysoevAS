"""
    Задача лабораторной работы №8.
"""


from tkinter import *
from tkinter.messagebox import *
from math import log, fabs


class GraphApp:
    def __init__(self):
        self.root = None
        self.cv = None
        self.MaxX = None
        self.MaxY = None
        self.Xmin = -5.0
        self.Xmax = -1.1
        self.Ymin = -3.0
        self.Ymax = 3.0
        self.dY = 0.0
        self.dX = 1.0
        self.Kx = None
        self.Ky = None
        self.ID1 = 0
        self.ID2 = 0
        self.entries = {}

    def arth_series(self, x):
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

    def arth_function(self, x):
        if fabs(x) <= 1:
            return None
        return 0.5 * log((x + 1) / (x - 1)) + self.dY

    def get_data(self):
        try:
            tmpXmax = float(self.entries['Xmax'].get())
            tmpXmin = float(self.entries['Xmin'].get())
            tmpYmax = float(self.entries['Ymax'].get())
            tmpYmin = float(self.entries['Ymin'].get())
            tmpDY = float(self.entries['shift'].get())
            tmpDX = float(self.entries['step'].get())

            if tmpXmin >= tmpXmax:
                showwarning(title="Ошибка", message="Xmax > Xmin")
                return False
            if tmpYmin >= tmpYmax:
                showwarning(title="Ошибка", message="Ymax > Ymin")
                return False
            if tmpDX <= 0:
                showwarning(title="Ошибка", message="Шаг меток > 0")
                return False

            self.Xmax = tmpXmax
            self.Xmin = tmpXmin
            self.Ymax = tmpYmax
            self.Ymin = tmpYmin
            self.dX = tmpDX
            self.dY = tmpDY

            self.Kx = self.MaxX / (self.Xmax - self.Xmin)
            self.Ky = self.MaxY / (self.Ymax - self.Ymin)
            return True
        except ValueError:
            showwarning(title="Ошибка", message="Введите числа")
            return False

    def set_mark(self, a, b, lr_bt=1):
        ax_xy = []
        if lr_bt:
            ax_xy.append((a, b))
            ax_xy.append((a + 10, b))
        else:
            ax_xy.append((a, b))
            ax_xy.append((a, b - 10))
        self.cv.create_line(ax_xy, fill='black', width=2)

    def plot_xy(self):
        self.cv.delete("axes")
        ax_xy = [(5, 5), (self.MaxX - 5, self.MaxY - 5)]
        self.cv.create_rectangle(ax_xy, fill="white", outline="green", width=2, tags="axes")

        y = self.Ymin
        y_pix = self.MaxY
        flg = False
        while y <= self.Ymax:
            text_y = str(round(y, 2))
            self.set_mark(0, y_pix, 1)
            if flg:
                self.cv.create_text(15, y_pix, text=text_y, anchor=W, font=("Arial", 9), tags="axes")
            self.set_mark(self.MaxX - 10, y_pix, 1)
            if flg:
                self.cv.create_text(self.MaxX - 15, y_pix, text=text_y, anchor=E, font=("Arial", 9), tags="axes")
            y += self.dX
            y_pix -= self.dX * self.Ky
            flg = not flg

        x = self.Xmin
        x_pix = 0
        flg = False
        while x <= self.Xmax:
            text_x = str(round(x, 2))
            self.set_mark(x_pix, 0, 0)
            if flg:
                self.cv.create_text(x_pix, 15, text=text_x, anchor=N, font=("Arial", 9), tags="axes")
            self.set_mark(x_pix, self.MaxY, 0)
            if flg:
                self.cv.create_text(x_pix, self.MaxY - 15, text=text_x, anchor=S, font=("Arial", 9), tags="axes")
            x += self.dX
            x_pix += self.dX * self.Kx
            flg = not flg

    def fdraw(self, func, color):
        lxy = []
        step = 1.0 / self.Kx
        x = self.Xmin
        while x <= self.Xmax:
            y = func(x)
            if y is not None:
                lxy.append((x, y))
            else:
                lxy.append((x, None))
            x += step

        lpix = []
        for xy in lxy:
            if xy[1] is not None:
                if self.Ymin <= xy[1] <= self.Ymax:
                    x_pix = self.Kx * (xy[0] - self.Xmin)
                    y_pix = self.MaxY - self.Ky * (xy[1] - self.Ymin)
                    lpix.append((x_pix, y_pix))
                else:
                    if len(lpix) >= 2:
                        self.cv.create_line(lpix, fill=color, width=2, smooth=True, tags="graph")
                    lpix = []
            else:
                if len(lpix) >= 2:
                    self.cv.create_line(lpix, fill=color, width=2, smooth=True, tags="graph")
                lpix = []
        if len(lpix) >= 2:
            self.cv.create_line(lpix, fill=color, width=2, smooth=True, tags="graph")

    def draw(self, event):
        if not self.get_data():
            return
        self.cv.delete("graph")
        self.plot_xy()
        self.fdraw(self.arth_series, 'blue')
        self.fdraw(self.arth_function, 'red')
        self.cv.create_text(self.MaxX - 120, 30, text="y(x) - ряд Тейлора", fill="blue", anchor=W, font=("Arial", 10), tags="graph")
        self.cv.create_text(self.MaxX - 120, 50, text=f"z(x) = Arth(x) + {self.dY:.2f}", fill="red", anchor=W, font=("Arial", 10), tags="graph")

    def final(self, event):
        self.window_deleted()

    def window_deleted(self):
        if askyesno("Выход", "Завершить работу?"):
            self.root.destroy()

    def show_xy(self, event):
        x = event.x
        y = event.y
        self.entries['X'].delete(0, END)
        self.entries['Y'].delete(0, END)
        self.entries['X'].insert(0, str(round(self.Xmin + x / self.Kx, 2)))
        self.entries['Y'].insert(0, str(round(self.Ymin + (self.MaxY - y) / self.Ky, 2)))
        self.cv.delete(self.ID1)
        self.cv.delete(self.ID2)
        self.ID1 = self.cv.create_line(0, y, self.MaxX, y, dash=(3, 5))
        self.ID2 = self.cv.create_line(x, 0, x, self.MaxY, dash=(3, 5))

    def setup_ui(self):
        self.root = Tk()
        self.root.title("Графика - Вариант 6")
        self.root.protocol('WM_DELETE_WINDOW', self.window_deleted)
        self.root.resizable(False, False)

        Kp = 0.7
        self.MaxX = self.root.winfo_screenwidth() * Kp
        self.MaxY = self.root.winfo_screenheight() * Kp

        self.cv = Canvas(self.root, width=self.MaxX, height=self.MaxY, bg="white")
        self.cv.grid(row=0, columnspan=9)
        self.cv.bind("<Button-1>", self.show_xy)

        self.Kx = self.MaxX / (self.Xmax - self.Xmin)
        self.Ky = self.MaxY / (self.Ymax - self.Ymin)

        row = 1
        self.entries['X'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['Y'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['Xmin'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['Xmax'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['Ymin'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['Ymax'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['step'] = Entry(self.root, width=5, font="Ubuntu, 12")
        self.entries['shift'] = Entry(self.root, width=5, font="Ubuntu, 12")

        labels = [
            ("X:", 1, 0, self.entries['X'], 1, 1),
            ("Y:", 2, 0, self.entries['Y'], 2, 1),
            ("Xmin:", 1, 2, self.entries['Xmin'], 1, 3),
            ("Xmax:", 1, 4, self.entries['Xmax'], 1, 5),
            ("Ymin:", 2, 2, self.entries['Ymin'], 2, 3),
            ("Ymax:", 2, 4, self.entries['Ymax'], 2, 5),
            ("Шаг меток:", 1, 6, self.entries['step'], 1, 7),
            ("Смещение:", 2, 6, self.entries['shift'], 2, 7)
        ]

        for text, row_l, col_l, entry, row_e, col_e in labels:
            Label(self.root, text=text, width=10, fg="blue", font="Ubuntu, 12").grid(row=row_l, column=col_l, sticky='e')
            entry.grid(row=row_e, column=col_e, sticky='w' if col_e == 1 else 'e')
            if text == "X:" or text == "Y:":
                entry.insert(0, 0)
            else:
                if text == "Xmin:":
                    entry.insert(0, self.Xmin)
                elif text == "Xmax:":
                    entry.insert(0, self.Xmax)
                elif text == "Ymin:":
                    entry.insert(0, self.Ymin)
                elif text == "Ymax:":
                    entry.insert(0, self.Ymax)
                elif text == "Шаг меток:":
                    entry.insert(0, self.dX)
                elif text == "Смещение:":
                    entry.insert(0, self.dY)

        btn1 = Button(self.root, width=20, bg="#ccc", text="Рисовать")
        btn1.grid(row=1, column=8)
        btn1.bind("<Button-1>", self.draw)

        btn2 = Button(self.root, width=20, bg="#ccc", text="Выход")
        btn2.grid(row=2, column=8)
        btn2.bind("<Button-1>", self.final)

    def run(self):
        self.setup_ui()
        self.plot_xy()
        self.fdraw(self.arth_series, 'blue')
        self.fdraw(self.arth_function, 'red')
        self.root.mainloop()


if __name__ == "__main__":
    app = GraphApp()
    app.run()