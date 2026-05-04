class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"✅ You borrowed '{book.title}'.")
                else:
                    print("❌ Book already borrowed.")
                return
        print("❌ Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"✅ You returned '{book.title}'.")
                else:
                    print("❌ Book was not borrowed.")
                return
        print("❌ Book not found.")

    def display_books(self):
        print("\n📖 Library Collection:")
        for book in self.books:
            print(book)

# --- Demo ---
library = Library()
n = int(input("Enter number of books to add: "))
for _ in range(n):
    title = input("Title: ")
    author = input("Author: ")
    library.add_book(title, author)

library.display_books()
library.borrow_book(input("\nEnter book title to borrow: "))
library.display_books()
library.return_book(input("\nEnter book title to return: "))
library.display_books()
