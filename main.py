from library import Book, Library

# Create a library object
library = Library()

# Add sample books to the library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books
search_criteria = input("Enter a search term: ")
results = library.search_books(search_criteria)

# Display search results
if results:
    print(f"Search results for '{search_criteria}':")
    for book in results:
        print(f"- {book.title} by {book.author} ({book.genre})")
else:
    print("No results found.")
