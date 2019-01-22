

### 不记文档，白忙一场

------

#### 报错信息

**selenium.common.exceptions.WebDriverException: Message: unknown error: cannot find Chrome binary** 

> ​	描述
>
> ```python
> 原因是，电脑上安装的chrome版本和chromedriver版本不一致导致的。
> 但是：我的chrome是v63，在网上搜到的对应驱动器版本是v2.35或者v2.36。
> 	我也去对应国内镜像网站上下载了，两种版本都试了，还是报错。
> ```
>
> ​	解决
>
> ```python
> 我到google官网上，下载了chromestandalonesetup.exe离线版本的谷歌，版本是 V71。
> 查看对应的驱动器v2.43或者v2.44或者v2.45。
> 我下载了v2.45，成功解决了。
> ```
>









```python
########################不是第一次犯这个错误了
#li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
#    for li_one in li_list:
        #某一个主播
        #title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip('\n')
        #路径应该是.//而不是//
#xpath中使用text，应该是'//xx/xx'.text 是属性  title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text
#driver.page_source  是属性
```

