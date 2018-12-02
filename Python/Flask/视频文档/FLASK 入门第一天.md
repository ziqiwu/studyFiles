## FLASK 入门第一天

#### 工作方式为

M   模型  负责数据的操作

V    视图  负责业务逻辑的处理 

T    模板  渲染模板

#### 网站架构

1. B/S

   浏览器与服务器端

2. C/S

   客户端与服务器端

**flask概念：** 是一个非常小 轻量级的WEB框架  只提供了一个强劲的核心 其它功能都需要通过第三方扩展去实现

**模板引擎：** jinja2

**安装：**   sudo pip3 install flask

## 一、完整运行的flask

**实例**

```python
from flask import Flask
app = Flask(__name__) #创建flask的实例

# @app.route('/') #路由  访问地址 127.0.0.1:5000 或  127.0.0.1:5000/
# @app.route('/index') #路由 访问地址 127.0.0.1:5000/index
@app.route('/index/') #路由 访问地址 127.0.0.1:5000/index 或 27.0.0.1:5000/index/
def index():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run()#执行flask的运行
```

**请求地址为 http://127.0.0.1:5000**



## 二、路由地址传参问题

#### (1) 无参路由

```python
@app.route('/') #路由  访问地址 127.0.0.1:5000 或  127.0.0.1:5000/
def index():
    return 'Hello Flask'
```

#### (2) 带一个参数的路由地址

```python
#带一个参数的路由地址
@app.route('/arg/<age>/') #127.0.0.1:5000/arg/18
def arg(age):
    return '参数的值为{}'.format(age)
```

#### (3) 传递多个参数

```python
#传递多个参数
#使用路由地址分隔符 进行分隔
@app.route('/args/<name>/<age>/') #http://127.0.0.1:5000/args/zhangsan/18/
#http://127.0.0.1:5000/args/zhangsan_18/
@app.route('/args/<name>_<age>/')
def args(name,age):
    return '我叫{} 我今年{}岁了'.format(name,age)
```

#### (4) 限制参数的类型 手动

```python
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
```

#### (5)  限制参数的类型 自动

```python
#传递参数 通过路由限制类型
@app.route('/args/<name>_<int:age>/') #限制参数类型为 int
@app.route('/args/<name>_<float:age>/') #限制参数类型为float
@app.route('/args/<name>_<age>/') #限制参数类型为float
@app.route('/args/<name>_<string:age>/') #限制参数类型为字符串 默认值就是
@app.route('/args/<name>_<path:age>/') #限制参数类型为float 将路由地址age后面的所有参数 都认为是当前age的参数值 /分隔符不再作为分隔符使用
def args(name,age):
    print(type(age))
    return '我叫{} 我今年{}岁了'.format(name,age)

str='a'
del str
print(str)  #<class 'str'>
```

## 三、response 响应

#### (1) 返回一个字符串进行响应 return

```python
@app.route('/response/')
def res():
    return '我是响应'
```

#### (2) 响应内容和状态码

```python
@app.route('/response/')
def res():
    return '我是响应',404#响应内容和状态码
```

#### (3) 使用系统的 make_response进行响应

```python
@app.route('/response/')
def res():
    res = make_response('我是响应',404) #设置cookie的时候使用 当前的make_response  其它情况都是响应一个html页面
    return res
```

**注意：**

1. 路由地址结尾/建议都加上 因为在访问有/作为结尾的地址的时候 浏览器会自动帮你添加
2. 路由传参写在`<参数名称>` 参数的名称为 形参名
	. 在flask中 路由地址可以相同  如果同为一个方法请求（如：GET） 则会按照顺序执行，执行在上方的视图函数.  视图函数 不可以重名										



## 四、flask启动的参数

#### app.run的参数

| 参数     | 参数说明                 |
| -------- | ------------------------ |
| debug    | 开启调试模式 默认为False |
| host     | 主机                     |
| port     | 端口号                   |
| threaded | 多线程 默认flase         |

>app.run(host='0.0.0.0',port=5001,threaded=True,debug=True)

## 五、请求对象

**概念：** request是根据每一个用户的请求 对应创建的request对象  是由flask创建 在使用的时候 只需要导入就可以

**导入**

from  flask import request

> 127.0.0.1:5000/request/canshu/?name=zhangsan&age=lisi&age=wangwu

**request属性**

1. url  请求的完整的url 

2. base_url  去掉get传参的url     http://127.0.0.1:5005/request/canshu/

