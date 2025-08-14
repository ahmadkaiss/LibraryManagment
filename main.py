# main.py
from book_functions import *
from user_functions import *


def main_menu():
    while True:
        print("""
===== Library Manager =====
1. Manage Books
2. Manage Users
3. Borrow a Book
4. Return a Book
5. View Stats
6. Search for a Book
7. Exit
""")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_users()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            view_stats()
        elif choice == '6':
            search_books()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()

