### 一、Django基础、前期准备环境

##### 1 virtualenv的概述

```
virtualenv是用来创建Python的虚拟环境的库，虚拟环境能够独立于真实环境存在，可以同时有多个互相独立的Python虚拟环境，每个虚拟环境都可以营造一个干净的开发环境，对于项目的依赖、版本的控制有着非常重要的作用。

虚拟环境有什么意义？
	如果我们要同时开发多个应用程序，应用A需要Django1.11，而应用B需要Django1.8怎么办？
	这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。
	virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。
```

##### 2 pip的常用命令

```
  安装pip
   	python: sudo apt install python-pip
  更新pip: 
  	pip install --upgrade pip
  	pip3 install xxx:安装xxx依赖包
    	pip3 list:查看所有依赖包
    	pip3 freeze:查看新安装的包
    	pip3 uninstall xxx ：卸载xxx包
```

##### 3  虚拟环境的安装和使用

```python
  	a, 安装虚拟环境
  		sudo apt update
  		sudo apt install virtualenvwrapper
  		如果不能使用虚拟环境命令，则需要配置环境变量
  		1, 进入目录: cd ~
  		2, 使用vim打开.bashrc, 定位到最后:shift+g，并添加以下3行代码
            # python
  			export WORKON_HOME=/home/chen/.virtualenvs
  			source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
  		3, 在家目录创建.virtualenvs目录: mkdir .virtualenvs
  		4, 加载修改后的设置，使之生效：source .bashrc	

  	b, 创建虚拟环境: 
  			mkvirtualenv env
            下面是根据版本创建虚拟环境。
  			mkvirtualenv env2  -p  /usr/bin/python 安装python2虚拟环境
             mkvirtualenv env3  -p  /usr/bin/python3 安装python3虚拟环境
  	c, 退出虚拟环境
  		deactivate 
    	进入虚拟环境: 
  		workon 虚拟环境名称
```

##### 4 安装Django

```python
注意：一个虚拟环境安装一次django
切换到root用户:  sudo -s
安装Django: pip3 install django（也可指定某一版本 pip3 install django==1.11）

测试Django是否安装成功 

进入python环境
	import django
	django.get_version()
```

##### 5 创建一个Django项目

```python
进入到指定要存放项目的目录，执行  xxx  来创建一个名字为xxx的工程
注意：一定要用普通用户创建项目，否则后面有很多麻烦事情。
	su xiaoguo之后django-admin startproject projectDay02还是报错，需要安装django
    其实env3的虚拟环境中，已经安装过django了
    所以，workon env3，进入虚拟环境
    再执行django-admin startproject projectDay02即可创建新的Django项目成功
```

##### 6 启动Django服务器

```
python manage.py runserver [ip:port]
python manage.py runserver 8002  8002指定端口，可以不写

可以直接进行服务运行 默认执行起来的端口是8000
也可以自己指定ip和端口：
监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）：python manage.py runserver 0.0.0.0:8000 
如果是外网或者局域网电脑上可以用其它电脑查看开发服务器，访问对应的 ip加端口，比如 10.36.132.2:8000
浏览器访问:http://localhost:8000 可以看到服务器启动成功
```

##### 7 数据迁移

```
迁移的概念:就是将模型映射到数据库的过程
生成迁移:python manage.py makemigrations
执行迁移:python manage.py migrate
```

##### 8 创建一个Django应用

```
python manage.py startapp XXX
创建名称为XXX的应用
使用应用前需要将应用配置到项目中，在settings.py中将应用加入到INSTALLED_APPS选项中
```

##### 9 Admin 后台管理

```
在admin.py中将model加入后台管理：
from django.contrib import admin  #这句话自带有
from .models import *
admin.site.register(Grade)
创建超级用户：python manage.py createsuperuser
访问admin后台：http://127.0.0.1:8000/admin/
```

##### 10、url反向解析

```
使用url给视图函数传参数
在url配置中将正则部分小括号括起来。比如：
	url(r'^time/plus/(\d{1,2})/$', views.hours_ahead)
如果有多个参数则用/隔开，参数需要用分组，比如：
	url(r'^time/plus/(\d{1,2})/(\d{1,2})/$', views.hours_ahead),
给参数命名，使用正则分组的别名，比如：
	url(r'^time/plus/(?P<time1>\d{1,2})/(?P<time2>\d{1,2})/$', views.hours_ahead)
使用分组别名之后，视图函数的参数必须用分组的别名，但是位置可以不固定。

给url取别名，那么在使用此url的地方可以使用别名。比如：
	url(r'^buy/$', views.buy, name='buy'),
	url(r'^login/$', views.login, name='login'),
```

