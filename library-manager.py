import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def library_save(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read,
    }
    library.append(new_book)
    library_save(library)
    print('Book added successfully')

def remove_book(library):
    title = input('Enter the title of the book to remove: ').lower()
    original_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]
    if len(library) < original_length:
        library_save(library)
        print('Book removed successfully')
    else:
        print('Book not found in library')

def search_books(library):
    search_by = input('Search by title or author: ').lower()
    if search_by not in ['title', 'author']:
        print('Invalid search field. Please use "title" or "author".')
        return
    search_term = input(f'Enter the {search_by} to search: ').lower()
    results = [book for book in library if search_term in book[search_by].lower()]
    
    if results:
        for book in results:
            status = 'read' if book['read'] else 'unread'
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f'No books found with {search_by} containing "{search_term}"')

def display_books(library):
    if library:
        for book in library:
            status = 'read' if book['read'] else 'unread'
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print('The library is empty')

def show_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    percentage = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books}")
    print(f"Percentage Read: {percentage:.2f}%")

def main():
    library = load_library()
    while True:
        print('\n--- Library Manager ---')
        print('1. Add a book')
        print('2. Remove a book')
        print('3. Search the library')
        print('4. Display all books')
        print('5. Show statistics')
        print('6. Exit')
        
        choice = input('\nEnter your choice (1-6): ')
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            show_statistics(library)
        elif choice == '6':
            print('Thank you for using Library Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')

if __name__ == '__main__':
    main()