class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_books(self, search_criteria):
        results = []
        for book in self.books:
            if (
                search_criteria.lower() in book.title.lower() or
                search_criteria.lower() in book.author.lower() or
                search_criteria.lower() in book.genre.lower()
            ):
                results.append(book)
        return results
