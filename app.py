import streamlit as st  # streamlit is the library that creates the web interface.
from functions import *  # Where we store the reusable logic

# Initialize session state
if "library" not in st.session_state:  # We using st session to store the library book list
    st.session_state.library = []  # Initialization

if "menu" not in st.session_state:
    st.session_state["menu"] = ""

st.title("📖 Library Management System")  # Title of the App

st.markdown("""
        <style>
            .stApp {
            # background-image: url("https://c7.alamy.com/comp/2R7G52F/book-stack-and-open-book-on-the-desk-in-modern-public-library-2R7G52F.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        div.stButton > button {
            background-color: #2e8b57;
            color: white;
            height: 3em;
            width: 100%;
            border-radius: 12px;
            font-size: 16px;
            margin-bottom: 10px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #246b44;
            transform: scale(1.02);
        }
    </style>
""", unsafe_allow_html=True)

# choose from the list of options (menu) ,st.sidebar creates a side panel and gets saved in the variable menu
# menu = st.sidebar.selectbox("Menu",
#                             ["Add Book", "Remove Book", "Edit Book", "Display Books", "Sort Books", "Count Books"])
#
# if menu == "Add Book":
#     st.subheader("Add a New Book")
#     id = st.number_input("Book ID", step=1)
#     title = st.text_input("Title")
#     author = st.text_input("Author")
#     year = st.number_input("Year", step=1)
#
#     if st.button("Add Book"):  # waits for the user to click "Add Book"
#         book = {"id": id, "title": title, "author": author, "year": year}
#         add_book(st.session_state.library, book)
#         st.success("Book added!")
#
# # Enter a book ID and click the button.
# elif menu == "Remove Book":
#     st.subheader("Remove a Book")
#     book_id = st.number_input("Enter book ID to remove",
#                               step=1)  # If the value is not specified, the format parameter will be used.
#     if st.button("Remove Book"):
#         if remove_book(st.session_state.library, book_id):
#             st.success("Book removed")
#         else:
#             st.error("Book not found")
#
# elif menu == "Edit Book":
#     st.subheader("Edit a Book")
#     book_id = st.number_input("Enter book ID to edit", step=1)
#     title = st.text_input("New Title")
#     author = st.text_input("New Author")
#     year = st.number_input("New Year", step=1)
#     if st.button("Edit Book"):
#         new_data = {"id": book_id, "title": title, "author": author, "year": year}
#         if edit_book(st.session_state.library, book_id, new_data):
#             st.success("Book updated")
#         else:
#             st.error("Book not found")
#
# elif menu == "Display Books":
#     st.subheader("All Books in Library")
#     display_books(st.session_state.library, st)
#
# elif menu == "Sort Books":
#     st.session_state.library = sort_books(st.session_state.library)
#     st.success("Books sorted by title!")
#
# elif menu == "Count Books":
#     count = count_books(st.session_state.library)
#     st.info(f"Total books: {count}")


st.markdown("<h1 style='text-align: center;'>📚 Library Management Dashboard</h1>", unsafe_allow_html=True)

# Row 1
col1, col2, col3 = st.columns(3)  # creates a new horizontal layout — a new row with 3 columns.

with col1:
    if st.button("➕ Add Book"):
        st.session_state.menu = "Add"

with col2:
    if st.button("❌ Remove Book"):
        st.session_state.menu = "Remove"

with col3:
    if st.button("📝 Edit Book"):
        st.session_state.menu = "Edit"

# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    if st.button("📋 Display Books"):
        st.session_state.menu = "Display"

with col5:
    if st.button("🔤 Sort Books"):
        st.session_state.menu = "Sort"

with col6:
    if st.button("🔢 Count Books"):
        st.session_state.menu = "Count"

if st.session_state.menu == "Add":
    st.subheader("Add a New Book")
    id = st.number_input("Book ID", step=1)
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", step=1)
    if st.button("Add Book to Library"):
        book = {"id": id, "title": title, "author": author, "year": year}
        add_book(st.session_state.library, book)
        st.success("Book added!")

elif st.session_state.menu == "Remove":
    st.subheader("Remove a Book")
    book_id = st.number_input("Enter book ID to remove", step=1)
    if st.button("Remove Book Now"):
        if remove_book(st.session_state.library, book_id):
            st.success("Book removed")
        else:
            st.error("Book not found")

elif st.session_state.menu == "Edit":
    st.subheader("Edit a Book")
    book_id = st.number_input("Enter book ID to edit", step=1)
    title = st.text_input("New Title")
    author = st.text_input("New Author")
    year = st.number_input("New Year", step=1)
    if st.button("Edit Book Info"):
        new_data = {"id": book_id, "title": title, "author": author, "year": year}
        if edit_book(st.session_state.library, book_id, new_data):
            st.success("Book updated")
        else:
            st.error("Book not found")

elif st.session_state.menu == "Display":
    st.subheader("All Books in Library")
    display_books(st.session_state.library, st)

elif st.session_state.menu == "Sort":
    st.session_state.library = sort_books(st.session_state.library)
    st.success("Books sorted by title!")

elif st.session_state.menu == "Count":
    count = count_books(st.session_state.library)
    st.info(f"Total books: {count}")
