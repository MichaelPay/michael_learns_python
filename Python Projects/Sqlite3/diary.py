import datetime
from collections import OrderedDict
import sys
import os

from peewee import *

db = SqliteDatabase('diary.db')


def clear_screen():
    os.system('cls'if os.name == 'nt' else 'clear')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear_screen()
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add an entry."""
    clear_screen()
    print("Enter your entry. Press ctrl+d (mac / linux) or ctrl +z and enter (windows) when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [Y/n] ').lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")


def view_entries(search_query=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    for entry in entries:
        clear_screen()
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('=' * len(timestamp))
        print(entry.content)
        print('N) next entry')
        print('d) delete entry')
        print('q) return to main menu')

        next_action = input('Action: [Nq] ').lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def search_entries():
    """Display entries based on keywords"""
    clear_screen()
    view_entries(input('Search query: '))


def delete_entry(entry):
    """Delete an entry"""
    clear_screen()
    entry_time = None
    entry_time = entry.timestamp
    if input('ARE YOU SURE YOU WANT TO DELETE THIS ENTRY? [yN] ').lower() == 'y':
        entry.delete_instance()
    clear_screen()
    input('Entry written on {} was deleted! '.format(entry_time))


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
    db.close()
