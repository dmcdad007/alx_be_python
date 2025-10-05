class Book:
    """Represents a single book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute for availability

    def check_out(self):
        """Mark the book as checked out if it’s available."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
            return False
        else:
            self._is_checked_out = True
            return True

    def return_book(self):
        """Mark the book as returned (available again)."""
        if not self._is_checked_out:
            print(f"'{self.title}' is not currently checked out.")
            return False
        else:
            self._is_checked_out = False
            return True

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of Book instances."""
    
    def __init__(self):
        self._books = []  # private list of books

    def add_book(self, book):
        """Add a new book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it exists and is available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    print(f"'{book.title}' has been checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    print(f"'{book.title}' has been returned.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print a list of all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
