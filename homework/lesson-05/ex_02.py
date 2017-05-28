"""
Модуль для перевода чисел из десятичной системы счисления в двоичную, восьмеричную и шестнадцатеричную и наоборот.
"""


def bin_to_dec(number):
    """Перевод числа из двоичной системы счисления в десятичную."""
    # изменяем тип аргумента с int на str для работы с ним как с итерируемым объектом
    bin_number = list(str(number))
    return convert_to_dec(bin_number, 2)


def oct_to_dec(number):
    """Перевод числа из восьмеричной системы счисления в десятичную."""
    # изменяем тип аргумента с int на str для работы с ним как с итерируемым объектом
    oct_number = list(str(number))
    return convert_to_dec(oct_number, 8)


def hex_to_dec(number):
    """Перевод числа из шестнадцатеричной системы счисления в десятичную."""
    # изменяем тип аргумента с int на str для работы с ним как с итерируемым объектом
    hex_number = list(str(number.upper()))
    for i, n in enumerate(hex_number):
        if n == 'A':
            hex_number[i] = 10
        elif n == 'B':
            hex_number[i] = 11
        elif n == 'C':
            hex_number[i] = 12
        elif n == 'D':
            hex_number[i] = 13
        elif n == 'E':
            hex_number[i] = 14
        elif n == 'F':
            hex_number[i] = 15
    return convert_to_dec(hex_number, 16)


def dec_to_bin(number):
    """Перевод числа из десятичной системы счисления в двоичную."""
    bin_list = convert_from_dec(number, 2)
    bin_number = ''
    for n in bin_list:
        bin_number += str(n)
    return bin_number


def dec_to_oct(number):
    """Перевод числа из десятичной системы счисления в восьмеричную."""
    oct_list = convert_from_dec(number, 8)
    oct_number = ''
    for n in oct_list:
        oct_number += str(n)
    return oct_number


def dec_to_hex(number):
    """Перевод числа из десятичной системы счисления в шестнадцатеричную."""
    hex_list = convert_from_dec(number, 16)
    hex_number = ''
    for n in hex_list:
        if n == 10:
            n = 'A'
        elif n == 11:
            n = 'B'
        elif n == 12:
            n = 'C'
        elif n == 13:
            n = 'D'
        elif n == 14:
            n = 'E'
        elif n == 15:
            n = 'F'
        hex_number += str(n)
    return hex_number


def convert_to_dec(number, notation):
    """Перевод числа в десятичную систему счисления.

    Args:
        number: число для перевода (list).
        notation: исходная система счисления (int).

    Returns:
        Число в десятичной системе.
    """
    # разворачиваем число задом наперед (для удобства работы с enumerate)
    number.reverse()

    dec_number = 0
    # получается, что начинаем с конца: последняя цифра числа number теперь имеет индекс 0 в списке
    # каждую цифру последовательно умножаем на 2 в степени, равной её индексу
    for i, n in enumerate(number):
        a = notation ** i * int(n)
        dec_number += a

    # способ без использования enumerate
    # dec_number = 0
    # e = len(number) - 1
    # for n in number:
    #     a = notation ** e * int(n)
    #     dec_number += a
    #     e -= 1

    return dec_number


def convert_from_dec(number, notation):
    """Перевод числа из десятичной системы счисления в другие.

    Args:
        number: число для перевода (int).
        notation: конечная система счисления (int).

    Returns:
        Число в указанной системе счисления.
    """
    new_number = []
    while number > 0:
        res = number // notation
        a = number % notation
        new_number.append(a)
        number = res

    new_number.reverse()
    return new_number

bin_num = 10110010111001
oct_num = 642537
hex_num = '42d6A'
dec_num = 1093754

print(
    'Перевод числа {bin} из двоичной системы в десятичную: {dec}'.format(
        bin=bin_num,
        dec=bin_to_dec(bin_num)
    )
)
print(
    'Перевод числа {oct} из восьмеричной системы в десятичную: {dec}'.format(
        oct=oct_num,
        dec=oct_to_dec(oct_num)
    )
)
print(
    'Перевод числа {hex} из шестнадцатеричной системы в десятичную: {dec}'.format(
        hex=hex_num,
        dec=hex_to_dec(hex_num)
    )
)
print(
    'Перевод числа {dec} из десятичной системы в двоичную: {bin}'.format(
        dec=dec_num,
        bin=dec_to_bin(dec_num)
    )
)
print(
    'Перевод числа {dec} из десятичной системы в восьмеричную: {oct}'.format(
        dec=dec_num,
        oct=dec_to_oct(dec_num)
    )
)
print(
    'Перевод числа {dec} из десятичной системы в шестнадцатеричную: {hex}'.format(
        dec=dec_num,
        hex=dec_to_hex(dec_num)
    )
)
