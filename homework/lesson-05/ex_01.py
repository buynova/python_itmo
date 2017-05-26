import datetime


def days_to_new_year(year):
    new_year_day = datetime.date(year + 1, 1, 1)
    today = datetime.date.today()
    return new_year_day - today

print(days_to_new_year(2017))
