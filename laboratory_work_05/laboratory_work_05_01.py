import numpy as np


def MakeMatr(rows, cols, a, b):
    Matr = (b - a) * np.random.random(size=(rows, cols)) + a
    return Matr


def SumRowsWithNegative(Matr):
    (nRow, nCol) = Matr.shape
    result = []

    for Row in range(nRow):
        has_negative = False
        for Col in range(nCol):
            if Matr[Row][Col] < 0:
                has_negative = True
                break

        if has_negative:
            row_sum = np.sum(Matr[Row])
            result.append((Row, row_sum))

    return result


def FindSaddlePoints(Matr):
    (nRow, nCol) = Matr.shape
    saddle_points = []

    for i in range(nRow):
        for j in range(nCol):
            is_min_in_row = True
            for k in range(nCol):
                if Matr[i][k] < Matr[i][j]:
                    is_min_in_row = False
                    break

            is_max_in_col = True
            for k in range(nRow):
                if Matr[k][j] > Matr[i][j]:
                    is_max_in_col = False
                    break

            if is_min_in_row and is_max_in_col:
                saddle_points.append((i, j, Matr[i][j]))

    return saddle_points


def PrintMatr(Matr):
    (nRow, nCol) = Matr.shape
    for Row in range(nRow):
        for Col in range(nCol):
            print("{0: 8.3f}".format(Matr[Row][Col]), end=" ")
        print()
    print()


def MidlDisp(Matr):
    total_sum = 0.0
    (nRow, nCol) = Matr.shape

    for Row in range(nRow):
        for Col in range(nCol):
            total_sum += Matr[Row][Col]

    Midl = total_sum / Matr.size

    Disp = 0.0
    for Row in range(nRow):
        for Col in range(nCol):
            Disp += (Matr[Row][Col] - Midl) ** 2

    return (Midl, Disp / (Matr.size - 1))


# Основная программа
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

MyMatr = MakeMatr(rows, cols, -5.0, 5.0)

print("Исходная матрица:")
PrintMatr(MyMatr)

# Статистика
mMidl, mDisp = MidlDisp(MyMatr)
print("Среднее = {0:7.3f}".format(mMidl))
print("Дисперсия = {0:7.3f}".format(mDisp))

# 1. Сумма строк с отрицательными элементами
print("\n1. Суммы элементов в строках с отрицательными элементами:")
negative_rows = SumRowsWithNegative(MyMatr)

if negative_rows:
    for row_num, row_sum in negative_rows:
        print(f"   Строка {row_num}: сумма = {row_sum:8.3f}")
else:
    print("   В матрице нет строк с отрицательными элементами")

# 2. Седловые точки
print("\n2. Поиск седловых точек:")
saddle_points = FindSaddlePoints(MyMatr)

if saddle_points:
    print("   Найдены седловые точки:")
    for row, col, value in saddle_points:
        print(f"   Строка {row}, Столбец {col}: значение = {value:8.3f}")
else:
    print("   Седловые точки не найдены")