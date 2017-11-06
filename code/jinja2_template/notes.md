### Flask渲染Jinja2模版和传参

1. 如何渲染模版：
    * 模版放在templates文件夹下
    * 从‘flask’中导入render_template函数
    * 在视图函数中使用render_template函数渲染模版
2. 模版传参：
    * 如果只有一个或者少量参数，直接在render_template函数中添加参数即可
    * 如果有多个参数，则定义一个字典，通过**dict分别传入字典中所有的参数给render_template函数
3. 模版中使用变量：`{{variable}}`
4. 模版中访问属性或者字典内容，可以通过`{{variable.property}}`来实现

### 过滤器

### if判断

1. 语法：
    ```
    {% if ... %}
    {% else %}
    {% endif %}
    ```
2. if的使用和python中相差无几，注意是通过传入参数来实现判断条件

### for循环遍历和字典

1. 字典的遍历，语法和python一样，可以使用items函数也可以使用keys函数还可以使用values，同样可以使用iterkeys，itervalues
    ```html
    {% for k,v in user.items() %}
    <p>
      {{k}} : {{v}}
    </p>
    {% endfor %}
    ```
2. 列表的遍历，语法和python一样
    ```html
    {% for website in websites %}
    <p>
      {{website}}
    </p>
    {% endfor %}
    ```

### 过滤器

1. 介绍和语法：
    * 介绍：过滤器可以处理变量，把原始的变量经过自己需求处理后展示出来，作用的对象是变量
    * 语法：
      ```html
      {{ variable|default('...') }}
      ```
2. default过滤器：如果当前变量不存在，则使用默认值
3. length过滤器：计算当前变量的长度，用法同python当中的length函数
4. 常用过滤器：
    * float：将传入变量代码块中的值转换为浮点数，类似于 Python 的 float()
    * int：类似于 Python 的 int()
    * title：将传入变量代码块的 String 的首字母转换成大写，成为一个合格的 Title
    * round：类似于 Python 的 round() 定义浮点数的精度
        - common 参数：四舍五入 - {{ 4.7 | rount(1, "common")}}
        - floor 参数：截取整数部分
        - ceil 参数：向上取整
    * join：将传入变量代码块的列表变量中的元素作为字符串连接起来，类似于 Python 的 join()
    * tojson：过滤器 tojoin 实际上是调用了 Python 的 json.dumps 函数来序列化对象，一样的需要确保传入变量代码块的是一个可以被序列化的对象 Dict
    * truncate：用于截取指定长度的 String 对象，并在截取后的子字符串后添加省略号
    * escape：如果传入变量代码块的是 HTML 字符串，则将该字符串中的 &、<、>、’、” 作为 HTML 的转义序列打印
    * safe：safe 过滤器含有 escape 的功能，将传入到变量代码块中的 HTML 字符串中的特殊符号进行 HTML 转义，这是必要的安全手段

### 继承和block

1. 继承作用和语法：
    * 作用：可以把一些公共的代码放在父模版中，避免重复代码
    * 语法：
      ```html
      {% extends 'base.html' %}
      ```
2. block:
    * python block:
      ```python
      class Person(object):
          name = ''
          age = 0

          def func():
              pass

      class Student(Person):

          def func():
              print("Student")
      ```
    * 作用：可以让子模版实现一些自己的需求，父模版需要提前定义好
    * 注意：子模版当中的代码块必须放在block当中
    * 语法：
      ```html
      <!--父模版-->
      {% block main %}
      {% endblock %}

      <!--子模版-->
      {% extends 'base.html' %}

      {% block main %}
          <h1>这是登录页面</h1>
      {% endblock %}
      ```

### url链接

### 加载静态文件
