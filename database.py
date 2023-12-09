import sqlite3

DB_NAME = 'bookstore.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create Genres table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create Books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    ''')

def insert_sample_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Insert sample genres
    cursor.execute("INSERT INTO genres (name) VALUES ('Fiction')")
    cursor.execute("INSERT INTO genres (name) VALUES ('Mystery')")
    cursor.execute("INSERT INTO genres (name) VALUES ('Science Fiction')")
    cursor.execute("INSERT INTO genres (name) VALUES ('Non-Fiction')")

    # Insert sample books
    cursor.execute("INSERT INTO books (title, author, genre_id) VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1)")
    cursor.execute("INSERT INTO books (title, author, genre_id) VALUES ('To Kill a Mockingbird', 'Harper Lee', 1)")
    cursor.execute("INSERT INTO books (title, author, genre_id) VALUES ('The Da Vinci Code', 'Dan Brown', 2)")
    cursor.execute("INSERT INTO books (title, author, genre_id) VALUES ('Dune', 'Frank Herbert', 3)")
    cursor.execute("INSERT INTO books (title, author, genre_id) VALUES ('Sapiens', 'Yuval Noah Harari', 4)")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    insert_sample_data()
