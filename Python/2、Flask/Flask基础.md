### 不记文档，白忙一场

#### 搭建环境

```python
第一步：创建虚拟环境
1、python -m pip install --upgrade pip   --> 更新pip
2、pip install virtualenv   --> 安装虚拟环境包
3、pip install virtualenvwrapper-win    -->安装虚拟环境管理包（Linux环境下使用virtualenvwrapper） 
4、设置workon_home环境变量   -->在系统变量里新建即可， 变量名：WORKON_HOME，变量值：创建虚拟环境的目      录。不需要添加PATH
5、mkvirtualenv testevn   --> 创建虚拟环境
   (如果需要指定Python的版本，
   使用参数：--python=D:\ProgramData\Anaconda3\python.exe；
    如果需要使用公共的包，使用参数：--system-site-packages:)
6、激活虚拟环境  --> workon testevn
7、查看现有的虚拟环境   --> workon
8、退出虚拟环境    --> deactivate
9、删除虚拟环境    --> rmvirtualenv testevn
第二步：安装flask
1、mkvirtualenv flaskEnv  --> 创建虚拟环境
2、workon flaskenv  --> 进入虚拟环境
3、pip install flask  --> 安装flask
第三步：创建工程
1、桌面新建空文件夹，起名firstFlask。
2、File --> New Project --> 点击Location三个点找到桌面的firstFlask文件夹 --> 
	Project Interpreter --> Existing interpreter --> 点击三个点 --> Interpreter点击三个点 --> 
	找到D:\workon_home\env1\Scripts\python.exe(即自己新建的虚拟环境) --> 
	make available to all projects --> create --> open in a new window
3、右键项目 --> new --> python file --> Name --> 写manage.py --> 至此搭建完成  
```

#### 项目开发

**1、项目结构**

```python
project/
	
```



#### 入门

**1、flask概念：**

>  ```python
>  是一个非常小 轻量级的WEB框架  只提供了一个强劲的核心 其它功能都需要通过第三方扩展去实现
>  ```

**2、模板引擎：** 

> ```python
> jinja2
> ```

**3、完整运行flask:**

> ```python
> from flask import Flask
> app = Flask(__name__) #创建flask的实例
> @app.route('/') #路由  访问地址 127.0.0.1:5000 或  127.0.0.1:5000/
> @app.route('/index') #路由 访问地址 127.0.0.1:5000/index
> @app.route('/index/') #路由 访问地址 127.0.0.1:5000/index 或 27.0.0.1:5000/index/
> def index():
>         return 'Hello Flask'
> if __name__== '__main__':
> 	app.run()   #执行flask的运行   如果更换为调试模式，即修改代码，不需要重启，则加参数debug=True
>     			   #请求地址为 http://127.0.0.1:5000
> ```

**4、路由地址传参**

> (1) 无参路由
>         @app.route('/')     #路由  访问地址 127.0.0.1:5000 或  127.0.0.1:5000/
>         def index():
>         	return 'Hello Flask'
> (2) 带一个参数的路由地址
>         @app.route('/arg/<age>/') 		#127.0.0.1:5000/arg/18
>         def arg(age):
>             	return '参数的值为{}'.format(age)
> (3) 传递多个参数
>     	#传递多个参数
>         #使用路由地址分隔符 进行分隔
>         @app.route('/args/<name>/<age>/') 		#http://127.0.0.1:5000/args/zhangsan/18/	
>
> ​		或者							
>         @app.route('/args/<name>_<age>/')                #http://127.0.0.1:5000/args/zhangsan_18/
>         def args(name,age):
>             return '我叫{} 我今年{}岁了'.format(name,age)
> (4) 限制参数的类型 手动
>
> ```python
> from flask import abort
> #传递参数限制值的类型  手动
> #http://127.0.0.1:5000/args/zhangsan_18/
> @app.route('/args/<name>_<age>/')
> def args(name,age):
>     try:
>         age = int(age) #限制类型转换为整形
>         except:
>             raise ValueError
>             abort(404) #抛出404
>             return '我叫{} 我今年{}岁了'.format(name,age)
> ```

> (5)  限制参数的类型 自动
>
> ```python
> #传递参数 通过路由限制类型
> @app.route('/args/<name>_int:age/') #限制参数类型为 int
> @app.route('/args/<name>_float:age/') #限制参数类型为float
> @app.route('/args/<name>_<age>/') #默认，限制参数类型为string
> @app.route('/args/<name>_string:age/') #限制参数类型为string 默认值就是
> @app.route('/args/<name>_path:age/') #将路由地址age后面的所有参数 都认为是当前age的参数值,/分隔		#符不再作为分隔符使用。比如：http://127.0.0.1:5000/args/zhangsan_18/12/abc/2/
> def args(name,age):
>     print(type(age))
>     return '我叫{} 我今年{}岁了'.format(name,age)
> ```

**5、response 响应**

> (1) 返回一个字符串进行响应 return
> 	@app.route('/response/')
>         def res():
>             return '我是响应'
> (2) 响应内容和状态码
>     	@app.route('/response/')
>         def res():
>             return '我是响应',404#响应内容和状态码
> (3) 使用系统的 make_response进行响应	
>
> ```python
> from flask import make_response
> @app.route('/response/')
> def res():
>     #设置cookie的时候使用 当前的make_response  其它情都是响应一个html页面
>     res = make_response('我是响应',404) 
>     return res
> ```
>
> ​     注意：
>
> ```python
> 1、路由地址结尾/建议都加上 因为在访问有/作为结尾的地址的时候 浏览器会自动帮你添加
> 2、路由传参写在<参数名称> 参数的名称为 形参名. 在flask中 路由地址可以相同如果同为一个方法请求		（如：GET） 则会按照顺序执行，执行在上方的视图函数.视图函数不可以重名。
> ```

**6、flask启动的参数**

> app.run的参数
>
> | 参数     | 参数说明                 |
> | -------- | ------------------------ |
> | debug    | 开启调试模式 默认为False |
> | host     | 主机                     |
> | port     | 端口号                   |
> | threaded | 多线程 默认flase         |
>
> 示例：app.run(host='0.0.0.0',port=5001,threaded=True,debug=True)

**7、请求对象**

> (1) 概念：
>
> ```python
> request是根据每一个用户的请求 对应创建的request对象  是由flask创建 在使用的时候 只需要导入就可以
> ```
>
> (2) 导入:
>
> ```python
> from  flask import request
> ```
>
> (3) request的属性
>
> ```python
> 示例：127.0.0.1:5000/request/canshu/?name=zhangsan&age=lisi&age=wangwu
> 1. url --> 请求的完整的url 
> 2. base_url --> 去掉get传参的url:http://127.0.0.1:5005/request/canshu/
> 3. host_url --> 主机和端口号的url:http://127.0.0.1:5005/
> 4. path --> 请求的路由地址:/request/canshu/
> 5. method --> 请求的方式:GET
> 6. args --> 获取get传参:
>     		ImmutableMultiDict([('name', 'zhangsan'), ('age', 'lisi'), ('age', 'wangwu')])
> 			注：args.getlist(key)获取有相同key的get传参    
>              getlist的参数为 多个值的key ['lisi', 'wangwu']
> 8. form --> 获取表单传递过来的数据。request.form 获取POST传过来的参数：ImmutableMultiDict([])
> 9. files --> 获取文件上传的数据:ImmutableMultiDict([])
> 10. headers --> 获取请求头信息:
>     		User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) 
>              Gecko/20100101 Firefox/60.0
>     		Accept-Language: en-GB,en;q=0.5
> 11. cookies --> 获取多个cookie:   					
>     		csrftoken=AA7yeEKEiY4DJtbB2mYc4Hjckyb14cY5MDFImfQ4yEUgVW4WNh9rHj3yCGZlZ47D
> ```

**8、abort终止**

