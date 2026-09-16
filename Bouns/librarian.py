import json
from pathlib import Path


FILE_PATH = Path(__file__).parent / "book.json"


def add_book(library, title, author, isbn):
    for book in library:
        if book["isbn"] == isbn:
            print("Book already exists.")
            return

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

    library.append(book)
    print(f"Book '{title}' added successfully.")


def remove_book(library, isbn):
    for book in library:
        if book["isbn"] == isbn:
            library.remove(book)
            print("Book removed successfully.")
            return

    print("Book not found.")


def check_out_book(library, isbn):
    for book in library:
        if book["isbn"] == isbn:
            if book["available"] == False:
                print("Book is already checked out.")
                return

            book["available"] = False
            print("Book checked out successfully.")
            return

    print("Book not found.")


def return_book(library, isbn):
    for book in library:
        if book["isbn"] == isbn:
            book["available"] = True
            print("Book returned successfully.")
            return

    print("Book not found.")


def display_books(library):
    if not library:
        print("No books in the library.")
        return

    for book in library:
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(
            f"{book['title']} by {book['author']} "
            f"(ISBN: {book['isbn']}) - {status}"
        )


def search_books(library, search_term):
    found = False

    for book in library:
        if (
            search_term.lower() in book["title"].lower()
            or search_term.lower() in book["author"].lower()
            or search_term.lower() in book["isbn"].lower()
        ):
            print(
                f"{book['title']} by {book['author']} "
                f"(ISBN: {book['isbn']})"
            )
            found = True

    if not found:
        print("No books found.")


def save_library(library):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4)

    print("Library saved successfully.")
    print("Saved in:", FILE_PATH)


def load_library():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []