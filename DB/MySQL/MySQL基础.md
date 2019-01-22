### 不记文档，白忙一场

------

#### 语句格式

**概述：**

> ```python
> 以下的记录，表格都按user表来记录
> ```

**1、显示创建表格语句**

> ```python
> show create table user\G
> ```

**2、表的增删改**

> (1) 增
>
> ```python
> 
> ```
>
> (2) 删：
>
> ```python
> drop table user;
> ```
>
> 

#### 储存引擎的区别

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

#### 安装

> (1) 服务：
>
> ```python
> net start mysql --> 启动服务命令
> net stop mysql --> 关闭服务命令
> ```
>