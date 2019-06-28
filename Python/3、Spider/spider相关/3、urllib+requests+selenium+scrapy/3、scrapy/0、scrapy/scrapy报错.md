### 不记文档，白忙一场

------

#### 报错记录

**Connection was closed cleanly**

> ```python
> 如果报Connection was closed cleanly。那么是网站的翻盘机制在阻止我们访问。
> 比如访问糗事百科不设headers时。
> 这时可以在访问时带上headers
> shell -s USER_AGENT='Mozilla/5.0' "https://www.qiushibaike.com/"
> 也可以去修改scrapy源码。让默认的设置中每次请求都能自动带上headers
> ```





