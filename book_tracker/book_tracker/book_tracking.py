import json
from model import Book
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
        json.dump([book.dict() for book in books], f, indent=4)

# Add a new book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre (optional): ")
    status = input("Enter status (to-read, reading, finished): ")
    
    try:
        # Validate input using Pydantic's Book model
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
            new_status = input("Enter new status (to-read, reading, finished): ")
            books[index].status = new_status
            save_books(books)
            print("Status updated.")
        else:
            print("Invalid book number.")
    except ValueError:
        print("Please enter a valid number.")

# Main CLI menu
def main():
    print("Personal Book Tracker CLI")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Update book status")
    print("4. Exit")
    
    while True:
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            update_status()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
