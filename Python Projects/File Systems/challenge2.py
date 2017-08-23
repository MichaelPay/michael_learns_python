# import os
#
#
# def create_daily_dir(string):
#     if int(string.split("-")[2]) > 31:
#         new_str = string.split("-")[2] + '-' + string.split("-")[0] + '-' + string.split("-")[1]
#     else:
#         new_str = string
#     os.makedirs(new_str, exist_ok=True)
#
# create_daily_dir('2017-04-22')

import os
import dateutil.parser

def create_daily_dir(string):
    os.makedirs(dateutil.parser.parse(string).strftime('%Y-%m-%d'), exist_ok=True)

create_daily_dir('05-04-2017')