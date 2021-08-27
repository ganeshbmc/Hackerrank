import datetime
import calendar

def findDay(date):
    dt = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return calendar.day_name[dt]

print(findDay(input()).upper())
