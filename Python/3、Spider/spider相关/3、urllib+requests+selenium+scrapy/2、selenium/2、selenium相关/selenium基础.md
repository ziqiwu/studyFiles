### 不记文档，白忙一场

------

#### 0、概述

> ```python
> Selenium是一个Web的自动化测试工具，最初是为网站自动化测试而开发的，类型像我们玩游戏用的`按键精灵`，可以按指定的命令自动操作，不同是Selenium 可以直接运行在浏览器上，它支持所有主流的浏览器（包括PhantomJS这些无界面的浏览器）。
> 
> Selenium 可以根据我们的指令，让浏览器自动加载页面，获取需要的数据，甚至页面截屏，或者判断网站上某些动作是否发生。
> 
> Selenium 自己不带浏览器，不支持浏览器的功能，它需要与第三方浏览器结合在一起才能使用。但是我们有时候需要让它内嵌在代码中运行，所以我们可以用一个叫 PhantomJS 的工具代替真实的浏览器
> 
> Selenium 库里有个叫 WebDriver 的 API。WebDriver 有点儿像可以加载网站的浏览器，但是它也可以像 BeautifulSoup 或者其他 Selector 对象一样用来查找页面元素，与页面上的元素进行交互 (发送文本、点击等)，以及执行其他动作来运行网络爬虫
> ```

#### 1、安装

> ```python
> pip install selenium
> ```

#### 2、创建浏览器

##### 有头模式

> ##### 应用场景
>
> ```python
> 适用于本地代码调试，有头模式可以看得更清楚
> ```
>
> ##### 代码示例
>
> ```python
> from selenium import webdriver
> import time
> 
> # 创建谷歌浏览器对象, 参数就是谷歌浏览器的驱动
> #如果想省略参数，则chromedriver.exe必须放在一个path的路径下面(随便一个path路径中有的就可以，我现在是在google下面放的)spider_driver = webdriver.Chrome()
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> spider_driver = webdriver.Chrome(driver_dir)
> ```

##### 无头模式

> ##### 应用场景
>
> ```python
> 如果本地开发测试，使用本地的浏览器结合selenium使用就可以。但是放在生产环境的服务器上，是没有浏览器的，就需要使用无头浏览器。
> ```
>
> ##### 代码示例
>
> ```python
> from selenium import webdriver
> import time
> #这儿没有参数path=，所以chromedriver.exe必须放在一个path的路径下面(随便一个path路径中有的就可以，我现在是在google下面放的)
> chrome_options = webdriver.ChromeOptions()  
> chrome_options.add_argument('headless')
> 
> #如果参数是chrome_options=会提示不推荐
> spider_driver = webdriver.Chrome(options=chrome_options)  
> ```

#### 3、对浏览器操作

> #### 退出
>
> ```python
> spider_driver.close()
> spider_driver.quit()
> ```
>
> #### 前进
>
> ```python
> spider_driver.forward()
> ```
>
> #### 后退
>
> ```python
> spider_driver.back()
> ```
>
> #### 截屏
>
> ```python
> spider_driver.save_screenshot('douban1.png')
> ```
>
> #### 窗口切换
>
> ```python
> from selenium import webdriver
> import time
> 
> driver_dir = 'H:\chrome_down_pack\chrome_download_dir\chromedriver2.45\chromedriver.exe'
> driver = webdriver.Chrome(driver_dir)
> 
> driver.get('https://www.douban.com/')
> driver.implicitly_wait(10)
> driver.find_element_by_link_text('豆瓣电影').click()
> #--------------------------------------------------
> handles = driver.window_handles
> driver.switch_to.window(handles[0])
> time.sleep(4)
> driver.switch_to.window(handles[1])
> time.sleep(4)
> #--------------------------------------------------
> driver.close()
> driver.quit()
> ```

#### 4、解析浏览器

