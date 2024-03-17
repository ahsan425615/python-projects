class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if not book.is_borrowed:
                book.is_borrowed = True
                return f"{book.title} by {book.author} has been borrowed."
            else:
                return "This book is already borrowed."
        else:
            return "Book not found."

    def return_book(self, title):
        book = self.search_book(title)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return f"{book.title} by {book.author} has been returned."
        elif book and not book.is_borrowed:
            return "This book is not currently borrowed."
        else:
            return "Book not found."

def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(Book(title, author))
            print("Book added successfully.")
        elif choice == '2':
            title = input("Enter book title to search: ")
            book = library.search_book(title)
            if book:
                print(f"Book found: {book.title} by {book.author}")
            else:
                print("Book not found.")
        elif choice == '3':
            title = input("Enter book title to borrow: ")
            print(library.borrow_book(title))
        elif choice == '4':
            title = input("Enter book title to return: ")
            print(library.return_book(title))
        elif choice == '5':
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
