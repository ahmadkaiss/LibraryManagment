# user_functions.py
from book_functions import books

users = [
    {
        'id': 1,
        'name': 'kaiss',
        'email': 'kaiss@example.com',
        'phone': '123-456-7890',
        'age': 30,
        'borrowed_books': []
    },
    {
        'id': 2,
        'name': 'Ahmad',
        'email': 'ahmad007@example.com',
        'phone': '123-456-7890',
        'age': 30,
        'borrowed_books': []
    }
]

user_id_counter = 1


def manage_users():
    while True:
        print("""
                --- User Management ---
                1. Add User
                2. Edit User
                3. Remove User
                4. Display Users
                5. Back to Main Menu
                """)
        choice = input("Choose an option: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            edit_user()
        elif choice == '3':
            remove_user()
        elif choice == '4':
            display_users()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


def add_user():
    global user_id_counter
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    age = input("Age: ")

    users.append({
        'id': user_id_counter,
        'name': name,
        'email': email,
        'phone': phone,
        'age': int(age) if age.isdigit() else None,
        'borrowed_books': []
    })
    print(f"User added with ID {user_id_counter}.")
    user_id_counter += 1


def edit_user():
    uid = int(input("Enter user ID to edit: "))
    for user in users:
        if user['id'] == uid:
            user['name'] = input(f"New name ({user['name']}): ") or user['name']
            user['email'] = input(f"New email ({user['email']}): ") or user['email']
            user['phone'] = input(f"New phone ({user.get('phone', '')}): ") or user.get('phone', '')
            age_input = input(f"New age ({user.get('age', '')}): ")
            if age_input.isdigit():
                user['age'] = int(age_input)
            print("User updated.")
            return
    print("User not found.")


def remove_user():
    uid = int(input("Enter user ID to remove: "))
    for user in users:
        if user['id'] == uid:
            users.remove(user)
            print("User removed.")
            return
    print("User not found.")


def display_users():
    if not users:
        print("No users available.")
        return
    for user in users:
        print(
            f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}, Phone: {user.get('phone', '')}, Age: {user.get('age', '')}, Borrowed Books: {user['borrowed_books']}")


def borrow_book():
    uid = int(input("Enter user ID: "))
    bid = int(input("Enter book ID to borrow: "))
    for user in users:
        if user['id'] == uid:
            for book in books:
                if book['id'] == bid:
                    if book['available_copies'] > 0:
                        book['available_copies'] -= 1
                        user['borrowed_books'].append(bid)
                        print("Book borrowed successfully.")
                        return
                    else:
                        print("No copies available.")
                        return
            print("Book not found.")
            return
    print("User not found.")


def return_book():
    uid = int(input("Enter user ID: "))
    bid = int(input("Enter book ID to return: "))
    for user in users:
        if user['id'] == uid:
            if bid in user['borrowed_books']:
                for book in books:
                    if book['id'] == bid:
                        book['available_copies'] += 1
                        user['borrowed_books'].remove(bid)
                        print("Book returned successfully.")
                        return
                print("Book not found.")
                return
            else:
                print("User did not borrow this book.")
                return
    print("User not found.")


def view_stats():
    total_books = sum(book['total_copies'] for book in books)
    available_books = sum(book['available_copies'] for book in books)
    total_users = len(users)
    print(f"Total Books: {total_books}")
    print(f"Available Books: {available_books}")
    print(f"Total Users: {total_users}")
