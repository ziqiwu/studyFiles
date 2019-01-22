### 不记文档，白忙一场

------

#### linux打开服务端和客户端

> (1) 打开服务端：
>
> ```python
> 
> ```
>
> (2) 打开客户端：
>
> ```python
> 
> ```
>
> (3) 注意：
>
> ​	打开客户端相关
>
> ```python
> 测试环境：10.18.76.197
> 连接测试的Redis：
> 	/usr/local/redis/bin/redis-cli -h 127.0.0.1 -p 6379
> 百度命令：
> 	去usr/local/bin下 输入 redis-cli  -h 127.0.0.1 -p 6379 -a 密码
> 注意：
> 	因为测试环境的Redis客户端没有密码，所以不用输入-a参数，而且find / -name redis-cli之后出现的是
> 	/usr/local/redis/bin/redis-cli。所以应该是没有加在环境变量中，直接		
>     输/usr/local/redis/bin/redis-cli -h 127.0.0.1 -p 6379
> ```
>
> ​	打开服务端相关
>
> ```python
> ps -ef | grep redis 可以看到redis-server(redis服务端)已经启动了
> netstat -tunpl | grep 6379 看下端口号有没有被占用
> ```
>
> ​	基础：
>
> ```python
> 1.每个人的redis和redis的配置文件放的地方不同，可以用whereis redis这种来查找
> 2.开启服务器，后面要加配置文件地址
> 3.开启客户端 后面要加密码（如果设置过密码的话，密码可以再redis.conf中找到
> ```

#### 学习全教程

> ```python
> http://www.runoob.com/redis/redis-keys.html
> ```