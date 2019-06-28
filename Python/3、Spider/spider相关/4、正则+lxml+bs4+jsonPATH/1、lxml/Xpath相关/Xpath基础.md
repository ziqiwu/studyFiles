### 不记文档，白忙一场

------

#### ***面试***

> ```python
> 1> XPath 是一门在 XML 文档中查找信息的语言。
> 2> 使用方法
> 	1 属性查找
> 	2 模糊查找
> 	3 下标查找
> 	4 取文本，取属性
>     
> 	4 层级查找
> 	
> ```

#### 0、概述

> ```python
> XPath 是一门在 XML 文档中查找信息的语言。XPath 可用来在 XML 文档中对元素和属性进行遍历。 
> 要想理解xpath是什么要先知道xml是什么。
> 
> http://www.w3school.com.cn --> 检索xpath
> w3school的xpath教程是非常好的xpath教程。
> 
> http://www.w3school.com.cn --> 检索xml
> w3school的xml教程是非常好的xml教程。
> ```

#### 语法

> ```python
> #注意：基本语法
> 	'''
> 		属性定位：根据属性查找标签
> 		层级定位：一级一级查找
> 		索引定位：【注】下标从1开始
> 		//  从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
> 		.   选取当前节点
> 		@   选取属性
> 	'''
> #注意：获取文本
> 	'''
> 		Xpath中string()/data()/text()的区别：
> 		https://blog.csdn.net/weixin_39285616/article/details/78463091
> 	'''
> 属性查找
> 	查找id是maincontent的div下面的h1节点
> 	//div[@id="maincontent"]/h1
> 	//div[@class="head_wrapper"]/div[@id="u"]/a[1]
> 逻辑运算
> 	//div[@id="head" and @class="s_down"]
> 模糊匹配
> 	查找所有的div，id中有he的div
> 	//div[contains(@id, "he")]
> 	查找所有的div，id中以he开头的div
> 	//div[starts-with(@id, "he")]
> 	查找所有的div，id中以he结尾的div
> 	//div[ends-with(@id, "he")]
> 取文本
> 	//div[@class="head_wrapper"]/div[@id="u"]/a[1]/text()
> 	//div[@class="head_wrapper"]/div[@id="u"]/a[1]
> 	obj.text   将内容获取到
>     使用string()方法：string('//p') --> 查找标签下的所有内容，包括字标签
> 取属性
> 	//div[@class="head_wrapper"]/div[@id="u"]/a[1]/@hre
> ```

#### 谷歌插件xpath.crx

> ​	安装
>
> ```python
> More tools --> Extensions --> 拖动xpath.crx文件到该页面上方 --> 显示Drop to install
> ```
>
> ​	使用
>
> ```python
> 打开谷歌浏览器，安装xpath插件，然后使用xpath插件
> 按 ctrl + shift + x
> ```