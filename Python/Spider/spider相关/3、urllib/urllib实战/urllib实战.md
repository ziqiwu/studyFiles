### 不记文档，白忙一场

------

#### 注意

> ```python
> #注意：Handler处理器、自定义Opener是为了解决：
> 	'''
> 		request对象不能携带cookie，也不能使用代理，所以引入了Handler处理器、自定义Opener
> 		代码的话参考，下面的需要cookie携带登录信息，和post、get中的代理ProxyHandler
> 	'''
> #注意：豆瓣的这个请求，返回的是json字符串，是ajax请求的
> #注意：parse使用，request使用
> #注意：异常捕获
>     '''
>         from urllib import request,parse
>         from urllib.error import URLError
> 
>         url = 'https://www.baidu.com/afsdasdgfa?rsv_idx=1'
>         data = {
>             'name':'adf'
>         }
>         data = parse.urlencode(data).encode('utf-8')
>         try:
>             req = request.Request(url=url)
>             res = request.urlopen(req)
>         except URLError as e:
>             print(e)
>         print(res.read().decode('utf-8'))
>     '''
> #注意：可以用urllib.request的Handler处理器来请求url，代替request.openurl(url/req)
> 	'''
>         from urllib import request
> 
>         url = 'http://www.baidu.com/'
>         #创建handler对象
>         handler = request.HTTPHandler()
>         #使用handler创建opener
>         opener = request.build_opener(handler)
>         #创建request对象那个
>         req = request.Request(url=url)
>         res = opener.open(req)
>         print(res.read().decode('utf-8'))
> 	'''
> #注意：可以使用代理ip，其中ProxyHandler也是urllib.request中Handler处理器的一种
> 	'''
> 		from urllib import request
> 		import os
> 		
> 		url = 'http://www.baidu.com/s?wd=ip'
> 		#创建代理
> 		handler = request.ProxyHandler({'http':'125.46.0.62:53281'})
> 		opener = request.build_opener(handler)
> 		
> 		#也可以创建request.Request(url)的req对象，然后request.Request(req)
> 		req = request.Request(url=url)
> 		res = opener.open(req)
> 		with open(os.path.join('./tieba','baiduip.html'),'w',encoding='utf-8') as fp:
> 			fp.write(res.read().decode('utf-8'))
> 	'''
> #注意：解决ssl证书问题
> 	'''
> 		import ssl
> 		#解决ssl证书问题
> 		ssl._create_default_https_context = ssl._create_unverified_context
> 	'''
> ```

#### PSOT请求

> ​	百度翻译：
>
> ```python
> from urllib import request,parse
> 
> url = 'https://fanyi.baidu.com/sug'
> #构造post请求的data
> word = input('请输入')
> data = {
>     'kw':word
> }
> #注意：urlencode是url编码解码，encode是字符串和byte之间的编码解码
> data = parse.urlencode(data).encode('utf-8')
> res = request.urlopen(url=url,data=data)
> print(res.read().decode('utf-8'))
> #注意：返回的是unicode编码的内容，到http://tool.chinaz.com/tools/unicode.aspx站长工具，点击unicode编码到中文，即可看到内容
> ```
> ​	豆瓣：
>
> ```python
> from urllib import request,parse
> #注意:豆瓣的这个请求，返回的是json字符串，是ajax请求的
> #注意：json的使用
> #注意：parse的使用
> #注意：restful编程思想，get也有，post也可以访问
> #注意：异常捕获
>     '''
>         from urllib import request,parse
>         from urllib.error import URLError
> 
>         url = 'https://www.baidu.com/afsdasdgfa?rsv_idx=1'
>         data = {
>             'name':'adf'
>         }
>         data = parse.urlencode(data).encode('utf-8')
>         try:
>             req = request.Request(url=url)
>             res = request.urlopen(req)
>         except URLError as e:
>             print(e)
>         print(res.read().decode('utf-8'))
>     '''
> #注意：可以用urllib.request的Handler处理器来请求url，代替request.openurl(url/req)
> 	'''
>         from urllib import request
> 
>         url = 'http://www.baidu.com/'
>         #创建handler对象
>         handler = request.HTTPHandler()
>         #使用handler创建opener
>         opener = request.build_opener(handler)
>         #创建request对象那个
>         req = request.Request(url=url)
>         res = opener.open(req)
>         print(res.read().decode('utf-8'))
> 	'''
> #注意：可以使用代理ip，其中ProxyHandler也是urllib.request中Handler处理器的一种
> 	'''
> 		from urllib import request
> 		import os
> 		
> 		url = 'http://www.baidu.com/s?wd=ip'
> 		#创建代理
> 		handler = request.ProxyHandler({'http':'125.46.0.62:53281'})
> 		opener = request.build_opener(handler)
> 		
> 		#也可以创建request.Request(url)的req对象，然后request.Request(req)
> 		req = request.Request(url=url)
> 		res = opener.open(req)
> 		with open(os.path.join('./tieba','baiduip.html'),'w',encoding='utf-8') as fp:
> 			fp.write(res.read().decode('utf-8'))
> 	'''
> #注意：解决ssl证书问题
> 	'''
> 		import ssl
> 		#解决ssl证书问题
> 		ssl._create_default_https_context = ssl._create_unverified_context
> 	'''
> #post请求参数
> #page_limit=50
> #page_start=0
> url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8' 
> 
> page = int(input('您要获取第几页'))
> data = {
>     'page_limit':page*50,
>     'page_start':(page-1)*50,
> }
> 
> #进行转化
> data = parse.urlencode(data).encode('utf-8')##需要写data = parse.urlencode(data).encode('utf-8')，因为post请求参数是二进制，不是字符串
> 
> #或者创建request.Request(url,headers=headers2)对象，request.urlopen(req,data=data)
> res = request.urlopen(url,data=data)  #注意：有data是post请求，没有data参数是get请求
> #print(res.read().decode('utf-8'))
> 
> 
> import json
> json_string = res.read().decode('utf-8')
> json_obj = json.loads(json_string)  ########注意是loads不是load，是dumps不是dump
> json_string = json.dumps(json_obj,ensure_ascii=False)
> 
> 
> 
> #with open('recode_json.txt','wb') as fb:
> with open('recode_json.txt','w',encoding='utf-8') as fb:  
>     #注意:第二个参数是'w'
>     # fb.write(res.read()),可以对比'wb'写入之后的文档内容，看不懂的。和'w'之后能看懂的区别
>     fb.write(json_string)
>     fb.flush()
> ```

