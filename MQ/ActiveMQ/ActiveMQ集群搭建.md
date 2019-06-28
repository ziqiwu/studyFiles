### 不记文档，白忙一场

------

#### ***最全文章***

> ```python
> 来源
> 	https://www.cnblogs.com/xbq8080/p/6429267.html
> 记录
>     调试命令，真的是帮了我大忙了。哈哈
>     调试zookeeper集群+activemq集群 -- zk集群是服务端，mq集群是客户端
> 	注* 我所使用的搭建集群方式只是主从，真正百万级别数据量的解决方案是ActiveMQ Master Slave + 			Broker Cluster。而仅仅是主从的时候，并不是三个节点同时都可以可以jetty中访问，并不是三个节		  点同时对外提供服务，另外两个是替补，当zookeeper检测到主节点挂掉，就会启用替补。这时                http://39.105.32.104:8161/不能再访问，:8162或者:8163两个中的一个可以访问。
> 		同时netstat -anp | grep 61616不再能监听此端口，gep 61617或gep 61618两个中的一个可以监听          到端口。
> ```

#### ***配置详解***

> ```python
> https://blog.csdn.net/Donald_Draper/article/details/88307192
> ```

#### 真正集群+高可用

> ```python
> 来源：
> 	https://blog.csdn.net/aa1215018028/article/details/82700872
> 详解：
> 	上述是ActiveMQ Master Slave + Broker Cluster的最小化配置，为了得到更高的高可用性，建议6个MQ	实例间全部需要有物理机承载。
> 	但是，上述情况是用于应对百万级并发消息的生产环境而言才需要如此大动干戈，对于常规环境笔者建议
> ```

#### 0、下载+解压+启动

> ```python
> 1> 下载
>     0、下载地址：http://activemq.apache.org/activemq-5153-release.html
>         http://activemq.apache.org -- 官网 --> 找download
>     1、在官网的Download Link下的可点击的apache-activemq-5.15.3-bin.tar.gz
>     2、右键 --> Copy link address
> 2> 解压
> 	tar -zxvf xxx
> 3> 启动
> 	cd bin --> ./activemq start
> ```

#### 1、伪集群搭建

> #### 来源
>
> ```java
> https://segmentfault.com/a/1190000014636822
> ```
>
> #### 集群信息
>
> ```python
> --	服务端口	jetty控制台端口	节点目录/opt/下
> node1	61616	8161	/activemq/node1
> node2	61617	8162	/activemq/node2
> node3	61618	8163	/activemq/node3
> ```

#### 2、真集群搭建

> #### 来源
>
> ```python
> https://blog.csdn.net/Donald_Draper/article/details/88307192
> ```

#### 3、注意

> #### 坎坷过程
>
> ```python
> 来源
>     linux修改主机名hostname：
>     https://zhidao.baidu.com/question/300956321.html
> 步骤
>     20:33 修改activemq.xml中的hostname为guozi_1，原来为localhost
>     next 修改为guozi1，因为猜测名称不规范，不能有下划线
>     next vim /etc/hosts --> 将127.0.0.1之后增加guozi1 
> ```
>
> #### 注意
>
> ```python
> activemq为了和zookeeper集合
> 1、zookeeper所在服务器开放2181、2182、2183三个端口号，这三个端口号是对外提供服务的。剩下的		zookeeper的两个端口号是内部使用的。
> 2、启动报错日志路径：activemq/data/activemq.log
> 3、所有问题的解决，都是看过了错误日志之后
> 4、原来日志文件记录了错误：<replicatedLevelDB />没有这个标签
>      猜测是<replicatedLevelDB和<kahaDB冲突了。
>      注释掉<kahaDB directory="${activemq.data}/kahadb"/>之后，启动，成功！
> 5、所有要开启端口
> 	[root@iz2ze82l26n5rq314e106gz conf]# firewall-cmd --query-port=61617/tcp 
> 		no
> 	[root@iz2ze82l26n5rq314e106gz conf]# firewall-cmd --query-port=61616/tcp 
> 		yes
>         
>         
> 	[root@iz2ze82l26n5rq314e106gz conf]# firewall-cmd --query-port=8161/tcp
> 		yes
> 	[root@iz2ze82l26n5rq314e106gz conf]# firewall-cmd --query-port=8162/tcp
> 		no
> 	[root@iz2ze82l26n5rq314e106gz conf]# firewall-cmd --query-port=8163/tcp
> 		no
> 	[root@iz2ze82l26n5rq314e106gz conf]# 
> ```