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

```python
注意：
	1、各个蓝本中，比如url.py、car.py中写的是各自模块的路由，然后统一在manage.py中注册
	2、创建某个模块的蓝本对象的时候，第一个参数的作用，是在蓝本之间跳转的时候，的一个标识。
		比如：car = Blueprint('car',__name__); -->存在于car.py模块中
		在另一个蓝本中，不用导入from car import car，就可以redirect(url_for('car.index'))
		可见：car并不是对象，而是蓝本管理的'car'标识，index是car.py模块中的视图函数  
	3、通过print(render_template('index.html')) --> 其中from flask import render_template
		index.html存在于templates目录下。
		可以从打印中看到，并不是return render_temlate('index.html',title='我是首页')是跳转到			index.html中的，而是把index.html模板拿过来，渲染，返回去浏览器的。
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
> 需要使用secret_key 进行加密
> 生成session所需要的加密种子
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
> ​	宏的导入和调用 from ... import ...
>
> ```python
> #注意：import form指的是macro form(参数)中的宏名称'form'，
> 	#python中是from 模块 import 方法
> {% from 'macrotest.html' import form %}
> {{ form('用户名：','text','username') }}
> {{ form('密码：','password','userpass') }}
> {{ form('','submit','submit','登录') }}
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



