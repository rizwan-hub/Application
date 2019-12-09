from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import random

project_dir = os.path.dirname(os.path.dirname(__file__))
database_file = "sqlite:///" + os.path.join(project_dir, "bookdatabase.db")
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(30), nullable=False)


db.create_all()


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route('/dropdown', methods=['GET', 'POST'])
def dropdown():
    return render_template("dropdown.html")


@app.route('/student')
def student():
    myuser = User.query.all()
    return render_template("student.html", studentuse=myuser)


@app.route('/teacher')
def teacher():
    myuser = User.query.all()
    return render_template("teacher.html", teacheruse=myuser)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        passw = 'admbbv24355336363'
        password = ''
        for c in range(6):
            password += random.choice(passw)
        entry = User(name=name, email=email, password=password)
        db.session.add(entry)
        db.session.commit()
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
