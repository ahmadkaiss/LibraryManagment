# book_functions.py

books = [
    {
        'id': 1,
        'title': 'The Pragmatic Programmer',
        'author': 'Andrew Hunt',
        'year': '1999',
        'genre': 'Programming',
        'total_copies': 2,
        'available_copies': 2,
        'location': 'Shelf A1'
    },
    {
        'id': 2,
        'title': 'Python Crash Course',
        'author': 'Eric Matthes',
        'year': '2015',
        'genre': 'Programming',
        'total_copies': 2,
        'available_copies': 2,
        'location': 'Shelf A2'
    }
]

book_id_counter = 3


def manage_books():
    while True:
        print("""
                --- Book Management ---
                1. Add Book
                2. Edit Book
                3. Remove Book
                4. Display All Books
                5. Search for a Book
                6. Back to Main Menu
                """)
        choice = input("Choose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            edit_book()
        elif choice == '3':
            remove_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            search_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")


def add_book():
    global book_id_counter
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    genre = input("Genre: ")
    total = int(input("Total Copies: "))
    location = input("Location in library (e.g., Shelf B3): ")


    books.append({
        'id': book_id_counter,
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'total_copies': total,
        'available_copies': total,
        'location': location
    })
    print(f"Book added with ID {book_id_counter}.")
    book_id_counter += 1


def edit_book():
    bid = int(input("Enter book ID to edit: "))
    for book in books:
        if book['id'] == bid:
            book['title'] = input(f"New title ({book['title']}): ") or book['title']
            book['author'] = input(f"New author ({book['author']}): ") or book['author']
            book['year'] = input(f"New year ({book['year']}): ") or book['year']
            book['genre'] = input(f"New genre ({book['genre']}): ") or book['genre']
            book['location'] = input(f"New location ({book['location']}): ") or book['location']
            print("Book updated.")
            return
    print("Book not found.")


def remove_book():
    bid = int(input("Enter book ID to remove: "))
    for book in books:
        if book['id'] == bid:
            books.remove(book)
            print("Book removed.")
            return
    print("Book not found.")


def display_books():
    if not books:
        print("No books available.")
        return
    for book in books:
        print(
            f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Location: {book['location']},"
            f" Copies: {book['available_copies']}/{book['total_copies']}")


def search_books():
    keyword = input("Enter title, author, or genre to search: ").lower()
    found = False
    for book in books:
        if keyword in book['title'].lower() or keyword in book['author'].lower() or keyword in book['genre'].lower():
            print(
                f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Copies: {book['available_copies']}/{book['total_copies']}")
            found = True
    if not found:
        print("No matching books found.")