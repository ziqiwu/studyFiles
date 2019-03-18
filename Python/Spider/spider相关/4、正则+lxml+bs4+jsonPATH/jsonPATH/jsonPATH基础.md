### 不记文档，白忙一场

------

#### 概述

> ```python
> JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，包括：		Javascript, Python， PHP 和 Java。
> 	JsonPath 对于 JSON 来说，相当于 XPATH 对于 XML
> ```

#### 示例一

> ```python
> 拉勾网城市JSON文件 http://www.lagou.com/lbs/getAllCitySearchLabels.json 为例，获取所有城市
> 
> import requests
> import jsonpath
> import json
> 
> url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json/'
> response = requests.get(url,verify = False)
> html = response.text
> 
> # 把json格式字符串转换成python对象
> jsonobj = json.loads(html)
> 
> # 从根节点开始，匹配name节点
> citylist = jsonpath.jsonpath(jsonobj,'$..name')
> 
> # 把一个Python对象编码转换成Json字符串
> content = json.dumps(citylist, ensure_ascii=False)
> 
> with open('city.json','wb') as f:
>     f.write(content.encode('utf-8'))
> ```

#### 示例二

> ```python
> import json
> import jsonpath
> 
> obj = json.load(open('book.json', 'r', encoding='utf-8'))
> print(type(obj))
> 
> # 通过如下函数使用jsonpath
> # 参数1：json对象，参数2：jsonpath
> # $ 代表的是根节点
> # . 就类似于xpath里面的 /
> # 【路径含义】从根开始一步一步找到指定书本的作者，如果写*代表所有的book，写下标代表的是指定book，注意，下标从0开始，查找所有book的作者，必须写*
> ret = jsonpath.jsonpath(obj, '$.store.book[*].author')
> ret = jsonpath.jsonpath(obj, '$..author')
> ret = jsonpath.jsonpath(obj, '$.store..price')
> # 查找最后一本书
> ret = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
> ret = jsonpath.jsonpath(obj, '$..book[:2]')
> print(ret)
> ```