> (1) 概念：
>
> ```python
> 在代码运行的过程中  出现任何的异常 可以使用abort 抛出标准的http状态码 终止当前程序的执行 和raise类似  抛出问题的代码的上方都正常执行  下面不再执行
> ```
>
> (2) 导入
>
> ```python
> from flask import abort
> ```
>
> (3) 示例
>
> ```python
> @app.route('/')
> def idnex():
>     abort(404)
>     下面代码不再执行
> ```
>
> (4) 捕获错误
>
> ```python
> #捕获http错误
> @app.errorhandler(404)
> def page_not_found(e):
>     return '错误信息为{}'.format(e)
> 
> #捕获http错误
> @app.errorhandler(500)
> def page_not_found(e):
>     return '错误信息为{}'.format(e)
> ```

**9、会话控制COOKIE SESSION**

**COOKIE**

> (1) 语法
>
> ```python
> Response.set_cookie(
> 	key,
>     value,
>     max_age=None,设置过期时间 单位为秒
>     expires=None,以秒为单位的寿命
>     path = '/'
> )
> ```
>
> (2) 设置COOKIE
>
> ```python
> 方法一：不设置过期时间
> #设置cookie 不设置过期时间 --> 默认为浏览器会话结束，即浏览器关闭
> @app.route('/set_cookie/')
> def setCookie():
>     res = make_response('设置cookie')
>     res.set_cookie('name','zhangsan')
>     return res
> 方法二：设置过期时间
> #设置cookie 并设置过期时间
> @app.route('/set_cookie/')
> def setCookie():
>     res = make_response('设置cookie')
>     # res.set_cookie('name','zhangsan',max_age=60) #设置当期cookie存活时间为1分钟
>     life_time = time.time()+60
>     res.set_cookie('name','zhangsan',expires=life_time) #设置当期cookie存活时间为1分钟
>     return res
> ```
>
> (3) 获取COOKIE
>
> ```python
> #查看cookie
> @app.route('/get_cookie/')
> def get_cookie():
>     myCookie = request.cookies #获取所有cookie
>     print(myCookie)
>     return 'key为name的值为{}'.format(myCookie.get('name'))
> ```
>
> (4) 删除COOKIE
>
> ```python
> #删除cookie
> @app.route('/del_cookie/')
> def del_cookie():
>     res = make_response('删除cookie')
>     res.delete_cookie('name') #删除key为name的cookie
>     return res
> ```

**SESSION**

> (1) 前提
>
> ```python
> #需要使用secret_key 进行加密,生成session所需要的加密种子 --> 秘钥
> #FlaskForm也需要secret_key
> app.config['SECRET_KEY']='abcdef'
> 导入：
> from flask import session
> ```
>
> (2) 设置SESSION
>
> ```python
> 方法一：不设置过期时间
> #设置session 不设置过期时间 --> 默认为浏览器会话结束，即浏览器关闭
> @app.route('/set_session/')
> def set_session():
>     session['uid'] = '1'
>     return '设置session'
> 方法二：设置过期时间
> #设置session 设置过期时间
> @app.route('/set_session/')
> def set_session():
>     #开启session持久化存储
>     session.permanent = True
>     #设置session存活时间为1分钟  如果不给当期的存活时间 则为1个月
>     app.permanent_session_lifetime = timedelta(seconds=60) 
>     session['uid'] = '1'
>     return '设置session'
> ```
>
> (3) 获取SESSION
>
> ```python
> #获取session
> @app.route('/get_session/')
> def get_session():
>     return 'uid的值为{}'.format(session.get('uid'))
> ```
>
> (4) 删除SESSION
>
> ```python
> #删除session
> @app.route('/del_session/')
> def del_session():
>     #删除key为uid的session值
>     # session.pop('uid')
>     #删除所有session
>     session.clear()
>     return '删除成功'
> ```

**10、flask-script扩展库**

> (1) 安装：
>
> ```python
> sudo pip install flask-script
> ```
>
> (2) 简介：
>
> ```python
> 简单来说 就是一个flask终端运行的解析器    因为在代码完成以后 不能有任何的改动  
> ```
>
> (3) 导入：
>
> ```python
> from flask_script import Manager
> ```
>
> (4) 常用的启动项：
>
> | 名称       | 作用           |
> | ---------- | -------------- |
> | -h         | host主机名     |
> | -p         | port 端口号    |
> | -d         | debug 调试模式 |
> | -r         | reloading 加载 |
> | --threaded | 开启多线程     |
>
> ```python
> 示例：
>     python  manage.py runserver -h0.0.0.0 -p5000 -d -r --threaded
>     python manage.py -d -r 只开启调试模式和重新加载
> ```
>
> (5) 使用：
>
> ```python
> from flask import Flask
> from flask_script import Manager
> 
> app = Flask(__name__)
> manager = Manager(app) #实例化 Manager类
> 
> @app.route('/')
> def index():
>     return 'index.html'
> 
> if __name__ == '__main__':
>     # app.run()
>     manager.run()
> ```

**11、蓝本Blueprint**

> (1)概述：
>
> ```python
> 当代码越来越复杂的时候 把所有的代码 都放在一个文件中 明显是不合理的   需要根据不同模块功能进行划分 蓝本就是解决这个问题的
> ```
>
> (2) 导入：
>
> ```python
> from flask import Blueprint
> ```
>
> (3) 示例：
>
> user.py蓝本中的代码：
>
> ```python
> from flask import Blueprint #导入蓝本
> #第一个user  因为当前是关于用户处理的蓝本 顾名思义 所有叫user user是给当前所有的视图添加装饰器来用的
> user = Blueprint('user',__name__)
> @user.route('/login/')
> def login():
>     return '欢迎登录'
> @user.route('/logout/')
> def logout():
>     return '退出登录'
> ```
>
> manager.py中的代码：
>
> ```python
> import user #导入user蓝本对象
> #注册user蓝本
> app.register_blueprint(user.user)
> #给当前的蓝本起前缀名称
> app.register_blueprint(user.user,url_prefix='/user')
> 注：1、如果是from user import user即是，从user.py模块中导入user对象，下面就不用再写user.user了，		直接写user。凡是.py结尾的，都是模块。
> 	2、python中是from 模块 import 方法
> 	3、如果在注册方法中有第二个参数，url的前缀，则url访问的时候，是localhost:5000/user/login/
> 	4、flask的路由，和Django一样，都是按功能不同，创建不同路由文件，然后再manager.py中注册
> ```
>
> (4) 访问：
>
> ```python
> 带前缀的访问
> 127.0.0.1:5000/user/login/
> 没有前缀的访问
> 127.0.0.1:5000/login/
> ```

**12、重定向**

