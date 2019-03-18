### 不记文档，白忙一场

------

#### urllib

##### urllib概念

> ```python
> urllib是一个库，是一个模块，是python为我们提供的操作url的模块。
> python2系列的有urllib和urllib2
> python3系列的只有urllib，
> ```

##### urllib.request属性方法

> ​	1、urllib.request.urlopen(url, data)
>
> ```python
> urllib.request:发送请求和获取响应
> 	友情提醒1：py程序爬取网页时，首先将fiddler关闭
> 	友情提醒2：网址要写全，http://www.baidu.com/,最后一个斜线不要忘记
> 	如果有data，那么说明这个请求是post请求，需要带data过去，如果没有data，就是get请求，需要将		参数拼接到url的后面	
> ```
> ​	2、urlretrieve
>
> ```python
> 使用urllib.request.urlretrieve方法可直接下载网上资源。
> urllib.request.urlretrieve(url, filename)   下载网页或者图片
> '''
> import urllib.request
> image_url = 'http://c.hiphotos.baidu.com/baike/pic/item/023b5bb5c9ea15ce6cb6231dbe003af33a87b24e.jpg'
> # 根据网址下载数据到相应的文件中。
> retrieve = urllib.request.urlretrieve(image_url, filename='meiyanfang.jpg')
> print(retrieve)
> '''
> ```
>
> ​	3、urllib.request中Handler处理器
>
> ```python
> 1、定义
> 　　自定义的urlopen()方法,urlopen()方法是一个特殊的opener(模块已定义好),不支持代理等功能,通过Handler处理器对象来自定义opener对象
> 2、常用方法
> 　　1、build_opener(Handler处理器对象) ：创建opener对象
> 　　2、opener.open(url,参数)
> 3、使用流程
> 　　1、创建相关的Handler处理器对象
> 　　　　http_handler = urllib.request.HTTPHandler()
> 　　2、创建自定义opener对象
> 　　　　opener = urllib.request.build_opener(http_handler)
> 　　3、利用opener对象打开url
> 　　　　req = urllib.request.Request(url,headers=headers)
> 　　　　res = opener.open(req)
> 　　　　result = res.read().decode("utf-8")
> 4、Handler处理器分类
> 　　1、HTTPHandler() ：没有任何特殊功能
> 　　2、ProxyHandler(普通代理)
> 　　　　代理: {"协议":"IP地址:端口号"}
> 　　3、ProxyBasicAuthHandler(密码管理器对象) ：私密代理
> 　　4、HTTPBasicAuthHandler(密码管理器对象) : web客户端认证
> 5、密码管理器对象作用
> 　　1、私密代理
> 　　2、Web客户端认证
> 　　3、程序实现流程
> 　　　　1、创建密码管理器对象
> 　　　　　　pwdmg = urllib.request.HTTPPasswordMgrWithDefaultRealm()
> 　　　　2、把认证信息添加到密码管理器对象
> 　　　　　　pwdmg.add_password(None,webserver,user,passwd)
> 　　　　3、创建Handler处理器对象
> 　　　　　　1、私密代理
> 　　　　　　　　proxy = urllib.request.ProxyAuthBasicHandler(pwdmg)
> 　　　　　　2、Web客户端
> 　　　　　　　　webbasic = urllib.request.HTTPBasicAuthHandler(pwdmg)
> ```

##### urllib.parse属性方法

> ```python
> urllib.parse：处理url的
> 	1、urllib.parse.urlencode()  下面将post请求再来说这个函数
> 	2、urllib.parse.quote()  url编码 ，在url中只能出现-_.a-z  中文
> 		http://www.baidu.com?username=狗蛋&password=123
> 		url编解码查看网页
> 		http://tool.chinaz.com/tools/urlencode.aspx
> 	3、urllib.parse.unquote()  url解码
> 	注意：不论是get还是Post，参数中有中文，才会用到url编码解码
> ```

##### response属性方法

> ```python
> response对象
> 	1、read():读取的是二进制数据
> 	2、字符串类型和字节类型
> 		字符串 -> 字节：编码  encode()
> 		字节 -> 字符串：解码  decode()
> 	3、readline():读取一行
> 	4、readlines()：读取全部，返回一个列表
> 	5、getcode()：状态码
> 	6、geturl()：获取url
> 	7、getheaders():响应头信息，列表里面有元组
> ```

##### json的使用

