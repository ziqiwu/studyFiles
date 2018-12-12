### 不记文档，白忙一场

#### 搭建环境

```python
第一步：创建虚拟环境
1、python -m pip install --upgrade pip   -->更新pip
2、pip install virtualenv   -->安装虚拟环境包
3、pip install virtualenvwrapper-win    -->安装虚拟环境管理包（Linux环境下使用virtualenvwrapper） 
4、设置workon_home环境变量   -->在系统变量里新建即可， 变量名：WORKON_HOME，变量值：创建虚拟环境的目      录。不需要添加PATH
5、mkvirtualenv testevn   -->创建虚拟环境
   (如果需要指定Python的版本，
   使用参数：--python=D:\ProgramData\Anaconda3\python.exe；
    如果需要使用公共的包，使用参数：--system-site-packages:)
6、激活虚拟环境  -->workon testevn
7、查看现有的虚拟环境   -->workon
8、退出虚拟环境    -->deactivate
9、删除虚拟环境    -->rmvirtualenv testevn
第二步：安装flask
1、mkvirtualenv flaskenv
2、workon flaskenv
3、pip install flask  -->安装flask
第三步：创建工程
1、桌面新建空文件夹，起名firstFlask。
2、打开pycharm，file，New Project，点击Location三个点找到桌面的firstFlask文件夹，Project 			Interpreter，Existing interpreter，点击三个点，Interpreter点击三个点，找到						D:\workon_home\env1\Scripts\python.exe(即自己新建的虚拟环境)，make available to all 			projects，create，open in a new window
3、右键项目firstFlask，new，python file，Name写manage.py。(至此搭建完成)  
```

#### 入门

