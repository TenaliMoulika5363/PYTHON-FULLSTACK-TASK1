import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Delete all users
cursor.execute("DELETE FROM users")

# Reset AUTOINCREMENT counter
cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

conn.commit()
conn.close()

print("All users deleted and ID reset")