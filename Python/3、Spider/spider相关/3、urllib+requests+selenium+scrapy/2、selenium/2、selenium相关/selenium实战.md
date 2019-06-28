### 不记文档，白忙一场

------

#### 爬取CSDN学院列表

> ```python
> #【注1】用微信二维码登录的时候，就让time睡会儿，拿手机在弹出页面，扫二维码，帮助程序往下执行，无头肯	定不能这么用了。所以这能用来自己玩儿的时候。
> #【注2】如果页面没有点击'显示更多'，则更多的内容，获取不到。虽然page_source里面内容都在
> from selenium import webdriver
> import time
> import pymysql
> 
> url = 'https://edu.csdn.net/mycollege'
> # 启动浏览器
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> driver.get(url)
> 
> #【注1】用微信二维码登录的时候，就让time睡会儿，拿手机在弹出页面，扫二维码，帮助程序往下执行，无头肯定不能这么用了。所以这能用来自己玩儿的时候。
> time.sleep(20)
> 
> res = driver.page_source
> driver.implicitly_wait(2)
> #【注】如果在chrome页面用xpath得出的路径，不能取到正确的值。则把page_source写入页面，分析
> with open('./csdn.html','w',encoding='utf-8') as fp:
>     fp.write(res)
> 
> driver.get('https://edu.csdn.net/course/detail/9995')
> res = driver.page_source
> driver.implicitly_wait(2)
> 
> with open('./info.html','w',encoding='utf-8') as fp:
>     fp.write(res)
> 
> #【注2】如果页面没有点击'显示更多'，则更多的内容，获取不到。虽然page_source里面内容都在
> driver.find_element_by_class_name('J_show_more_mask').click() #【注】页面的此处的class值为show_more_mask J_show_more_mask，如果这么写会报错，不能写组合的class选择器，所以只写后半个就可以
> driver.implicitly_wait(2)
> 
> #章的集合
> chapter_arr = driver.find_element_by_class_name('J_outline_content').find_elements_by_xpath('./dl')
> #挨个点开章
> #【注3】同注2，必须把剩下的章，都加上挨个点击事件，点开列表
> num =1
> for dl in chapter_arr:
>     if num == 1:
>         num += 1
>         continue
>     dl.click()
>     print('点开章：',dl.find_elements_by_xpath('./dt//span')[0].text.strip())
>     driver.implicitly_wait(1)
>     num += 1
> #每一个课程的对象集合
> item_arr = []
> #章的名称集合
> chapter_name_map = {}
> 
> no = 1
> for dl in chapter_arr:
>     #章名称
>     chapter_name = dl.find_elements_by_xpath('./dt//span')[0].text.strip()
>     print('=====:'+chapter_name)
>     chapter_name_map[str(no)] = chapter_name
> 
>     article_arr = dl.find_elements_by_xpath('./dd/ul/li')
>     for dd in article_arr:
>         #存放每一个小节的信息
>         item = {}
>         #小节名称
>         article_name = dd.find_element_by_xpath('./span[1]/a/span').text.strip()
>         print('---article_name:', article_name)
>         # 小节时间
>         article_time = dd.find_element_by_xpath('./span[last()]').text.strip()
>         print('---article_time:', article_time)
>         # 小节url
>         article_url = dd.find_element_by_xpath('./span/a').get_attribute('href') #【注】属性值的取值方式，不是find_element_by_xpath('./span/a/@href')，而是用get_attribute('属性名称')
>         print('---article_url:', article_url)
> 
>         # 小节对应章的序号
>         item['chapter_no'] = no
>         item['article_name'] = article_name
>         item['article_time'] = article_time
>         item['article_url'] = article_url
>         item_arr.append(item)
>     no += 1
> 
> print(item_arr)
> print(chapter_name_map)
> 
> host='127.0.0.1'
> port=3306
> user='root'
> password='123456'
> db='cdsn'
> charset='utf8'
> 
> conn = pymysql.connect(host=host,port=port,user=user,password=password,db=db,charset=charset)
> cursor = conn.cursor()
> 
> #章名称，存入数据库
> for chapter_no in chapter_name_map:
>     sql = 'insert into csdn_chapter (chapter_no,chapter_name) values("%s","%s")' % (chapter_no,chapter_name_map[chapter_no])
>     cursor.execute(sql)
>     conn.commit()
>     print('章名称，存入数据库',chapter_no)
> 
> #小节详情，存入数据库
> for item in item_arr:
>     sql = 'insert into csdn_article (chapter_no,article_name,article_time,article_url) values("%s","%s","%s","%s")' % (item['chapter_no'],item['article_name'],item['article_time'],item['article_url'])
>     cursor.execute(sql)
>     conn.commit()
>     print('小节详情，存入数据库',item['article_name'])
> driver.close()
> driver.quit()
> cursor.close()
> conn.close()
> exit()
> ```

#### 【实战】对百度首页进行设置