> (1) 概述：
>
> ```python
> 从一个路由跳转到另外的一个路由地址
> 
> ```
>
> (2)使用：
>
> ```python
> redirect
> ```
>
> (3) 导入：
>
> ```python
> from flask import redirect
> ```
>
> (4) 参数：
>
> ```python
> 要跳转的路由地址
> ```
>
> (5) 示例：
>
> ```python
> @app.route('/')
> def index():
>     return 'index.html'
> #重定向的测试的视图函数
> @app.route('/test/')
> def test():
>     # return 'test'
>     # return redirect('/')       #index.html
>     return redirect('/arg/18/')  #会跳到下面的参数路由 age的值为18
> #带参数的路由
> @app.route('/arg/<int:age>/')
> def arg(age):
>     return 'age的值为{}'.format(age)
> ```
>
> (6) url_for 
>
> ​	作用：
>
> ```python
> 通过视图函数，反向构造出路由地址
> 因为redirect 重定向 是没有任何问题 但是 一旦路由地址发生改变 所有对应当期的重定向的地址 都需要修改
> 所以通过视图函数(即def定义的方法名称)可以不必担心地址的改变
> ```
>
> ​	导入：
>
> ```python
> from flask import url_for
> ```
>
> ​	示例：
>
> ```python
> #重定向的测试的视图函数
> @app.route('/test/')
> def test():
>     return url_for('index') # /
>     return url_for('indexx') #传递一个不存在的视图函数 则报错
>     return url_for('arg',age=18) #传递一个不存在的视图函数 则报错
>     return url_for('arg',age=18,name='zhangsan') #传递一个不存在的视图函数 则报错
>     return redirect(url_for('arg',age=18,name='zhangsan')) #传递一个不存在的视图函数 则报错
>     return redirect('/arg/18/zhangsan/') #传递一个不存在的视图函数 则报错
> #带参数的路由
> # @app.route('/arg/<int:age>/')
> @app.route('/arg/<int:age>/<name>/')
> def arg(age,name):
>     return 'age的值为{}'.format(age)
> ```
>
> (7) 蓝本之间的跳转
>
> ​	manage.py
>
> ```python
> import user #导入user蓝本对象
> from car import car
> #注册user蓝本
> # app.register_blueprint(user.user)
> #给当前的蓝本起前缀名称
> app.register_blueprint(user.user,url_prefix='/user')
> app.register_blueprint(car)
> ```
>
> ​	car.py
>
> ```python
> from flask import Blueprint,redirect,url_for
> car = Blueprint('car',__name__)
> @car.route('/show/')
> def show():
>     # return '查看购物车'
>     return redirect(url_for('user.login'))
> 注意：可以看到蓝本间的跳转，在该模块中，是没有导入user对象的，所以此处的user是user.py模块中，创建其蓝本对象的时候，第一个参数的标识，用以被url_for管理 --> user = Blueprint('user',__name__)
> ```
>
> ​	user.py
>
> ```python
> from flask import Blueprint #导入蓝本
> 
> #第一个user  因为当前是关于用户处理的蓝本 顾名思义 所有叫user user是给当前所有的视图添加装饰器来用的
> user = Blueprint('user',__name__)
> @user.route('/login/')
> def login():
>     return '欢迎登录'
> @user.route('/logout/')
> def logout():
>     return '退出登录'
> ```

**13、请求钩子函数**

> (1) 概述：
>
> ```python
> 类似django的中间件
> ```
>
> (2) 在manager.py中的注解：
>
> | 钩子函数             | 功能描述                 |
> | -------------------- | ------------------------ |
> | before_first_request | 第一次请求之前           |
> | before_request       | 每次请求之前             |
> | after_request        | 请求之后  没有异常       |
> | teardown_request     | 请求之后  即使有异常出现 |
>
> ```python
> 示例：
> #请求钩子函数
> @app.before_first_request
> def before_first_request():
>     print('before_first_request')
> #每次请求之前
> @app.before_request
> def before_request():
>     # print(request.method)
>     # print(request.path)
>     if request.path == '/check_form/' and request.method == 'GET':
>         abort(500)
>     print('before_request')
> #请求之后
> @app.after_request
> def after_request(res):
>     print('after_request')
>     return res
> #请求之后
> @app.teardown_request
> def teardown_request(res):
>     print('teardown_request')
>     return res
> ```
>
> (3) 在蓝本模块中的注解：
>
> | 钩子函数                 | 功能描述                 |
> | ------------------------ | ------------------------ |
> | before_app_first_request | 第一次请求之前           |
> | before_app_request       | 每次请求之前             |
> | after_app_request        | 请求之后  没有异常       |
> | teardown_app_request     | 请求之后  即使有异常出现 |
>
> ```python
> 注意：在一个蓝本中导入，则所有蓝本中有效
> 示例：
> #请求钩子函数
> @car.before_app_first_request
> def before_first_request():
>     print('before_first_request')
> #每次请求之前
> @car.before_app_request
> def before_request():
>     if request.path == '/check_form/' and request.method == 'GET':
>         abort(500)
>     print('before_request')
> #请求之后
> @car.after_app_request
> def after_request(res):
>     print('after_request')
>     return res
> #请求之后
> @car.teardown_app_request
> def teardown_request(res):
>     print('teardown_request')
>     return res
> ```

#### 模板引擎

**1、概念**

> ```python
> 模板文件就是按照一定的规则进行替换   负责展示效果的html文件
> 模板引擎：jinja2
> 模板语法：
>     1. 变量
>        {{ 变量名 }}   遵循标识符的命名规则
>     2. 标签
>        {% 标签名称 %}
>        {% end 标签名 %}
> 注意：如果模板中使用的变量不存在 则插入的是空字符串(什么都没有)  不会报错
> ```

**2、创建模板目录**

> ```python
> templates
> 即：在工程下直接创建文件夹，名称为templates
> 创建完成之后，右键，mark as templates --> language --> jinjia2 --> 然后就有语法提示了
> #注意：return render_template('')中的参数路径，默认是templates路径，所有参数接着往下写就可以了
> ```

**3、模板的渲染**

> (1) 导入：
>
> ```python
> from flask import render_template,render_template_string
> ```
>
> (2) 示例
>
> ```python
> @app.route('/')
> def index():
>     # return render_template_string('<h1 style="color:red;">首页</h1>')
>     # print(render_template('index.html')) 找到这个页面，吧页面的内容拿到，而非跳转到这个页面
>     return render_template('index.html',title='我是首页')
>     return '首页'
> #注意：return render_template('')中的参数路径，默认是templates路径，所有参数接着往下写就可以了
> ```

**4、过滤器**

> (1) 概述：
>
> ```python
> 过滤器 是通过管道符 | 来实现的  过滤器相当于是一个函数  用来过滤当前传递过来变量的值
> ```
>
> (2) 常用的过滤器
>
> ```python
> 1. var|abs 绝对值
>    {{ num|abs }}
> 2. default 默认值
>    {{ abc|default('我是默认值') }} abc不存在执行默认值  值有变量不存在则执行
>    {{ bool|default('我是默认值bool',boolean=True) }}   当变量不存在和值为False则执行
> 3. first  (str)第一个值
> 4. last   (str)最后一个值
> 5. format  格式化 
>    {{ "我叫%s 我今年%d岁了 存款为%.2f"|format(name,age,money) }}
> 6. leng  长度
> 7. safe   原样显示html代码
> 8. int  转换为整形
> 9. float  转换为浮点形
> 10. list   转换为列表
> 11. lower  转换为小写
> 12. upper  转换为大小
> 13. join    拼接成字符串
>     {{ [1,2,3,4]|join('') }}
> 14. replace  替换
>     {{ string|replace('a','x') }}
> 15. striptags  去除html标签
> ```

**5、标签**

> (1) if - else
>
> ```python
> {% if grade>=90 %}
> 	<li>成绩为优 {{ grade }}</li>
> {% elif grade>=70 %}
> 	<li>成绩为良 {{ grade }}</li>
> {% elif grade>=60 %}
> 	<li>成绩为及格 {{ grade }}</li>
> {% else %}
> 	<li>成绩为1804</li>
> {% endif %}
> ```
>
> (2) for循环
>
> ```python
> 示例一：迭代数组
> {% for foo in range(10) %}
>     <li>{{foo }}</li>
> {% endfor %}
> 示例二：迭代字典
> {% for key,val in data.items() %}
>     <li>{{ key }}===>{{ val }}</li>
> {% endfor %}
> 示例三：else在for循环中的使用
> {% for key,val in abcdefg %}
>     <li>{{ key }}===>{{ val }}</li>
> {% else %}
>     <li>当给定的变量不存在则执行else</li>
> {% endfor %}
> ```
>
> ​	获取当前迭代的状态
>
> | 变量名称    | 变量说明                     |
> | ----------- | ---------------------------- |
> | loop.index  | 获取当期迭代的索引值 从1开始 |
> | loop.index0 | 获取当期迭代的索引值 从0开始 |
> | loop.first  | 是否为第一次迭代             |
> | loop.last   | 是否为最后一次迭代           |
> | loop.length | 迭代的长度                   |
>
> ​	注意：
>
> ```python
> break和continue不存在
> ```

**6、注释**

> ```python
> {# 注释的内容 #}
> 多行注释
> ```

