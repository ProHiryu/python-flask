#-*-coding:utf8-*-
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    class Person(object):
        name = u'onetwo'
        age = 18

    p = Person()

    context = {
        'username':'oneone',
        'gender':'female',
        'age':23,
        'person':p,
        'websites':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('index.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