> ```python
> #【注】driver = webdriver.Chrome(driver_dir)这是带参数的，如果想不带参数，就把chromedriver.exe随便放到系统环境变量能访问到的一个路径下面。
> from selenium import webdriver
> from time import sleep
> 
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> # 用get打开百度页面
> driver.get("http://www.baidu.com")
> # 查找页面的“设置”选项，并进行点击
> sleep(2)
> driver.find_elements_by_link_text('设置')[0].click()
> sleep(2)
> # 打开设置后找到“搜索设置”选项，设置为每页显示50条
> driver.find_elements_by_link_text('搜索设置')[0].click()
> sleep(2)
> m = driver.find_element_by_id('nr')
> sleep(2)
> # m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
> m.find_element_by_xpath('.//option[3]').click()
> sleep(2)
> 
> # 点击保存设置
> driver.find_elements_by_class_name("prefpanelgo")[0].click()
> sleep(2)
> 
> # 处理弹出的警告页面   确定accept() 和 取消dismiss()
> # driver.switch_to_alert().accept()
> driver.switch_to.alert.dismiss()
> sleep(2)
> # 找到百度的输入框，并输入 美女
> driver.find_element_by_id('kw').send_keys('美女')
> sleep(2)
> # 点击搜索按钮
> driver.find_element_by_id('su').click()
> sleep(2)
> # 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
> driver.find_elements_by_link_text('美女_百度图片')[0].click()
> sleep(2)
> 
> # 关闭浏览器
> driver.quit()
> ```

#### 【实战】自定义百度页面

> ```python
> #【注】执行JS
> #【注】页面滚动
> from selenium import webdriver
> import time
> 
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> driver.get("https://www.baidu.com/")
> 
> # 给搜索输入框标红的javascript脚本
> js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
> 
> # 调用给搜索输入框标红js脚本
> driver.execute_script(js)
> 
> #查看页面快照
> driver.save_screenshot("redbaidu.png")
> 
> #js隐藏元素，将获取的图片元素隐藏
> img = driver.find_element_by_xpath("//div[@id='lg']/img")
> driver.execute_script('$(arguments[0]).fadeOut()',img)
> 
> time.sleep(5)
> 
> driver.get("https://movie.douban.com/")
> # 向下滚动到页面底部
> driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
> 
> #查看页面快照
> driver.save_screenshot("nullbaidu.png")
> 
> driver.quit()
> ```

#### 【实战】古诗文模拟登陆

> ```python
> from selenium import webdriver
> import time
> 
> url = 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx/'
> 
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> 
> driver.get(url)
> 
> driver.find_element_by_id('email').send_keys('455098435@qq.com')
> 
> driver.find_element_by_id('pwd').send_keys('31415926abc')
> 
> code = input('请输入验证码：')
> 
> driver.find_element_by_id('code').send_keys(code)
> 
> driver.find_element_by_id('denglu').click()
> 
> time.sleep(20)
> 
> driver.quit()
> ```

#### 【实战】ie浏览器操作cnaf

> ```python
> from selenium import webdriver
> import time
> from selenium.webdriver.common.keys import Keys
> 
> 
> 
> ie_path = 'H:\chrome_down_pack\chrome_download_dir\iedriver_win32_3.11\IEDriverServer.exe'
> driver=webdriver.Ie(executable_path=ie_path)
> url='http://10.18.76.201:8081/aqjk/loginController.do?login'
> driver.get(url)
> driver.implicitly_wait(10)
> 
> driver.find_element_by_id('userName').send_keys('admin')
> driver.find_element_by_id('password').send_keys('123456')
> driver.find_element_by_id('but_login').click()
> driver.implicitly_wait(3)
> 
> #【注0】这儿选择重新打开一个url而不是选择点击页面的gis的button，原因是点击gis的button完全没有效果。
> gis_path = 'http://10.18.76.201:8081/aqjk/loginController.do?login4'
> driver.get(gis_path)
> driver.implicitly_wait(10)
> 
> with open('./gisMap.text','w',encoding='utf-8') as fp:
>     fp.write(driver.page_source)
> 
> 
> #【注1】下面的行不通，原因是输入框的class属性值，会随着页面操作而改变，就比如选中时候，class值增加action一样，所以选择了通过xpath来找输入框。一开始以为是iframe的原因，一直提示没有这个class得选择器，最后排除。
> #【注2】通过输入框打开某个机场的视频，而不是通过点击某个gis标点的原因，是gis根本就选不中。没有办法选择选择器，所以选了折中的办法。
> #【注3】选择send_keys(Keys.ENTER)通过键盘来控制确定，而不是像登录时候一样选择点击，原因是页面做的是模糊查询，把查询结果列出来一列，就想百度搜索一样。还好选择回车可以出结果，否则还需要一通麻烦
> # driver.find_element_by_css_selector('.unitSelection blueTxt').send_keys('华北公司')
> # driver.find_element_by_class_name('unitSelection blueTxt').send_keys('华北公司')
> # driver.find_element_by_class_name('unitSelection blueTxt').send_keys(Keys.ENTER)
> 
> #【注4】直接运行js的方法给输入框赋值，也是可行的。
> # driver.execute_script('$(".unitSelection").val("华北公司")')
> 
> driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/input').send_keys("华北公司")
> driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
> driver.implicitly_wait(3)
> driver.find_element_by_xpath('//div[@id="companydetail"]/div/div[2]/div/div[2]').click()
> driver.implicitly_wait(3)
> time.sleep(10)
> 
> 
> 
> # gisMap = driver.find_elements_by_xpath('//div[@id="sidebar-shortcuts-large"]/button[@class="btn btn-danger gisMap"]')[0]
> # gisMap.click()
> # driver.implicitly_wait(10)
> #
> # handles = driver.window_handles
> # driver.switch_to.window(handles[0])
> # time.sleep(4)
> # driver.switch_to.window(handles[1])
> # time.sleep(4)
> #关闭浏览器
> #driver.close()
> exit()
> 
> 
> 
> 
> 
> #以下是通过谷歌浏览器进行模拟操作
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> driver.get('http://10.18.76.201:8081/aqjk/loginController.do?login')
> driver.implicitly_wait(10)
> driver.find_element_by_id('userName').send_keys('admin')
> driver.find_element_by_id('password').send_keys('aqscjK,6789')
> driver.find_element_by_id('but_login').click()
> driver.implicitly_wait(3)
> driver.save_screenshot('cnaf.png')
> exit()
> ```

