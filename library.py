import json
import os

LIBRARY_FILE = 'library.json'

def load_books():
    """Load books from JSON file"""
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_books(books):
    """Save books to JSON file"""
    with open(LIBRARY_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def add_book(books):
    """Add a new book to the library"""
    clear_screen()
    print("\nAdd a New Book")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    genre = input("Genre: ").strip()
    
    while True:
        year = input("Publication Year: ").strip()
        if year.isdigit() and len(year) == 4:
            year = int(year)
            break
        print("Please enter a valid 4-digit year")
    
    new_book = {
        'title': title,
        'author': author,
        'genre': genre,
        'year': year
    }
    
    books.append(new_book)
    save_books(books)
    print(f"\n'{title}' has been added to your library!")

def list_books(books):
    """Display all books in the library"""
    clear_screen()
    print("\nYour Library\n" + "="*40)
    
    if not books:
        print("No books in the library")
        return
    
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Genre: {book['genre']}")
        print(f"   Year: {book['year']}\n")

def search_books(books):
    """Search books by any field"""
    clear_screen()
    print("\nSearch Books")
    term = input("Enter search term: ").lower()
    
    results = []
    for book in books:
        if (term in book['title'].lower() or
            term in book['author'].lower() or
            term in book['genre'].lower() or
            term in str(book['year'])):
            results.append(book)
    
    print(f"\nFound {len(results)} matching books:")
    for i, book in enumerate(results, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
    
    return results

def remove_book(books):
    """Remove a book from the library"""
    results = search_books(books)
    if not results:
        return
    
    try:
        choice = int(input("\nEnter book number to remove (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(results):
            book_to_remove = results[choice-1]
            books.remove(book_to_remove)
            save_books(books)
            print(f"\n'{book_to_remove['title']}' has been removed")
        else:
            print("Invalid selection")
    except ValueError:
        print("Please enter a valid number")

def main_menu():
    """Display main menu and handle user input"""
    books = load_books()
    
    while True:
        clear_screen()
        print("\nPersonal Library Manager")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Books")
        print("4. Remove Book")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            remove_book(books)
        elif choice == '5':
            print("\nGoodbye! Your library has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main_menu()