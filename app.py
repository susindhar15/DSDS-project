from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUSINDHAR15082006",
    database="student_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template("index.html", students=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    cursor.execute(
        "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
        (name, email, course)
    )
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)