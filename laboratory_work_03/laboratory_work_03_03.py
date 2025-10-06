import math

print('Введите Xbeg, Xend, Dx и Eps')

xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))

print("+--------+--------+-----+")
print("I   X    I   Y    I  N  I")
print("+--------+--------+-----+")

x = xb
while x <= xe:
    # Проверка области определения
    if -1 <= x < 1:
        print("|{:12.4f}|{:^15}|{:15}|".format(x, "не опр.", n))
    else:
        n = 1
        term = -x
        sum_series = term

        while abs(term) >= eps:
            n += 1
            term = -(x ** n) / n
            sum_series += term

            if n > 10:
                break

            math_result = math.log(1 - x)
            print("|{:12.4f}|{:15.8f}{:15}|".format(x, math_result, n))

    x = x + dx
print("+--------+--------+-----+")