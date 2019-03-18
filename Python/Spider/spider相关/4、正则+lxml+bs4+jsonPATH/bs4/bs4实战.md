### 不记文档，白忙一场

------

#### 简单爬取智联招聘数据

> ​	url:
>
> ```python
> 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&p=1'
> ```
>
> ​	代码：
>
> ```python
> import urllib.request
> from bs4 import BeautifulSoup
> 
> url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&p=1'
> 
> headers = {
> 	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
> }
> 
> request = urllib.request.Request(url=url, headers=headers)
> response = urllib.request.urlopen(request)
> 
> soup = BeautifulSoup(response.read(), 'lxml')
> 
> # print(soup)
> # 
> jobname = soup.select('.zwmc > div > a')[0].string
> company = soup.select('.gsmc > a')[0].string
> salary = soup.select('.zwyx')[1].string
> area = soup.select('.gzdd')[1].string
> 
> print(jobname)
> print(company)
> print(salary)
> print(area)
> ```

#### 批量爬取智联招聘数据

> ​	url:
>
> ```python
> 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
> ```
>
> ​	代码：
>
> ```python
> import urllib.request
> from bs4 import BeautifulSoup
> import urllib.parse
> import json
> 
> class ZhiLian(object):
> 	"""docstring for ZhiLian"""
> 	def __init__(self, url, area, gangwei, start_page, end_page):
> 		super(ZhiLian, self).__init__()
> 		self.url = url
> 		self.area = area
> 		self.gangwei = gangwei
> 		self.start_page = start_page
> 		self.end_page = end_page
> 		self.headers = {
> 			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537'
> 		}
> 		self.items = []
> 
> 	# 将url生成请求对象的函数
> 	def handle_url(self, page):
> 		data = {
> 			'jl': self.area,
> 			'kw': self.gangwei,
> 			'p': page
> 		}
> 		data = urllib.parse.urlencode(data)
> 		url = self.url + data
> 		request = urllib.request.Request(url=url, headers=self.headers)
> 		return request
> 
> 	# 处理下载请求的函数
> 	def download(self, request):
> 		response = urllib.request.urlopen(request)
> 		data = response.read()
> 		soup = BeautifulSoup(data, 'lxml')
> 		# print(soup,data)
> 		table_list = soup.select('#newlist_list_content_table > table')[1:]
> 		for table in table_list:
> 			item = {}
> 			# 获取职位名称
> 			zwmc = table.select('.zwmc > div > a')[0].get_text()
> 			# 去除最后的&nbsp
> 			zwmc = zwmc.strip()
> 			# 获取公司名称
> 			gsmc = table.select('.gsmc > a')[0].string
> 			# 获取职位月薪
> 			zwyx = table.select('.zwyx')[0].string
> 			# 获取工作地点
> 			gzdd = table.select('.gzdd')[0].string
> 			item['zwmc'] = zwmc
> 			item['gsmc'] = gsmc
> 			item['zwyx'] = zwyx
> 			item['gzdd'] = gzdd
> 			self.items.append(item)
> 
> 	# 对外提供的接口函数
> 	def start(self):
> 		for page in range(self.start_page, self.end_page + 1):
> 			request = self.handle_url(page)
> 			self.download(request)
> 		# 将保存的内容写入到文件中
> 		string = json.dumps(self.items, ensure_ascii=False)
> 		with open('zhilian.json', 'w', encoding='utf-8') as fp:
> 			fp.write(string)
> 
> def main():
> 	url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
> 	area = input('请输入工作地点:')
> 	gangwei = input('请输入工作岗位:')
> 	start_page = int(input('请输入起始页面:'))
> 	end_page = int(input('请输入结束页面:'))
> 	
> 	obj = ZhiLian(url, area, gangwei, start_page, end_page)
> 	obj.start()
> 
> 
> if __name__ == '__main__':
> 	main()
> ```

#### 腾讯社招数据爬取

> ​	url:
>
> ```python
> http://hr.tencent.com/position.php?&start=0#a
> ```
>
> ​	代码：
>
> ```python
> import requests
> from bs4 import BeautifulSoup
> import json
> 
> 
> def tencent():
>     url = 'http://hr.tencent.com/position.php?&start=10#a'
>     head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
>     response = requests.get(url,headers = head)
> 	# 成功获取数据
>     html = BeautifulSoup(response.text,'lxml')
>     # 属性查找
>     result = html.select('tr[class="even"]')
>     result2 = html.select('tr[class=odd]')
> 
>     result += result2
>     items = []
>     for site in result:
> 		# 获取数据
>         name = site.select('td a')[0].get_text()
>         detail_link=url+site.select('td a')[0].attrs['href']
>         category = site.select('td')[1].get_text()
>         recruit_number = site.select('td')[2].get_text()
>         location = site.select('td')[3].get_text()
>         date = site.select(('td'))[4].get_text()
>         item = {}
>         item['name'] = name
>         item['detail_link'] = detail_link
>         item['category'] = category
>         item['recruit_number'] = recruit_number
>         item['location'] = location
>         item['date'] = date
>         items.append(item)
> 
> 	# 保存json数据
>     with open('./tencent.json','bw') as file:
>         line = json.dumps(items, ensure_ascii=False)
>         file.write(line.encode('utf-8'))
>         print('数据保存成功')
> 
> if '__main__' == __name__:
>     tencent()
> ```