"""
Activity 8 - Additional Exercises
Run each exercise in a separate Jupyter cell.
If using one notebook, copy one exercise at a time.
"""

# Jupyter Notebook Version

# ==========================================
# ADDITIONAL EXERCISE 1: LIBRARY MANAGEMENT
# ==========================================

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return f'"{self.title}" has been borrowed successfully.'
        return f'"{self.title}" is already borrowed.'

    def return_book(self):
        if not self.available:
            self.available = True
            return f'"{self.title}" has been returned successfully.'
        return f'"{self.title}" is already available.'

    def __str__(self):
        status = 'Available' if self.available else 'Borrowed'
        return f'{self.title} by {self.author} - {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            return book.borrow()
        return 'Book not found in the library.'

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            return book.return_book()
        return 'Book not found in the library.'

    def display_books(self):
        print('\nLibrary Collection:')
        for book in self.books:
            print(book)


library = Library()
num_books = int(input('Enter number of books to add: '))

for i in range(num_books):
    print(f'\nBook {i + 1}')
    title = input('Title: ')
    author = input('Author: ')
    status = input('Available? (yes/no): ').strip().lower()
    available = status == 'yes'
    library.add_book(Book(title, author, available))

library.display_books()

borrow_title = input('\nEnter title to borrow: ')
print(library.borrow_book(borrow_title))
cart.display_cart()