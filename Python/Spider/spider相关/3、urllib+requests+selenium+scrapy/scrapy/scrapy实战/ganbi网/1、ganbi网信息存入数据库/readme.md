### 不记文档，白忙一场

------

#### 备注

> ```python
> 1、从start_urls的地址之后，进行深度匹配爬取数据
> 2、rules是一个元组，可以设置多个url，但是第一个必须和start_urls数组中的url相同。 (给我的理解，		start_urls是要打开的页面，rules是从打开页面中进一步深度匹配的。如果Rule对象的follow=False，则	  只深度匹配一次，也就是start_url页面中匹配一次。)
> 3、pipe.py中有两个类，一个是数据写入text文件，一个是数据写入数据库，都需要在settings.py中进行配置
> 【注意】后期加上，重写start_request的步骤，就上需要先登录后爬取的情景。
> ```

