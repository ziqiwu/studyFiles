### 不记文档，白忙一场

#### JDK

```python
第一步：下载jdk安装包
1、登录www.oracle.com
2、找到menu --> developers --> java --> download --> downloads --> java archive(archive是档案室)
	--> 下载对应版本的jdk
第二步：安装lrzsz
1、简介：lrzsz是一款在linux里可代替ftp上传和下载的程序。
2、安装
	(1)CentOS下yum install lrzsz
	(2)Ubuntu下apt update --> apt install lrzsz
	(3)安装包情况下：
		a.到网上下载lrzsz安装包，这里以lrzsz-0.12.20.tar.gz为例
		b.tar zxvf lrzsz-0.12.20.tar.gz 解压安装包
		c.进入解压好的目录里cd lrzsz-0.12.20 
		d.配置安装路径./configure --prefix=/usr/local/lrzsz
		e.编译make
		f.安装make install
		g.配置系统命令
			#cd /usr/bin 
			#ln -s /usr/local/lrzsz/bin/lrz rz 
			#ln -s /usr/local/lrzsz/bin/lsz sz
			如果/usr/bin下已存在，删除
第三步：安装jdk
	1、https://www.cnblogs.com/Dylansuns/p/6974272.html
	2、后面再补充
    
```

#### Tomcat

