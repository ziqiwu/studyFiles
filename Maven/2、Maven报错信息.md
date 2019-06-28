### 不记文档，白忙一场

------

#### 0、jackson-bom:pom:1.9.13

> #### 报错信息
>
> ```python
> in offline mode and the artifact com.fasterxml.jackson:jackson-bom:pom:1.9.13 has not been downloaded from it before.
> ```
>
> #### 解决
>
> ```python
> https://blog.csdn.net/weixin_43232196/article/details/82760093
> ```
>
> #### 概述
>
> ```python
> 官网，该版本已经失效下架，使用其他版本即可。	
> ```
>
> #### 备注
>
> ```python
> 直接在<properties>标签里面加上版本号就还可以了。maven的springboot会自己读取的
> ```