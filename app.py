from flask import Flask, render_template, request,redirect
import sqlite3

import os

print("APP DB:", os.path.abspath("database.db"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    # Fetch all users
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("index.html", users=users)

if __name__ == '__main__':
    app.run(debug=True)