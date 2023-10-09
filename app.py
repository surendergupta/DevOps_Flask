from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'

# class Base(DeclarativeBase):
#  pass

# db = SQLAlchemy(app, model_class=Base)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/contactus')
def contactUs():
    return 'Conctact Us'


@app.route('/student', methods=['GET', 'POST'])
def info():
    students = []

    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        student = {
            "name": name,
            "age": int(age),
        }
        students.append(student)
        return "<form method='POST' action='/student'>Tell Student details: <input type='text' name='name' id='name' /> <input type='text' name='age' id='age' /> <button type='submit'>Submit</button><p id='tell'>" + str(students) + "</p></form>"
    else:
        return "<form method='POST' action='/student'>Tell Student details: <input type='text' name='name' id='name' /> <input type='text' name='age' id='age' /> <button type='submit'>Submit</button></form>"


@app.route('/identify')
def pallindrome():
    number = int(request.args.get('num1'))
    temp = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if (temp == rev):
        return "The number is a palindrome!"
    else:
        return "The number isn't a palindrome!"


@app.route('/reverse-strings')
def reverseString():
    about = request.args.get('str1')
    return 'Reversed Strings : ' + about[::-1]


@app.route('/about-you', methods=['GET', 'POST'])
def aboutYou():
    if request.method == "POST":
        about = request.form.get('aboutyou')
        return "<form method='POST' action='/about-you'>Tell me about you: <input type='text' name='aboutyou' id='aboutyou' /> <button type='submit'>Submit</button><p id='tell'>" + about + "</p></form>"
    else:
        return "<form method='POST' action='/about-you'>Tell me about you: <input type='text' name='aboutyou' id='aboutyou' /> <button type='submit'>Submit</button></form>"


if __name__ == "__main__":
    app.run(debug=True)
