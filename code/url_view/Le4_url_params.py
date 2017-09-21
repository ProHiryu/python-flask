# -*-coding:utf8-*-
from flask import Flask

# init flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'

# 获取传入url当中的对应参数，用<name>表示对应的参数名称
# 视图函数中需要放置与url参数同名的参数
@app.route('/artical/<id>')
def artical(id):
    return u'the id is: {}'.format(id)

if __name__ == "__main__":
    app.run(debug=True)
