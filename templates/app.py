from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template("index.html", students=students)

@app.route('/add', methods=['POST'])
def add():
    id = request.form['ID']
    name = request.form['NAME']
    Email = request.form['EMAIL']
    Course = request.form['COURSE']

    students.append((name, email, course))

    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)