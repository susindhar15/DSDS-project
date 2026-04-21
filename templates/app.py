from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template("index.html", students=students)

@app.route('/add', methods=['POST'])
def add():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    students.append((id, name, email, course))  # ✅ CORRECT

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)