#### 有验证码的登录

> ```python
> #【注】多窗口切换
> #【注】手动输入验证码
> #【注】放大显示图片
> from selenium import webdriver
> import time
> from selenium.webdriver.common.keys import Keys
> from PIL import Image
> import requests
> 
> url = 'http://www.douban.com/accounts/login'
> # 启动浏览器
> path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
> driver = webdriver.Chrome()
> # driver = webdriver.PhantomJS()
> 
> driver.get(url)
> # 输入用户名和密码
> driver.find_element_by_name('form_email').send_keys('18513106743')
> driver.find_element_by_name('form_password').send_keys('31415926abc')
> 
> image_url = driver.find_element_by_id('captcha_image').get_attribute('src')
> response = requests.get(image_url,verify = False)
> 
> with open('image_code.jpg','wb') as file:
>     file.write(response.content)
> 
> Image.open('image_code.jpg').show()
> driver.save_screenshot('code123.png')
> 
> code = input('请输入验证码：')
> 
> driver.find_element_by_name('captcha-solution').send_keys(code)
> 
> #模拟点击登录
> driver.find_element_by_xpath('//input[@class="btn-submit"]').click()
> 
> time.sleep(2)
> # 生成登录快照
> driver.save_screenshot('douban.png')
> 
> driver.find_element_by_xpath('//div[@class = "global-nav-items"]/ul/li[3]').click()
> time.sleep(2)
> 
> # 多窗口切换，无界面PhantomJS不行
> handles = driver.window_handles
> driver.switch_to.window(handles[0])
> time.sleep(3)
> driver.switch_to.window(handles[1])
> time.sleep(3)
> driver.switch_to.window(handles[0])
> 
> # 保存网页数据
> with open('douban.txt','w',encoding='utf-8') as file:
>     file.write(driver.page_source)
> 
> # 结束任务
> time.sleep(3)
> driver.quit()
> ```

#### 操作下一面，判断最后一页

> ```python
> from selenium import webdriver
> import time
> import json
> ########################不是第一次犯这个错误了
> #li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
> #    for li_one in li_list:
>         #某一个主播
>         #title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip('\n')
>         #路径应该是.//而不是//
> #xpath中使用text，应该是'//xx/xx'.text 是属性  title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text
> #driver.page_source  是属性
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> 
> #打开浏览器
> driver.get('https://www.douyu.com/directory/all')
> driver.implicitly_wait(12)
> #循环所有页，直到最后一页退出
> fp = open('./douyu.txt','w',encoding='utf-8')
> num = 1
> 
> while True:
>     #每循环一次，就新创建一个数组s
>     items = []
>     time.sleep(3)
>     # 一页的所有li集合
>     li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
>     print('第%d页有%d条数据'%(num,len(li_list)))
>     # with open('./douyu.html','w',encoding='utf-8') as fpp:
>     #     fpp.write(driver.page_source)
>     #抓取某一页的数据
>     for li_one in li_list:
>         #某一个主播
>         title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip('\n')
>         type = li_one.find_element_by_xpath('.//span[@class="tag ellipsis"]').text
>         broadcaster = li_one.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
>         hot = li_one.find_element_by_xpath('.//span[@class="dy-num fr"]').text
> 
>         item_map = {
>             'title':title,
>             'type':type,
>             'broadcaster':broadcaster,
>             'hot':hot
>         }
>         items.append(item_map)
>     # 全部爬完，就写入文件
>     fp.write(json.dumps(items, ensure_ascii=False)+'\n')
>     #爬完一页，就判断是否是最后一页，若是，则跳出循环
>     if driver.page_source.find('shark-pager-next shark-pager-disable shark-pager-disable-next') != -1 or num>=3:
>         break
>     # 若不是，则点击下一页
>     driver.find_element_by_class_name('shark-pager-next').click()
>     num = num + 1
> #关闭fp
> fp.close()
> #关闭浏览器
> driver.close()
> ```

