import sqlite3

import os

print("CHECK DB:", os.path.abspath("database.db"))

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print(users)

conn.close()