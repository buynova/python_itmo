# модули и пакеты
# модуль - это файл python
# .pyc - скомпилированные pycache-файлы, которые используются при повторном запуске кода.
# Могут работать без самого кода.


import sys
import square_shapes
from square_shapes import calculate_square_area
from square_shapes import calculate_rectangle_area as calc_rect_area
from square_shapes import *  # импортировать имена из модуля в текущее пространство имен. лучше не использовать
import os.path as Path

print(sys.path)

print(
    square_shapes.calculate_square_area(4)
)

print(calculate_square_area(5))

print(
    calc_rect_area(6, 3)
)

print(__name__)


if __name__ == '__main__':
    print(square_shapes.calculate_square_area(4))
