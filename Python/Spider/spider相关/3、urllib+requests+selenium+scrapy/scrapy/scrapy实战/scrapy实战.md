### 不记文档，白忙一场

------

#### 爬取电影天堂电影

> ```python
> url:http://www.dytt8.net
> ```
>
> ```python
> 创建项目scrapy startproject movie
> ```
>
> ​	settings设置
>
> ```python
> USER_AGENT = 'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
> ROBOTSTXT_OBEY = False
> DEFAULT_REQUEST_HEADERS = {
>   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
>   'Accept-Language': 'en,zh_CN',
> }
> ITEM_PIPELINES = {'movie.pipelines.MoviePipeline': 300,}
> ```
>
> ​	Spiders爬虫代码
>
> ```python
> import scrapy
> from movieproject.items import MovieprojectItem
> 
> class MovieSpider(scrapy.Spider):
>     name = 'movie'
>     allowed_domains = ['www.dytt8.net']
>     start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']
> 
>     def parse(self, response):
>         # 找到所有的电影
>         table_list = response.xpath('//div[@class="co_content8"]/ul//table')
>         # 遍历所有的电影列表，得到电影的详细信息
>         for table in table_list:
>             # 在当前的页面的只能提取到两个信息，一个是name，一个是movie_info
>             # 创建一个对象
>             item = MovieprojectItem()
>             # 提取对应的信息  
>             # 【注】在点的后面要加两个杠
>             item['name'] = table.xpath('.//a[@class="ulink"]/text()').extract_first()
>             item['movie_info'] = table.xpath('.//tr[last()]/td/text()').extract_first()
>             # 获取电影的链接
>             movie_url = 'http://www.dytt8.net' + 													table.xpath('.//a[@class="ulink"]/@href').extract_first()
>             # yield item
> 
>             # 这里面涉及到一个传递item的问题，我们要学习如何传参,加上一个meta参数，meta参数是一个				字典，过去之后，通过字典的键获取其值
>             yield scrapy.Request(url=movie_url, callback=self.parse_info, meta={'item': 				item})
> 
>     # 获取item的其它信息
>     def parse_info(self, response):
>         # 获取到传递过来的参数
>         item = response.meta['item']
>         # 接着解析网页，获取item的其它信息
>         item['image_url'] = 																	response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
>         # item['story_info'] = response.xpath('')
>         item['download_url'] = 																	response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract_first()
>         yield item
> ```
>
> ​	pipelines数据保存
>
> ```python
> import json
> class MoviePipeline(object):
>     def __init__(self):
>         self.fp = open('movie2.txt', 'w', encoding='utf-8')
> 
>     def process_item(self, item, spider):
>         obj = dict(item)
>         string = json.dumps(obj, ensure_ascii=False)
>         print(string)
>         self.fp.write(string + '\n')
>         return item
> 
>     def close_spider(self, spider):
>         self.fp.close()
> ```

#### 爬取天涯论坛

> ```python
> url：http://bbs.tianya.cn/post-140-393977-1.shtml
> ```
>
> ​	Spiders
>
> ```python
> # -*- coding: utf-8 -*-
> import scrapy
> import re
> from myspider.items import MyspiderItem
> 
> class TianyaSpider(scrapy.Spider):
>     name = 'tianya'
>     allowed_domains = ['bbs.tianya.cn']
>     start_urls = ['http://bbs.tianya.cn/post-140-393977-1.shtml']
> 
>     def parse(self, response):
>         html = response.text
>         email = re.compile(r'[A-Z0-9_]+@[A-Z0-9]+.[A-Z]{2,4}', re.I)
>         email_list = email.findall(html)
>         mydict = []
>         for e in email_list:
>             item = MyspiderItem()
>             item["email"] = e
>             mydict.append(item)
>             yield item
>         # return mydict
> ```
>
> ​	pipelines
>
> ```python
> class MyspiderPipeline(object):
>     def __init__(self):
>         self.f = open('tianya.txt', 'w', encoding='utf-8')
> 
>     def process_item(self, item, spider):
>         self.f.write(str(item))
>         return item
> 
>     def close_spider(self, spider):
>         self.f.close()
> ```
>
> ​	settings
>
> ```python
> ITEM_PIPELINES = {
>    'myspider.pipelines.MyspiderPipeline': 300,
> }
> ```

#### 爬取腾讯社招--原始分页

> ​	【备注】
>
> ```python
> 原始分页 + 使用框架的items + 使用框架的管道
> 【注】既然使用了框架管道，settings文件也需要改一下
> ```
>
> ```python
> url：https://hr.tencent.com/position.php?lid=2218&start=0#a
> ```
>
> ​	Spiders
>
> ```python
> class HireSpider(scrapy.Spider):
>     name = 'hire'
>     allowed_domains = ['tensent.com']
>     start_urls = ['https://hr.tencent.com/position.php?lid=2218&start=0#a']
> 
>     def parse(self, response):
>         for data in response.xpath("//tr[@class=\"even\"] | //tr[@class=\"odd\"]"):
>             item = items.TencentItem()
>             item["jobTitle"] = data.xpath("./td[1]/a/text()")[0].extract()
>             # item["jobLink"] = data.xpath("./td[1]/a/@href")[0].extract()
>             item["jobCategories"] = data.xpath("./td[1]/a/text()")[0].extract()
>             item["number"] = data.xpath("./td[2]/text()")[0].extract()
>             item["location"] = data.xpath("./td[3]/text()")[0].extract()
>             item["releasetime"] = data.xpath("./td[4]/text()")[0].extract()
>             yield item
> 
>         for i in range(1, 200):
>             newurl = "https://hr.tencent.com/position.php?lid=2218&start=%d#a" % (i * 10)
>             yield scrapy.Request(newurl, callback=self.parse)
> ```
>
> ​	pipelines
>
> ```python
> class TencentPipeline(object):
>     def __init__(self):
>         self.file = open("tencent.txt", "w", encoding="utf-8")
> 
>     def process_item(self, item, spider):
>         line = str(item) + "\r\n"
>         self.file.write(line)
>         self.file.flush()
>         return item
> 
>     def __del__(self):
>         self.file.close()
> ```
>
> ​	items
>
> ```python
> class TencentItem(scrapy.Item):
>     # define the fields for your item here like:
>     # name = scrapy.Field()
>     jobTitle = scrapy.Field()
>     jobCategories = scrapy.Field()
>     number = scrapy.Field()
>     location = scrapy.Field()
>     releasetime = scrapy.Field()
> ```

#### 读书网--分页爬取+数据库

> ```python
> 创建项目：scrapy startproject dushuproject
> ```

> ```python
> 创建爬虫类：scrapy genspider -t crawl read www.dushu.com
> ```

**items**

> ```python
> import scrapy
> 
> class DushuprojectItem(scrapy.Item):
>     # define the fields for your item here like:
>     # name = scrapy.Field()
>     image_url = scrapy.Field()
>     book_name = scrapy.Field()
>     author = scrapy.Field()
>     info = scrapy.Field()
> ```

**Spiders**

