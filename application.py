from bottle import Bottle, template, request, redirect,route,run
import sqlite3


# Database setup
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Home Page
@route('/')
def home():
    return template('home')

# Books Page
@route('/books')
def books():
    cursor = conn.cursor()
    cursor.execute('''
        SELECT books.title, books.author, genres.name AS genre
        FROM books
        JOIN genres ON books.genre_id = genres.id
    ''')
    books = cursor.fetchall()
    return template('books', books=books)

# Genres Page
@route('/genres')
def genres():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM genres')
    genres = cursor.fetchall()
    return template('genres', genres=genres)

# Run the app
if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)