class Book(object):
    """A book in an online bookstore."""

    def __init__(self, title, author, price):
        """Creates a book with a title, an author, and a price."""
        self.title = title
        self.author = author
        self.price = price

    # Task 1: add a method get_title() that returns the title


    # Task 2: add a method get_price() that returns the price


    # Task 3 (teams of three only): add a method get_author() that returns the author


    # Task 4: add a method __str__() that returns e.g. 'Persuasion by Jane Austen'


book = Book('Persuasion', 'Jane Austen', 8.99)

# Tests: when your task is done, remove the # at the start of its line and run the file

# print(book.get_title())    # Task 1

# print(book.get_price())    # Task 2

# print(book.get_author())   # Task 3

# print(book)                # Task 4