> ```python
> # -*- coding: utf-8 -*-
> import scrapy
> from scrapy.linkextractors import LinkExtractor
> from scrapy.spiders import CrawlSpider, Rule
> 
> from dushuproject.items import DushuprojectItem
> 
> 
> class ReadSpider(CrawlSpider):
>     name = 'read'
>     allowed_domains = ['www.dushu.com']
>     start_urls = ['https://www.dushu.com/book/1163.html']
>     # 假设我把follow修改为True，那么爬虫会从start_urls爬取的页面中在寻找符合规则的url，如此循环，		直到把全站爬取完毕。如果页面总30页，分页只显示了前3页，False只爬3页，True则30页。
>     rules = (
>         Rule(LinkExtractor(allow=r'/book/1163_\d+\.html'), 										callback='parse_item',follow=True),
>     )
> 
>     def parse_item(self, response):
>         # 首先查找到所有的书籍
>         book_list = response.xpath('//div[@class="bookslist"]/ul/li')
>         # 遍历所有书籍，获取每本书详细的内容
>         for book in book_list:
>             item = DushuprojectItem()
>             item['image_url'] = book.xpath('./div[@class="book-info"]/div/a/img/@data-					original').extract_first()
>             item['book_name'] = book.xpath('./div[@class="book-											info"]/h3/a/text()').extract_first()
>             item['author'] = book.xpath('./div[@class="book-											info"]/p/a/text()').extract_first()
>             item['info'] = book.xpath('./div[@class="book-info"]/p[@class="disc 						eps"]/text()').extract_first()
>             yield item
> ```

**Settings**

> ```python
> #后面的数字越小，则越先执行
> ITEM_PIPELINES = {
>    'dushuproject.pipelines.DushuprojectPipeline': 300,
>    'dushuproject.pipelines.MysqlPipeline': 299,
> }
> 
> DB_HOST = '127.0.0.1'
> DB_PORT = 3306
> DB_USER = 'softpo'
> DB_PWD = 'root'
> DB_NAME = 'test'
> DB_CHARSET = 'utf8'
> ```

**pipelines -- 数据保存到本地**

> ```python
> class DushuprojectPipeline(object):
>     def open_spider(self, spider):
>         self.fp = open('book.json', 'w', encoding='utf-8')
> 
>     def process_item(self, item, spider):
>         obj = dict(item)
>         string = json.dumps(obj, ensure_ascii=False)
>         self.fp.write(string + '\n')
>         return item
> 
>     def close_spider(self, spider):
>         self.fp.close()
> ```

**pipelines -- 数据保存到mysql数据库**

> ```python
> class MysqlPipeline(object):
>     """docstring for MysqlPipeline"""
>     def __init__(self):
>         settings = get_project_settings()
>         self.host = settings['DB_HOST']
>         self.port = settings['DB_PORT']
>         self.user = settings['DB_USER']
>         self.pwd = settings['DB_PWD']
>         self.name = settings['DB_NAME']
>         self.charset = settings['DB_CHARSET']
>         self.connect()
> 
>     def connect(self):
>         self.conn = pymysql.connect(host=self.host,
>                              port=self.port,
>                              user=self.user,
>                              passwd=self.pwd,
>                              db=self.name,
>                              charset=self.charset)
>         self.cursor = self.conn.cursor()
> 
>     def close_spider(self, spider):
>         self.conn.close()
>         self.cursor.close()
> 
>     def process_item(self, item, spider):
>         sql = 'insert into book(image_url, book_name, author, info) values("%s", "%s", "%s", "%s")' % (item['image_url'], item['book_name'], item['author'], item['info'])
>         # 执行sql语句
>         self.cursor.execute(sql)
>         self.conn.commit()
>         return item
> ```

#### 百度翻译--scrapy-post请求

**Spiders**

> ```python
> import scrapy
> import json
> 
> class BaiduSpider(scrapy.Spider):
>     name = 'baidu'
>     allowed_domains = ['www.baidu.com']
> 
>     # http://fanyi.baidu.com/sug
>     # start_urls = ['http://www.baidu.com/']
> 
>     # def parse(self, response):
>     #     pass
> 
>     # 如果想要自己直接发送post请求，则需要重写这个方法。
>     # 这个方法以前就是遍历start_urls列表，生成请求对象的
>     # 注意，是自己直接发送post请求
>     # 注意，上面的注释掉的地方，在post请求中就不要了
>     def start_requests(self):
>     	post_url = 'http://fanyi.baidu.com/sug'
>     	word = 'world'
>     	data = {
>     		'kw': word
>     	}
>     	yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.parse_post)
> 
>     def parse_post(self, response):
>     	print('---------------------',json.loads(response.text))
> ```