**7、文件包含 include**

> (1) 概述：
>
> ```python
> include语句 可以把代码 包含在某个文件中   类似于将代码 copy到当前模板的某个位置
> ```
>
> (2) 语法：
>
> ```python
> {% include '路径/文件名称.html' %}
> ```
>
> (3) 示例：
>
> ​	index.html
>
> ```python
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>Title</title>
> </head>
> <body>
> {% include 'header.html' %}
> <div>content 我是代码的主体部分</div>
> {% include 'footer.html' %}
>     
> 当前的header和footer存放在 common的目录中    
> {% include 'common/header.html' %}
> <div>content 我是代码的主体部分</div>
> {% include 'common/footer.html' %}
> </body>
> </html>
> ```
>
> ​	header.html
>
> ```python
> <header>我是头部</header>
> ```
>
> ​	footer.html
>
> ```python
> <footer>我是尾部</footer>
> ```
>
> ​	注意：
>
> ```python
> header.html和footer.html中都可以写<!DOCTYPE html><html>等完整页面标签，在index.html的源码中虽然存在这些完整代码，但是并不影响显示。
> 但是，不建议这么写。只写需要的部分标签即可。
> ```

**8、继承 extends**

> (1) 作用：
>
> ```python
> 通过继承 能够更加方便快捷的实现 模板的复用
> ```
>
> (2) 语法：
>
> ```python
> {% extends '模板名称.html' %}
> ```
>
> (3) 示例
>
> ​	需要配合block来使用
>
> ​	base.html
>
> ```python
> <!DOCTYPE html>
> <html>
> <head>
> {% block header %}
>     {% block meta %}
>         <meta charset="UTF-8">
>     {% endblock %}
>     <title>{% block title %}Title{% endblock %}</title>
>     <style>
>         {% block style %}
>             #con{
>                 color: red;
>                 font-size: 20px;
>             }
>         {% endblock %}
>     </style>
>     {% block linkscript %}
>     {% endblock %}
> {% endblock %}
> </head>
> <body>
> <header>头部</header>
> <div id="con">
> {% block con %}
>     中间的内容部分
> {% endblock %}
> </div>
> <footer>尾部</footer>
> </body>
> </html>
> ```
>
> ​	test.html
>
> ```python
> {% extends 'common/base.html' %}
> {% block title %}
>     test测试模板继承的页面
> {% endblock %}
> {% block style %}
>     {{ super() }}
>     #con{
>         color:green;
>     }
> {% endblock %}
> {% block con %}
>     test测试模板继承的页面
> {% endblock %}
> 新的额内容 阿达萨达萨达撒的撒的撒大大的阿达是啊啊的阿三都是阿达
> ```
>
> ​	注意：
>
> ```python
> test.html中的最后一行'新的额内容 阿达萨达萨达撒的撒的撒大大的阿达是啊啊的阿三都是阿达'并不会在页面显示，因为他们不再继承页面的block中
> ```

**9、flask-bootstrap**

> (1) 安装
>
> ```python
> sudo pip3 install  flask-bootstrap
> ```
>
> (2) 使用
>
> ```python
> from flask_bootstrap import Bootstrap
> bootstrap = Bootstrap(app) 	
> #注意：模板中的{% extends 'bootstrap/base.html' %}bootstrap，就是bootstrap = Bootstrap(app) 		这个对象
> #注意：只有在后端的manager.py模块中创建了Bootstrap的对象，前端模板才能用。
> ```
>
> (3) 自定义base.html基础模板
>
> ```python
> #注意：继承了bootstrap下的base.html之后，什么都不写，页面就在源码上可看到有东西了。然后在flask-	bootstrap的模块下，找到base.html文件所在包，打开该文件。可看到，下面的block中，都是在该			bootstrap的base.html中定义了的。
> {% extends 'bootstrap/base.html' %}
> {% block title %}
>     首页
> {% endblock %}
> {% block navbar %}
>     <nav class="navbar navbar-inverse" style="border-radius: 0;">
>         <div class="container-fluid">
>             <!-- Brand and toggle get grouped for better mobile display -->
>             <div class="navbar-header">
>                 <button type="button" class="navbar-toggle collapsed" data-				   						toggle="collapse" data-target="#bs-example-navbar-collapse-1" 
>                        aria-expanded="false">
>                     <span class="sr-only">Toggle navigation</span>
>                     <span class="icon-bar"></span>
>                     <span class="icon-bar"></span>
>                     <span class="icon-bar"></span>
>                 </button>
>                 <a class="navbar-brand" href="#"><span class="glyphicon glyphicon-eye-open"
>                     aria-hidden="true"></span></a>
>             </div>
> 
>             <!-- Collect the nav links, forms, and other content for toggling -->
>             <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
>                 <ul class="nav navbar-nav">
>                     <li class="active"><a href="#">首页<span class="sr-only">(current)	
>                     	</span></a></li>
>                     <li><a href="#">发表博客</a></li>
>                     <li><a href="#">我收藏的</a></li>
>                 </ul>
> 
>                 <ul class="nav navbar-nav navbar-right">
>                     <form class="navbar-form navbar-left">
>                         <div class="form-group">
>                             <input type="text" class="form-control" placeholder="Search">
>                         </div>
>                         <button type="submit" class="btn btn-default">搜索</button>
>                     </form>
>                     <li><a href="#">注册</a></li>
>                     <li><a href="#">登录</a></li>
>                     <li class="dropdown">
>                         <a href="#" class="dropdown-toggle" data-toggle="dropdown" 	
>                         	role="button" aria-haspopup="true"
>                            aria-expanded="false">个人中心<span class="caret"></span></a>
>                         <ul class="dropdown-menu">
>                             <li><a href="#">个人信息</a></li>
>                             <li><a href="#">修改头像</a></li>
>                             <li><a href="#">修改密码</a></li>
>                             <li role="separator" class="divider"></li>
>                             <li><a href="#">修改邮箱</a></li>
>                         </ul>
>                     </li>
>                 </ul>
>             </div><!-- /.navbar-collapse -->
>         </div><!-- /.container-fluid -->
>     </nav>
> {% endblock %}
> {% block content %}
>     <div class="container">
>       {% block page_content %}
> 
>       {% endblock %}
>     </div>
> {% endblock %}
> ```
>
> (4) 使用自定义的base模板
>
> ```python
> {% extends'common/base.html' %}
> ```

**10、宏 macro**

> (1) 概述：
>
> ```python
> 类似python中的函数
> ```
>
> (2) 语法：
>
> ```python
> {% macro 名称([参数]) %}
> {% endmacro %}
> ```
>
> (3) 示例：
>
> ​	自定义一个创建单行文本域的宏
>
> ```python
> {# 自定义一个创建表单里单行文本域的标签 #}
> {% macro form(inputName,type,name,value='') %}
>     <p>{{ inputName}}<input type="{{ type }}" name="{{ name }}" value="{{ value }}"></p>
> {% endmacro %}
> ```
>
> ​	宏的导入和调用 
>
> ```python
> #注意：import form指的是macro form(参数)中的宏名称'form'，
> 	#python中是from 模块 import 方法
> 方法一：from ... import ... --> 导入一个宏
> {% from 'macrotest.html' import form %}
> {{ form('用户名：','text','username') }}
> {{ form('密码：','password','userpass') }}
> {{ form('','submit','submit','登录') }}
> 方法二：import ... as 别名 --> 导入模板中的所有宏
> {% import 'macrotest.html' as macroform %}
> {{ macroform.form('用户名：','text','username') }}
> {{ macroform.form('密码：','password','userpass') }}
> {{ macroform.form('','submit','submit','登录') }}
> ```
>
> (4) 注意：
>
> ```python
> 1. 只能在宏定义的下方去调用
> 2. 如果宏存在形参 且没有默认值 则可以不传实参(不建议)
> 3. 实参个数不能大于形参个数
> 4. 形参默认值遵循默认值规则 有默认值的放在右侧
> 5. 在参数定义处  不存在**kwargs的使用  在调用处可以使用
> 	因为**{name:'zhangsan',age:12}就是将其转换为：name='zhangsan',age=12
> ```

