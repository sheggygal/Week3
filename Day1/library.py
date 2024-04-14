class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been issued.")
        else:
            print(f"The book '{self.title}' is already issued.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' is already available.")

    def __str__(self):
        availability = "available" if self.available else "not available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def find_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(book)

    def list_all_books(self):
        print("All Books:")
        for book in self.books:
            print(book)


# Creating Book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("Sugar Kremlin", "Viktor Pelevin", "8865642025.")
book3 = Book("1984", "George Orwell", "9780451524935")

# Creating Library instance and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


book1.issue_book()
book1.issue_book()
book1.return_book()


print("\nBooks with 'Sugar' in title:")
print(library.find_books_by_title("Sugar"))

print("\nBooks by 'George Orwell':")
print(library.find_books_by_author("George Orwell"))


print("\nAll Books in the Library:")
library.list_all_books()

print("\nAvailable Books in the Library:")
library.list_available_books()
