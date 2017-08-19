# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:04:27 2017

@author: Monic
"""

# Timezone

import datetime

pacific = datetime.timezone(datetime.timedelta(hours = -8))
eastern = datetime.timezone(datetime.timedelta(hours = -5))
naive = datetime.datetime(2014,4,21,9)
aware = datetime.datetime(2014,4,21,9, tzinfo = pacific)

# naive.astimezone(eastern) yields error
aware.astimezone(eastern)
auckland = datetime.timezone(datetime.timedelta(hours = 13))

mumbai = datetime.timezone(datetime.timedelta(hours=5, minutes = 30))

# replacing timezones for a naive data

import datetime as dt

naive = dt.datetime(2015, 10, 21, 4, 29)

pacific = dt.timezone(dt.timedelta(hours = -8))
hill_valley = naive.replace(tzinfo = pacific)

# moving timezone to a new timezone

new_time_zone = dt.timezone(dt.timedelta(hours = 1))
paris = hill_valley.astimezone(new_time_zone)

# pytz

import pytz

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
utc = pytz.utc

# localize makes a naive datetime localized datetime
start = pacific.localize(dt.datetime(2014, 4, 21, 9))
print(start.strftime(fmt))

# as timezone converts a timezone into a local timezone 
start_eastern = start.astimezone(eastern)
print(start_eastern.strftime(fmt))

# usually you would want to start the timezone as utc
# and then convert them to the current time zone such as 
# below
start_utc = dt.datetime(2014,4,21,1, tzinfo = utc)

print(start_utc.strftime(fmt))

start_pacific = start_utc.astimezone(pacific)
print(start_pacific.strftime(fmt))

auckland = pytz.timezone('Pacific/Auckland')
mumbai = pytz.timezone('Asia/Calcutta')

# process of converting stirng to localized string to eastern
# so that you can conver easily to another dates and times

apollo_13_naive = dt.datetime(1970, 4, 11, 14, 13)
apollo_13_eastern = eastern.localize(apollo_13_naive)
print(apollo_13_naive)
print(apollo_13_eastern)

apollo_13_utc = apollo_13_eastern.astimezone(utc)
print(apollo_13_utc.strftime(fmt))

# finding timezone tools in pytz

print(pytz.all_timezones)
print(pytz.country_timezones['us'])

# pytz challenge

import datetime as dt
import pytz

fmt = '%m-%d %H:%M %Z%z'
starter = dt.datetime(2015, 10, 21, 4, 29)

pac = pytz.timezone('US/Pacific')
local = pac.localize(starter)

pytz_string = local.strftime(fmt)

