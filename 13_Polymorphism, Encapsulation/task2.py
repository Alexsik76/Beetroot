# Library
from datetime import datetime
from typing import List, Any


class Author:

    def __init__(self, name: str, country: str, birthday: str):
        self.name = name
        self.country = country
        self.birthday = datetime.date(datetime.strptime(birthday, '%Y-%m-%d'))
        self.books = []

    def __repr__(self):
        return f"Author('{self.name}, {self.country}, {self.birthday}')"

    def __str__(self):
        return f"Author: {self.name} was born in {self.birthday} in {self.country}"


class Library:

    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        """Returns an instance of Book class and adds the book to the books list for the current library"""
        self.books.append(Book(name, year, author))

    def group_by_author(self, author: Author):
        """Returns a list of all books grouped by the specified author"""
        list_by_author = list(filter(lambda x: x.author is author, self.books))
        return list_by_author

    def group_by_year(self, year: int):
        """Returns a list of all the books grouped by the specified year"""
        list_by_year: List[Any] = list(filter(lambda x: x.year is year, self.books))
        return list_by_year

    def __repr__(self):
        return f"Library('{self.name}')"

    def __str__(self):
        list_of_books = '\n'.join(map(lambda x: f'{x.author.name}, {x.name}, {x.year}', self.books))
        return list_of_books


class Book:
    all_books = 0

    def __init__(self, name: str, year: int, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.all_books += 1

    def __del__(self):
        Book.all_books -= 1

    def __repr__(self):
        return f"Book('{self.name}, {self.year}, {self.author}')"

    def __str__(self):
        return f"The book: {self.name} was written in {self.year} by {self.author}"


a1 = Author('Тарас Шевченко', 'Україна', '1814-02-25')

lib1 = Library('Вінницька центральна міська бібліотека')
lib1.new_book('Кобзар', 1840, a1)
lib1.new_book('Гайдамаки', 1841, a1)
print(lib1)
print(Book.all_books)
