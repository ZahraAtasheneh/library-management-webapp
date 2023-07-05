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
#This file contains the code for creating a library system.
#defines two classes. Book class represents a book and has three attributes
# An  __init__  method: gets called when a new Book object is created. The __init__ method takes in three parameters (title, author, genre)
#and assigns them to the corresponding attributes of the object.
#The library class represents a collection of books and has three methods: __init__ , add_book and search_books 
#__init__ method in library: initializes an empty list to store the books when a new Library object is created.
#add_book method: It takes a book parameter and adds the book to the list of books in the library. This method is used to add books to the library.
#search_books method: It takes a search_criteria parameter, which is a term used to search for books in the library. 
#The method goes through each book in the library and checks if the search criteria matches the book's title, author, or genre.
#If there's a match, the book is added to the results list. Finally, the method returns the list of matching books.
