from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create Database Table
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS donors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            blood TEXT,
            phone TEXT,
            age INTEGER,
            date TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def Home():
    return render_template("blood.html")

@app.route("/About")
def About():
    return render_template("About.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    blood = request.form["blood"]
    phone = request.form["phone"]
    age = request.form["age"]
    date = request.form["trip-start"]

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO donors(name,blood,phone,age,date) VALUES (?,?,?,?,?)",
            (name, blood, phone, age,date))
    conn.commit()
    conn.close()

    return render_template("blood.html", message="Data Stored Successfully ✅")

if __name__ == "__main__":
    app.run(debug=True)
