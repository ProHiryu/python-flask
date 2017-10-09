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
3. 

### 继承和block

### url链接

### 加载静态文件
