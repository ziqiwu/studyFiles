

### 不记文档，白忙一场

------

#### 报错信息

**Scrapy ImportError: No module named items**

> ​	描述
>
> ```python
> 代码中导入from tianya.items import TianyaItem爆红，
> 且执行报错Scrapy ImportError: No module named items
> ```
>
> ​	解决 --> 方法一
>
> ```python
> 1.找到你的scrapy项目上右键
> 2.然后点击make_directory as
> 3.最后点击sources root
> 4.看到文件夹变成蓝色就成功了
> 注意：是在项目上右键
> 	且最后项目包变成了蓝色，证明是对了
> ```
>
> ​	解决 --> 方法二
>
> ```python
> from ..items import DushuprojectItem
> from包名的时候，写..然后会自动提示items，然后再import对应的Item模块
> 注意：最好用第一种方法，因为第二种方法在scrapy分布式的时候，会报错
> ```
>
> 

​	