**11、加载静态资源**

> (1) 概述：
>
> ```python
> 在工程下创建static文件夹，专门存放静态资源。在static下还可以创建多个文件夹：css、js、img
> 静态资源有：css、js、img、视频、音频
> ```
>
> (2) 目录结构：
>
> ```python
> project/
> 	static/
> 	templates/
> 	manage.py
> #注意：静态资源中的参数路径，默认是工程下的static文件夹开始，所有参数接着往下写就可以了
> ```
>
> (3) 示例：
>
> ```python
> {% extends'common/base.html' %}
> {% block page_content %}
>     <img src="{{ url_for('static',filename='img/meinv.jpg',_external=True) }}" alt="">
> {% endblock %}
> 
> {#
>     _external参数 将当期路由地址变成绝对路径的路由地址(可选参数)
>     name  公有变量
>     _name 受保护变量
>     __name 私有变量 
>     注意： 在不同的python解释器中 解释是不同的 从当前模块中 导入到其它模块使用 _ 和 __ 是不能导入			（只能在当前文件中执行）
> #}
> ```
>
> (4) 注意：
>
> ```python
> 如果加载的静态资源文件 在static的顶级目录 则filename=文件名称 如果包含在某个目录中 则filename='目录名/文件名'
> ```

**12、在后端中传递多个参数到模板中**

> (1) 使用关键字方式
>
> ```python
> @app.route('/')
> def index():
>     return render_template('index.html',title='标题',con='首页')
> ```
>
> (2) 使用字典
>
> ```python
> #比方法一多麻烦一步
> @app.route('/')
> def index():
>     return render_template('index.html',data=data{'title':'标题','con':'首页'})
> ```
>
> (3) 使用**
>
> ```python
> #和方法一一模一样，只是写法不一样，这就是**的作用
> @app.route('/')
> def index():
>     return render_template('index.html',**{'title':'标题','con':'首页'})
> ```
>
> (4) 使用 **locals()
>
> ```python
> #最好的方法
> @app.route('/')
> def index():
>     name = 'zhangsan'
>     age = 18
>     # print(locals()) #返回当前的所有局部变量 以字典的形式 
>     return render_template('index.html',**locals())
> #注意：在函数中包含函数的时候，即糖语言的语法，打印出返回的内函数print，就可以看到类型是locals。
> #作用：把局部变量都变为参数
> ```
>
> (5) 使用全局变量g
>
> ```python
> from flask import g
> @app.route('/')
> def index():
>     g.name = 'zhangsan'
>     g.age = 18
>     return render_template('index.html')
> 使用:
> g.name
> g.age
> ```

**13、flash消息的显示**

> (1) 概述：
>
> ```python
> flash() --> 后端存储消息
> get_flashed_messages() --> 前端/后端获取存储的值，值是一个列表，需要for循环取出
> ```
>
> (2) 导入：
>
> ```python
> from flask import flash,get_flashed_messages
> ```
>
> (3) 示例：
>
> ​	manage.py
>
> ```python
> @app.route('/login/',methods=['GET','POST'])
> def login():
>     form = Login()
>     # form.hidde.data = '我是默认值'
>     if form.validate_on_submit():
>         # form.username.data
>         if form.username.data != 'lisi':
>             flash('当前用户不存在')
>         elif form.confirm.data != '123456':
>             flash('请输入正确的密码')
>         else:
>             flash('欢迎{}'.format(form.username.data))
>             return redirect(url_for('index'))
>         # print(get_flashed_messages())
>     return render_template('boot-quick-form.html',form=form)
> #注意：form = Login()是class Login(FlaskForm)定义的类。get_flashed_messages()前后端都可以使用
> ```
>
> ​	base.html
>
> ```python
> {% for info in get_flashed_messages() %}
>     <div class="alert alert-warning alert-dismissible" role="alert">
>     <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span>
>     </button>{{ info }}
>     </div>
> {% endfor %}
> #注意：{%for%}循环标签中的div是bootstrap官网上，扒下来的警告框样式
> ```

#### 表单

**1、原生表单**

> (1) 方法一：进入表单和表单提交是两个视图函数
>
> ​	form.html
>
> ```python
> <form action="{{ url_for('check_login') }}" method="post">
>     <p>用户名： <input type="text" maxlength="12" name="username" placeholder="请输入用户			名..."></p>
>     <p>密码： <input type="password" name="userpass" placeholder="请输入密码..."></p>
>     <p><input type="submit" value="登录"></p>
> </form>
> #注意：模板中也有url_for函数，其中的check_login是manager.py中的def check_login()函数名。
> #进入form.html页面的url是localhost:5000/login/，表单提交的action是localhost:5000/check_login/
> ```
>
> ​	manager.py中的视图函数
>
> ```python
> #表单第一种 原生form
> @app.route('/login/')
> def login():
>     return render_template('yuanshengform/form.html')
> 
> #获取表单提交过来的数据
> @app.route('/check_login/',methods=['POST']) #设置当前的路由地址只允许post请求
> # @app.route('/check_login/') #设置当前的路由地址只允许post请求
> def check_login():
>     # print(request.form) #获取不到get传递过来的数据
>     # print(request.args) #获取get传递过来的数据
>     # print(request.form) #获取不到get传递过来的数据
>     username = request.form.get('username')
>     userpass = request.form.get('userpass')
>     return '欢迎{} 密码为{}'.format(username,userpass)
>     # return '获取到数据了'
> ```
>
> (2) 方法二：进入表单和表单提交是同一个视图函数
>
> ```python
> #俩个视图合并为同一个视图
> @app.route('/login/',methods=['GET','POST'])
> def login():
> 	if request.method == 'POST' and request.form.get('username') and 							request.form.get('userpass'):							
>         print(request.form)
>         return '数据提交过来'
>     return render_template('yuanshengform/form.html')
> #注意：此处并没有csrf_token加密验证，不安全，别人在网页扒走提交地址和数据框，自己写一个form提交。因为没有csrf_token验证，别人的伪提交，也可以成功
> ```
>
> (3) 注意：
>
> ```python
> #如果form表单的action属性是空字符串，则路径还是打开form表单所在页面的对应原视图函数本身
> ```
>
> 

**2、flask-wtf表单扩展库**

