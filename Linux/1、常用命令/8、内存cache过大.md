### 不记文档，白忙一场

------

#### 0、方法1

> #### 一次性释放
>
> ```python
> sync
> echo 1 > /proc/sys/vm/drop_caches
> echo 2 > /proc/sys/vm/drop_caches
> echo 3 > /proc/sys/vm/drop_caches
> ```
>
> #### 来源
>
> ```python
> https://www.cnblogs.com/balala/p/5646501.html
> ```

#### 1、方法2

> #### 配置文件，永久有效
>
> ```python
> 
> ```
>
> #### 来源
>
> ```python
> https://www.cnblogs.com/lailailai/p/4497352.html
> ```