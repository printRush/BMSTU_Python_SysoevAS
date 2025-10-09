import numpy as np


with open('input6.txt', 'r') as f:
    rows, cols = map(int, f.read().split(', '))

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
    M = []
    for Row in range(nRow):
        for Col in range(nCol):
            M.append("{0:.3f}".format(Matr[Row][Col]))
        M.append("|")
    return M


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



MyMatr = MakeMatr(rows, cols, -5.0, 5.0)


# Статистика
mMidl, mDisp = MidlDisp(MyMatr)

# 1. Сумма строк с отрицательными элементами
negative_rows = SumRowsWithNegative(MyMatr)

# if negative_rows:
#     for row_num, row_sum in negative_rows:
#         print(f"   Строка {row_num}: сумма = {row_sum:8.3f}")
# else:
#     print("   В матрице нет строк с отрицательными элементами")

# 2. Седловые точки
# print("\n2. Поиск седловых точек:")
saddle_points = FindSaddlePoints(MyMatr)

# if saddle_points:
#     print("   Найдены седловые точки:")
#     for row, col, value in saddle_points:
#         print(f"   Строка {row}, Столбец {col}: значение = {value:8.3f}")
# else:
#     print("   Седловые точки не найдены")



with open('output6.txt', 'w+') as f:
    f.write(f'Исходная матрица: \n{PrintMatr(MyMatr)}\n'
                 f'Среднее = {mMidl:7.3f}\n'
            f'Дисперсия = {mDisp:7.3f}\n'
            f'1. Суммы элементов в строках с отрицательными элементами:\n')
    if negative_rows:
        for row_num, row_sum in negative_rows:
            f.write(f"Строка {row_num}: сумма = {row_sum:8.3f}\n")
    else:
        f.write(f"В матрице нет строк с отрицательными элементами")
    f.write('\n2. Поиск седловых точек:\n')
    if saddle_points:
        f.write("Найдены седловые точки:\n\n")
        for row, col, value in saddle_points:
            f.write(f"Строка {row}, Столбец {col}: значение = {value:8.3f}\n\n")
    else:
        f.write("Седловые точки не найдены\n\n")




print("Done!")