```python
一、概念
1、flask概念： 是一个非常小 轻量级的WEB框架  只提供了一个强劲的核心 其它功能都需要通过第三方扩展去实现
2、模板引擎： jinja2
3、完整运行flask
    from flask import Flask
    app = Flask(__name__) #创建flask的实例

    # @app.route('/') #路由  访问地址 127.0.0.1:5000 或  127.0.0.1:5000/
    # @app.route('/index') #路由 访问地址 127.0.0.1:5000/index
    @app.route('/index/') #路由 访问地址 127.0.0.1:5000/index 或 27.0.0.1:5000/index/
    def index():
        return 'Hello Flask'

    if __name__ == '__main__':
        app.run()#执行flask的运行   如果更换为调试模式，即修改代码，不需要重启，则加参数debug=True
    请求地址为 http://127.0.0.1:5000
4、路由地址传参
	(1) 无参路由
        @app.route('/') #路由  访问地址 127.0.0.1:5000 或  127.0.0.1:5000/
        def index():
        return 'Hello Flask'
    (2) 带一个参数的路由地址
        @app.route('/arg/<age>/') #127.0.0.1:5000/arg/18
        def arg(age):
            return '参数的值为{}'.format(age)
    (3) 传递多个参数
    	#传递多个参数
        #使用路由地址分隔符 进行分隔
        @app.route('/args/<name>/<age>/') #http://127.0.0.1:5000/args/zhangsan/18/
        #http://127.0.0.1:5000/args/zhangsan_18/
        @app.route('/args/<name>_<age>/')
        def args(name,age):
            return '我叫{} 我今年{}岁了'.format(name,age)
    (4) 限制参数的类型 手动
    	from flask import abort
        #传递参数限制值的类型  手动
        #http://127.0.0.1:5000/args/zhangsan_18/
        @app.route('/args/<name>_<age>/')
        def args(name,age):
            try:
                age = int(age) #限制类型转换为整形
            except:
                # raise ValueError
                abort(404) #抛出404
            return '我叫{} 我今年{}岁了'.format(name,age)
    (5)  限制参数的类型 自动
    	#传递参数 通过路由限制类型
        @app.route('/args/<name>_<int:age>/') #限制参数类型为 int
        @app.route('/args/<name>_<float:age>/') #限制参数类型为float
        @app.route('/args/<name>_<age>/') #默认，限制参数类型为string
        @app.route('/args/<name>_<string:age>/') #限制参数类型为string 默认值就是
        @app.route('/args/<name>_<path:age>/') #将路由地址age后面的所有参数 都认为是当前age的参数			值,/分隔符不再作为分隔符使用  比如：http://127.0.0.1:5000/args/zhangsan_18/12/abc/2/
        def args(name,age):
            print(type(age))
            return '我叫{} 我今年{}岁了'.format(name,age)

        str='a'
        del str
        print(str)  #<class 'str'>
5、response 响应
	(1) 返回一个字符串进行响应 return
		@app.route('/response/')
        def res():
            return '我是响应'
    (2) 响应内容和状态码
    	@app.route('/response/')
        def res():
            return '我是响应',404#响应内容和状态码
    (3) 使用系统的 make_response进行响应
    	@app.route('/response/')
        def res():
            res = make_response('我是响应',404) #设置cookie的时候使用 当前的make_response  其它情都				是响应一个html页面
            return res
     注意：
        1. 路由地址结尾/建议都加上 因为在访问有/作为结尾的地址的时候 浏览器会自动帮你添加
        2. 路由传参写在<参数名称> 参数的名称为 形参名. 在flask中 路由地址可以相同如果同为一个方法请求			（如：GET） 则会按照顺序执行，执行在上方的视图函数.视图函数不可以重名
6、flask启动的参数
	参数 			 参数说明
	debug           开启调试模式 默认为False
     host           主机
     port           端口号
     threaded       多线程 默认flase
     比如：app.run(host='0.0.0.0',port=5001,threaded=True,debug=True)
7、请求对象
	(1)概念：request是根据每一个用户的请求 对应创建的request对象，是由flask创建。在使用的时候，只需要			导入就可以
	(2)列举：
    	request属性
        1. url  请求的完整的url  127.0.0.1:5000/request/canshu/?name=zhangsan&age=lisi&age=wangwu 
        2. base_url  去掉get传参的url        http://127.0.0.1:5005/request/canshu/
        3. host_url   主机和端口号的url      http://127.0.0.1:5005/
        4. path     请求的路由地址           /request/canshu/
        5. method  请求的方式                GET
        6. args   获取get传参         
        	ImmutableMultiDict([('name', 'zhangsan'), ('age', 'lisi'),('age', 'wangwu')])
        7. args.getlist(key) 获取有相同key的get传参    getlist的参数为多个值的key['lisi','wangwu']
        8. form   获取表单传递过来的数据  request.form 获取POST传过来的参数ImmutableMultiDict([])
        9. files  获取文件上传的数据  ImmutableMultiDict([])
        10. headers 获取请求头信息    
        	User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:60.0)Gecko/20100101 							Firefox/60.0
            Accept-Language: en-GB,en;q=0.5
        11. cookies  获取多个cookie   											
        	csrftoken=AA7yeEKEiY4DJtbB2mYc4Hjckyb14cY5MDFImfQ4yEUgVW4WNh9rHj3yCGZlZ47D
	（3）示例：
    	#请求对象
        from  flask import request
        @app.route('/request/<arg>/')
        def Request(arg):
            # print('请求的完整的url',request.url)
            # print('去掉get传参的url',request.base_url)
            # print('主机和端口号的url',request.host_url)
            # print('请求的路由地址',request.path)
            # print('请求的方式',request.method)
            # print('获取get传参',request.args)
            # print('获取get传参',request.args.get('age'))
            # print('获取get传参',request.args['age'])
            # print('获取get传参',request.args.get('name'))
            # print('获取get传参使用getlist 返回name键的多个值',request.args.getlist('name'))
            # print('获取表单传递过来的数据',request.form)
            # print('files',request.files)
            # print('获取请求头信息',request.headers)
            # print('获取多个cookie',request.cookies)
            # print('获取传递的json数据',request.json)
            return 'request请求对象'
8、abort终止
	(1)概念：在代码运行的过程中，出现任何的异常可以使用abort 抛出标准的http状态码 终止当前程序的执行			和raise类似，抛出问题的代码的上方都正常执行，下面不再执行
	(2)错误的捕获(自定义错误页面)
        #捕获http错误
        @app.errorhandler(404)
        def page_not_found(e):
            return '错误信息为{}'.format(e)

        #捕获http错误
        @app.errorhandler(500)
        def page_not_found(e):
            return '错误信息为{}'.format(e)
	(3)abort示例(注意：返回的404页面是上面自定义的404返回内容)
    	from flask import abort
        @app.route('/')
        def idnex():
            abort(404)
            下面代码不再执行
```