#### 百度翻译--代理+post请求

**Spiders**

> ```python
> import scrapy
> import json
> 
> class BaiduSpider(scrapy.Spider):
>     name = 'baidu'
>     allowed_domains = ['www.baidu.com']
> 
>     # http://fanyi.baidu.com/sug
>     # start_urls = ['http://www.baidu.com/']
> 
>     # def parse(self, response):
>     #     pass
> 
>     # 如果想要自己直接发送post请求，则需要重写这个方法。
>     # 这个方法以前就是遍历start_urls列表，生成请求对象的
>     def start_requests(self):
>     	post_url = 'http://fanyi.baidu.com/sug'
>     	word = 'world'
>     	data = {
>     		'kw': word
>     	}
>     	yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.parse_post)
> 
>     def parse_post(self, response):
>     	print('---------------------',json.loads(response.text))
> ```

**Settings**

> ```python
> 到settings.py中，打开一个选项
> 	DOWNLOADER_MIDDLEWARES = {'postproject.middlewares.Proxy': 543,}
> ```

**middlewares.py**

> ```python
> 到middlewares.py中写代码
> def process_request(self, request, spider):
>     request.meta['proxy'] = 'https://113.68.202.10:9999'
>     return None
> ```

#### 豆瓣模拟登录--post请求

**Spiders**

> ```python
> # -*- coding: utf-8 -*-
> import scrapy
> import urllib.request
> from PIL import Image
> 
> class DoubanSpider(scrapy.Spider):
>     name = 'douban'
>     allowed_domains = ['douban.com']
>     start_urls = ['https://accounts.douban.com/login']
> 
>     def parse(self, response):
>         # 去查找有没有验证码
>         # 【注】如果找不到，那么返回None
>         image_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
>         # 如果没有验证码图片，image_url就是None
>         if not image_url:
>             data = {
>                 'source': '',
>                 'redir': 'https://www.douban.com',
>                 'form_email': '18513106743',
>                 'form_password': '31415926abc',
>                 'login': '登录',
>             }
>         else:
>             # 获取验证码id
>             captcha_id = response.xpath('//input[@name="captcha-										id"]/@value').extract_first()
>             # 保存验证码图片，并且提示用户输入验证码
>             urllib.request.urlretrieve(image_url, './douban.png')
>             Image.open('./douban.png').show()
>             yanzhengma = input('请输入验证码:')
>             data = {
>                 'source': '',
>                 'redir': 'https://www.douban.com',
>                 'form_email': '18513106743',
>                 'form_password': '31415926abc',
>                 'captcha-solution': yanzhengma,
>                 'captcha-id': captcha_id,
>                 'login': '登录',
>             }
>             headers = {
>                 
>             }
>         post_url = 'https://accounts.douban.com/login'
>         print('-------------------------------------------------------')
>         return scrapy.FormRequest(url=post_url, formdata=data, callback=self.accounts)
> 
>     def accounts(self, response):
>         with open('douban1.html', 'wb') as fp:
>           fp.write(response.body)
>         url = 'https://www.douban.com/accounts/'
>         print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
>         return scrapy.Request(url=url, callback=self.parse_accounts)
> 
>     def parse_accounts(sef, response):
>         print('===================================================================')
>         with open('豆瓣.html', 'wb') as fp:
>             fp.write(response.body)
> ```

**判断是否有验证码**

> ```python
> 查看示意图
> ```

#### 微博模拟登陆--post请求

**Spiders**

