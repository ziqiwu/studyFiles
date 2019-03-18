### 不记文档，白忙一场

------

#### 概述

> ```python
> Scrapy，非常的强悍，通过python语言编写的，非常知名的爬虫框架
> 
> 对照框架示意图理解下面的解释：
> 1、Scrapy Engine(引擎):负责Spider、ItemPipeline、Downloader、Scheduler中间的通讯，信号、数据传	 递等
> 2、Scheduler(调度器):它负责接受引擎发送过来的Request请求，并按照一定的方式进行整理排列，入队，当引	  擎需要时，交还给引擎
> 3、Downloader（下载器）:负责下载Scrapy Engine(引擎)发送的所有Requests请求，并将其获取到的		    Responses交还给Scrapy Engine(引擎)，由引擎交给Spider来处理
> 4、Spider（爬虫）:它负责处理所有Responses,从中分析提取数据，获取Item字段需要的数据，并将需要跟进的    URL提交给引擎，再次进入Scheduler(调度器)
> 5、Item Pipeline(管道):它负责处理Spider中获取到的Item，并进行进行后期处理（详细分析、过滤、存储      等）的地方
> ```

#### 安装

**pip安装**

> ```python
> pip install scrapy
> ```
>

**如果出现安装错误解决方案**

> ```python
> building 'twisted.test.raiser' extension
> error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
> 
> 解决方案：
> 		http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 
> 		进入页面ctrl + F查找twisted即可
> 下载twisted对应版本的whl文件（如我的Twisted-17.5.0-cp36-cp36m-win_amd64.whl），cp后面是python版本python3.6，amd64代表电脑是64位，运行命令：
> 		pip install C:\Users\CR\Downloads\Twisted-17.5.0-cp36-cp36m-win_amd64.whl
> 
> 之后正常安装即可
> ```

#### 基本使用

**简介**

> ```python
> 1、上面5部分有4部分你都莫需关心，只需要关注spiders即可，你的代码也是写到了spiders里面
> 2、管道是用来处理数据的，框架为我们留下接口，只需要实现接口即可
> 	Item 定义结构化数据字段，用来保存爬取到的数据，有点像Python中的dict，但是提供了一些额外的保护	  减少错误
> ```
>

**步骤**

> ```python
> 第一步：通过指令创建项目
> 	scrapy startproject xxx
> 第二步：通过指令创建文件
> 	cd 目标文件
> 	scrapy genspider qiubai "www.qiushibaike.com"
> 	注：不需要加"http://"，从"www"开始写起
> 	注：创建的文件中
> 		name: 爬虫的名字，启动的时候根据爬虫的名字启动项目
> 		allowed_domains：允许的域名，就是爬取的时候这个请求要不要发送，如果是该允许域名之下url，
>                就会发送，如果不是，则过滤掉这个请求，这是一个列表，可以写多个允许的域名
> 		start_urls：爬虫起始url，是一个列表，里面可以写多个，一般只写一个
> 		def parse(self, response): 这个函数非常重要
> 			就是你以后写代码的地方，parse函数名是固定的，当收到下载数据的时候会自动的调用这个方法
> 			该方法第二个参数为response，这是一个响应对象，从该对象中获取html字符串，然后解析之。
> 			这个parse函数必须返回一个可迭代对象
> 第三步：定制item.py
> 	其实就是数据结构，格式非常简单，复制粘贴即可
> 第四步：打印response对象
> 	scrapy crawl qiubai
>     	【注】报错：ModuleNotFoundError: No module named 'win32api'
> 			安装对应pywin32版本即可https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32
> 			和上面pip install scrapy时候报错找的是一样的网址。
> 	根据response  获取网页内容
> 		response.text    字符串类型
> 		response.body    二进制类型
> 第五步：运行
> 	scrapy crawl xxx -o data.json
> 	scrapy crawl xxx -o data.xml
> 	scrapy crawl xxx -o data.csv
> ```
>

**第五步补充**

> ```python
> 编码问题:
>     scrapy用-o filename.json 输出时，会默认使用unicode编码，当内容为中文时，输出的json文件不便于		查看
>     可以在setting.py文件中修改默认的输出编码方式，
>     只需要在setting.py中增加如下语句（默认似乎是没有指定的，所以要增加，如果默认有，就直接修改）		FEED_EXPORT_ENCODING = 'utf-8'
> ```

#### scrapy shell

**简介**

> ```python
> Scrapy终端是一个交互终端，我们可以在未启动spider的情况下尝试及调试代码，也可以用来测试XPath或CSS表达式，查看他们的工作方式，方便我们爬取的网页中提取的数据
> 
> 【注】Jupyter --> 尝试安装
> 如果安装了 Jupyter ，Scrapy终端将使用 Jupyter (替代标准Python终端)。 Jupyter 终端与其他相比更为强大，提供智能的自动补全，高亮输出，及其他特性。推荐安装Jupyter
> 
> 当shell载入后，将得到一个包含response数据的本地 response 变量，输入 response.body将输出response的包体，输出 response.headers 可以看到response的包头
> 
> Scrapy也提供了一些快捷方式, 例如 response.xpath()同样可以生效
> ```
>

**使用**

