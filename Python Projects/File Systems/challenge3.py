import os
import re
import dateutil.parser
import datetime


# Filenames consist of a username (alphanumeric, 3-12 characters)
# and a date (four digit year, two digit month, two digit day),
# and an extension. They should end up in the format
# year-month-day-username.extension.

# Example: kennethlove2-2012-04-29.txt becomes 2012-04-29-kennethlove2.txt

def cleanup(path):
    for name in os.listdir(path):
        # parse out username from file name
        username = re.search(r'[\w\d]*\d{3-12}', name).group()
        # parse out time from filename:
        re_time_search = re.search(r'\d{2,4}-\d{2,4}-\d{2,4}', name).group()
        # reformats parsed out time into YYYY-MM-DD format and save it as date variable
        date = dateutil.parser.parse(re_time_search).strftime('%Y-%m-%d')
        # parse out extension from file, alphanumeric allowed (.mp3, etc)
        ext = re.search(r'\.[\w\d]*', name).group()
        rename = date + '-' + username + '-' + ext
        os.rename(os.path.join(path, name), os.path.join(path, rename))
