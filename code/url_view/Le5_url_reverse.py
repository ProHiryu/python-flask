# -*-coding:utf8-*-
from flask import Flask,url_for

# init flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # 反转url：从视图函数到url的转换为反转url
    # 反转url的用处为：
    #   1.在页面重定向的时候会使用
    #   2.在模版中也会使用url反转（点击某些按钮触发事件的时候）
    print(url_for('my_list'))
    print(url_for('article',id='abc'))
    return 'hello_world'

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/article/<id>/')
def article(id):
    return u'your id is: {}'.format(id)

if __name__ == "__main__":
    app.run(debug=True)
