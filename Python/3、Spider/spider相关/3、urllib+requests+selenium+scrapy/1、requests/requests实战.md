### 不记文档，白忙一场

------

#### 批量爬取阳光宽频网视频

> ​	fiddler抓包确认url
>
> ```python
> url = 'https://365yg.com/'
> 
> ajax_url =' https://365yg.com/api/pc/feed/?category=video&utm_source=toutiao&widen=3&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1253AF48A0FCE5&cp=5A4A4F4CAEE59E1&_signature='
> ```
>
> ​	使用requests进行下载
>
> ```python
> import requests
> from lxml import etree
> import json
> from selenium import webdriver
> import time
> 
> def handle_video(name, url):
> 	headers = {
> 		'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/
> 		4.0.1'
> 	}
> 	driver = webdriver.PhantomJS()
> 	# 向指定地址发送请求
> 	driver.get(url)
> 	# 让程序稍微休眠一下，去执行里面的js代码
> 	time.sleep(5)
>     
> 	# 【注】得到网页源代码,此时page_source是执行js之后的网页代码
> 	html_tree = etree.HTML(driver.page_source)
> 	video_src = html_tree.xpath('//video[@class="vjs-tech"]/source/@src')[0]
> 	r = requests.get(url=video_src, headers=headers)
> 	filename = './video/' + name + '.mp4'
> 	with open(filename, 'wb') as fp:
> 		fp.write(r.content)
> 	print(filename + '下载完毕')
> 
> def handle_index(json_url):
> 	headers = {
> 		'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/
> 		4.0.1'
> 	}
> 	r = requests.get(url=json_url, headers=headers,verify = False)
> 	obj = json.loads(r.text)
> 	print('开始下载。。。。。。。')
> 	for video_obj in obj['data']:
> 		# 获取视频名字
> 		name = video_obj['title']
> 		# 获取视频连接
> 		video_url = 'https://365yg.com' + video_obj['source_url']
> 		# 获取视频连接，并且下载视频
> 		handle_video(name, video_url)
> 	print('结束下载。。。。。。。')
> 
> def main():
> 	json_url = 'https://365yg.com/api/pc/feed/?category=video&utm_source=toutiao&widen=3&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1253AF48A0FCE5&cp=5A4A4F4CAEE59E1&_signature='
> 	handle_index(json_url)
> 
> if __name__ == '__main__':
> 	main()
> ```

#### 批量爬取今日头条视频

> ​	fiddler抓包确认url
>
> ```python
> url_base = 'https://www.toutiao.com/'
> 
> ajax_url ='https://365yg.com/api/pc/feed/?category=video&utm_source=toutiao&widen=3&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1253AF48A0FCE5&cp=5A4A4F4CAEE59E1&_signature='
> 
> !!!对这个今日头条视频url进行网络请求时必须添加header{'Referer': 'https://www.ixigua.com/?utm_source=toutiao&utm_medium=video_channel'}，有跳转，不然数据无法获取
> ```
>
> ​	使用requests进行下载
>
> ```python
> from selenium import webdriver
> import requests
> import json
> import time
> 
> base_url = 'https://www.toutiao.com/'
> 
> def download_video(title, video_page_url):
> 
>     driver = webdriver.PhantomJS()
>     driver.get(video_page_url)
>     # 休眠，为了将所有的数据都加载出来
>     time.sleep(3)
> 
>     video_url = driver.find_elements_by_xpath('//video[@class="vjs-tech"]/source')[0].get_attribute('src')
> 
>     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
> 
>     r = requests.get(video_url,headers = headers)
> 
>     with open('%s.mp4'%title,'wb') as file:
>         file.write(r.content)
>     print('成功下载视频：%s'%(title))
>     pass
> 
> 
> def spider(url):
>     headers = {
>         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
>         'Referer': 'https://www.ixigua.com/?utm_source=toutiao&utm_medium=video_channel'
>                    ''}
>     response = requests.get(url, headers=headers,verify = False)
>     
>     # 保存json数据
>     with open('toutiao.json', mode='w', encoding='utf-8') as file:
>         loads = json.loads(response.text)
>         file.write(json.dumps(loads,ensure_ascii=False))
> 
>     j_data = json.loads(response.text)
>     print('开始下载……')
>     for video_info in j_data['data']:
>         video_page_url = base_url+video_info['source_url']
>         title = video_info['title']
>         print(title,video_page_url)
>         # 调用方法下载video
>         download_video(title,video_page_url)
>     print('下载结束…………')
> 
> if __name__ == '__main__':
>     url = 'https://www.toutiao.com/'
>     ajax_url = 'https://www.ixigua.com/api/pc/feed/?min_behot_time=0&category=video_new&' \ 'utm_source=toutiao&widen=1&tadrequire=true&as=A135FA25492F69B&cp=5A59DF86491B8E1&_signature=6j9f-hAasHEkVNkob36ofeo.X'
>     spider(ajax_url)
> ```
>
> 