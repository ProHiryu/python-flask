#-*-coding:utf8-*-
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    comments = [
        {
            'user':u'dsfjks',
            'comment':u'you are one'
        },
        {
            'user':u'fsfkjsl',
            'comment':u'you are two'
        }
    ]
    return render_template('index_filter.html',comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
