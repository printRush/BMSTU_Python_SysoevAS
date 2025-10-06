R = float(input("Введите R: "))
X = float(input("Введите X: "))
Y = float(input("Введите Y: "))

flag = False

if X >= 0 and Y >= 0:
    if X**2 + Y**2 <= R**2:
        flag = True

elif X <= 0 and Y <= 0:
    if Y >= -R - X:
        flag = True

if flag:
    print(f"Точка ({X}, {Y}) попадает в область.")
else:
    print(f"Точка ({X}, {Y}) вне области.")