> ```python
> response
> 	属性:
>         text：字符串格式的html
>         body：二进制格式的html
>         url：所请求的url
>         status：响应的状态码
> 
>         注意使用shell时，url需要使用双引号。或者不加引号，不要用单引号
>         如果报Connection was closed cleanly。那么是网站的翻盘机制在阻止我们访问。
>         比如访问糗事百科不设headers时。
>         这时可以在访问时带上headers
>         shell -s USER_AGENT='Mozilla/5.0' "https://www.qiushibaike.com/"
>         也可以去修改scrapy源码。让默认的设置中每次请求都能自动带上headers
> 	方法：
>     	xpath(): 根据xpath路径获取符合的路径所有selector对象（是scrapy自己封装的一个类的对象）的			列表
> selector
> 	xpath('./'): 从当前节点向下开始查找 
> 	extract(): 将对象转化为unicode字符串，供你的代码使用
> 	extract_first(): 理论上相当于上面的  
>      	name_list.extract()[0] == name_list.extract_first()
>      	但实际上，extract_first()要比extract()强大，如果xpath没有获取到内容，extract_first()会		 返回None
> ```

#### yield

> ```python
> 1、带有 yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代
> 2、yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次	 迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行
> 3、简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开	始
> ```
>

**上接第三点**

> ```python
> def main():
> 	lt = []
> 	for x in range(1, 11):
> 		lt.append(x)
> 	return lt
>     def main_yield():
>         for x in range(1, 11):
>             yield x
>     # lt = main()
>     # print(lt)
> 
>     ge = main_yield()
>     print(ge)
>     for x in ge:
>         print(x)
> ```

#### CrawlSpider

**继承**

> ```python
> 继承自scrapy.Spider
> ```

**独门秘笈**

> ```python
> CrawlSpider可以定义规则，再解析html内容的时候，可以根据链接规则提取出指定的链接，然后再向这些链接发送请求
> 所以，如果有需要跟进链接的需求，意思就是爬取了网页之后，需要提取链接再次爬取，使用CrawlSpider是非常合适的
> 比如分页
> 【注】具体看示意图
> ```

**提取链接**

> ```python
> 链接提取器，在这里就可以写规则提取指定链接
> scrapy.linkextractors.LinkExtractor(
> 	 allow = (),    # 正则表达式  提取符合正则的链接
> 	 deny = (),     # (不用)正则表达式  不提取符合正则的链接
> 	 allow_domains = (),  # （不用）允许的域名
> 	 deny_domains = (),   # （不用）不允许的域名
> 	 restrict_xpaths = (), # xpath，提取符合xpath规则的链接
> 	 restrict_css = ()  # 提取符合选择器规则的链接)
> ```
>
> ​	模拟使用
>
> ```python
> scrapy shell "http://www.dytt8.net/html/gndy/dyzz/index.html"
> 正则用法：links1 = LinkExtractor(allow=r'list_23_\d+\.html')
> xpath用法：links2 = LinkExtractor(restrict_xpaths=r'//div[@class="x"]')
> css用法：links3 = LinkExtractor(restrict_css='.x')
> ```

**注意事项**

> ```python
> rules = (
> 	   Rule(LinkExtractor(allow=r'/book/1163_\d+\.html'), callback='parse_item', 
>             follow=False),
> )
> ```
>
> ```python
> 【注1】callback只能写函数名字符串, callback='parse_item'
> 【注2】在基本的spider中，如果重新发送请求，那里的callback写的是   callback=self.parse_item
> ```

#### 日志信息和日志等级

**日志级别**

> ```python
> 级别：
> 	CRITICAL：严重错误
> 	ERROR：一般错误
> 	WARNING：警告
> 	INFO: 一般信息
> 	DEBUG：调试信息
> 
> ```

**settings.py文件设置**

> ```python
> 默认的级别为DEBUG，会显示上面所有的信息
> 在配置文件中  settings.py
>     LOG_FILE  : 将屏幕显示的信息全部记录到文件中，屏幕不再显示
>     LOG_LEVEL : 设置日志显示的等级，就是显示哪些，不显示哪些
> ```

#### 自学scrapy爬虫命令解析

> ```python
> https://blog.csdn.net/djd1234567/article/details/45913967
> ```

#### settings.py文件

> ```python
> 1、管道设置
>     #后面的数字越小，则越先执行
>     ITEM_PIPELINES = {
>        'dushuproject.pipelines.DushuprojectPipeline': 300,
>        'dushuproject.pipelines.MysqlPipeline': 299,
>     }
> 2、USER_AGENT设置
> 	USER_AGENT = 													
>     'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
> 3、是否遵循robots协议设置
> 	ROBOTSTXT_OBEY = False
> 5、请求头设置
>     DEFAULT_REQUEST_HEADERS = {
>       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
>       'Accept-Language': 'en,zh_CN',
>     }
> 6、日志设置
>     LOG_FILE  : 将屏幕显示的信息全部记录到文件中，屏幕不再显示
>     LOG_LEVEL : 设置日志显示的等级，就是显示哪些，不显示哪些
> 7、数据库设置
>     DB_HOST = '127.0.0.1'
>     DB_PORT = 3306
>     DB_USER = 'softpo'
>     DB_PWD = 'root'
>     DB_NAME = 'test'
>     DB_CHARSET = 'utf8'
> 8、使用代理
> 	DOWNLOADER_MIDDLEWARES = {'postproject.middlewares.Proxy': 543,}
> ```

#### scrapy-post请求

> ```python
> 详情见scrapy实战
> ```