> ```python
> 将json数据写入文件中：
> # 注意：这行必须注释掉，文件中才有数据。
> # print(response.read().decode('utf-8'))  因为这儿指针已经动了
> with open('ret.json', 'wb') as file:
>     file.write(response.read())
>     
> #注意：这样我们发现ret.json中的数据是人类看不懂的内容。
> #将json转换成人类可读的内容再进行写入。
> json_string = response.read().decode('utf-8')
> import json
> # 将json字符串转换为json对象
> json_obj = json.loads(json_string)
> # 将json对象变成普通字符串，并且禁止使用默认的ascii编码方式
> json_string = json.dumps(json_obj, ensure_ascii=False)
> 
> # print(response.read().decode('utf-8'))
> # 二进制模式下无法修改编码方式，所以把b去掉
> with open('ret.json', 'w', encoding='utf-8') as file:
>     file.write(json_string)
> 
> ```

##### headers设置

> ```python
> 有时光指定User-Agent是不够的，甚至需要将整个headers都设置一下。
> 注意在设置headers的时候，千万不要设置Content-Length: 121，Accept-Encoding: gzip, deflate这些参数。
> ```

##### 没有分页的ajax实现

> ```python
> 1、分析豆瓣电影排行榜发现，排行榜没有分页，只要往下拉，就能自动刷出新的电影来，这是典型的ajax请求。
> 分析发现豆瓣电影通过ajax的get请求实现了这一功能。
> 2、肯德基官网的店铺分页就是ajax post实现的。
> ```
>
> ​	豆瓣：
>
> ```python
> # 爬取豆瓣动作电影，没有分页，一直往下翻的效果。
> from urllib import request, parse
> import ssl
> 
> ssl._create_default_https_context = ssl._create_unverified_context
> 
> url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
> 
> page = int(input('请输入您想要第几页电影：'))
> 
> data = {
>     'start': (page -1) * 20,
>     'limit': '20'
> }
> # 将data拼接为get请求的查询字符串
> data = parse.urlencode(data)
> url = url + data
> 
> headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
> # 构建request对象
> req = request.Request(url=url, headers=headers)
> response = request.urlopen(req)
> print(response.read().decode('utf-8'))
> ```
>
> ​	肯德基
>
> ```python
> from urllib import request, parse
> 
> url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
> 
> data = {
> 'cname': '深圳',
> 'pid': '',
> 'pageIndex':'2',
> 'pageSize': '10'
> }
> 
> # 转换格式
> data = parse.urlencode(data).encode('utf-8')
> 
> response = request.urlopen(url=url, data=data)
> print(response.read().decode('utf-8'))
> ```

##### 封装函数抓取百度贴吧

> ```python
> from urllib import request, parse
> import os
> import ssl
> 
> # 解决ssl证书问题
> ssl._create_default_https_context = ssl._create_unverified_context
> # 处理url，返回request
> 
> 
> 
> def handle_url(url, page, name):
>     # 拼接url
>     pn = (page -1) * 50
>     data = {
>         'kw': name,
>         'pn': pn
>     }
>     data = parse.urlencode(data)
>     url = url + data
>     req = request.Request(url=url)
>     return req
> 
> 
> # 负责下载动作
> def download(req, page):
>     response = request.urlopen(req)
>     dirname = 'tieba'
>     filename = '第' + str(page) + '页.html'
>     filepath = os.path.join(dirname, filename)
>     with open(filepath, 'wb') as fp:
>         fp.write(response.read())
> 
> 
> def main():
>     name = input('请输入要爬取的贴吧名：')
>     start_page = int(input('请输入起始页码：'))
>     end_page = int(input('请输入起始页码：'))
>     url = 'https://tieba.baidu.com/f?ie=utf-8&'
> 
>     # 循环下载每一页的内容
>     for page in range(start_page, end_page+1):
>         # 封装函数获取request对象
>         req = handle_url(url, page, name)
>         print('开始下载第%d页'%page)
>         # 封装函数执行下载功能
>         download(req, page)
>         print('结束下载第%d页' % page)
> 
> 
> 
> if __name__ == '__main__':
>     main()
> ```

##### 百度翻译(手机端和PC端)

