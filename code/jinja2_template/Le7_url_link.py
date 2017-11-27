#-*-coding:utf8-*-
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_url_link.html')

@app.route('/login/')
def login():
    return render_template('index_url_link_login.html')

if __name__ == '__main__':
    app.run(debug=True)
