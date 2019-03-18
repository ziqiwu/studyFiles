不记文档，白忙一场

------

#### 概述

> ```python
> 和 lxml 一样，Beautiful Soup 也是一个HTML/XML的解析器，主要的功能也是如何解析和提取 HTML/XML 数据。
> lxml 只会局部遍历，而Beautiful Soup 是基于HTML DOM的，会载入整个文档，解析整个DOM树，因此时间和内存开销都会大很多，所以性能要低于lxml
> BeautifulSoup 用来解析 HTML 比较简单，API非常人性化，支持CSS选择器、Python标准库中的HTML解析器，也支持 lxml 的 XML解析器 
> ```

#### 安装

> ```python
> pip install Beautifulsoup4 
> ```

#### 原理

> ```python
> Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种。
> 1、BeautifulSoup：对象表示的是一个文档的内容。大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，	我们可以分别获取它的类型，名称，以及属性
> 2、Tag：通俗点讲就是 HTML 中的一个个标签
> 3、NavigableString：既然我们已经得到了标签，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简	单，用 .string 即可
> 4、Comment：对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号
> 	a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容时，注释符号已经去掉了
> 	<a href="http://example.com/elsie" class="sister" id="link1">
> 	<!-- Elsie -->
> 	</a>
> ```
>

#### 操作

> ​	遍历文档树：
>
> ```python
> print(len(soup.body.contents),soup.body.contents)
> print(soup.body.children)
> print(soup.body.descendants)
> for haha in soup.body.descendants:
> 	print(haha)
> 1、直接子节点 ：.contents .children 属性
> 	字符串也属于一个节点，例如'\n'，'and'
> 2、所有子孙节点: .descendants 属性
> ```
>
> ​	搜索文档树：
>
> ```python
> find_all(name, attrs, recursive, text, **kwargs)
> 
> print(soup.find('a'))
> import re
> print(soup.find_all('a', title= re.compile(r'.*')))
> print(soup.find_all('a', id=['hong','gu']))
> print(soup.find('a', class_='taohua'))
> print(soup.find('a', href='http://www.163.com'))
> 
> 
> print(soup.find_all('a'))
> print(soup.find_all(['a', 'span']))
> print(soup.find_all('a', limit=2))
> 
> print(soup.select('.tang > ul > li > a')[-1].string)
> 1、name
> 	字符串：print(soup.find_all('a'))
> 	传正则表达式：
>     	# 使用正则表达式，该正则表示匹配字符串开头
> 		import re
> 		for tag in soup.find_all(re.compile("^b")):
>     		print(tag.name)
> 	传列表：
>     	ret = soup.find_all(["a", "b"])
> 		print(ret)
> 2、keyword 参数
> 	# keyword参数
> 	ret = soup.find_all(id = 'link2' )
> 	print(ret)
> 	ret = soup.find_all(classe_='sister')
> 	print(ret)
> ```
>
> ​	CSS选择器
>
> ```python
> 这就是另一种与 find_all 方法有异曲同工之妙的查找方法
> 	写 CSS 时，标签名不加任何修饰，类名前加.，id名前加#
> 	在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
> 查找方式:
>     通过标签查找
>     	# 通过标签查找
> 		print(soup.select('title'))
> 		print(soup.select('a'))
> 		print(soup.select('b'))
> 	通过类名查找
> 		# 通过类名查找
> 		print(soup.select('.sister'))
> 	通过 id 名查找
>     	# 通过 id 名查找
> 		print(soup.select('#link1'))
> 	组合查找
> 		组合查找即和写class文件时，标签名与类名、id名进行的组合原理是一样的，例如查找 p 标签中，id 		等于 link2的内容，注意不要有空格
> 		# 组合查找
> 		print(soup.select('p#link2'))
> 
> 		直接子标签查找，则使用 > 分隔，>前后要有空格
> 		print(soup.select('head > title'))
> 	属性查找
>     	查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能		 加空格，否则会无法匹配到。
> 		# 属性查找
> 		print(soup.select('a[class="sister"]'))
> 		print(soup.select('a[href="http://example.com/elsie"]'))
> 		同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
> 		print(soup.select('p a[href="http://example.com/elsie"]'))
> 	获取内容:get_text()
> 		以上的select方法返回的结果都是列表形式，可以遍历形式输出，然后用get_text()方法来获取它的		内容。
> 		print(type(soup.select('title')))
> 		print(soup.select('title')[0].get_text())
> 		for title in soup.select('title'):
>     		print(title.get_text())
> ```

#### 各解析工具比较

> | 抓取工具 | 速度 | 使用难度 | 安装难度 |
> | :------: | :--: | :------: | :------: |
> |   正则   | 最快 |   困难   | 无(内置) |
> |   bs4    |  慢  |  最简单  |   简单   |
> |   lxml   |  快  |   简单   |   一般   |