#### GET请求

> ```python
> from urllib import request,parse
> #注意：豆瓣的这个请求，返回的是json字符串，是ajax请求的
> #注意：parse使用，request使用
> #注意：异常捕获
>     '''
>         from urllib import request,parse
>         from urllib.error import URLError
> 
>         url = 'https://www.baidu.com/afsdasdgfa?rsv_idx=1'
>         data = {
>             'name':'adf'
>         }
>         data = parse.urlencode(data).encode('utf-8')
>         try:
>             req = request.Request(url=url)
>             res = request.urlopen(req)
>         except URLError as e:
>             print(e)
>         print(res.read().decode('utf-8'))
>     '''
> #注意：可以用urllib.request的Handler处理器来请求url，代替request.openurl(url/req)
> 	'''
>         from urllib import request
> 
>         url = 'http://www.baidu.com/'
>         #创建handler对象
>         handler = request.HTTPHandler()
>         #使用handler创建opener
>         opener = request.build_opener(handler)
>         #创建request对象那个
>         req = request.Request(url=url)
>         res = opener.open(req)
>         print(res.read().decode('utf-8'))
> 	'''
> #注意：可以使用代理ip，其中ProxyHandler也是urllib.request中Handler处理器的一种
> 	'''
> 		from urllib import request
> 		import os
> 		
> 		url = 'http://www.baidu.com/s?wd=ip'
> 		#创建代理
> 		handler = request.ProxyHandler({'http':'125.46.0.62:53281'})
> 		opener = request.build_opener(handler)
> 		
> 		#也可以创建request.Request(url)的req对象，然后request.Request(req)
> 		req = request.Request(url=url)
> 		res = opener.open(req)
> 		with open(os.path.join('./tieba','baiduip.html'),'w',encoding='utf-8') as fp:
> 			fp.write(res.read().decode('utf-8'))
> 	'''
> #get请求参数
> #page_limit=50&page_start=0
> url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&' 
> #参数应该是&page_limit=50&page_start=0
> 
> page = int(input('您要获取第几页'))
> data = {
>     'page_limit':page*50,
>     'page_start':(page-1)*50,
> }
> 
> #进行转化
> data = parse.urlencode(data)
> #注意：不能写data = parse.urlencode(data).encode('utf-8')，因为get请求拼接的是字符串
> url = url + data
> 
> #或者创建request.Request(url,headers=headers2)对象，request.urlopen(req)
> res = request.urlopen(url)
> print(res.read().decode('utf-8'))
> ```

#### 需要cookie携带登录信息

