from library import Book, Library

# Create a library object(We create an instance of the Library class in library.py by using the line library = Library())
library = Library()

# Add sample books to the library(by creating three 'Book' objects, these books are then added to the library using the add_book method.)
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books(we ask the user to enter a search term using the input function and store it in the search_criteria variable.)
#The program then calls the search_books method on the library object, passing the search_criteria, from the user's input. 
#The search results are stored in the 'results' variable (empty list from library.py file).
search_criteria = input("Enter a search term: ")
results = library.search_books(search_criteria)

# Display search results
if results:
    print(f"Search results for '{search_criteria}':")
    for book in results:
        print(f"- {book.title} by {book.author} , genre: ({book.genre})")
else:
    print("No results found.")
