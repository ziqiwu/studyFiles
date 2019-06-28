### 不记文档，白忙一场

------

#### ***面试***

> ```python
> xpath的语法有，比如：
> 	1> //和/，//是获取所有层级下匹配到的，/是获取下级一层匹配到的
> 	2> class等于什么
> 	3> class以什么开头
> 	4> 第几个
> 	好长时间不永，api名称模糊了，但是我都有记录的API文档，可以快速查询到这几个用法的API
> ```

#### 0、概述

> ```python
> 这个库是解析html的库，主要就是解析和提取数据
> ```

#### 1、安装

> ```python
> pip install lxml  -i https://pypi.douban.com/simple 
> 【注】-i参数以及后面的地址，是指国内源，豆瓣源。不加也可以，只是加了速度快。
> 【注】pip安装包的时候，要记得将fiddler关闭
> ```

#### 2、代码中使用

> #### python3.7之前
>
> ```python
> from lxml import etree
> ```
>
> #### python3.7之后
>
> ```python
> from lxml import html
> etree = html.etree
> ```
>
> #### 解析
>
> ```python
> html_etree = etree.parse('可以获取本地html文件')     
> html_etree = etree.HTML('网上获取的html字符串(也可以是字节类型)')
> html_etree.xpath('xpath路径')
> #【注】永远记住xpath返回的是一个列表
> 获取到节点对象之后obj
> obj.xpath('xpath路径')
> ```

#### 3、语法

> ```python
> from lxml import html
> from urllib import request,parse
> #永远记住xpath返回的是一个列表
> etree = html.etree
> 
> #注意：etree有parse、HTML、fromstring等解析方法
> 	'''	
>         html_etree = etree.parse('./test.html')
>         
>         html_etree = etree.fromstring(str)  #str是一段html字符串
> 
>         res = request.urlopen(url='http://www.baidu.com')
>         html_etree = etree.HTML(res.read().decode('utf-8'))
> 	'''
> #注意：*代表模糊匹配，如第七点所示
> #注意：//和/的区别
> 	'''
> 		//表示在该标签下所有层级标签匹配，报错儿子、孙子等
> 		/表示只在儿子标签内匹配
> 	'''
>     
> # 1、获取所有的li标签
> # li_list = html.xpath('//li')
> li_list = html.xpath('/html/body/div/ul/li')
> # print(li_list)
> 
> 
> # 2、获取li标签下的class属性
> c_list = html.xpath('//*/@*')
> # print(c_list)
> 
> #3、获取li标签下所有的span标签,
> # 标签中内容：element.text
> s_list = html.xpath('//li//span')
> # print(s_list[0].text)
> 
> # print(html.xpath('//li//span/text()'))
> 
> # 4、获取倒数第二个li标签
> r = html.xpath('//li[last()-1]')
> # print(r)
> # print(etree.tostring(r[0]).decode('utf-8'))
> # result = r[0].xpath('./a')
> # print(result)
> 
> # // 和 /  两个表示查询全部，不分层级；一个表示查询子层级，直属的标签
> span = r[0].xpath('.//span')
> # print(span)
> 
> # 5 、查询li 并且class值等于item-0
> r = html.xpath('//li[@class!="item-0"]')
> # print(r)
> 
> # 6、contains和not contains用法
> r = html.xpath('//li[contains(@class,"-inactive")]')
> # print(r)
> 
> r = html.xpath('//li[not(contains(@class,"-ina"))]')
> # print(r)
> 
> # 7、获取class 等于bold 的标签
> r = html.xpath('//*[@class="bold"]')
> # print(r)
> 
> r = html.xpath('//*[contains(text(),"items")]')
> print(r)
> ```

#### 4、抓取图片

> #### 概述
>
> ```python
> 抓取图片
> http://sc.chinaz.com/tupian/xingganmeinvtupian.html
> http://sc.chinaz.com/tupian/xingganmeinvtupian_2.html
> ```
>
> #### 代码
>
> ```python
> import urllib.request
> from lxml import etree
> import os
> import ssl
> 
> ssl._create_default_https_context = ssl._create_unverified_context
> 
> def handle_url(url):
> 	headers = {
> 		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
> 	}
> 	request = urllib.request.Request(url=url, headers=headers)
> 	return request
> 
> def download_image(image_url_list, name_list):
> 	# 获取文件夹名字
> 	dirpath = './images'
> 	# 遍历url列表，和名字列表
> 	for i in range(len(name_list)):
> 		# 根据url获取到图片的后缀名
> 		suffix = os.path.splitext(image_url_list[i])[-1]
> 		# 得到图片的全路径
> 		filepath = os.path.join(dirpath, name_list[i]) +suffix
> 		# 下载图片
> 		try:
> 			urllib.request.urlretrieve(image_url_list[i], filepath)
> 			print('%s 下载完毕' % filepath)
> 		except Exception as e:
> 			print('%s xxxxxxxxxxxxx图片丢失' % filepath)
> 
> def handle_data(request):
> 	response = urllib.request.urlopen(request)
> 	html = response.read().decode('utf-8')
> 	html_tree = etree.HTML(html)
> 	# print(type(html_tree))
> 	# //div[@id="container"]/div/div/a/img/@src
> 	image_url_list = html_tree.xpath('//div[@id="container"]/div/div/a/img/@src2')
> 	# print(len(image_url_list))
> 	# exit()
> 	name_list = html_tree.xpath('//div[@id="container"]/div/div/a/img/@alt')
> 	# 遍历image_url_list，依次下载图片
> 	download_image(image_url_list, name_list)
> 
> def main():
> 	start_page = int(input('请输入起始页面:'))
> 	end_page = int(input('请输入结束页面:'))
> 	url_tmp = 'http://sc.chinaz.com/tupian/xingganmeinvtupian'
> 	print('开始下载图片')
> 	for page in range(start_page, end_page + 1):
> 		if page != 1:
> 			url = url_tmp + '_' + str(page) + '.html'
> 		else:
> 			url = url_tmp + '.html'
> 		request = handle_url(url)
> 		handle_data(request)
> 	print('结束下载图片')
> 
> 
> if __name__ == '__main__':
> 	main()
> ```
>