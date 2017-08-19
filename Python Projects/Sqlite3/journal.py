import datetime

from peewee import *

db = SqliteDatabase('journal.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create database and the table if it doesn't already exist"""
    db.connect()
    db.create_tables([Entry], safe = True)
    db.close()

def menu_loop():
    """show the menu"""
    pass


def add_entry():
    """Add an entry"""
    pass


def view_entries():
    """View Previous Entries"""
    pass


def delete_entry(entry):
    """Delete an entry"""
    pass


if __name__ == '__main__':
    initialize()
    menu_loop()
