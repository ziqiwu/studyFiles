### 不记文档，白忙一场

------

#### 步骤

**第一步：创建项目**

> ```python
> scrapy startproject dushuProject
> cd dushuProject
> scrapy genspider -t crawl dushuSpider "wwww.dushu.com"
> ```
>
> ```python
> 【注】之前不写-t的，默认是继承scrapy.spider。
> 	写-t crawl继承的是CrawlSpider，而CrawlSpider是scrapy.spider的子类。
> 【注】dushuSpider类中的rules=()是一个元组，里面写的是匹配规则，可以写多个匹配规则。
> 	比如匹配多页的rule，是不能匹配到第一页的，就可以把第一页写成一个rule放在元组中。
> ```

**第二步：配置mysql数据库**

> ```python
> 1、pipelines.py文件中，复制一份class，改名为mysql相关的类名。
> 2、在settings.py文件中写mysql连接相关的属性，比如用户名密码，host端口等。
>     DB_HOST='127.0.0.1'
>     DB_PORT=3306
>     DB_USER='root'
>     DB_PASSWORD='123456'
>     DB_DB='books'
>     DB_CHARSET='utf8'
> 3、把管道加入settings.py中
> 	ITEM_PIPELINES = {
>        'dushuProject.pipelines.DushuprojectPipeline': 300,
>        'dushuProject.pipelines.DushuprojectMySQLPipeline': 200,   #比如这个就是新加的
>        'scrapy_redis.pipelines.RedisPipeline': 100
>     }
> ```

**第三步：上官网，复制settings.py中需要的部分**

> ```python
> 百度搜索：scrapy-redis github，找到应该是https://pypi.org/project/scrapy-redis/这个，
> 	下拉到Usage，复制：
> 		SCHEDULER = "scrapy_redis.scheduler.Scheduler"
> 		DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
> 		ITEM_PIPELINES = {
>             'scrapy_redis.pipelines.RedisPipeline': 300
>         } #注，如果还有其他管道，都加进来，比如mysql的管道，只是rdis的数字要小，要先执行
> 		REDIS_HOST = 'localhost'
> 		REDIS_PORT = 6379
> 同时：
> 	修改USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, 				like Gecko) Chrome/71.0.3578.98 Safari/537.36'
> 	修改ROBOTSTXT_OBEY=False
> 	去掉注释：DEFAULT_REQUEST_HEADERS
> 	去掉注释：ITEM_PIPELINES
> ```

