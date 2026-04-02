"""
Лабораторная работа №12
Модули и пакеты в Python
"""

print("=" * 60)
print("ЛАБОРАТОРНАЯ РАБОТА №12")
print("Модули и пакеты")
print("=" * 60)

# ==================== 1. Импорт всего модуля ====================
print("\n--- 1. Импорт всего модуля ---")
import mymodule.math_ops as math_ops

print(f"add(10, 5) = {math_ops.add(10, 5)}")
print(f"multiply(10, 5) = {math_ops.multiply(10, 5)}")
print(f"power(2, 8) = {math_ops.power(2, 8)}")
print(f"factorial(5) = {math_ops.factorial(5)}")
print(f"PI = {math_ops.PI}")

# ==================== 2. Импорт конкретных элементов ====================
print("\n--- 2. Импорт конкретных элементов ---")
from mymodule.math_ops import add, multiply, PI

print(f"add(7, 3) = {add(7, 3)}")
print(f"multiply(7, 3) = {multiply(7, 3)}")
print(f"PI = {PI}")

# ==================== 3. Импорт с переименованием ====================
print("\n--- 3. Импорт с переименованием ---")
from mymodule.math_ops import power as pow_func
from mymodule.math_ops import factorial as fact

print(f"power(3, 4) = {pow_func(3, 4)}")
print(f"factorial(6) = {fact(6)}")

# ==================== 4. Импорт всех элементов (__all__) ====================
print("\n--- 4. Импорт всех элементов (__all__) ---")
from mymodule.math_ops import *

print(f"add(2, 2) = {add(2, 2)}")
print(f"multiply(2, 2) = {multiply(2, 2)}")
print(f"power(3, 3) = {power(3, 3)}")
print(f"factorial(4) = {factorial(4)}")
# subtract и divide не импортируются, так как их нет в __all__

# ==================== 5. Импорт модуля из пакета ====================
print("\n--- 5. Импорт модуля из пакета ---")
import mypackage.geometry

print(f"Площадь круга (r=3): {mypackage.geometry.circle_area(3)}")
print(f"Площадь прямоугольника (5x8): {mypackage.geometry.rectangle_area(5, 8)}")

# ==================== 6. Импорт элементов из модуля в пакете ====================
print("\n--- 6. Импорт элементов из модуля в пакете ---")
from mypackage.geometry import circle_area, rectangle_area

print(f"Площадь круга (r=4): {circle_area(4)}")
print(f"Площадь прямоугольника (6x7): {rectangle_area(6, 7)}")

# ==================== 7. Импорт из подпакета ====================
print("\n--- 7. Импорт из подпакета ---")
from mypackage.subpackage.strings import reverse, to_upper, count_vowels

print(f"reverse('Python'): {reverse('Python')}")
print(f"to_upper('hello'): {to_upper('hello')}")
print(f"count_vowels('Hello World'): {count_vowels('Hello World')}")

# ==================== 8. Импорт всего подпакета ====================
print("\n--- 8. Импорт всего подпакета ---")
from mypackage.subpackage import strings

print(f"reverse('lab'): {strings.reverse('lab')}")
print(f"to_lower('PYTHON'): {strings.to_lower('PYTHON')}")

print("\n" + "=" * 60)
print("Работа программы завершена")
print("=" * 60)