"""
Модуль с геометрическими функциями.
"""

__all__ = ['circle_area', 'rectangle_area', 'triangle_area']

# Константа
PI = 3.14159

def circle_area(radius):
    """Площадь круга"""
    return PI * radius ** 2

def rectangle_area(width, height):
    """Площадь прямоугольника"""
    return width * height

def triangle_area(base, height):
    """Площадь треугольника"""
    return 0.5 * base * height

def circumference(radius):
    """Длина окружности"""
    return 2 * PI * radius


if __name__ == "__main__":
    print("=== Модуль geometry запущен как программа ===")
    print(f"Площадь круга (r=5): {circle_area(5)}")
    print(f"Площадь прямоугольника (4x6): {rectangle_area(4, 6)}")
    print(f"Площадь треугольника (3,4): {triangle_area(3, 4)}")
else:
    print("Модуль geometry импортирован.")