> (1) 安装：
>
> ```python
> sudo pip3 install flask-wtf
> ```
>
> (2) 说明：
>
> ```python
> 是一个用于表单处理的扩展库 提供了csrf  和表单验证等功能
> ```
>
> (3) 字段类型：
>
> | 字段名称      | 字段说明       |
> | ------------- | -------------- |
> | StringField   | 普通文本字段   |
> | SubmitField   | 提交字段       |
> | PasswordField | 密码字段       |
> | HiddenField   | 隐藏域         |
> | TextAreaField | 多行文本域字段 |
> | DateField     | 日期字段       |
> | DateTimeField | 日期时间字段   |
> | IntegerField  | 整形字段       |
> | FloatField    | 浮点形字段     |
> | BooleanField  | bool字段       |
> | RadioFIeld    | 单选           |
> | SelectField   | 下拉字段       |
> | FileField     | 文件上传       |
>
> (4) 验证器：
>
> | 验证器       | 验证器说明               |
> | ------------ | ------------------------ |
> | DataRequired | 必填                     |
> | Length       | 长度 min  max            |
> | IPAddress    | ip地址                   |
> | URL          | url地址验证              |
> | NumberRange  | 值的范围 min 和max       |
> | EqualTo      | 验证俩个字段值的是否相同 |
> | Regexp       | 正则匹配                 |
> | Email        | 验证邮箱                 |
>
> ​	注意：还可以自定义验证器
>
> ```python
> 示例：
> class Login(FlaskForm):
> 	username = StringField('用户名',validators=[DataRequired(message='用户名不能为空')])
> 	#自定义验证器
>     def validate_username(self,field):
>         # print(field.data)
>         # print(self.username.data)
>         if field.data == 'zhangsan':
>             raise ValidationError('该用户以存在')
> #注意：函数名称validate_是固定的，体现了'约定优于配置'，username是FlaskForm对象中的一个属性       
> ```
>
> (6) 示例
>
> ​	manager.py
>
> ```python
> from flask import Flask ,render_template,flash,get_flashed_messages,redirect,url_for
> from flask_script import Manager
> from flask_wtf import FlaskForm
> from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateTimeField, IntegerField, FloatField, BooleanField
> from wtforms.validators import DataRequired, IPAddress, URL, Email, EqualTo, NumberRange, ValidationError, Regexp
> from flask_bootstrap import Bootstrap
> 
> app=Flask(__name__)
> app.config['SECRET_KEY']='abcdf'
> bootstrap=Bootstrap(app)
> manager=Manager(app)
> 
> class Login(FlaskForm):
>     username = StringField('用户名',validators=[DataRequired(message='用户名不能为空')])
>     userpass = PasswordField('密码',validators=[DataRequired(message='密码不能为						空'),EqualTo('confirm',message='俩次输入密码不一致')])          				
>     confirm = PasswordField('确认密码')
> 	userinfo = TextAreaField('个人信息简介',render_kw={'style':'resize:none;',
>         'placeholder':'发表你此刻的感想...'})
>     birth = DateField('出生年月')
>     birth = DateTimeField('注册时间')
> 	age = IntegerField('年龄',validators=[NumberRange(min=6,max=99,message='年龄的范围为6~99		岁')])
>     money = FloatField('money')
>     agree = BooleanField('是否同意')
>     sex = RadioField('性别',choices=[('w','女'),('m','男')])
>     address = SelectField('地址',choices=[('1001','北京'),('1002','天津'),('1003','河北')])
>     file = FileField('选择头像')
>     hidde = HiddenField()
>     ip = StringField('ip地址',validators=[IPAddress(message='请输入正确的IP地址')])
>     url = StringField('网址',validators=[URL(message='请输入正确的url')])
>     email = StringField('邮箱',validators=[Email(message='请输入正确的邮箱地址')])
>     phone = StringField('phone',validators=[Regexp('^1[3-8][0-9]{9}$',message='请输入正确的手			机号码')])
>     submit = SubmitField('登录')
>     #自定义验证器
>     def validate_username(self,field):
>         # print(field.data)
>         # print(self.username.data)
>         if field.data == 'zhangsan':
>             raise ValidationError('该用户以存在')
> ```
>
> 注意：
>
> ```python
> render_kw 属性 可以给当前字段添加属性和样式 
> 示例：
> userinfo = TextAreaField('个人信息简介',render_kw={'style':'resize:none;','placeholder':'发表你此刻的感想...'})
> ```
>
> ​	对应的模板有三种方法：
>
> ​	方法一：普通拿到FlaskForm对象，进行页面加载
>
> ​	form.html
>
> ```python
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>wtf-form</title>
> </head>
> <body>
> <form action="" method="post">
>     {{ form.csrf_token }}
>     {{ form.username.label() }}
>     {{ form.username(placeholder='请输入用户名...',style='color:red;') }}
> 	{#    {{ form.username.errors }}#}
>     {% if form.username.errors %}
>         <span style="color: red;">{{ form.username.errors.0 }}</span>
>     {% endif %}
>     <br>
>     {{ form.userpass.label() }}
>     {{ form.userpass() }}
> 	{#    {{ form.userpass.errors }}#}
>     {% if form.userpass.errors %}
>         <span style="color: red;">{{ form.userpass.errors.0 }}</span>
>     {% endif %}
>     <br>
>     {{ form.submit() }}
> </form>
> </body>
> </html>
> #注意：1、{{ form.csrf_token }}是指manager.py中app.config['SECRET_KEY']='abcdf'加密过flask-wtf提供的csrf_token。
> #2、form.username.label()指的是DateField('出生年月')等的第一个参数，就和type = 'radio'的label一样，效果即使点击汉字，就触发框
> #3、form.username()就是该选择框了
> #4、form.username.errors.0指的是，.errors是message，.0是索引
> ```
>
> ​	方法二：相对于方法一，只是封装成了宏
>
> ​	form.html
>
> ```python
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>Title</title>
>     <style>
>         .error{
>             color: red;
>             list-style: none;
>         }
>     </style>
> </head>
> <body>
> {% from 'common/wtf-macro.html' import formField %}
> <form action="" method="post">
>     <table>
>         {{ formField(form.username) }}
>         {{ formField(form.userpass) }}
>     </table>
>         {{ form.submit() }}
> </form>
> </body>
> </html>
> ```
>
> ​	宏的代码：
>
> ```python
> {% macro formField(field) %}
>     <tr>
>         <td>{{ field.label() }}</td>
>         <td>{{ field() }}</td> 
>         	{# form.username() 在这个位置实现 能添加 placeholder属性 style class  #}
>         <td>
>             {% if field.errors %}
>                 <ul class="error">
>                 {% for error in field.errors %}
>                     <li>{{ error }}</li>
>                 {% endfor %}
>                 </ul>
>             {% endif %}
>         </td>
>     </tr>
> {% endmacro %}
> #使用宏，测试
> {#{{ formField(form.username)) }}#}
> 
>     
> 
> #注意： 添加样式如下
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>表单</title>
> </head>
> <body>
> {% macro formField(field) %}
>     <p>{{ field.label() }}</p>
>     <p>{{ field(**kwargs ) }}</p>
> {% endmacro %}
> {{ formField(form.username,class='usernameclass',
>        style='color:red;' ) }}
> </body>
> </html>
> ```
>
> ​	方法三：使用bootstrap的quick-form
>
> ```python
> {% extends 'common/base.html' %}
> {% import 'bootstrap/wtf.html' as wtf %}
> {% block page_content %}
>     <div class="row">
>         <div class="col-md-8"><img src="{{ url_for('static',filename='img/meinv.jpg') }}" 			alt=""></div>
>         <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
>     </div>
> {% endblock %}
> #注意：其中的<div class="col-md-8"></div><div class="col-md-4"></div>是bootstrap中粘过来的栅格样式。其中的'common/base.html'是在{% extends 'bootstrap/base.html' %}之后自定义的基准模板
> ```

#### 文件上传

**注意：**

> (1) 文件上传有几点：
>
> ```python
> 1、文件大小
> 2、文件路径
> 3、文件类型(jpg、png)
> 4、文件缩放
> 5、文件名称
> 6、文件前台默认展示和选择之后展示
> ```
>

**1、原生文件上传**