> #### 获取节点属性值
>
> ```python
> spider_driver.find_element_by_id('captcha_image').get_attribute('src')
> #【注】以后获取a标签中的url值，可以用这个办法，不一定要用正则匹配
> #get_attribute()
> ```
>
> #### 获取标签内的值
>
> ```python
> title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip('\n')
> #text 是属性
> ```
>

#### 5、对键盘操作

> ```python
> send_keys(Keys.BACK_SPACE)                   删除键
> send_keys(Keys.SPACE)                        空格键
> send_keys(Keys.TAB)                          制表键
> send_keys(Keys.ESPACE)                       回退键
> send_keys(Keys.ENTER)                        回车键
> send_keys(Keys.CONTROL,'a')                  全选
> send_keys(Keys.CONTROL,'c')                  复制
> send_keys(Keys.CONTROL,'x')                  剪切
> send_keys(Keys.CONTROL,'v')                  粘贴
> send_keys(Keys.F1)                           F1
> ```

#### 6、模拟滚动

> ```python
> #【注】https://blog.csdn.net/jlminghui/article/details/50477283
> from selenium import webdriver
> import time
> 
> driver = webdriver.Firefox()
> url = 'http://sc.chinaz.com/tupian/ribenmeinv.html'
> url = 'https://movie.douban.com/'
> driver.get(url)
> 
> # chrome浏览器
> js = 'document.body.scrollTop=10000'
> # firefox浏览器
> js = 'document.documentElement.scrollTop=10000'
> driver.execute_script(js)
> time.sleep(5)
> driver.quit()
> ```

#### 7、执行JavaScript语句

> ```python
> js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"
> 
> driver.execute_script('$(arguments[0]).fadeOut()',img)
> 
> driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
> ```

#### 8、动态页面模拟点击

> #### 导包
>
> ```python
> from selenium import webdriver
> from bs4 import BeautifulSoup
> import  time
> ```
>
> #### 初始化
>
> ```python
> def __init__(self):
>     path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
>     self.driver = webdriver.PhantomJS(path)
>     # self.driver = webdriver.Firefox()
>     # self.driver = webdriver.Chrome()
> ```
>
> #### 使用soup获取网页信息模拟点击下一页
>
> ```python
> # 具体的代码操作
> def douyu(self):
>     self.driver.get('http://www.douyu.com/directory/all')
>     while True:
>         # 指定xml解析
>         soup = BeautifulSoup(self.driver.page_source, 'xml')
>         # 返回当前页面所有房间标题列表 和 观众人数列表
>         # titles = soup.find_all('h3', {'class': 'ellipsis'})
>         # nums = soup.find_all('span', {'class': 'dy-num fr'})
>         titles = self.driver.find_elements_by_css_selector('h3.ellipsis')
>         nums = self.driver.find_elements_by_xpath('//span[@class="dy-num fr"]')
>         for num, title in zip(nums, titles[10:]):
>          	# print(u"观众人数:" + num.get_text().strip(), u"\t房间标题: " + title.get_text(
>             ).strip())
>             print(u"观众人数:" + num.text.strip(), u"\t房间标题: " + title.text.strip())
> 
>             # page_source.find()未找到内容则返回-1
>             flag = self.driver.page_source.find('shark-pager-disable-next')
>             if flag !=-1:
>                 break
>             try:
>                 num = self.driver.find_elements_by_xpath('//a[@class="shark-pager-item 						current"]')[0].text
>             except Exception as e:
>                 print('------------------',e)
>             print('-----------------------当前页码是： ', num)
>             
>             try:
>                 next = self.driver.find_element_by_class_name("shark-pager-next")
>                 next.click()
>             except Exception as e:
>                 print('发生异常----------------------： ',e)
> ```
>
> #### main函数中调用
>
> ```python
> if __name__ == "__main__":
>     douyu = DouyuSelenium()
>     douyu.douyu()
> ```

#### 9、关闭两个地方

> ```python
> #关闭fp
> fp.close()
> #关闭浏览器
> driver.close()
> driver.quit()
> ```