> ```python
> import os
> from urllib import request,parse
> from http import cookiejar
> #注意：如果只是访问一次需要cookie的页面，则只需要在headers中加入Cookie一项即可。
> 	'''
> 		headers = {
>     		'Host': 'weibo.com',
>     		'Connection': 'keep-alive',
>     		'Cache-Control': 'max-age=0',
>     		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 				(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
>     		'Upgrade-Insecure-Requests': '1',					'				
>     		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,
>     			image/webp,image/apng,*/*;q=0.8',
>     		'Accept-Language': 'zh-CN,zh;q=0.9',
>     		'Cookie': 'Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; 			
>     			login_sid_t=d39bff17f13559c4e7d0aa22caa2631e; cross_origin_proto=SSL; TC-				 V5-G0=ac3bb62966dad84dafa780689a4f7fc3; wb_view_log=1366*7681; '
> 		}
> 	'''
> #创建cookie对象
> cookie = cookiejar.CookieJar()
> #创建handler
> handler = request.HTTPCookieProcessor(cookie)
> #创建opener
> opener = request.build_opener(handler)
> 
> ###登录的地址框显示是https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=https%3A%2F%2Fpad.weibo.cn%2F
> ###其实https://passport.weibo.cn/signin/login就可以
> ###上面的是，显示登录页面的url地址
> ###通过fiddler抓包之后，可以看到登录页面的数据，提交给服务器的地址是：https://passport.weibo.cn/sso/login
> ###就相当于这个地址是form标签里面的action的值
> url = 'https://passport.weibo.cn/sso/login'
> data = {
>     'username': '18210553849',
>     'password': '1314shuangfeike',
>     'savestate': '1',
>     'r': '',
>     'ec': '1',
>     'pagerefer': '',
>     'entry': 'mweibo',
>     'wentry': '',
>     'loginfrom': '',
>     'client_id': '',
>     'code': '',
>     'qq': '',
>     'mainpageflag': '1',
>     'hff': '',
>     'hfp': ''
> }
> data = parse.urlencode(data).encode('utf-8')
> headers = {
>     'Host': 'passport.weibo.cn',
>     'Connection': 'keep-alive',
>     'Origin': 'https//passport.weibo.cn',
>     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, 		like Gecko) Chrome/63.0.3239.132 Safari/537.36',
>     'Content-Type': 'application/x-www-form-urlencoded',
>     'Accept': '*/*',
>     'Referer': 'https://passport.weibo.cn/signin/login',
>     'Accept-Language': 'zh-CN,zh;q=0.9'
> }
> 
> #注意：Accept-Encoding: gzip, deflate, br不要
> #注意：Content-Length: 154不要
> 
> #构建Request对象
> req = request.Request(url=url,headers=headers,data=data)
> res = opener.open(req)
> print(res.read().decode('utf-8'))
> 
> 
> ###访问个人详细地址
> ###一开始失败的原因是：
> ###访问详情页的地址写错了，写成了下面注释掉的地址，
> ###通过fiddler抓包之后，发现，现在的微博改了进入详情页的方式，改成了ajax请求，返回json字符串
> '''
>     GET https://m.weibo.cn/profile/info?uid=5803031936 HTTP/1.1
>     Host: m.weibo.cn
>     Connection: keep-alive
>     Accept: application/json, text/plain, */*
>     MWeibo-Pwa: 1
>     X-Requested-With: XMLHttpRequest
>     User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like 		Gecko) Chrome/71.0.3578.98 Safari/537.36
>     Referer: https://m.weibo.cn/profile/5803031936
>     Accept-Encoding: gzip, deflate, br
>     Accept-Language: en-US,en;q=0.9
>     Cookie: _T_WM=4427139fef71f7bd2d7345d518f51db0; 			
>     	SUB=_2A25xQsEjDeRhGeNG61ER8y_FyDqIHXVSzO9rrDV6PUJbkdANLRb8kW1NS5F20ncU9I1d9j-			oVpfiuyer1LGZ8sC6; SUHB=0IIV8AIZEmcaJC; 					
>     	SCF=AkMnxGoeIOxcby2tu6tWVaDC2hcRUaMnwMJ0iJaTHpJYeWcwP-
>     	302ibxUPCzaqVqSLGAsh3zD9bC8vn98PrKHHM.; SSOLoginState=1548136820; MLOGIN=1; XSRF-
>     	TOKEN=e6151f; WEIBOCN_FROM=1110006030; 
>     	M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D20000174
> '''
> # url2 = 'https://m.weibo.cn/profile/5803031936'
> url2 = 'https://m.weibo.cn/profile/info?uid=5803031936'
> headers2 = {
>     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, 
>     	like Gecko) Chrome/63.0.3239.132 Safari/537.36',
> }
> #构建Request对象
> req2 = request.Request(url=url2,headers=headers2)
> res2 = opener.open(req2)
> #print(res2.read().decode('utf-8'))
> with open(os.path.join('./tieba', 'login2.html'), 'w', encoding='utf-8') as fb:
>     fb.write(res2.read().decode('utf-8'))
> #注意：返回的是unicode编码的内容，到http://tool.chinaz.com/tools/unicode.aspx站长工具，点击unicode编码到中文，即可看到内容
> ```

#### urllib.request.urlretrieve抓取

> ```python
> from urllib import request
> 
> url = 'http://www.xiaohuar.com/images/banner/a.jpg'
> if __name__ == '__main__':
>     res = request.urlretrieve(url=url,filename='beauty.jpg')
>     print(res)
> ```