> (1) 示例：
>
> ​	manage.py
>
> ```python
> from flask import Flask,render_template,request
> from flask_script import Manager
> import os
> #pip install pillow
> from PIL import Image 
> 
> app = Flask(__name__)
> #允许上传的文件类型
> ALLOWED_FILE = ['jpg','jpeg','gif','png']
> #设置文件上传的路径
> app.config['UPLOAD_DEST'] = os.path.join(os.getcwd(),'static/upload')
> manager = Manager(app)
> 
> 
> @app.route('/')
> def index():
>     return render_template('index.html')
> 
> #当前上传的文件是否允许
> def allowd_file(suffix):
>     return suffix in ALLOWED_FILE
> 
> #生成随机的图片名称
> def random_name(suffix,length=32):
>     import string, random
>     Str = string.ascii_letters + '0123456789'
>     return ''.join(random.choice(Str) for i in range(length))+'.'+suffix
> 
> #图片缩放
> def img_zoom(path,width=300,height=200,prefix='s_'):
>     # 图片缩放处理
>     img = Image.open(path)
>     print(img.size)  # 获取图片的大小
>     # 重新设计图片大小
>     img.thumbnail((width, height))
>     newPath = os.path.join(os.path.split(path)[0],prefix+path.split('/')[-1])
>     img.save(newPath)
> 
> #原生文件上传的视图函数
> @app.route('/upload/',methods=['GET','POST'])
> def upload():
>     img_url = None
>     #判断：提交了文件，并且是选择了文件的，不是空文件
>     if request.method == 'POST' and 'file' in request.files:
>         #取出文件上传的对象
>         file = request.files.get('file')
>         filename = file.filename #获取图片名称
>         suffix = filename.split('.')[-1] #获取图片后缀
>         if allowd_file(suffix): #判断是否允许上传
>             # 获取生成的随机图片名称
>             while True:
>                 newName = random_name(suffix)
>                 path = os.path.join(app.config['UPLOAD_DEST'],newName)
>                 if not os.path.exists(path):
>                     break
>             file.save(path) #保存上传的图片
>             #图片缩放的处理
>             img_zoom(path)
>             img_url = newName
>     return render_template('yuansheng-file/form.html',img_url=img_url)
> 
> 
> if __name__ == '__main__':
>     manager.run()
> ```
>
> ​	form.html
>
> ```python
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>修改头像</title>
> </head>
> <body>
> {% if img_url %}
> <img src="{{ url_for('static',filename='upload/s_'+img_url) }}" alt="">
> {% else %}
> <img src="{{ url_for('static',filename='img/myf.jpg') }}" alt="">
> {% endif %}
> <form action="" method="post" enctype="multipart/form-data">
>     <p>选择图像</p>
>     <p><input type="file" name="file"></p>
>     <p><input type="submit" value="submit"></p>
> </form>
> </body>
> </html>
> ```

**2、flask-uploads文件上传扩展库**

> (1) 安装：
>
> ```python
> sudo pip3 install flask-uploads
> ```
>
> (2) 示例：
>
> ​	manage.py
>
> ```python
> from flask import Flask,render_template,request
> from flask_script import Manager
> from flask_uploads import UploadSet,IMAGES,patch_request_class,configure_uploads
> import os
> 
> app = Flask(__name__)
> #原生文件上传的设置，此处都在app和manager中间的代码中设置了，app中有了上传大小，文件路径，UploadSet对象中有了文件类型，最后再把app和UploadSet对象绑定在一起configure_uploads(app,file)
> #-------------------------------------------------------------------------
> app.config['MAX_CONTENT_LENGTH'] = 1024*1024*64
> app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(),'static/upload')
> file = UploadSet('photos',IMAGES) #上传文件对象配置#注意：此处'photos'是固定的，否则报错    							比如改为'pho',RuntimeError: no destination for set 'pho'
> configure_uploads(app,file)
> patch_request_class(app,size=None)
> #-------------------------------------------------------------------------
> manager = Manager(app)
> 
> @app.route('/')
> def index():
>     return render_template('index.html')
> 
> @app.route('/upload/',methods=['GET','POST'])
> def upload():
>     img_url = None  #注意：此处必须先定义，因为最后一行img_url = img_url的第二个img_usr引用
>     #判断：提交了文件，并且是选择了文件的，不是空文件
>     if request.method == 'POST' and 'file' in request.files:
>         #文件上传   
>         fileName = file.save(request.files.get('file'))
>         print(fileName) #timg.jpg
>         # 获取 图片的地址
>         img_url = file.url(fileName)
>         #print(img_url) http://127.0.0.1:5000/_uploads/photos/timg.jpg
>         #吧上面的配置的 photos也作为了一个路径
> 
>     return render_template('flask-uploads-form/form.html',img_url = img_url)
> 
> if __name__ == '__main__':
>     manager.run()
> #UploadSet对象有两个主要方法，file.save(xx)自动去找app.config[]中找路径，村进入。
> #file.url(xx)找当前文件的路径，以便于给前端的模板传过去的。
> ```
>
> ​	form.html
>
> ```python
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>修改头像</title>
> </head>
> <body>
> {% if img_url %}
>     <img src="{{ img_url }}" alt="">
> {% endif %}
> <form action="" method="post" enctype="multipart/form-data">
>     <p>选择图像</p>
>     <p><input type="file" name="file"></p>
>     <p><input type="submit" value="submit"></p>
> </form>
> </body>
> </html>
> #注意：图片路径可以直接适用{{img_url}}。这儿的img_url不是后端拼接起来的全路径，或者只是图片的名称，而是通过img_url = file.url(fileName)这个api获取到的。
> #file = UploadSet('photos',IMAGES) #上传文件对象配置。图片存储的路径，大小，类型都是在UploadSet这个类对象中配置。
> ```

**3、完整的文件上传**

> ​	manage.py
>
> ```python
> from flask import Flask,render_template
> from flask_script import Manager
> from flask_bootstrap import Bootstrap
> from flask_wtf import FlaskForm
> from flask_wtf.file import FileField,FileRequired,FileAllowed
> from wtforms import SubmitField
> from flask_uploads import UploadSet,configure_uploads,patch_request_class,IMAGES
> import os
> from PIL import Image
> 
> app = Flask(__name__)
> app.config['SECRET_KEY'] = 'abcdef'
> app.config['MAX_CONTENT_LENGTH'] = 1024*1024*64
> app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(),'static/upload')
> bootstrap = Bootstrap(app)
> file = UploadSet('photos',IMAGES)
> configure_uploads(app,file)
> patch_request_class(app,size=None)
> manager = Manager(app)
> 
> 
> class Upload(FlaskForm):
>     photos = FileField('上传头像',validators=[FileRequired(message='您还没有选择文件'),FileAllowed(file,message='请上传正确的格式的图片...')])
>     submit = SubmitField('上传')
> 
> 
> @app.route('/')
> def index():
>     return 'index'
> 
> #生成随机的图片名称
> def random_name(suffix,length=32):
>     import string, random
>     Str = string.ascii_letters + '0123456789' #数字+字母的字符串
>     return ''.join(random.choice(Str) for i in range(length))+'.'+suffix
> #图片缩放
> def img_zoom(path,width=300,height=200,prefix='s_'):
>     # 图片缩放处理
>     img = Image.open(path)
>     print(img.size)  # 获取图片的大小
>     # 重新设计图片大小
>     img.thumbnail((width, height))
>     #保存缩放后的新图片的路径（原图缩放后的图片都保存）
>     newPath = os.path.join(os.path.split(path)[0],prefix+path.split('/')[-1])
>     img.save(newPath)
> 
> @app.route('/upload/',methods=['GET','POST'])
> def upload():
>     form = Upload()
>     img_url = None
>     if form.validate_on_submit():
>         photos = form.photos.data
>         suffix = photos.filename.split('.')[-1]
>         # print(suffix)
>         while True:
>             newName = random_name(suffix)
>             path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], newName)
>             if not os.path.exists(path):
>                 break
>         file.save(photos,name=newName)
>         img_zoom(path)
>         img_url = file.url(filename='s_'+newName)
>     return render_template('form.html',form=form,img_url=img_url)
> 
> if __name__ == '__main__':
>     manager.run()
> ```
>
> ​	form.html
>
> ```python
> {% extends 'bootstrap/base.html' %}
> {% from 'bootstrap/wtf.html' import quick_form %}
> {% block content %}
>     {% if img_url %}
>         <img src="{{ img_url }}" alt=""> 
>     {% endif %}
> {#    {{ quick_form(form,action=url_for('index'),method='GET') }}#}
>     {{ quick_form(form) }}
> {% endblock %}
> ```

#### 邮件发送

**安装**

> ```python
> pip install flask-mail
> ```

**设置临时的环境变量**

> ```python
> windows   set 名=值
> set 名
> 如：
> set MAIL_PASSWORD=123456
> 
> Ubuntu  export 名=值
> echo $名
> ```

**同步发送**

