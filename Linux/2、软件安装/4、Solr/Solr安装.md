### 不记文档，白忙一场

#### 1、单机安装+集群安装

> ```python
> 来源：https://www.cnblogs.com/dijia478/p/8075638.html
> ```

#### 2、实践步骤

> ```python
> 注* cp -r是复制文件和文件夹，详情参见linux章节
> 1> 概述：
> 	JDK 1.8.0_192
> 	tomcat 8.5.42
> 	solr 7.7.2
> 2> 步骤
> 	参见来源
> 3> 注意
> 	1 第五步：把server/resources/目录下的log4j.properties，添加到刚才部署的solr工程中
> 		注* solr 7.7.2下面用的不是log4j而是log4j2，所以我是把server/resources/*所有文件都拷贝到
> 			了solr工程中
> 	2 关联solr及solrhome
> 		注* solr 7.7.2中默认没有这一段，需要手动加上去
> ```