# задача 1
print('Задача 1.\n')


# def palindrome_check(str):



# задача 2
print('Задача 2.\n')


def point_coordinates_check(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        print('Одна или обе координаты равны 0.')

print(
    'Точка лежит в четверти', point_coordinates_check(2, -4)
)