> (1) 概述：
>
> ```python
> 同步发送，就是一条线程，只有右键真正发送成功了，页面才会显示弹框，发送成功！
> ```
>
> (2) 示例：
>
> ```python
> from flask import Flask,render_template_string
> from flask_script import Manager
> from flask_mail import Mail,Message
> import os
> 
> app = Flask(__name__)
> app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
> app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','xialigang@1000phone.com')
> app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','123456')
> 
> mail = Mail(app)
> manager = Manager(app)
> 
> @app.route('/')
> def send_mail():
>     msg = Message(subject='我是主题',recipients=['793390457@qq.com'],sender=app.config['MAIL_USERNAME'])
>     msg.html = render_template_string('<h1>你好 我发邮件了</h1>')
>     mail.send(message=msg)
>     return '发送邮件'
> 
> if __name__ == '__main__':
>     manager.run()
> ```

**异步发送**

> (1) 概述：
>
> ```python
> 异步发送，就是在发送邮件时候新建一条线程，主线程会直接执行完毕，显示发送成功了，新建线程慢慢执行发送邮件的过程。
> ```
>
> (2) 示例：
>
> ```python
> from flask import Flask,render_template
> from flask_script import Manager
> from flask_mail import Mail,Message
> import os
> from threading import Thread
> #flask-sqlalchemy
> app = Flask(__name__)
> app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER','smtp.1000phone.com')
> app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME','xialigang@1000phone.com')
> app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD','123456')
> mail = Mail(app)
> manager = Manager(app)
> 
> def async_send_mail(msg):
>     #程序上下文
>     with app.app_context():
>         mail.send(message=msg)
> @app.route('/')
> def send_mail():
>     msg = Message(subject='我是主题',recipients=						
>                   ['793390457@qq.com'],sender=app.config['MAIL_USERNAME'])
>     msg.html = render_template('email.html')
>     thr = Thread(target=async_send_mail,args=(msg,))
>     thr.start()
>     return '发送邮件'
> 
> if __name__ == '__main__':
>     manager.run()
> ```

#### 操作数据库

**1、flask-sqlalchemy**

> (1) 概述：
>
> ```python
> flask作为一个MVT框架 支持ORM    
> 随着项目越来越大  如果使用原生sql
> 
> 1. 原生SQL重复使用率不大  代码越长   出现很多相似的SQL 语句
> 2. 很多SQL语句  都是在业务逻辑中拼接出来的   如果数据库发生了改变  就要去修改这些逻辑    就会容易出现遗漏某个SQL的修改
> 3. 在写SQL 的时候  容易忽略安全问题  SQL注入
> 
> 使用ORM：
> 1. 减少了重复SQL的几率    写出来的代码更加直观和清晰
> 2. 可移植性    支持对多个数据库的链接的操作
> 3. 使用灵活  可以很方便的写出SQL语句
> 4. ORM最终还是转换成SQL语句去操作数据库
> 
> 注意：
> 如果数据库使用的是默认的latin1字符编码 则插入中文 结果为报错 或者是值为???   
> 1. 删除数据库
> 2. 改库的编码  表的编码 表中没=每个char或者varchar的字段类型改为 utf8
> ```
>
> (2) 使用sqlalchemy操作原生SQL：
>
> ​	安装
>
> ```python
> pip install pymysql
> pip install flask-sqlalchemy
> ```
>
> ​	示例：
>
> ```python
> from sqlalchemy import create_engine
> HOST = '127.0.0.1'
> USERNAME = 'root'
> PASSWORD = '123456'
> PORT = 3306
> DATABASE = 'demo'
> DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
> engine = create_engine(DB_URI)
> with engine.connect() as con:
>     con.execute('create table user(id int,username varchar(255))')
>     con.execute('sql语句')
> ```
>
> (3)	使用flask-SQLalchemy

#### 注意

**1、manager.py文件的作用**

> ```python
> 如果只是单个文件来执行，以显示前台页面，则随便起名字，比如起名字为test，则在终端写入命令为：
> python test.py runserver -d -r
> 因为python只是编译该文件的命令
> ```

**2、window和linux下路径中斜杠的不同**

> ```python
> 1、在window下一定要用：flask.config['UPLOADED_PHOTOS_DEST']= 								os.path.join(os.getcwd(),'static\\upload')
> 	效果是：H:\desktop\flaskProject\day05\static\upload\13I3q1VM3AXtlMaDWApmT1mjRExMuWzK.jpg
>     而且，prefix+path.split('\\')[-1])可以成功
>     如果用'/'则效果是有反斜杠，有正斜杠，而且path.split('/')[-1])什么都获取不到
> 2、在模板中，正常用斜杠就好：<img src="{{ url_for('static',filename='upload/mei.jpg') }}">
> 3、如果是linux的话，不存在这个问题
> ```

**3、基本知识注意点**

> ```python
> 注意：
> 	1、各个蓝本中，比如url.py、car.py中写的是各自模块的路由，然后统一在manage.py中注册
> 	2、创建某个模块的蓝本对象的时候，第一个参数的作用，是在蓝本之间跳转的时候，的一个标识。
> 		比如：car = Blueprint('car',__name__); -->存在于car.py模块中
> 		在另一个蓝本中，不用导入from car import car，就可以redirect(url_for('car.index'))
> 		可见：car并不是对象，而是蓝本管理的'car'标识，index是car.py模块中的视图函数  
> 	3、通过print(render_template('index.html')) --> 其中from flask import render_template
> 		index.html存在于templates目录下。
> 		可以从打印中看到，并不是return render_temlate('index.html',title='我是首页')是跳转到		index.html中的，而是把index.html模板拿过来，渲染，返回去浏览器的。
> ```











































































```python
1、return redirect(url_for('index'))不要忘写return了,url_for()参数不要忘了加引号
2、模板中是get_flashed_messages()，要加s
3、注意：
base.html
    {% block content %}
        <div class="container">
            {% for info in get_flashed_messages() %}
                <div class="alert alert-warning alert-dismissible" role="alert">
                  <button type="button" class="close" data-dismiss="alert" aria-label="Close">						<span aria-hidden="true">&times;</span></button>
                  <p>{{ info }}</p>
                </div>
            {% endfor %}

            {% block page_content %}

            {% endblock %}
        </div>
    {% endblock %}
boot-quick-form.html
	{% extends 'common/base.html' %}
    {% from 'bootstrap/wtf.html' import quick_form %}
    {% block page_content %}
    {#    <h1>{{ get_flashed_messages() }}</h1>#}
        {{ quick_form(form) }}
    {% endblock %}
#则此处一定是 {% block page_content %}，而不是{% block container %}否则直接把警告框也覆盖了
4、request也需要导入,from flask inport request
5、    if request.method == 'POST' and 'pic' in request.files:
        file = request.files.get('pic')
        filename = file.filename
        print(filename)
        suffix = filename.split('.')[-1]
        if allow_file(suffix):
            file.save(os.path.join(flask.config['UPLOAD_DEST'],filename))    
    注意：if request.method == 'POST' and 'pic' in request.files:这儿的'pic'是input的name属性值
```

如果form标签下的method不写，即使url传参，request.args获取。

直接F5刷新，输入url都是get

app.config['SECRET_KEY']='abcdef'
导入：
from flask import session

session也需要secret_key秘钥，作用就是加密。比如form表单提交，如果别人查看源码，自己写一个form表单，看到url则自己提交就可以了。有csrf就不会这样了。

所以目前，secret_key有两个地方需要：

一是：session需要

二是：flaskForm的csrf-token需要

模板中{{form.user.label()}}：form是后端的form=Login()对象，username是该对象的属性，label是属性的属性，应为Username是对象StringField()



```python
    {% if img_url %}{# 注意：原生的文件上传，不能用{{ img_url }}，而flask-upload扩展库可以 #}
        <img src="{{ url_for('static',filename='upload/'+img_url) }}">
    {% else %}
        <img src="{{ url_for('static',filename='upload/mei.jpg') }}">
    {% endif %}
```



```
import string
```