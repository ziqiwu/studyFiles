### 不记文档，白忙一场

------

#### 概述

> ```python
> JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，它使得人们很容易的进行阅读和编写。同时也方便了机器进行解析和生成。适用于进行数据交互的场景，比如网站前台与后台之间的数据交互。
> 
> JSON和XML的比较可谓不相上下。
> ```

#### 对象

> ```python
> 对象：对象在js中表示为{ }括起来的内容，数据结构为 { key：value, key：value, ... }的键值对的结构，在面向对象的语言中，key为对象的属性，value为对应的属性值，所以很容易理解，取值方法为 对象.key 获取属性值，这个属性值的类型可以是数字、字符串、数组、对象这几种。
> ```

#### 数组

> ```python
> 数组：数组在js中是中括号[ ]括起来的内容，数据结构为 ["Python", "javascript", "C++", ...]，取值方式和所有语言中一样，使用索引获取，字段值的类型可以是 数字、字符串、数组、对象几种。
> ```

#### JOSN方法

> ​	json文件
>
> ```python
> { "store": {
>     "book": [ 
>       { "category": "reference",
>         "author": "李白",
>         "title": "Sayings of the Century",
>         "price": 8.95
>       },
>       { "category": "fiction",
>         "author": "杜甫",
>         "title": "Sword of Honour",
>         "price": 12.99
>       },
>       { "category": "fiction",
>         "author": "白居易",
>         "title": "Moby Dick",
>         "isbn": "0-553-21311-3",
>         "price": 8.99
>       },
>       { "category": "fiction",
>         "author": "苏轼",
>         "title": "The Lord of the Rings",
>         "isbn": "0-395-19395-8",
>         "price": 22.99
>       }
>     ],
>     "bicycle": {
>       "color": "red",
>       "price": 19.95
>     }
>   }
> }
> ```
>
> ​	load打开文件
>
> ```python
> 读取文件中json形式的字符串元素 转化成python类型
> obj = json.load(open('book.json', 'r', encoding='utf-8'))
> print(type(obj))
> ```
>
> ​	loads字符串
>
> ```python
> 把Json格式字符串解码转换成Python对象
> 从json到python的类型转化对照如图所示
> 
> with open('./book.json',mode='r',encoding='utf-8') as f:
>     json_string = f.read()
> # 将json格式字符串转化为对象
> obj = json.loads(json_string)
> print(type(obj))
> 
> 
> JSON    Python
> object  dict
> array   list
> string  unicode
> number(int)  int,long
> number(real)  float
> true    True
> false   False
> null    None
> ```
>
> ​	dump
>
> ```python
> 将Python内置类型序列化为json对象后写入文件
> 
> import json
> 
> dictStr = {"city": "北京", "name": "大刘",'info':'\u8c22\u8c22\u5927'}
> # Serialize ``obj`` as a JSON formatted stream to ``fp
> json.dump(dictStr, open("dictStr.json","w",encoding='utf-8'), ensure_ascii=False,)
> ```
>
> ​	dumps
>
> ```python
> 实现python类型转化为json字符串，返回一个str对象 把一个Python对象编码转换成Json字符串
> 从python原始类型向json类型的转化对照
> 
> import json
> str = '''{"has_more": false, "message": "success", "data": [{"single_mode": true, "abstract": "\u8c22\u8c22\u5927\u5bb6\u559c\u6b22\u6bcf\u65e5\u64b8"}]}'''
> 
> print(type(str))
> print(json.dumps(str,ensure_ascii=False))
> ```