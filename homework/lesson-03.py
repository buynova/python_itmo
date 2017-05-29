# задача 1
print('Задача 1.\n')

total_square = 10 * 100
garden_bed_square = 15 * 25
free_space = total_square % garden_bed_square
print('Незанято {} м2.\n\n'.format(free_space))


# задача 2
print('Задача 2.\n')

plates = int(input('Количество тарелок: '))
fairy = float(input('Количество моющего средства: '))

while plates >= 1 and fairy >= 0.5:
    plates -= 1
    fairy -= 0.5
    print('Осталось {} моющего средства.'.format(fairy))

if plates < 1 and fairy >= 0.5:
    print('\nВсе тарелки вымыты. Осталось {} моющего средства.\n\n'.format(fairy))
elif fairy < 0.5 and plates >= 1:
    print('\nКончилось моющее средство. Осталось {} грязных тарелок.\n\n'.format(plates))
else:
    print('\nВсе тарелки вымыты и моющее средство кончилось.\n\n')


# задача 3
print('Задача 3.\n')

x_a = int(input('Введите координату x точки A: '))
y_a = int(input('Введите координату y точки A: '))
x_b = int(input('Введите координату x точки B: '))
y_b = int(input('Введите координату y точки B: '))
x_c = int(input('Введите координату x точки C: '))
y_c = int(input('Введите координату y точки C: '))

# находим квадраты длин сторон треугольника
ab = (x_b - x_a) ** 2 + (y_b - y_a) ** 2
print(ab)
bc = (x_c - x_b) ** 2 + (y_c - y_b) ** 2
print(bc)
ca = (x_a - x_c) ** 2 + (y_a - y_c) ** 2
print(ca)

# в прямоугольном треугольнике сумма квадратов катетов равна квадрату гипотенузы
if ab == bc + ca or bc == ab + ca or ca == ab + bc:
    print('Треугольник является прямоугольным.')
else:
    print('Треугольник не прямоугольный.')
