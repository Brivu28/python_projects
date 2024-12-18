import sqlite3
from datetime import datetime

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT,
        available BOOLEAN NOT NULL CHECK (available IN (0, 1))
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        issue_date TEXT NOT NULL,
        due_date TEXT NOT NULL,
        return_date TEXT,
        fine REAL,
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (member_id) REFERENCES Members(member_id)
    )
''')

conn.commit()
conn.close()

def add_member(name, email):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Members (name, email) VALUES (?, ?)
    ''', (name, email))
    conn.commit()
    conn.close()

def add_book(title, author, genre):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Books (title, author, genre, available) VALUES (?, ?, ?, 1)
    ''', (title, author, genre))
    conn.commit()
    conn.close()

def issue_book(book_id, member_id, issue_date, due_date):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Transactions (book_id, member_id, issue_date, due_date)
        VALUES (?, ?, ?, ?)
    ''', (book_id, member_id, issue_date, due_date))
    cursor.execute('''
        UPDATE Books SET available = 0 WHERE book_id = ?
    ''', (book_id,))
    conn.commit()
    conn.close()


def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Member")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. View Members")
        print("5. View Books")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter member name: ").strip()
                email = input("Enter member email: ").strip()
                if name and email:
                    add_member(name, email)
                    print("Member added successfully!")
                else:
                    print("Error: Name and email cannot be empty.")

            elif choice == 2:
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                genre = input("Enter book genre (optional): ").strip()
                if title and author:
                    add_book(title, author, genre)
                    print("Book added successfully!")
                else:
                    print("Error: Title and author cannot be empty.")

            elif choice == 3:
                book_id = int(input("Enter book ID to issue: "))
                member_id = int(input("Enter member ID: "))
                issue_date = input("Enter issue date (YYYY-MM-DD): ").strip()
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                if validate_date(issue_date) and validate_date(due_date):
                    issue_book(book_id, member_id, issue_date, due_date)
                else:
                    print("Error: Invalid date format.")

            elif choice == 4:
                view_members()

            elif choice == 5:
                view_books()

            elif choice == 6:
                print("Exiting the Library Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Error: Please enter a valid number.")

# Supporting Functions for Viewing Members and Books
def view_members():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()
    print("\n--- Members List ---")
    for member in members:
        print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")
    conn.close()

def view_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    print("\n--- Books List ---")
    for book in books:
        availability = "Available" if book[4] else "Not Available"
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Status: {availability}")
    conn.close()

# Date Validation
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()

