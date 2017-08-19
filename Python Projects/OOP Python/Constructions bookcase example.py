# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:37:21 2017

@author: Monic
"""

# Constructions

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

class Bookcase:
    def __init__(self, books = None):
        self.books = books
    
    @classmethod
    def create_book(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)

bok = Bookcase.create_book([('Michael Pay','Cool'),('You','me')])
print(bok.books[1])
print(bok.books[0])