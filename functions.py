# functions.py

def add_book(library, book):
    library.append(book)


def remove_book(library, book_id):
    for book in library:
        if book["id"] == book_id:
            library.remove(book)
            return True
    return False


def edit_book(library, book_id, new_data):
    for i, book in enumerate(library):
        if book["id"] == book_id:
            library[i] = new_data
            return True
    return False


def display_books(library, st):
    if library:
        for book in library:
            st.write(f'📖 **{book["title"]}** by {book["author"]} ({book["year"]}) - ID: {book["id"]}')
    else:
        st.write("No books in library.")


def sort_books(library):
    return sorted(library, key=lambda x: x["title"])


def count_books(library):
    return len(library)
