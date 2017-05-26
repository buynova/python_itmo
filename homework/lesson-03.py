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

a_x = int(input('Задайте координату x вершины A (целое число): '))
a_y = int(input('Задайте координату y вершины A (целое число): '))
b_x = int(input('Задайте координату x вершины B (целое число): '))
b_y = int(input('Задайте координату y вершины B (целое число): '))
c_x = int(input('Задайте координату x вершины C (целое число): '))
c_y = int(input('Задайте координату y вершины C (целое число): '))
