# Исключения. Exceptions
try:
    # code block, в котором ловим исключения
    a = 'no string'
    i = int(a)
    print('wowowow')
except ValueError as e:  # ловим ошибку типа ValueError
    print(e)  # в переменной е - сама ошибка
except:
    # обработка ошибок
    print('Любая ошибка')


try:
    # выбрасываем ошибку
    raise RuntimeError('сообщение об ошибке')
except RuntimeError as e:
    print(e)


class MyCustomError(BaseException):
    pass

try:
    raise MyCustomError('что-то пошло не так')
except MyCustomError as e:
    print(e)


try:
    f = open('lesson-09.py')
    a = 1
    s = f.readd()
except AttributeError as e:
    print(e)
finally:
    print('сюда программа не дойдет без finally')
    print(f, a)
    f.close()
