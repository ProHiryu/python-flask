# -*-coding:utf8-*-
from flask import Flask

# init flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world!'

if __name__ == "__main__":
    # app.run(debug=True)
    # 设置debug模式
    # 1.将所有的错误信息全部输出至127.0.0.1:5000
    # 2.当文件产生改变的时候，同步所有更改的效果
    app.run(debug=True)
