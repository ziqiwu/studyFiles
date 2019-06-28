### 不记文档，白忙一场

------

#### 启动报错

> #### 报错信息
>
> ```python
> There is insufficient memory for the Java Runtime Environment to continue.
> ```
> #### 解决方法
>
> ```python
> 来源：
> 	https://blog.csdn.net/jiangyu1013/article/details/81486374
> 方法：	
> 	修改bin下的runserver.sh   runbroker.sh   tools.sh三个sh启动文件的java的VM配置信息
> 备注：
> 	Xms、Xmx、Xmn等参数含义见：https://www.jianshu.com/p/bf54d8493626
> ```
>
> 