> ​	第一：
>
> ```python
> from urllib import request, parse
> 
> 
> url = 'http://fanyi.baidu.com/sug'
> 
> headers = {
>     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
> }
> 
> # 构造post请求的data
> word = input('请输入您要查询的单词：')
> data = {
>     'kw': word,
> }
> data = parse.urlencode(data).encode('utf-8')
> 
> req = request.Request(url=url, headers=headers, data=data)
> 
> response = request.urlopen(req)
> print(response.read().decode('utf-8'))
> ```
>
> ​	第二：
>
> ```python
> #尝试换另一个地址（http://fanyi.baidu.com/v2transapi ）来提交post请求。发现会一直报997的错误。原因是这个地址提交的form表单数据中，有两个是js计算出来的。手机版的百度翻译没有这两个数据 ，可以正常提交。
> 
> 
> from urllib import request, parse
> 
> # 手机版百度翻译
> url = 'http://fanyi.baidu.com/basetrans'
> 
> headers = {
> # 手机浏览器的UA
>     "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
> }
> 
> # 构造post请求的data
> # word = input('请输入您要查询的单词：')
> data = {
>     'from': 'en',
>     'to': 'zh',
>     'query': 'love',
> }
> data = parse.urlencode(data).encode('utf-8')
> 
> req = request.Request(url=url, headers=headers, data=data)
> 
> response = request.urlopen(req)
> print(response.read().decode('utf-8'))
> ```

##### URLError和HttpError

> ​	概述：
>
> ```python
> HTTPError类是URLError类的子类。
> 
> 通过urllib发送请求的时候，有可能会发送失败，这个时候如果想让你的代码更加的健壮，可以通过try-except进行捕获异常，异常有两类，URLError\HTTPError。
> 
> 注意，urllib可以为我们处理重定向的页面（也就是3开头的响应码），100-299范围的号码表示成功，所以我们只能看到400-599的错误号码
> 
> 一般URLError错误可能由这些原因引起：没有网络连接，找不到指定的服务器，服务器连接失败等。
> 
> 为了让我们的代码更加健壮，我们可以尝试捕获可能出现的异常，比如：
> ```
>
> ​	代码：
>
> ```python
> import urllib.request, urllib.parse, urllib.error
> import ssl
> 
> # 解决ssl证书问题
> ssl._create_default_https_context = ssl._create_unverified_context
> 
> url = 'https://blog.csdn.net/blogdevteam/article/details/805290321'
> 
> try:
>     response = urllib.request.urlopen(url)
>     print(response.read().decode('utf-8'))
>     # 范围小的异常写在前面
> except urllib.error.HTTPError as e:
>     print(100)
>     print(e)
> # 范围大的异常写在后面
> except urllib.error.URLError as e:
>     print(200)
>     print(e)
> ```

##### cookie简单登录

> ​	概述：
>
> ```python
> weibo.cn
> 
> cookie是浏览器用来保持会话的机制。
> 
> 我们是通过先登录weibo.cn，然后访问登陆之后的页面，通过抓包将cookie抓取到，然后写程序，将这个cookie复制过去，在程序中访问登录之后的页面即可。
> 
> ```
>
> ​	代码：
>
> ```python
> import urllib.request
> 
> url = 'https://weibo.cn/6388179289/info'
> headers = {
> 	'Host': 'weibo.cn',
> 	'Connection': 'keep-alive',
> 	'Upgrade-Insecure-Requests': '1',
> 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
> 	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
> 	'Referer': 'https://weibo.cn/',
> 	# 'Accept-Encoding': 'gzip, deflate, br',
> 	'Accept-Language': 'zh-CN,zh;q=0.9',
> 	'Cookie': '_T_WM=920b3a13d4ce0e96b7095bae150f49a4; SUB=_2A253RNk_DeRhGeBN41oQ9yfOwzWIHXVUxud3rDV6PUJbkdAKLRXFkW1NRAKzwQTU6AzdbUjwMMpXvo7AGzssYLlI; SUHB=0TPVRtulUlEGQH; SCF=AjJAqLCK3WtcHNrB_BDm-MEyfxO0_WBywpu0iVPhWTZ5zaWLZ7rKradvhU-49lyGcv9j3VXLgvd5k3XTUUnMpBI.; SSOLoginState=1514187119',
> 
> 
> }
> request = urllib.request.Request(url=url, headers=headers)
> 
> response = urllib.request.urlopen(request)
> 
> # print(response.read().decode('gbk'))
> with open('weibo.html', 'wb') as fp:
> 	fp.write(response.read())
> ```

##### Handler处理器、自定义Opener