```
在视图函数中，反向解析url：
    from django.shortcuts import render, redirect
    from django.urls import reverse
    def buy(request):
        return redirect(reverse('index'))
        return redirect(reverse('detail', args=[2]))
        return redirect(reverse('detail', kwargs={"id": 2}))
	
在templates中，使用别名：
	{% url 'detail' stu.id %}

使用命名空间:
    在工程的urls.py文件中，在include时，可以指定命名空间，更加细化的划分url。比如： 
		url(r'^App/', include('App.urls', namespace='App')),
	指定命令空间后，使用反向解析时需要加上命名空间，比如：
		在视图函数中: return redirect(reverse('students:index'))
		在templates中: {% url 'students:detail' %}
注意：项目下的urls路由要习惯加namespace，应用下的urls路由要习惯加name，一个namespace+name可以唯一确定	view控制器返回的页面
```

##### 11、模板

```
模板中的变量: 视图传递给模板的数据，遵守标识符规则
	语法： {{ var }}
	如果变量不存在，则插入空字符串
模板主要有两个部分
	HTML静态代码
	动态插入的代码段（挖坑，填坑）
	from django.template import Template, Context
	t = Template('My name is {{ name }}.')    //挖坑
	c = Context({'name': 'Nige'})   //填坑的土
	t.render(c)   //填坑
模板中的点语法	
	from django.template import Template, Context
	person = {'name': 'Sally', 'age': '43'}
	t = Template('{{ person.name }} is {{ person.age }} years old.')
	c = Context({'person': person})
	t.render(c)
方法不能有参数。
	#只能写upper，不能写upper()
	from django.template import Template, Context
	t = Template('{{ var }} -- {{ var.upper }} -- {{ var.isdigit }}')
	t.render(Context({'var': 'hello'}))
	'hello -- HELLO -- False'
列表，使用索引，不允许负索引	
	from django.template import Template, Context
	t = Template('Item 2 is {{ items.2 }}.')
	c = Context({'items': ['apples', 'bananas', 'carrots']})
	t.render(c)
	'Item 2 is carrots.'
	
if 语句：
	if单分支
		{% if  表达式 %}
	    	语句
		{% endif  %}
	if双分支
		{%  if 表达式 %}
	    	语句
		{% else  %}
	    	语句
		{% endif %}
	if多分支
		{% if 表达式 %}
        	语句	
 		{% elif 表达式 %}
        	语句
        {% else  %}
	    	语句
		{% endif %}
判断true或false
		{% if today_is_weekend %}
			<p>Welcome to the weekend!</p>
		{% endif %}
使用and or not,可结合使用，and具有更高优先权。
		{% if athlete_list and coach_list %}
	    	<p>Both athletes and coaches are available.</p>
		{% endif %}
	
		{% if not athlete_list %}
	    	<p>There are no athletes.</p>
		{% endif %}
	
		{% if athlete_list or coach_list %}
	    	<p>There are some athletes or some coaches.</p>
		{% endif %}
		
		{% if not athlete_list or coach_list %}
			<p>There are no athletes or there are some coaches.</p>
		{% endif %}

		{% if athlete_list and not coach_list %}
			<p>There are some athletes and absolutely no coaches.</p>
		{% endif %}
使用多个相同的逻辑操作关键字也是允许的，比如：
		{% if athlete_list or coach_list or parent_list or teacher_list %}
	使用in和not in，
		{% if "bc" in "abcdef" %}
			This appears since "bc" is a substring of "abcdef"
		{% endif %}
		{% if user not in users %}
			If users is a list, this will appear if user isn't an element of the list.
		{% endif %}
	使用is 和is not
		{% if somevar is True %}
			This appears if and only if somevar is True.
		{% endif %}

		{% if somevar is not None %}
			This appears if somevar isn't None.
		{% endif %}
for 语句：
	{% for 变量 in 列表 %}
		语句1
	{% empty %}
		语句2
	{% endfor %}
	当列表为空或不存在时,执行empty之后的语句
	
	{{ forloop.counter }}: 表示当前是第几次循环，从1数数
	{% for item in todo_list %}
	    <p>{{ forloop.counter }}: {{ item }}</p>
	{% endfor %}
	
	{{ forloop.counter0}}表示当前是第几次循环，从0数数
	{{ forloop.revcounter}}表示当前是第几次循环，倒着数数，到1停
	{{ forloop.revcounter0}}表示当前第几次循环，倒着数，到0停
	{{ forloop.first }} 是否是第一个  布尔值
	{% for object in objects %}
	    {% if forloop.first %}
	        <li class="first">
	    {% else %}
	        <li>
	    {% endif %}
	    {{ object }}</li>
	{% endfor %}
	
	{{ forloop.last }} 是否是最后一个 布尔值
	{% for link in links %}
		{{ link }}{% if not forloop.last %} | {% endif %}
	{% endfor %}
	
	forloop.parentloop
	{% for country in countries %}
	  <table>
	      {% for city in country.city_list %}
	      <tr>
	          <td>Country #{{ forloop.parentloop.counter }}</td>
	          <td>City #{{ forloop.counter }}</td>
	          <td>{{ city }}</td>
	      </tr>
	      {% endfor %}
	  </table>
	 {% endfor %}
	 
注释：
	单行注释
	{#  被注释掉的内容  #}
	多行注释
	{% comment %}
		内容
	{% endcomment %}
	
过滤器: 
	{{ var|过滤器 }}
	作用：在变量显示前修改
	add	{{ value|add:2 }}
	没有减法过滤器，但是加法里可以加负数
		{{ value|add:-2 }}
	lower 	
		{{ name|lower }}
	upper
		{{ my_list|first|upper }}
	截断：
		{{ bio|truncatechars:30 }}
	过滤器可以传递参数，参数需要使用引号引起来
	比如join：	{{ students|join:'=' }}
	
	默认值:default，格式 {{var|default:value}}
	如果变量没有被提供或者为False，空，会使用默认值

	根据指定格式转换日期为字符串，处理时间的
	就是针对date进行的转换	
		{{  dateVal | date:'y-m-d' }}
		
HTML转义
	将接收到的数据当成普通字符串处理还是当成HTML代码来渲染的一个问题

	渲染成html:{{ code|safe }}
	关闭自动转义
	{% autoescape off%}
		code
	{% endautoescape %}
	打开自动转义转义
	{% autoescape on%}
		code
	{% endautoescape %}
	
模板继承
    如果在外面吧所有的HTML写到一起，需要设置settings.py中TEMPLATES中 'DIRS'路径
         'DIRS': [os.path.join(BASE_DIR,'templates')],
	block:挖坑
		{% block XXX%}
			code
		{% endblock %}

	extends 继承，写在开头位置
		{% extends '父模板路径' %}

	include: 加载模板进行渲染
         {% include '模板文件' %}
语法附加：
	{% extends 'base.html' %}
    {% block title %}
        这是我的block页面
    {% endblock %}
    {% block content %}
        <div style="background: green;width: 100%;height: 1000px;text-align: center"></div>
    {% endblock %}

    <script>
        $(function () {
            alert(1);
            console.log("hello jQuery");
        })
    </script>
```

