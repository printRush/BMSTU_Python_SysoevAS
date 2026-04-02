"""
Модуль со строковыми функциями.
"""

__all__ = ['reverse', 'to_upper', 'to_lower', 'count_vowels']

def reverse(s):
    """Переворот строки"""
    return s[::-1]

def to_upper(s):
    """Преобразование в верхний регистр"""
    return s.upper()

def to_lower(s):
    """Преобразование в нижний регистр"""
    return s.lower()

def count_vowels(s):
    """Подсчёт гласных букв"""
    vowels = 'aeiouyаеёиоуыэюя'
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

def capitalize(s):
    """Первая буква заглавная"""
    if not s:
        return s
    return s[0].upper() + s[1:].lower()


if __name__ == "__main__":
    print("=== Модуль strings запущен как программа ===")
    print(f"reverse('hello'): {reverse('hello')}")
    print(f"to_upper('hello'): {to_upper('hello')}")
    print(f"count_vowels('hello world'): {count_vowels('hello world')}")
else:
    print("Модуль strings импортирован.")