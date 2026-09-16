import LAB_FILES_IO.Bouns.librarian as librarian


library = librarian.load_library()


while True:

    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Check Out Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Search Books")
    print("7. Save Library")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")


    if choice == "1":

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")

        librarian.add_book(
            library,
            title,
            author,
            isbn
        )

        librarian.save_library(library)


    elif choice == "2":

        isbn = input("Enter ISBN to remove: ")

        librarian.remove_book(
            library,
            isbn
        )

        librarian.save_library(library)


    elif choice == "3":

        isbn = input("Enter ISBN to check out: ")

        librarian.check_out_book(
            library,
            isbn
        )

        librarian.save_library(library)


    elif choice == "4":

        isbn = input("Enter ISBN to return: ")

        librarian.return_book(
            library,
            isbn
        )

        librarian.save_library(library)


    elif choice == "5":

        librarian.display_books(library)


    elif choice == "6":

        search_term = input(
            "Enter title, author, or ISBN: "
        )

        librarian.search_books(
            library,
            search_term
        )


    elif choice == "7":

        librarian.save_library(library)


    elif choice == "8":

        librarian.save_library(library)

        print(
            "Thank you for using the Library System."
        )

        break


    else:

        print("Invalid choice.")