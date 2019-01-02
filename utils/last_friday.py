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


def last_friday(day):
    # day = input("Input date (Y-m-d):")
    friday = datetime.datetime.strptime(day, "%Y-%m-%d")
    one_day = datetime.timedelta(days=1)

    while friday.weekday() != calendar.SUNDAY:
        friday -= one_day

    return friday.strftime("%Y-%m-%d")
