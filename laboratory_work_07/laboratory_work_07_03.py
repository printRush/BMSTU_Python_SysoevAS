import math
import turtle

print('Введите Xbeg, Xend, Dx и Eps')

xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))

# Создаем списки для хранения данных
x_values = []
y_series_values = []
valid_points = []

print("+-----------+-----------+-----+")
print("I     X     I     Y     I  N  I")
print("+-----------+-----------+-----+")

# Вычисляем значения функции
x = xb
while x <= xe:
    if -1 <= x < 1:  # Область сходимости ряда
        n = 1
        term = -x
        sum_series = term

        # Вычисляем сумму ряда
        while abs(term) >= eps and n < 1000:
            n += 1
            term = -(x ** n) / n
            sum_series += term

        x_values.append(x)
        y_series_values.append(sum_series)
        valid_points.append(True)
        print(f"|{x:10.4f} |{sum_series:10.4f} |{n:4} |")
    else:
        x_values.append(x)
        y_series_values.append(None)
        valid_points.append(False)
        print(f"|{x:10.4f} |{'не опр.':^10} |{' -':4} |")

    x = x + dx

print("+-----------+-----------+-----+")

# Настройка окна turtle
screen = turtle.Screen()
screen.title(f"График функции ln(1-x) через ряд Тейлора (точность {eps})")
screen.bgcolor("white")
screen.setup(width=0.9, height=0.9)  # Занимает 90% экрана

# Определяем границы данных для масштабирования
valid_x = [x_values[i] for i in range(len(x_values)) if valid_points[i]]
valid_y = [y_series_values[i] for i in range(len(x_values)) if valid_points[i]]

if not valid_x:  # Если нет валидных точек
    print("Нет точек для построения графика в области сходимости")
    turtle.done()
    exit()

x_min, x_max = min(valid_x), max(valid_x)
y_min, y_max = min(valid_y), max(valid_y)

# Добавляем отступы для красоты
x_padding = (x_max - x_min) * 0.1
y_padding = (y_max - y_min) * 0.1

x_min -= x_padding
x_max += x_padding
y_min -= y_padding
y_max += y_padding

# Настраиваем мировые координаты
screen.setworldcoordinates(x_min, y_min, x_max, y_max)

# Создаем черепашку для рисования
graph_turtle = turtle.Turtle()
graph_turtle.speed(0)
graph_turtle.pensize(2)

# Рисуем оси координат
graph_turtle.penup()
graph_turtle.goto(x_min, 0)
graph_turtle.pendown()
graph_turtle.goto(x_max, 0)  # Ось X
graph_turtle.penup()
graph_turtle.goto(0, y_min)
graph_turtle.pendown()
graph_turtle.goto(0, y_max)  # Ось Y

# Подписи осей
graph_turtle.penup()
graph_turtle.goto(x_max * 0.9, y_max * 0.05)
graph_turtle.write("X", font=("Arial", 12, "bold"))
graph_turtle.goto(x_max * 0.05, y_max * 0.9)
graph_turtle.write("Y", font=("Arial", 12, "bold"))

# Заголовок графика
graph_turtle.goto((x_min + x_max) / 2, y_max * 0.95)
graph_turtle.write(f"ln(1-x) через ряд Тейлора (ε={eps})",
                   align="center", font=("Arial", 14, "bold"))


# Разметка осей (примерные деления)
def draw_ticks():
    graph_turtle.pensize(1)
    graph_turtle.color("gray")

    # Деления на оси X
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

    # Деления на оси Y
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


draw_ticks()

# Рисуем график
graph_turtle.pensize(2)
graph_turtle.color("blue")
graph_turtle.penup()

# Находим первую валидную точку
first_valid = False
for i in range(len(x_values)):
    if valid_points[i]:
        graph_turtle.goto(x_values[i], y_series_values[i])
        first_valid = True
        break

if first_valid:
    graph_turtle.pendown()

    # Рисуем линию через все валидные точки
    for i in range(len(x_values)):
        if valid_points[i]:
            graph_turtle.goto(x_values[i], y_series_values[i])
        else:
            # Прерываем линию при разрыве
            graph_turtle.penup()

# Область сходимости
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

# Подпись области сходимости
graph_turtle.penup()
graph_turtle.goto(0, y_max * 0.8)
graph_turtle.color("green")
graph_turtle.write("Область сходимости:\n-1 ≤ x < 1",
                   align="center", font=("Arial", 10, "bold"))

# Легенда
graph_turtle.penup()
graph_turtle.goto(x_min * 0.8, y_max * 0.9)
graph_turtle.color("blue")
graph_turtle.write("ln(1-x) через ряд", font=("Arial", 10, "normal"))

# Информация о параметрах
graph_turtle.goto(x_min * 0.8, y_max * 0.8)
graph_turtle.color("black")
info_text = f"Xbeg={xb}\nXend={xe}\nDx={dx}\nEps={eps}"
graph_turtle.write(info_text, font=("Arial", 9, "normal"))

# Скрываем черепашку после рисования
graph_turtle.hideturtle()

# Ждем клика для закрытия
screen.exitonclick()

# Дополнительная информация в консоль
print(f"\nОбласть сходимости ряда: -1 ≤ x < 1")
print(f"Количество точек на графике: {len(valid_x)}")
print(f"Диапазон X на графике: [{min(valid_x):.4f}, {max(valid_x):.4f}]")
print(f"Диапазон Y на графике: [{min(valid_y):.4f}, {max(valid_y):.4f}]")
print("Нажмите на график для выхода")