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
	https://www.cnblogs.com/Dylansuns/p/6974272.html
	1、检查一下系统中的jdk版本
    	[root@localhost software]# java -version
        显示：
        openjdk version "1.8.0_102"
        OpenJDK Runtime Environment (build 1.8.0_102-b14)
        OpenJDK 64-Bit Server VM (build 25.102-b14, mixed mode)
    2、检测jdk安装包
    	[root@localhost software]# rpm -qa | grep java
        显示：
        java-1.7.0-openjdk-1.7.0.111-2.6.7.8.el7.x86_64
        python-javapackages-3.4.1-11.el7.noarch
        tzdata-java-2016g-2.el7.noarch
        javapackages-tools-3.4.1-11.el7.noarch
        java-1.8.0-openjdk-1.8.0.102-4.b14.el7.x86_64
        java-1.8.0-openjdk-headless-1.8.0.102-4.b14.el7.x86_64
        java-1.7.0-openjdk-headless-1.7.0.111-2.6.7.8.el7.x86_64
   3、卸载openjdk
		[root@localhost software]# rpm -e --nodeps tzdata-java-2016g-2.el7.noarch
		[root@localhost software]# rpm -e --nodeps java-1.7.0-openjdk-1.7.0.111-	
        		2.6.7.8.el7.x86_64
		[root@localhost software]# rpm -e --nodeps java-1.7.0-openjdk-headless-1.7.0.111-
        		2.6.7.8.el7.x86_64
		[root@localhost software]# rpm -e --nodeps java-1.8.0-openjdk-1.8.0.102-
        		4.b14.el7.x86_64
		[root@localhost software]# rpm -e --nodeps java-1.8.0-openjdk-headless-1.8.0.102-
        		4.b14.el7.x86_64
    	或者使用
        [root@localhost jvm]# yum remove *openjdk*
        之后再次输入rpm -qa | grep java 查看卸载情况：
        [root@localhost software]# rpm -qa | grep java
        python-javapackages-3.4.1-11.el7.noarch
        javapackages-tools-3.4.1-11.el7.noarch
   4、安装新的jdk
		首先到jdk官网上下载你想要的jdk版本，下载完成之后将需要安装的jdk安装包放到Linux系统指定的文件夹
    		下，并且命令进入该文件夹下：
        [root@localhost software]# ll
		total 252664
		-rw-r--r--. 1 root root  11830603 Jun  9 06:43 alibaba-rocketmq-3.2.6.tar.gz
		-rw-r--r--. 1 root root  43399561 Jun  9 06:42 apache-activemq-5.11.1-bin.tar.gz
		-rwxrw-rw-. 1 root root 185540433 Apr 21 09:06 jdk-8u131-linux-x64.tar.gz
		-rw-r--r--. 1 root root   1547695 Jun  9 06:44 redis-3.2.9.tar.gz
		-rw-r--r--. 1 root root  16402010 Jun  9 06:40 zookeeper-3.4.5.tar.gz
            
         解压 jdk-8u131-linux-x64.tar.gz安装包
        
        [root@localhost software]# mkdir -p /usr/lib/jvm
		[root@localhost software]# tar -zxvf jdk-8u131-linux-x64.tar.gz -C /usr/lib/jvm
   5、设置环境变量
		[root@localhost software]# vim /etc/profile
    	在最前面添加：
        export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_131  
		export JRE_HOME=${JAVA_HOME}/jre  
		export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib  
		export  PATH=${JAVA_HOME}/bin:$PATH
   6、执行profile文件
		[root@localhost software]# source /etc/profile
    	这样可以使配置不用重启即可立即生效。
   7、检查新安装的jdk
		[root@localhost software]# java -version
    	显示：
        java version "1.8.0_131"
		Java(TM) SE Runtime Environment (build 1.8.0_131-b11)
		Java HotSpot(TM) 64-Bit Server VM (build 25.131-b11, mixed mode)
   到此为止，整个安装过程结束。
```

#### Tomcat

