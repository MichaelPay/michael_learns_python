# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:41:32 2017

@author: Monic
"""

# meetings scheduler

from datetime import datetime as dt

import pytz

OTHER_TIMEZONES = [
        pytz.timezone('US/Eastern'),
        pytz.timezone('Pacific/Auckland'),
        pytz.timezone('Asia/Calcutta'),
        pytz.timezone('UTC'),
        pytz.timezone('Europe/Paris'),
        pytz.timezone('Africa/Khartoum'),
        
        
]

fmt = '%Y-%m-%d %H:%M:%S %Z%z'
fmt1 = '%m/%d/%Y %H:%M'

while True:
    date_input = input('When is your meeting? Please use MM/DD/YYYY HH:MM format. ')
    try:
        local_date = dt.strptime(date_input, fmt1)
    except ValueError:
        print("{} doesn't seem to be a valid date & time.".fomrat(date_input))
    else:
        local_date = pytz.timezone('US/Pacific').localize(local_date)
        utc_date = local_date.astimezone(OTHER_TIMEZONES[3])
        
        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
    
# timezone converter, accepts a string that matches one of the pytz's utc codes

import datetime as dt
import pytz

starter = pytz.utc.localize(dt.datetime(2015, 10, 21, 23, 29))

def to_timezone(zonename):
    zone = pytz.timezone(zonename)
    new_zone = starter.astimezone(zone)
    return new_zone