# задача 1
print('Задача 1.\n')


def palindrome_check(string):
    list_a = list(str(string))
    list_b = list(list_a)
    list_b.reverse()
    if list_a == list_b:
        return True
    else:
        return False

num1 = 12521
num2 = 56268
str1 = 'ololo'
str2 = 'hello'
print('Is \'{num}\' a palindrome? {res}'.format(num=num1, res=palindrome_check(num1)))
print('Is \'{num}\' a palindrome? {res}'.format(num=num2, res=palindrome_check(num2)))
print('Is \'{str}\' a palindrome? {res}'.format(str=str1, res=palindrome_check(str1)))
print('Is \'{str}\' a palindrome? {res}\n'.format(str=str2, res=palindrome_check(str2)))


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


# задача 3
print('Задача 3.\n')


def bubble_sort(num_list):
    l = len(num_list)
    i = 0
    while i < l:
        for j in range(l - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
        i += 1
    return num_list

print(bubble_sort([2, 7, 5, 1, 6]))
