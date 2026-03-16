# Library management systems
class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = None


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter Book Title: ")
        book = Book(title)
        self.books.append(book)
        print("Book Added Successfully")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Issued" if book.issued else "Available"
            print(book.title, "-", status)

    def issue_book(self):
        title = input("Enter Book Title to Issue: ")
        for book in self.books:
            if book.title == title and not book.issued:
                member = input("Enter Member Name: ")
                book.issued = True
                print("Book Issued to", member)
                return
        print("Book Not Available")

    def return_book(self):
        title = input("Enter Book Title to Return: ")
        for book in self.books:
            if book.title == title and book.issued:
                book.issued = False
                print("Book Returned Successfully")
                return
        print("Invalid Book")


lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        lib.add_book()
    elif choice == 2:
        lib.issue_book()
    elif choice == 3:
        lib.return_book()
    elif choice == 4:
        lib.display_books()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")