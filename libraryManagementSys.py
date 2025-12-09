
library = []

def add_book():
    print("\n Add a Book ")
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    count = int(input("No of count? "))

    book = {
        "title": title,"author": author, "count": count
    }

    library.append(book)
    print("Books added\n")


def search_book():
    print("\n Search for a Book ")
    name = input("Enter title to search: ")

    for book in library:
        if book["title"].lower() == name.lower():
            print("Book found:")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Available copies: {book['count']}")
            return

    print("books not found\n")


def borrow_book():
    print("\n Borrow a Book ")
    name = input("Enter book title: ")

    for book in library:
        if book["title"].lower() == name.lower():
            if book["count"] > 0:
                book["count"] -= 1
                print("book borrowed successfully.")
            else:
                print("No copies.")
            return

    print("Book not found.\n")


def return_book():
    print("\n Return a Book ")
    name = input("Enter book title: ")

    for book in library:
        if book["title"].lower() == name.lower():
            book["count"] += 1
            print("Book returned. Thank you!")
            return

    print("Book not found in the system.\n")


def LibrayManagementSystem():
    while True:
        print("\n    Library Management System     ")
        print("1. Add a book")
        print("2. Search a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

LibrayManagementSystem()
