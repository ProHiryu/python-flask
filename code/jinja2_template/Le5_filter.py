#-*-coding:utf8-*-
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_filter.html',avator='https://i0.hdslb.com/bfs/face/3075872e777c6001b4a5233230f4d7aa49eb2146.jpg@68w_68h.webp')


if __name__ == '__main__':
    app.run(debug=True)
