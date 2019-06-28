### 不记文档，白忙一场

------

#### ***真正集群（百万级别数据）***

> ```python
> https://blog.csdn.net/aa1215018028/article/details/82700872 -- 高可用牛逼版本（需6台物理机搭建		MQ实例）
> ActiveMQ Master Slave + Broker Cluster
> ```

#### 0、下载+解压+启动

> ```python
> 0、http://zookeeper.apache.org/
>     --找download
> 1、解压
> 2、启动
> 	cd bin --> ./zkServer.sh start或者./zkServer.sh start ../conf/zoo.cfg
> ```
>

#### 1、伪集群搭建

> #### 来源
>
> ```java
> https://segmentfault.com/a/1190000014636822
> ```
>
> #### 注意
>
> ```python
> 0、验证是否启动成功
> 	ps -ef | grep zookeeper
> 1、公网ip问题
> 	有关：
> 		server.1等后面的ip不能写公网ip，只能写127.0.0.1或者0.0.0.0
> 2、防火墙/开放端口号问题
> 	排除：
>     	因为是伪集群，三个节点部署在一台虚拟机上面，是不需要开放端口号的。对外服务的才需要走防火墙
> 	注：
>     	先启动node1，查看状态，错误。紧接着启动node2，发现状态是follower，启动node3，发现还是			follower。回过头来看node1的状态，已经正常
> 		而且是leader
> 3、端口号问题
> 	排除：
> 		node1从clientPort=2183改回2181，重启zkServer.sh，查看状态，正常
> 过程：
> 	1> 启动报错日志路径：出现错误的日志文件在节点下的bin下的.out文件中，这个是日志文件
> 	2> 启动命令cd bin --> ./zkServer.sh start 或者 ./zkServer.sh start ../conf/zoo.cfg
> 	3> 如果不向外提供服务，只是集群启动，不需要开放端口。不影响
> 	4> 所有问题的解决，都是看过了错误日志之后
> ```
> #### 启动zk服务，查看zk服务状态
>
> ```python
> $ /opt/zookeeper/zk1/bin/zkServer.sh start # 启动zk1服务
> $ /opt/zookeeper/zk2/bin/zkServer.sh start # 启动zk2服务
> $ /opt/zookeeper/zk3/bin/zkServer.sh start # 启动zk3服务
> 
> $ /opt/zookeeper/zk1/bin/zkServer.sh status # 查看zk1服务状态
> $ /opt/zookeeper/zk2/bin/zkServer.sh status # 查看zk2服务状态
> $ /opt/zookeeper/zk3/bin/zkServer.sh status # 查看zk3服务状态
> ```

#### 2、真集群搭建

> #### 来源
>
> ```python
> https://segmentfault.com/a/1190000014635114 -- 简易版本
> https://blog.csdn.net/aa1215018028/article/details/82700872 -- 高可用牛逼版本（需6台物理机搭建		MQ实例）
> 	 ActiveMQ Master Slave + Broker Cluster
> ```

