### 不记文档，白忙一场

------

#### log4j初相识

> ```python
> https://blog.csdn.net/qq_34721505/article/details/77892189
> https://www.cnblogs.com/gaishishengzhu/articles/1735441.html
> https://blog.csdn.net/x6582026/article/details/52179817
> https://www.cnblogs.com/chanedi/articles/2106040.html
> ```

#### log4j日志输出路径配置问题

> ```python
> https://www.cnblogs.com/doit8791/p/5372004.html
>     
> 直接输入/根目录，应该指的是tomcat下的bin目录。因为我突然发现之前的log都在bin目录下找到了
>     
>     
>     （3）使用环境变量相对路径法：程序会优先找jvm环境变量，然后再找系统环境变量，来查找配置文件中的变量。
>         log4j.appender.logfile.File=${user.dir}/logs/app.log，使用tomcat容器时${user.dir}对应tomcat的bin目录；
>         log4j.appender.logfile.File=${user.home}/logs/app.log，${user.home}对应操作系统当前用户目录；
>         log4j.appender.logfile.File=${webApp.root}/logs/app.log，${webApp.root}对应当前应用根目录；
> ```



