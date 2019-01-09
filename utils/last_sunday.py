# import datetime
#
#
# day = input("Input date (Y-m-d):")
# day_datetime = datetime.datetime.strptime(day, "%Y-%m-%d")
# last_monday = day_datetime - datetime.timedelta(days=day_datetime.weekday())
# coming_monday = day_datetime + datetime.timedelta(days=-day_datetime.weekday(), weeks=1)
# print("Date:", day_datetime)
# print("Last Monday:", last_monday)
# print("Coming Monday:", coming_monday)
# print(day_datetime.weekday())
# print(datetime.timedelta(days=day_datetime.weekday()))
# print(datetime.timedelta(days=day_datetime.weekday(), weeks=1))

import datetime
import calendar


def last_sunday(day):
    # day = input("Input date (Y-m-d):")
    sunday = datetime.datetime.strptime(day, "%Y-%m-%d")
    one_day = datetime.timedelta(days=1)

    while sunday.weekday() != calendar.SUNDAY:
        sunday -= one_day

    return sunday.strftime("%Y-%m-%d")


def human_date(date):
    datetime_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    return datetime_object.strftime("%d %B %Y")
