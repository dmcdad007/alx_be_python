class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor that initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """Destructor that runs when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
