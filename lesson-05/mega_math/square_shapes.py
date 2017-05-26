# coding: utf-8
# для python 3 указание кодировки не обязательно!

"""
Модуль расчета площадей геометрических фигур.
"""


def calculate_square_area(a):
    """Возвращает площадь квадрата."""
    return a ** 2


def calculate_rectangle_area(a, b):
    """Возвращает площадь прямоугольника."""
    return a * b

# указываем, что будет импортироваться, если используем import *
__all__ = [
    'calculate_square_area',
    'calculate_rectangle_area'
]

if __name__ == '__main__':
    print('tests here')
