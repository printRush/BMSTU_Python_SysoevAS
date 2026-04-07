"""
    Задача лабораторной работы №7 задание 3.
"""


import math
import turtle


class SeriesPlotter:
    def __init__(self):
        self.xb = None
        self.xe = None
        self.dx = None
        self.eps = None
        self.x_values = []
        self.y_series_values = []
        self.valid_points = []

    def get_input(self):
        print('Введите Xbeg, Xend, Dx и Eps')
        self.xb = float(input('Xbeg='))
        self.xe = float(input('Xend='))
        self.dx = float(input('Dx='))
        self.eps = float(input('Eps='))

    def calculate_series(self):
        print("+-----------+-----------+-----+")
        print("I     X     I     Y     I  N  I")
        print("+-----------+-----------+-----+")

        x = self.xb
        while x <= self.xe:
            if -1 <= x < 1:
                n = 1
                term = -x
                sum_series = term
                while abs(term) >= self.eps and n < 1000:
                    n += 1
                    term = -(x ** n) / n
                    sum_series += term
                self.x_values.append(x)
                self.y_series_values.append(sum_series)
                self.valid_points.append(True)
                print(f"|{x:10.4f} |{sum_series:10.4f} |{n:4} |")
            else:
                self.x_values.append(x)
                self.y_series_values.append(None)
                self.valid_points.append(False)
                print(f"|{x:10.4f} |{'не опр.':^10} |{' -':4} |")
            x = x + self.dx
        print("+-----------+-----------+-----+")

    def setup_screen(self):
        self.screen = turtle.Screen()
        self.screen.title(f"График функции ln(1-x) через ряд Тейлора (точность {self.eps})")
        self.screen.bgcolor("white")
        self.screen.setup(width=0.9, height=0.9)

    def get_boundaries(self):
        valid_x = [self.x_values[i] for i in range(len(self.x_values)) if self.valid_points[i]]
        valid_y = [self.y_series_values[i] for i in range(len(self.x_values)) if self.valid_points[i]]

        if not valid_x:
            print("Нет точек для построения графика в области сходимости")
            turtle.done()
            exit()

        x_min, x_max = min(valid_x), max(valid_x)
        y_min, y_max = min(valid_y), max(valid_y)

        x_padding = (x_max - x_min) * 0.1
        y_padding = (y_max - y_min) * 0.1

        x_min -= x_padding
        x_max += x_padding
        y_min -= y_padding
        y_max += y_padding

        self.screen.setworldcoordinates(x_min, y_min, x_max, y_max)
        return x_min, x_max, y_min, y_max

    def draw_axes(self, x_min, x_max, y_min, y_max, graph_turtle):
        graph_turtle.penup()
        graph_turtle.goto(x_min, 0)
        graph_turtle.pendown()
        graph_turtle.goto(x_max, 0)
        graph_turtle.penup()
        graph_turtle.goto(0, y_min)
        graph_turtle.pendown()
        graph_turtle.goto(0, y_max)

        graph_turtle.penup()
        graph_turtle.goto(x_max * 0.9, y_max * 0.05)
        graph_turtle.write("X", font=("Arial", 12, "bold"))
        graph_turtle.goto(x_max * 0.05, y_max * 0.9)
        graph_turtle.write("Y", font=("Arial", 12, "bold"))

    def draw_title(self, x_min, x_max, y_max, graph_turtle):
        graph_turtle.goto((x_min + x_max) / 2, y_max * 0.95)
        graph_turtle.write(f"ln(1-x) через ряд Тейлора (ε={self.eps})",
                           align="center", font=("Arial", 14, "bold"))

    def draw_ticks(self, x_min, x_max, y_min, y_max, graph_turtle):
        graph_turtle.pensize(1)
        graph_turtle.color("gray")

        x_step = (x_max - x_min) / 10
        for i in range(1, 10):
            x_pos = x_min + i * x_step
            graph_turtle.penup()
            graph_turtle.goto(x_pos, -0.1)
            graph_turtle.pendown()
            graph_turtle.goto(x_pos, 0.1)
            graph_turtle.penup()
            graph_turtle.goto(x_pos, -0.3)
            graph_turtle.write(f"{x_pos:.1f}", align="center", font=("Arial", 8))

        y_step = (y_max - y_min) / 10
        for i in range(1, 10):
            y_pos = y_min + i * y_step
            graph_turtle.penup()
            graph_turtle.goto(-0.1, y_pos)
            graph_turtle.pendown()
            graph_turtle.goto(0.1, y_pos)
            graph_turtle.penup()
            graph_turtle.goto(-0.5, y_pos)
            graph_turtle.write(f"{y_pos:.1f}", align="center", font=("Arial", 8))

    def draw_graph(self, graph_turtle):
        graph_turtle.pensize(2)
        graph_turtle.color("blue")
        graph_turtle.penup()

        first_valid = False
        for i in range(len(self.x_values)):
            if self.valid_points[i]:
                graph_turtle.goto(self.x_values[i], self.y_series_values[i])
                first_valid = True
                break

        if first_valid:
            graph_turtle.pendown()
            for i in range(len(self.x_values)):
                if self.valid_points[i]:
                    graph_turtle.goto(self.x_values[i], self.y_series_values[i])
                else:
                    graph_turtle.penup()

    def draw_convergence_region(self, y_min, y_max, graph_turtle):
        graph_turtle.penup()
        graph_turtle.goto(-1, y_min)
        graph_turtle.pendown()
        graph_turtle.color("green")
        graph_turtle.pensize(3)
        graph_turtle.goto(-1, y_max)
        graph_turtle.penup()
        graph_turtle.goto(1, y_min)
        graph_turtle.pendown()
        graph_turtle.goto(1, y_max)

        graph_turtle.penup()
        graph_turtle.goto(0, y_max * 0.8)
        graph_turtle.color("green")
        graph_turtle.write("Область сходимости:\n-1 ≤ x < 1",
                           align="center", font=("Arial", 10, "bold"))

    def draw_legend(self, x_min, y_max, graph_turtle):
        graph_turtle.penup()
        graph_turtle.goto(x_min * 0.8, y_max * 0.9)
        graph_turtle.color("blue")
        graph_turtle.write("ln(1-x) через ряд", font=("Arial", 10, "normal"))

        graph_turtle.goto(x_min * 0.8, y_max * 0.8)
        graph_turtle.color("black")
        info_text = f"Xbeg={self.xb}\nXend={self.xe}\nDx={self.dx}\nEps={self.eps}"
        graph_turtle.write(info_text, font=("Arial", 9, "normal"))

    def print_info(self):
        valid_x = [self.x_values[i] for i in range(len(self.x_values)) if self.valid_points[i]]
        valid_y = [self.y_series_values[i] for i in range(len(self.x_values)) if self.valid_points[i]]
        print(f"\nОбласть сходимости ряда: -1 ≤ x < 1")
        print(f"Количество точек на графике: {len(valid_x)}")
        print(f"Диапазон X на графике: [{min(valid_x):.4f}, {max(valid_x):.4f}]")
        print(f"Диапазон Y на графике: [{min(valid_y):.4f}, {max(valid_y):.4f}]")
        print("Нажмите на график для выхода")

    def run(self):
        self.get_input()
        self.calculate_series()
        self.setup_screen()

        x_min, x_max, y_min, y_max = self.get_boundaries()

        graph_turtle = turtle.Turtle()
        graph_turtle.speed(0)
        graph_turtle.pensize(2)

        self.draw_axes(x_min, x_max, y_min, y_max, graph_turtle)
        self.draw_title(x_min, x_max, y_max, graph_turtle)
        self.draw_ticks(x_min, x_max, y_min, y_max, graph_turtle)
        self.draw_graph(graph_turtle)
        self.draw_convergence_region(y_min, y_max, graph_turtle)
        self.draw_legend(x_min, y_max, graph_turtle)

        graph_turtle.hideturtle()
        self.print_info()
        self.screen.exitonclick()


if __name__ == "__main__":
    plotter = SeriesPlotter()
    plotter.run()