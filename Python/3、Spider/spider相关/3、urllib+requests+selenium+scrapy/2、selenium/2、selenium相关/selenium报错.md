### 不记文档，白忙一场

------

#### 报错记录

**selenium中获取标签内容(即element的内容)，text是属性，不是方法**

> ```python
> li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
> 	for li_one in li_list:
>         #某一个主播
> 		title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip('\n')
> ```

**selenium中在elements中在接着用xpath往下找时，应该用'.//'，而不是'//'**

> ```python
> li_list = driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')
> 	for li_one in li_list:
>         #某一个主播
> 		title = li_one.find_element_by_xpath('.//h3[@class="ellipsis"]').text.strip('\n')
> ```

**selenium中获取html源码，是属性page_source，不是方法page_source()**

> ```python
> driver.get('https://www.douyu.com/directory/all')
> resource = driver.page_resource
> ```

