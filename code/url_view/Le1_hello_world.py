from flask import Flask

# init flask
app = Flask(__name__)

# 以@开头为一个装饰器
# 作用为url与视图函数的映射
# 127.0.0.1:5000/ -> 请求hello_world函数，将结果返回给浏览器
@app.route('/')
def hello_world():
    return 'hello_world'

if __name__ == "__main__":
    # app.run
    # 启动一个应用服务器，接受用户请求
    # while True:
    #   listen()
    app.run()