3. host_url   主机和端口号的url  http://127.0.0.1:5005/

4. path     请求的路由地址           /request/canshu/

5. method  请求的方式               GET

6. args   获取get传参         ImmutableMultiDict([('name', 'zhangsan'), ('age', 'lisi'), ('age', 'wangwu')])

7. args.getlist(key) 获取有相同key的get传参    getlist的参数为 多个值的key  ['lisi', 'wangwu']

8. form   获取表单传递过来的数据  request.form 获取POST传过来的参数      ImmutableMultiDict([])

9. files  获取文件上传的数据                               ImmutableMultiDict([])

10. headers 获取请求头信息    User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0

    Accept-Language: en-GB,en;q=0.5

11. cookies  获取多个cookie   csrftoken=AA7yeEKEiY4DJtbB2mYc4Hjckyb14cY5MDFImfQ4yEUgVW4WNh9rHj3yCGZlZ47D

## 六、abort 终止

在代码运行的过程中  出现任何的异常 可以使用abort 抛出标准的http状态码 终止当前程序的执行 和raise类似  抛出问题的代码的上方都正常执行  下面不再执行

**导入**

from flask import abort

```python
@app.route('/')
def idnex():
    abort(404)
    下面代码不再执行
```

**错误的捕捉**

```python
#捕获http错误
@app.errorhandler(404)
def page_not_found(e):
    return '错误信息为{}'.format(e)

#捕获http错误
@app.errorhandler(500)
def page_not_found(e):
    return '错误信息为{}'.format(e)
```

## 七、会话控制 COOKIE SESSION

#### 为什么会有cookie和session？

http协议为无状态协议 

#### 什么是http协议？

超文本传输协议

### (1) cookie 

**主体结构**

```python
Response.set_cookie(
	key,
    value,
    max_age=None,设置过期时间 单位为秒
    expires=None,以秒为单位的寿命
    path = '/'
)
```

#### 设置cookie  存活时间为当期浏览结束

```python
#设置cookie 不设置过期时间
@app.route('/set_cookie/')
def setCookie():
    res = make_response('设置cookie')
    res.set_cookie('name','zhangsan')
    return res
```

#### 设置cookie并设置过期时间

```python
#设置cookie 并设置过期时间
@app.route('/set_cookie/')
def setCookie():
    res = make_response('设置cookie')
    # res.set_cookie('name','zhangsan',max_age=60) #设置当期cookie存活时间为1分钟
    life_time = time.time()+60
    res.set_cookie('name','zhangsan',expires=life_time) #设置当期cookie存活时间为1分钟
    return res
```

#### 获取cookie

```python
#查看cookie
@app.route('/get_cookie/')
def get_cookie():
    myCookie = request.cookies #获取所有cookie
    print(myCookie)
    return 'key为name的值为{}'.format(myCookie.get('name'))
```

#### 删除cookie

```python
#删除cookie
@app.route('/del_cookie/')
def del_cookie():
    res = make_response('删除cookie')
    res.delete_cookie('name') #删除key为name的cookie
    return res
```

### (2) session

服务器要识别来自同一个用户的请求  依赖与cookie  访问者在第一次请求 服务器的时候 服务器会在其cookie中 设置唯一的sessionId值  服务器就可以通过唯一的sessionid来去区分不同用户的请求(访问)

需要使用secret_key 进行加密

生成session所需要的加密种子
app.config['SECRET_KEY']='abcdef'

**导入**

from flask import session

#### 设置session  默认存活为当期浏览会话结束

```python
#设置session
@app.route('/set_session/')
def set_session():
    session['uid'] = '1'
    return '设置session'
```

#### 设置sesison存活时间

```python
#设置session 设置过期时间
@app.route('/set_session/')
def set_session():
    #开启session持久化存储
    session.permanent = True
    #设置session存活时间为1分钟  如果不给当期的存活时间 则为1个月
    app.permanent_session_lifetime = timedelta(seconds=60) 
    session['uid'] = '1'
    return '设置session'
```

#### 获取session

```python
#获取session
@app.route('/get_session/')
def get_session():
    return 'uid的值为{}'.format(session.get('uid'))
```

#### 删除session

```python
#删除session
@app.route('/del_session/')
def del_session():
    #删除key为uid的session值
    # session.pop('uid')
    #删除所有session
    session.clear()
    return '删除成功'
```





























































































