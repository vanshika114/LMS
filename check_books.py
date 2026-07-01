import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM books")

books = cursor.fetchall()

for book in books:
    print(book)

conn.close()