import datetime


def days_to_new_year(my_day, my_month, my_year):
    """Возвращает количество дней, оставшихся до нового года."""
    # по умолчанию пусть дата будет сегодняшняя
    user_date = datetime.date.today()
    # если день передан - заменяем его
    if my_day != '':
        user_date = user_date.replace(day=int(my_day))
    # если месяц передан - заменяем его
    if my_month != '':
        user_date = user_date.replace(month=int(my_month))
    # если год передан - заменяем его
    if my_year != '':
        user_date = user_date.replace(year=int(my_year))

    # вычисляем 1 января следующего года
    new_year_date = user_date.replace(year=user_date.year + 1, month=1, day=1)

    last_days = new_year_date - user_date
    return last_days.days

my_day = input('Введите день: ')
my_month = input('Введите месяц: ')
my_year = input('Введите год: ')

print(
    "До нового года {} дней.".format(days_to_new_year(my_day, my_month, my_year))
)