##### 12、进入Django环境下的python

```
python manage.py shell: 进入Python环境, 且会自动导入Django配置，建议使用
>>> python manage.py shell   # 进入python环境
>>> from django import template
>>> t = template.Template('My name is {{ name }}.')
>>> c = template.Context({'name': 'Nige'})
>>> print (t.render(c))
My name is Nige.
>>> c = template.Context({'name': 'Barry'})
>>> print (t.render(c))
My name is Barry.
```

##### 13、创建完整的Django项目流程

1、项目用xiaoguo普通用户创建，不光是普通用户，还一定要用workon env3，然后django-admin startproject 

​	newPorjectName。因为虚拟环境就是安装了好多包的一个环境，里面安装了django，所以可以用django-

​	admin命令。

2、做数据迁移：

​	改settings配置文件的databases项，改成所用数据库，然后

3、python manage.py createsuperuser 创建后台登录用户

4、from django.contrib import admin

​	from .models import Student

​	admin.site.register(Student)   使该应用可以在后台管理

5、在settings中改两个配置项：

​	LANGUAGE_CODE = 'zh-hans'       后台显示都是中文了

​	TIME_ZONE = 'Asia/Shanghai'	    显示时间

注意：1、项目创建完成之后，需要makemigrations和migrate，如果是新建了应用，需要在settings中加入，否	

​		则运行了命令，也不会生成某班的数据库文件。

​	    2、在虚拟环境中，用xiaoguo进入mysql -uroot -p是进不去的，用su root可以，但是运行项目，不要乱切	

​		换到root，否则又会很乱。所以做法是新建一个用户，赋予所有权限。在settings也是配置该用户

​	     3、在env3下用python manage.py makemigrations执行数据迁移的时候，报错：

​		django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 

​		'MySQLdb'.

​		则是包是新版本，赶潮流的问题，需要在django项目下的`__init__.py`中加入两行代码：

​		import pymysql

​		pymysql.install_as_MySQLdb()

​	     4、在Typora里写`__init__`,是鼠标引起来以后，点格式，代码，或者快捷键：ctrl+shift+`

​	     5、尝试新建一个虚拟环境，总结里面都需要安装哪些包，比如MySQL-python等，或者因为

​		  在`__init__.py`中已经写了pymysql.install_as_MySQLdb()，是不是直接安装pymysql就可以了。

​		  目前知道的环境依赖包有：Django，pymysql

​	      6、比如在settings配置文件中，换了数据库，原来是mydb现在是mydb2，或者原来用的自带的数据库，

​			现在用的是mysql，都必须重新python manage.py makemigrations，也就必须重新python 	

​			manage.py createsuperuer，因为本来这些数据都是在自动生成的数据库表--user表、group等表		

​			中存储的。所以以上情况，都必须重新生成超级管理用户，因为表是有了，只是空表。

​		7、执行python manage.py命令，需要workon env3进入虚拟环境执行，因为它的依赖的包都在虚拟

​			环境中