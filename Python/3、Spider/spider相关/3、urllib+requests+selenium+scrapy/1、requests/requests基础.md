### 不记文档，白忙一场

------

#### ***面试***

> ```python
> 1> requests的作者并没有自己造轮子，而完全是对urllib3的封装。
> 2> 相比urllib
> 	1 方法简单 
> 		r = requests.get(url=url)
> 	2 中文参数不需要编码 
> 		r = requests.get(url=url, params=data, headers=headers)
> 		r = requests.post(url=url, data=data)
> 	3 返回内容格式自动转换
> 		print(r.text) # 响应的字符串方式
> 		print(r.json()) # 自动 将返回的json解码。
> 	4 使用代理更方便
> 		proxy = {
> 			'https': '114.237.147.155:9999'
> 		}
> 		r = requests.get(url=url, params=data, headers=headers, proxies=proxy)
> 	5 使用会话更方便
> 		session = requests.Session()
> 		session.post(url=login_url, data=data, headers=headers)
> 	6 下载网上资源更方便
> 		res = requests.get(url=url, headers=headers)
> 		# content返回的是bytes型也就是二进制的数据。
> 		html = res.content
> ```

#### 0、概述

> ```python
> requests的作者并没有自己造轮子，而完全是对urllib3的封装。
> requests比urllib要好用的多，所以以后建议都用requests。
> 官方文档【中文】：http://cn.python-requests.org/zh_CN/latest/
> ```

#### 1、安装

> ```python
> pip install requests -i https://pypi.douban.com/simple
> ```

#### 2、GET请求

> #### 代码使用：
>
> ```python
> import requests
> 
> url = 'https://www.baidu.com/'
> 
> r = requests.get(url=url)
> 
> print(r.text)
> # 查看网页编码
> print(r.encoding)
> # 设置网页编码方式
> r.encoding = 'utf-8'
> 
> # 重新查看网页
> # print(r.text)
> 
> # 带参数的get请求 ，以baidu搜索为例
> url= 'https://www.baidu.com/s'
> 
> # 要搜索的关键字，是一个字典。不需要跟以往一样把中文编码
> data = {
>     'wd': '日本'
> }
> # 还可以定制头部, 也是个字典
> headers = {
>     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
> }
> 
> r = requests.get(url=url, params=data, headers=headers)
> print(r.text)
> ```
>
> #### 响应的属性
>
> ```python
>   r.text       	响应字符串类型
>   r.encoding   	编码方式   
>   r.url        	请求的url 
>   r.content    	响应的字节类型
>   r.status_code	响应状态码  
>   r.headers    	响应的头部信息
> ```

#### 3、POST请求

> ```python
> import requests
> 
> 
> url = 'http://fanyi.baidu.com/sug'
> 
> data = {
>     'kw': 'hello'
> }
> 
> r = requests.post(url=url, data=data)
> # 响应的字符串方式
> print(r.text)
> # 自动 将返回的json解码。
> print(r.json())
> ```

#### 4、使用代理

> ```python
> import requests
> 
> url= 'https://www.baidu.com/s'
> 
> data = {
>     'wd': 'ip'
> }
> 
> headers = {
>     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
> }
> # 代理也是一个字典。
> proxy = {
>     'https': '114.237.147.155:9999'
> }
> # 只需要传入proxies参数即可。
> r = requests.get(url=url, params=data, headers=headers, proxies=proxy)
> 
> with open('daili.html', 'w', encoding='utf-8') as fp:
>     fp.write(r.text)
> ```

#### 5、会话

> #### 概述：
>
> ```python
> requests中使用session跟踪会话，session会自动记录cookie，相当于urllib和cookiejar结合。
> 在requests中使用session跟踪会话非常简单：
> ```
>
> #### 代码：
>
> ```python
> import requests
> 
> # session自动记录cookie
> session = requests.Session()
> 
> login_url = 'https://passport.weibo.cn/sso/login'
> 
> data = {
>     'username': '18676689715',
>     'password': 'xuke666',
>     'savestate': '1',
>     'r': 'http://weibo.cn/',
>     'ec': '0',
>     'pagerefer': '',
>     'entry': 'mweibo',
>     'wentry': '',
>     'loginfrom': '',
>     'client_id': '',
>     'code': '',
>     'qq': '',
>     'mainpageflag': '1',
>     'hff': '',
>     'hfp': '',
> }
> headers = {
>     'Host': 'passport.weibo.cn',
>     'Connection': 'keep-alive',
>     'Origin': 'https://passport.weibo.cn',
>     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
>     'Content-Type': 'application/x-www-form-urlencoded',
>     'Accept': '*/*',
>     'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
>     'Accept-Language': 'zh-CN,zh;q=0.9',
> }
> 
> session.post(url=login_url, data=data, headers=headers)
> 
> headers = {
> 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
> }
> url = 'https://weibo.cn/2952685222/info'
> # 访问个人信息页面
> r = session.get(url=url, headers=headers)
> 
> print(r.text)
> ```

#### 6、下载视频

> ```python
> import requests
> 
> url = 'http://vf1.mtime.cn/Video/2015/03/20/mp4/150320094140850937_480.mp4'
> headers = {
> 	'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
> }
> 
> res = requests.get(url=url, headers=headers)
> # content返回的是bytes型也就是二进制的数据。
> html = res.content
> 
> with open('1.mp4', 'wb') as fp:
> 	fp.write(html)
> ```
>
> 