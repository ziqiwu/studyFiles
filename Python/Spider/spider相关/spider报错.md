

### 不记文档，白忙一场

------

#### 报错信息

**(1) AttributeError: module 'urllib' has no attribute 'request'**

> ​	描述
>
> ```python
> 简单代码：
>     from urllib import request
>     url="http://www.baidu.com/"
>     response1=request.urlopen(url)
>     print (response1.read().decode('utf-8'))
> 但是：
> 	from urllib import request的request下爆红
> 	改为import urllib.request，urllib.request.urlopen(url)之后，运行报上面的错误
> ```
>
> ​	解决
>
> ```python
> 因为自己的模块名称写成了urllib.py
> 和系统模块名称冲突了
> 验证方式：
> 	我给urllib.py右键，重命名为urllib_demo之后，代码中原来的urllib都改为了urllib_demo，所以可以证实代码中的urllib引用的并不是系统的模块urllib，而是自己的模块urllib。
> ```
>
> ​	教训
>
> ```python
> 模块名称，包名称，类名称等等，一定要规避，防止和系统名称冲突
> ```
>

**(2) 在页面的F12下看不到应该有的JS**

> ​	描述
>
> ```python
> 爬虫有道翻译
> 请求数据的POST请求参数data中有加密，盐等，他们只要两种可能生成方式，一是页面先请求后台，后端生成后传回页面，二是页面的JS自己生成。
> F12查看后，发现请求路径只有一个。所以只能是第二种方式页面的JS自己生成的。
> 但是F12查看，点JS，发现是空的，并没有JS文件
> ```
>
> ​	解决
>
> ```python
> 原因是页面刷新自己冲掉了。
> 打开F12的JS保持不动，重新刷新页面，就是主页面刷新的时候，所有JS就都显示出来了。
> 注意不是写入单词，查询的时候，加载的JS，而是主页面刷新的时候，加载的JS。写入单词查询只是主页面上行的一个ajax请求而已。
> ```
>
> ​	附录
>
> ```python
> js的命名，比如jquery.min.js，其中的min表示的意思是压缩过后的。
> 打开这样的文件，需要网上随便找一个js在线格式化，格式化完再在IDE上查看即可
> ```
>

**(3) 最新版本的lxml没有etree模块**

> ```python
> import lxml.html
> etree = lxml.html.etree
> 这样就可以使用etree了
> ```

**(4) pip安装出现sslerror的问题**

> ​	描述
>
> ```python
> Collecting slwt
>   Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None))
>  after connection broken by 'SSLError(SSLError(1, u'[SSL: CERTIFICATE_VERIFY_FAI
> ```
>
> ​	解决
>
> ```python
> pip install lightgbm -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
> ```

**(5) requests爬虫报错：SSLError**

> ​	描述
>
> ```python
> raise SSLError(e, request=request)
> requests.exceptions.SSLError: HTTPSConnectionPool(host='weibo.com', port=443): Max retries exceeded with url: /5803031936/info (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1045)')))
> ```
>
> ​	解决
>
> ```python
> import requests
> session = requests.Session()
> res = session.get(url=url,headers=headers,verify=False)
> #增加verify参数
> ```

















```python
#############################requests+bs4
#requests模拟访问url，得到返回的内容
#bs4将上面返回的内容进行所需数据的提取

#############################urllib3+xpath
#urllib3模拟访问url，得到返回的内容
#xpath将上面返回的内容进行所需数据的提取
```



```python
1、浏览器设置代理
	chrome --> 设置 --> 搜索'代理' --> 打开代理设置 --> HTTP(H)和安全(S)都改为网上的代理IP和PORT
2、新浪微博的登录页面
https://passport.weibo.cn/signin/welcome?entry=mweibo&r=https%3A%2F%2Fpad.weibo.cn%2F%3Fsudaref%3Dwww.baidu.com%26display%3D0%26retcode%3D6102&sudaref=www.baidu.com&display=0&retcode=6102&_T_WM=4680b0fcfbeda5b3095f6e98de7d731c
    上面是错的，下面是打开的正确姿势
https://passport.weibo.cn/signin/login
    因为post参数中有一个参数，表示从哪个页面跳过来的。如果用第一个，会超级多，没法用
    
    
错错错，完全错了 --> 用第一个完全搞定，用第二个反而各种报错。而且第一个都不用把里面的https什么的在url编码解码里面改一下。直接放在代码里就可以搞定了。
```

