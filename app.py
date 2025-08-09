from flask import Flask, render_template, request, redirect, url_for
from book_functions import books
from user_functions import users

app = Flask(__name__)

book_id_counter = max(book['id'] for book in books) + 1 if books else 1
user_id_counter = max(user['id'] for user in users) + 1 if users else 1


@app.route('/')
def index():
    return render_template('index.html')


# ---------------- BOOKS ----------------
@app.route('/books')
def list_books():
    return render_template('books.html', books=books)


@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    global book_id_counter
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        total = int(request.form['total_copies'])
        location = request.form['position']

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
        book_id_counter += 1
        return redirect(url_for('list_books'))
    return render_template('book_form.html', action="Add", book={})


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return "Book not found", 404

    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['year'] = request.form['year']
        book['genre'] = request.form['genre']
        book['total_copies'] = int(request.form['total_copies'])
        book['available_copies'] = int(request.form['available_copies'])
        book['location'] = request.form['position']
        return redirect(url_for('list_books'))
    return render_template('book_form.html', action="Edit", book=book)


@app.route('/books/delete/<int:book_id>')
def delete_book(book_id):
    global books
    books[:] = [b for b in books if b['id'] != book_id]
    return redirect(url_for('list_books'))


# ---------------- USERS ----------------
@app.route('/users')
def list_users():
    return render_template('users.html', users=users)


@app.route('/users/add', methods=['GET', 'POST'])
def add_user():
    global user_id_counter
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')
        age = request.form.get('age', '')

        try:
            age = int(age)
        except (ValueError, TypeError):
            age = None

        users.append({
            'id': user_id_counter,
            'name': name,
            'email': email,
            'phone': phone,
            'age': age,
            'borrowed_books': []
        })
        user_id_counter += 1
        return redirect(url_for('list_users'))
    return render_template('user_form.html', action="Add", user={})


@app.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404

    if request.method == 'POST':
        user['name'] = request.form['name']
        user['email'] = request.form['email']
        user['phone'] = request.form.get('phone', '')

        age = request.form.get('age', '')
        try:
            user['age'] = int(age)
        except (ValueError, TypeError):
            user['age'] = None

        return redirect(url_for('list_users'))
    return render_template('user_form.html', action="Edit", user=user)


@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):
    global users
    users[:] = [u for u in users if u['id'] != user_id]
    return redirect(url_for('list_users'))


# ---------------- BORROW / RETURN ----------------
# @app.route('/borrow_return', methods=['GET', 'POST'])
# def borrow_return():
#     if request.method == 'POST':
#         uid = int(request.form['user_id'])
#         bid = int(request.form['book_id'])
#         action = request.form['action']
#
#         user = next((u for u in users if u['id'] == uid), None)
#         book = next((b for b in books if b['id'] == bid), None)
#
#         if user and book:
#             if action == 'borrow' and book['available_copies'] > 0:
#                 book['available_copies'] -= 1
#                 user['borrowed_books'].append(bid)
#             elif action == 'return' and bid in user['borrowed_books']:
#                 book['available_copies'] += 1
#                 user['borrowed_books'].remove(bid)
#         return redirect(url_for('borrow_return'))
#     return render_template('borrow_return.html', users=users, books=books)
@app.route('/borrow_return', methods=['GET', 'POST'])
def borrow_return():
    message = None  # Initialize message variable
    if request.method == 'POST':
        uid = int(request.form['user_id'])
        bid = int(request.form['book_id'])
        action = request.form['action']

        user = next((u for u in users if u['id'] == uid), None)
        book = next((b for b in books if b['id'] == bid), None)

        if not user:
            message = "User not found."
        elif not book:
            message = "Book not found."
        else:
            if action == 'borrow':
                if book['available_copies'] > 0:
                    if bid not in user['borrowed_books']:
                        book['available_copies'] -= 1
                        user['borrowed_books'].append(bid)
                        message = f"Successfully borrowed '{book['title']}'."
                    else:
                        message = "You already borrowed this book."
                else:
                    message = "No available copies to borrow."
            elif action == 'return':
                if bid in user['borrowed_books']:
                    book['available_copies'] += 1
                    user['borrowed_books'].remove(bid)
                    message = f"Successfully returned '{book['title']}'."
                else:
                    message = "You did not borrow this book."
            else:
                message = "Invalid action."

    return render_template('borrow_return.html', users=users, books=books, message=message)



# ---------------- STATS ----------------
@app.route('/stats')
def stats():
    total_books = sum(book['total_copies'] for book in books)
    available_books = sum(book['available_copies'] for book in books)
    total_users = len(users)
    return render_template('stats.html',
                           total_books=total_books,
                           available_books=available_books,
                           total_users=total_users)


# ---------------- SEARCH ----------------
@app.route('/search', methods=['GET', 'POST'])
def search_books():
    results = []
    if request.method == 'POST':
        keyword = request.form['keyword'].lower()
        results = [b for b in books if keyword in b['title'].lower()
                   or keyword in b['author'].lower()
                   or keyword in b['genre'].lower()]
    return render_template('search.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
