# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:40:41 2017

@author: Monic
"""

# datetime

import datetime

print(datetime.datetime.now())

current_time = datetime.datetime.now().replace(hour = 14)
print(current_time)

current_time = current_time.replace(hour = 2, minute = 0, second = 0, microsecond = 0)
print(current_time)

gen_date = datetime.datetime(2014,10,15,9,0)
print(gen_date)

print(datetime.datetime.now() - gen_date)
time_worked = datetime.datetime.now() - gen_date

print(time_worked.days)
print(time_worked.seconds)
print(time_worked.microseconds)
hours_worked = time_worked.days*12
print(hours_worked)

# timedelta

now = datetime.datetime.now()

# move forward by 3 days
print('move forward by 3 days')
print(now + datetime.timedelta(days = 3))

print(now + datetime.timedelta(days =-5))

# getting back time
print('getting back time')
print(now.time())
print(datetime.datetime.now().time())

# getting back date
print('getting back date')

print(now.date())
print(datetime.datetime.now().date())

# creating a timedelta

appointment = datetime.timedelta(minutes = 45)
print('Here is the appointment duration: {}'.format(appointment))

start = datetime.datetime(2017, 8, 2, 8, 00)
print('start = {}'.format(start))

end_time = start + appointment
print('end = {}'.format(end_time))

today = datetime.datetime.combine(datetime.date.today(), datetime.time())

print(today)


# POSIX TIMESTAMP QUIZ

# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.
import datetime
def timestamp_oldest(*arg):
    something = []
    for x in arg:
        something.append(x)
    something.sort()
    datetime_obj = datetime.datetime.fromtimestamp(something[0])
    return datetime_obj

