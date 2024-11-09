import json
from book_tracker.model import Book
from typing import List
from pathlib import Path

# File to store book data
BOOKS_FILE = Path("books.json")

# Load books from the JSON file
def load_books() -> List[Book]:
    if BOOKS_FILE.exists():
        with open(BOOKS_FILE, "r") as f:
            data = json.load(f)
            return [Book(**item) for item in data]  # Load data as Book instances
    return []

# Save books to the JSON file
def save_books(books: List[Book]):
    with open(BOOKS_FILE, "w") as f:
        json.dump([book.model_dump() for book in books], f, indent=4)


# Add a new book

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre (optional): ")

    # Repeatedly ask for a valid status input
    while True:
        status = input("Enter status (1 for to-read, 2 for reading, 3 for finished): ")
        if status in ["1", "2", "3"]:
            # Map the number to the actual status text
            status_map = {"1": "to-read", "2": "reading", "3": "finished"}
            status = status_map[status]
            break  # Exit the loop once valid status is entered
        else:
            print("Invalid status number. Please enter 1, 2, or 3.")

    try:
        book = Book(title=title, author=author, genre=genre, status=status)
        books = load_books()
        books.append(book)
        save_books(books)
        print(f"Added '{title}' by {author}.")
    except ValueError as e:
        print(f"Error: {e}")

# List all books
def list_books():
    books = load_books()
    if books:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.title} by {book.author} - Status: {book.status}")
    else:
        print("No books found.")

# Update book status
def update_status():
    books = load_books()
    list_books()
    try:
        index = int(input("Enter the number of the book to update: ")) - 1
        if 0 <= index < len(books):
            print("Choose status of the book: ")
            print("1. to-read")
            print("2. reading")
            print("3. finished")
            book_status = input("Enter number corresponding to book status: ")
            status_map = {
                "1.": "to-read",
                "2.": "reading",
                "3.": "finished"
            }
            new_status = status_map.get(book_status)
            if new_status is None:
                print("Invalid choice. Please enter: 1, 2 or 3")
                return

        
            books[index].status = new_status
            save_books(books)
            print("Status updated.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_book():
    books = load_books()
    list_books()

    if not books:
        print('List of books is empty!.')
        return

    try:
        index = int(input("Enter book number to be deleted: ")) - 1
        if 0 <= index < len(books):
            deleted_book = books.pop(index)
            save_books()
            print(f"{deleted_book} deleted from book list")
        else:
            print("Invalid book number")
            return
    except ValueError:
        print("Enter valid book number.")
       

# Main CLI menu
def main():
    print("Personal Book Tracker CLI")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Update book status")
    print("4. Delete book")
    print("5. Exit")
    
    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            update_status()
        elif choice == "4":
            delete_book()     
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
