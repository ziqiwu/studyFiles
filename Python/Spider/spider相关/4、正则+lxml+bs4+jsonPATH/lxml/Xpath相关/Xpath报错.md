### 不记文档，白忙一场

------

#### 报错信息

##### 一个标签下所有字标签的内容

> ​	比如：
>
> ```python
> <p class="">元·<a href="/author/%e8%84%b1%e5%9b%a0/" title="更多同作者相关作品" target="_blank" class="">脱因</a></p>
> 现在xpath定为到p标签，想把p和它的字标签中的内容都一次性取出来。
> 但是，text()方法只能把p中的一层内容取出。
> //p/text()
> ```
>
> ​	解决：
>
> ```python
> 使用string()方法：
> 	string('//p')
> ```
>
> ​	链接：
>
> ```python
> Xpath中string()/data()/text()的区别：
> https://blog.csdn.net/weixin_39285616/article/details/78463091
> ```