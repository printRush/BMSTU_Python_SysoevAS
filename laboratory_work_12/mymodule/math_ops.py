"""
Модуль с математическими функциями.
"""

__all__ = ['add', 'multiply', 'power', 'factorial']

# Константа
PI = 3.14159

# Функции
def add(a, b):
    """Сложение"""
    return a + b

def subtract(a, b):
    """Вычитание"""
    return a - b

def multiply(a, b):
    """Умножение"""
    return a * b

def divide(a, b):
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b

def power(a, b):
    """Возведение в степень"""
    return a ** b

def factorial(n):
    """Факториал"""
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("=== Модуль запущен как программа ===")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(5, 3) = {subtract(5, 3)}")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"divide(6, 3) = {divide(6, 3)}")
    print(f"power(2, 4) = {power(2, 4)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"PI = {PI}")
else:
    print("Модуль math_ops импортирован.")