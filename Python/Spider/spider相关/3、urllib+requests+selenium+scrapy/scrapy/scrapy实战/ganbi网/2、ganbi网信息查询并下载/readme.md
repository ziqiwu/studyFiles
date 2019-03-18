### 不记文档，白忙一场

------

#### 备注

> ```python
> 1、start_urls中存放n多个爬虫的地址 (比如这些地址都是从数据库中取出来的)
> 2、数据库连接
> 3、数据库取值 (数据库取出来的对象是元组，按照索引取值)
> 4、字典的应用 (给每个下载的视频命名都用数据库中的title，而不是随机名称)
> 5、正则的使用 (详情页中匹配视频下载地址)
> 6、根据爬虫返回的response对象，获取url地址 (response.url)
> 7、获取到的url地址是编码之后的，进行解码 (from urllib import parse,parse.unquote(response.url))
> 8、全局变量的使用 (根据详情页url匹配title，class下url_dict = {}，方法内self.url_dict，取值用get)
> 9、捕获异常的使用，如下载失败的判定，如下载视频名称的判定
> 10、获取settings对象，以取出其中的信息 (get_project_settings)
> ```