> ​	概述
>
> ```python
> （1）前面学习的urllib.request.urlopen()很简单的一个获取网页的函数，但是它不能自己构建请求头
> （2）引入了request对象，request = urllib.request.Request(url=url, headers=headers),它的高级之	处就是可以自己定制请求头
> （3）request对象不能携带cookie，也不能使用代理，所以引入了Handler处理器、自定义Opener
> ```
>
> ​	代码
>
> ```python
> import urllib.request
> 
> # 首先创建一个handler对象
> handler = urllib.request.HTTPHandler()
> 
> # 创建opener对象
> opener = urllib.request.build_opener(handler)
> 
> # 构建请求对象
> url = 'http://www.baidu.com/'
> headers = {
> 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
> }
> request = urllib.request.Request(url=url, headers=headers)
> 
> response = opener.open(request)
> 
> print(response.read().decode('utf-8'))
> ```

##### 代理

> ​	概述
>
> ```python
> 代理服务器需要购买的，当然也有免费的，用免费的进行演示
> 	http://www.kuaidaili.com/
> 	http://www.xicidaili.com/
> 
> ```
>
> ​	本地实现
>
> ```python
> 本地浏览器配置代理步骤
> 	设置==》高级==》打开代理设置==》链接==》局域网设置==》代理服务器==》选中为LAN配置、跳过xxx，将代理服务器的地址和端口号写入，保存即可，百度访问ip，查看ip地址
> 代码配置代理
> 	【注】访问的网址是http时候，你用http代理服务器，访问https的时候，你用https代理服务器
> ```
>
> ​	代码实现
>
> ```python
> import urllib.request
> 
> 
> url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'
> headers = {
> 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
> }
> request = urllib.request.Request(url=url, headers=headers)
> '''
> response = urllib.request.urlopen(request)
> 
> with open('ip.html', 'wb') as fp:
> 	fp.write(response.read())
> '''
> 
> # 配置代理
> handler = urllib.request.ProxyHandler({'http': '101.205.84.107:808'})
> # 创建opener
> opener = urllib.request.build_opener(handler)
> # 发送请求
> response = opener.open(request)
> with open('ip_daili.html', 'wb') as fp:
> 	fp.write(response.read())
> ```

##### cookie库

> ​	概述
>
> ```python
> 通过cookiejar库，创建一个handler，然后根据这个handler创建一个opener，然后通过这个opener去登录你的微博，然后再opener去访问登录后的页面即可，这个handler会自动的保存登录之后的cookie。
> ```
>
> ​	代码
>
> ```python
> import urllib.request
> import http.cookiejar
> import urllib.parse
> 
> # 创建一个cookiejar对象
> cookie = http.cookiejar.CookieJar()
> # 根据cookiejar对象创建handler对象
> handler = urllib.request.HTTPCookieProcessor(cookie)
> # 根据handler对象创建一个opener对象
> opener = urllib.request.build_opener(handler)
> 
> # 通过代码模拟登录
> post_url = 'https://passport.weibo.cn/sso/login'
> data = {
> 	'username': '18676689715',
> 	'password': 'xuke666',
> 	'savestate': '1',
> 	'r': 'http://weibo.cn/',
> 	'ec': '0',
> 	'pagerefer': '',
> 	'entry': 'mweibo',
> 	'wentry': '',
> 	'loginfrom': '',
> 	'client_id': '',
> 	'code': '',
> 	'qq': '',
> 	'mainpageflag': '1',
> 	'hff': '',
> 	'hfp': '',
> }
> data = urllib.parse.urlencode(data).encode('utf-8')
> headers = {
> 	'Host': 'passport.weibo.cn',
> 	'Connection': 'keep-alive',
> 	'Origin': 'https://passport.weibo.cn',
> 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
> 	'Content-Type': 'application/x-www-form-urlencoded',
> 	'Accept': '*/*',
> 	'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
> 	'Accept-Language': 'zh-CN,zh;q=0.9',
> }
> 
> # 构建请求
> request = urllib.request.Request(url=post_url, data=data, headers=headers)
> # 发送请求
> response = opener.open(request)
> 
> # print(response.read().decode('utf-8'))
> 
> url = 'https://weibo.cn/6388179289/info'
> headers1 = {
> 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
> }
> request = urllib.request.Request(url=url, headers=headers1)
> # 因为opener已经保存了登录之后的cookie信息，所以再使用opener去访问其它的页面
> 
> response = opener.open(request)
> print(response.read().decode('utf-8'))
> ```