> ```python
> # -*- coding: utf-8 -*-
> import scrapy
> 
> 
> class WeiboSpider(scrapy.Spider):
>     name = 'weibo'
>     allowed_domains = []
>     # start_urls = ['http://www.weibo.cn/']
> 
>     # def parse(self, response):
>     #     pass
> 
> 
>     def start_requests(self):
>         post_url = 'https://passport.weibo.cn/sso/login'
>         data = {
>             'username': '18515178949',
>             'password': '31415926abc',
>             'savestate': '1',
>             'r': '',
>             'ec': '0',
>             'pagerefer': 'http://weibo.cn/',
>             'entry': 'mweibo',
>             'wentry': '',
>             'loginfrom': '',
>             'client_id': '',
>             'code': '',
>             'qq': '',
>             'mainpageflag': '1',
>             'hff': '',
>             'hfp': '',}
>         headers = {
>             'Referer': 'https://passport.weibo.cn/signin/login?										entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
>         }
>         yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.lala, 					headers=headers)
> 
>     def lala(self, response):
>         # print(response.text)
>         url = 'https://weibo.cn/6433251843/info/'
>         # 再次发送request请求即可
>         yield scrapy.Request(url=url, callback=self.haha)
> 
>     def haha(self, response):
>         with open('weibopo.html', 'w', encoding='utf-8') as fp:
>             fp.write(response.text)
> ```

#### 微博示意图

> ```python
> 详情见微博示意图
> ```

#### 步骤注意点

**1、想用框架自带的item的时候，需要注意**

> ```python
> 1、需要把项目右键，Mark Directory as，Resource
> 2、在Spider.py中引入Item类
> 3、在Settings.py中打开注释
> 	ITEM_PIPELINES = {
>        'dushuProject.pipelines.DushuprojectPipeline': 300,
>     }
> 【注】item.py注册变量名的时候，scrapy.Field()是方法，不是属性。千万不要写成scrapy.Field。会一直报	错，Item类没有这个属性。
> 【注】def parse_item(self, response):方法中，返回的一定是Item对象，而不是item的数组，如下：
> 		for li in li_list:
>             item = DushuprojectItem()
>             bookname = li.xpath('.//h3/a/text()').extract_first()
>             author =  li.xpath('string(.//div/p[1])').extract_first(default="暂缺作者")
>             brief = li.xpath('.//div/p[2]/text()').extract_first()
>             item['bookname'] = bookname
>             item['author'] = author
>             item['brief'] = brief
>             # yield是将item提交给管道，yield语句之后，还可以执行其他代码
>             yield item
> 		不是：
> 		item_arr = []
> 		for li in li_list:
>             item = DushuprojectItem()
>             bookname = li.xpath('.//h3/a/text()').extract_first()
>             author =  li.xpath('string(.//div/p[1])').extract_first(default="暂缺作者")
>             brief = li.xpath('.//div/p[2]/text()').extract_first()
>             item['bookname'] = bookname
>             item['author'] = author
>             item['brief'] = brief
>             item_arr.append(item)
> 		yield item_arr
> 	如果是返回Item对象数组，会发现pipe.py管道中的process_item完全没有执行，因为pipe.py中方法定义		是    
>     def process_item(self, item, spider):
>         self.fp.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
>         return item
>     参数就是Item对象，方法名称也是process处理item对象
>     return返回的也是Item对象  	
> ```

**2、爬取分页数据，进行规则匹配**

> ```python
> 1、例子如下：
> class DushuspiderSpider(CrawlSpider):
>     name = 'dushuSpider'
>     allowed_domains = ['www.ganbi99.com']
>     # start_urls = ['https://www.ganbi99.com/videos/asian']
>     start_urls = ['https://www.ganbi99.com/videos/asian?page=1']
> 
>     rules = (
>         Rule(LinkExtractor(allow=r'https://www.ganbi99.com/videos/asian'), 							callback='parse_item', follow = False),
>         Rule(LinkExtractor(allow=r'https://www.ganbi99.com/videos/asian?page=\d+/'), 				callback='parse_item', follow=False)
>     )
> 2、start_urls两种都可以，带不带参数page=1都可以
> 3、rules元组中，第一个Rule对象必须有，否则它匹配不到开始路径
> 4、Rule对象的follow参数值是False，则只匹配这一条，不会接着往下匹配，就比如分页，只会匹配第一页，匹	配一次
> ```
>
> 

