### 不记文档，白忙一场

------

#### 0、语句格式



> ***注意：***
>
> ```python
> 以下的记录，表格都按user表来记录
> ```
> #### 语句
>
> ```python
> 1> 列出所有数据库
> 	show databases;
> 2> 进入数据库jeesite
> 	use jeesite;
> 3> 列出该数据库中所有表
> 	show tables;
> 3> 显示创建表user的sql
> 	show create table user\G;
> 4> 创建表user
> 
> 5> 删除表user
> 	drop table user;
> ```

#### 1、储存引擎的区别

> ```python
> 表的存储引擎的区别
> 
> MyISAM
>   文件存储为 3个  数据,表结构,索引   MYD  MYI
> InnoDB
> 文件存储为 2个 表结构   数据和索引
> 
> 1. MyISAM 不支持外键
> 2. innodb支持
> 3. innodb支持事物 所以安全性高
> 4. myisam不支持事物
> 5. myisam查询效率高于innodb
> 6. innodb用于对数据安全性较高的存储
> 7. myisam用于对数据安全性要求不高 但是查询效率高的网站  帖子
> ```
>

#### 2、安装

> #### 服务
>
> ```python
> net start mysql --> 启动服务命令
> net stop mysql --> 关闭服务命令
> ```
>
> #### cmd连接mysql
>
> ```python
> mysql -u root -p 
> 注意：
> 	不要少了杠，变成mysql uroot -p
> ```
>
> 