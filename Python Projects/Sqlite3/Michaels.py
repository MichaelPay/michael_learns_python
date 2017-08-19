from peewee import *

db = SqliteDatabase('todolist.db')


class Item(Model):
    priority = IntegerField(default=5)
    description = CharField(max_length=255, unique=True)
    checked = BooleanField(default=False)

    class Meta:
        database = db


todo = [
    {'checked': False, 'priority': 5, 'description': 'Something Interesting'},
    {'checked': False, 'priority': 2, 'description': 'Cool beans'},
    {'checked': False, 'priority': 1, 'description': 'Eat!!!'},

]

def add_todos():
    for x in todo:
        Item.create(checked = x['checked'], priority = x['priority'],description = x['description'])

if __name__ == '__main__':
    db.connect()
    db.create_tables([Item], safe=True)
    add_todos()
