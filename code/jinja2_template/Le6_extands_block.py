#-*-coding:utf8-*-
from flask import Flask,render_template

app = Flask(__name__)

class Person(object):
    name = ''
    age = 0

    def func():
        pass

class Student(Person):

    def func():
        print("Student")

@app.route('/')
def index():
    return render_template('index_extends_block.html')

@app.route('/login/')
def login():
    return render_template('index_login.html')

if __name__ == '__main__':
    app.run(debug=True)
