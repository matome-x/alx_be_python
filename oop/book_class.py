# book_class.py

class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title: str, author: str, year: int):
        """Constructor: initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation: user-friendly."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation: should recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# main.py

from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Uses __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Uses __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
