#-*-coding:utf8-*-
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/<is_login>')
def index(is_login):
    class Person(object):
        name = u'onetwo'
        age = 18

    if is_login == '1':
        p = Person()
        user = {
            'username':'oneone',
            'gender':'female',
            'age':23,
            'person':p,
            'websites':{
                'baidu':'www.baidu.com',
                'google':'www.google.com'
                }
        }
        return render_template('index.html',user=user)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
