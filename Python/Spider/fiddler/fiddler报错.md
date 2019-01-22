### 不记文档，白忙一场

------

#### 报错

**(1) 刷新页面，但是抓不到包**

> ```python
> fiddler页面的最左下角有两个图标，一个显示Capturing，一个显示All Processes。
> 如果点左边的，会变成空白方块，也抓不到包。如果把右边点成Hidden All，也抓不到包。
> ```

**(2) 爬取智联招聘，输入搜索框"python"关键字，在fiddler中没有找到返回html的get请求**

> ​	原因
>
> ```python
> 因为返回html的get请求是在执行https://sou.zhaopin.com/之后，加载的。
> 而输入搜索框"python"，点击搜索按钮，是执行的ajax，所以不会重新再加载html了。
> ```
>
> ​	解决
>
> ```python
> cls清空fiddler。
> 浏览器输入https://sou.zhaopin.com/之后，抓包，就可以抓到get请求的返回html页面的请求了。
> ```

**(3) 返回html过大，response的raw框中只显示一部分**

> ​	说明
>
> ```python
> 框中最后一行显示
> *** FIDDLER: RawDisplay truncated at 262144 characters. Right-click to disable truncation. ***
> ```
>
> ​	解决
>
> ```python
> 在框中右键，去掉Auto Truncate前的对勾
> ```