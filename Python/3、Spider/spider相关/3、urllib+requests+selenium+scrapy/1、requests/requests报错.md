### 不记文档，白忙一场

------

#### 代理http/https问题

> ​	问题1：
>
> ```python
> import requests
> 
> url = 'https://www.baidu.com/s'
> data={
>     'wd': 'ip'
> }
> proxies = {
>     'https':'125.46.0.62:53281'
> }
> r = requests.get(url=url,params=data,proxies=proxies)
> r.encoding='utf-8'
> 
> with open('./baidu58.html','w',encoding='utf-8') as fp:
>     fp.write(r.text)
> ```
>
> ​	解决：
>
> ```python
> url写成http://www.baidu.com/s。
> proxies写成'http':'125.46.0.62:53281'。
> 因为Upgrade-Insecure-Requests: 1，它会自动加https，所以找代理ip，不需要非得找https的。
> ```
> ​	问题2：
>
> ```python
> import requests
> 
> url = 'https://fanyi.baidu.com/sug'
> data = {
>     'kw' :'hello'
> }
> proxies = {
>     'http':'125.46.0.62:53281'
> }
> headers = {
>     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
>     'Upgrade-Insecure-Requests': '1',
> }
> res = requests.post(url=url,data=data,proxies=proxies)
> print(res.text)
> 
> #编译json数据
> print(res.json())
> 
> ###url是http的话，proxies也需要是http
> ```
>
> ​	结论：
>
> ```python
> 上面的问题2代码中的代理可以成功运行，说明https的地址，代理完全可以是http。不需要专门找https的代理ip。
> ```
>
> 
>
> ​	