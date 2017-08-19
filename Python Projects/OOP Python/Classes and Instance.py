# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:12:09 2017

@author: Monic
"""
# a method is a function associated with a class

class Employee:
    pass

# emp_1 is called an INSTANCE of the class Employee
emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Michael'
emp_1.last = 'Pay'
emp_1.email = emp_1.first + '.' + emp_1.last + '@gmail.com'

print(emp_1.email)


class Employee_2:
    # init is a method since it is a function
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    # full_name is a function that concatenates the first and last
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    # a classmethod is a method that works
    # for the entire class, where the convention
    # cls is used instead of self
    # and the declarator @classmethod is used
    # to change the input from self to cls
    # the following class method splits up a
    # string with dashes '-' and returns the
    # variables from the string, essentially
    # parsing the string
    # it can be called with 
    # Employee_2.from_string(emp_str_1)
    # where emp_str_1 is a string that looks like
    # emp_str_1 = "Michael-Pay-40000"
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    # static methods
    # methods should be a statis method
    # if you don't access the INSTANCE
    # or the CLASS anywhere in the function
    # i.e. the following method never calls 
    # self or Employee_2 anywhere
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True
            
emp_3 = Employee_2('Michael','Pay',50000)
print(emp_3.email)
import datetime
my_date = datetime.date(2016, 7, 10)

# both the following calls are the same
print(emp_3.full_name())
print(Employee_2.full_name(emp_3))
print(Employee_2.is_workday(my_date))


# setattr example, allowing a class to 
# automatically set attributes for the instance
# upon instance creation

class Student:
    smart = True
    
    def __init__(self, name, smart=True, **kwargs):
        self.name = name
        self.smart = smart
        # kwargs is a definition
        # such as michael = 'Cool'
        # dictionary.items() returns a tuple
        # the tuple is then packed into key and value
        # key and value 
        for key, value in kwargs.items():
            setattr(self, key, value)

Michael = Student('Michael', GPA = 4.00, classcount = 48, student_ID = '20199993')

print(Michael.GPA)
print(Michael.student_ID)
print(Michael.classcount)
print(Michael.name)


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        list.sort(self.slots)
    pass
        