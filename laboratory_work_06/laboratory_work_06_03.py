import numpy as np


with open('input6.txt', 'r') as f:
    rows, cols = map(int, f.read().split(', '))


def make_matrix(rows, cols, a, b):
    matrix = (b - a) * np.random.random(size=(rows, cols)) + a
    return matrix


def sum_rows_with_negative(matrix):
    (n_row, n_col) = matrix.shape
    result = []

    for row in range(n_row):
        has_negative = False
        for col in range(n_col):
            if matrix[row][col] < 0:
                has_negative = True
                break

        if has_negative:
            row_sum = np.sum(matrix[row])
            result.append((row, row_sum))

    return result


def find_saddle_points(matrix):
    (n_row, n_col) = matrix.shape
    saddle_points = []

    for i in range(n_row):
        for j in range(n_col):
            is_min_in_row = True
            for k in range(n_col):
                if matrix[i][k] < matrix[i][j]:
                    is_min_in_row = False
                    break

            is_max_in_col = True
            for k in range(n_row):
                if matrix[k][j] > matrix[i][j]:
                    is_max_in_col = False
                    break

            if is_min_in_row and is_max_in_col:
                saddle_points.append((i, j, matrix[i][j]))

    return saddle_points


def print_matrix(matrix):
    (n_row, n_col) = matrix.shape
    for row in range(n_row):
        for col in range(n_col):
            print("{0: 8.3f}".format(matrix[row][col]), end=" ")
        print()
    print()


def midl_disp(matrix):
    total_sum = 0.0
    (n_row, n_col) = matrix.shape

    for row in range(n_row):
        for col in range(n_col):
            total_sum += matrix[row][col]

    midl = total_sum / matrix.size

    disp = 0.0
    for row in range(n_row):
        for col in range(n_col):
            disp += (matrix[row][col] - midl) ** 2

    return midl, disp / (matrix.size - 1)


my_matrix = make_matrix(rows, cols, -5.0, 5.0)


# Статистика
m_midl, m_disp = midl_disp(my_matrix)

negative_rows = sum_rows_with_negative(my_matrix)

saddle_points = find_saddle_points(my_matrix)


with open('output6.txt', 'w+') as f:
    f.write(f'Исходная матрица: \n{print_matrix(my_matrix)}\n'
                 f'Среднее = {m_midl:7.3f}\n'
            f'Дисперсия = {m_disp:7.3f}\n'
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
