### 不记文档，白忙一场

------

#### 0、为什么使用集群

> ```python
> 1、使用集群的原因：	
> 	我们日常在对于redis的使用中，经常会遇到一些问题
> 	1、高可用问题，如何保证redis的持续高可用性。
> 	2、容量问题，单实例redis内存无法无限扩充，达到32G后就进入了64位世界，性能下降。
> 	3、并发性能问题，redis号称单实例10万并发，但也是有尽头的。
> 	来源：http://www.cnblogs.com/kerwinC/p/6611634.html
> 2、为了达到redis的高可用，有四种部署方式
> 	主从复制+哨兵机制；集群模式(服务器分片)；集群服务(客户端分片)；集群模式(twenproxy)
> 	哨兵机制是redis2.8开始支持。
> 	集群模式是redis3.0开始支持。
> 	来源：https://blog.csdn.net/ls1645/article/details/78931605
> ```

#### 1、主从配置

> #### 前言
>
> ```python
> 搭建主从:
> 	如果是一台机器:
> 		用同一个redis中的redis-server配合不同的redis.conf配置文件，就可以创建不同的实例(进程)
> 		详情见下面的实战(两台机器+四个实例)
> 	如果是两台机器
> 		要各自都安装redis
> 		详情见下面的实战(两台机器+两个实例)
>         
> 从机特性：
> 	只读特性。如果想执行set操作，报错：-READONLY You can't write against a read only slave.
>     
> 结论：
> 	1> src/redis-server就是用来创建实例(redis进程)的工具。
> 	2> 工具，当然是可以重复使用的，也就是配合不同配置文件来使用该工具，就可以创建不同的redis进程。
> 	3> 验证方法，就是一台机器三个实例启动后，ps -ef | grep redis可以看到三个不同端口redis进程。
> 	4> 所以，一台机器，安装一个redis就可以；多台机器，就需要每台机器都安装一个redis
> ```
>
> #### 实战(两台机器+两个实例)
>
> ```python
> 超简单，就两步：
> 准备工作：
> 	1> 两台机器都安装了redis
> 	2> 配置了不同的端口
> 	3> 都设置了密码auth
> 	4> 注释了bind 127.0.0.1
> 	5> 都设置了deamonize yes
> 	6> 都操作防火墙放行了各自的端口
> 步骤：
> 	第一步：测试联通性
> 		1> ping和telnet测试。如果linux没有安装telnet，就用redis-cli的ping-pong机制就可以验证				了。既验证redis实例存活，也验证了可以联通ip和端口
> 			【从机输入】./redis-cli -h 192.168.1.125 -p 1111 -a 123456 -r 3 -i 2 ping
> 			【主机输入】./redis-cli -h 192.168.1.126 -p 2222 -a 123456 -r 3 -i 2 ping
> 			【本地输入】./redis-cli -h 192.168.1.125 -p 1111 -a 123456 -r 3 -i 2 ping
> 			注1：验证主机和从机可以相互联通；验证客户端和主机的联通。(代码在本地，所以验证本地可以				和主机联通)。
> 			注2：redis-cli的使用参数详见redis基础.md
> 	第二步：修改从机配置文件
> 		注：直接把redis.conf拉出来，用notepad++全文检索slaveof和masterauth，都在REPLICATION下
> 		1> 修改slaveof 192.168.1.125  1111    
> 		2> 修改masterauth 123456
> 	第三步：分别杀掉主机和从机的进程，分别重新启动redis服务端
> 测试：
> 	1> 本地打开两个powershell窗口，分别使用telnet命令连接主机和从机的redis端口
>         telnet 192.168.1.125 1111 --> auth 123456
>         telnet 192.168.1.125 2222 --> auth 123456
> 	2> 主机 keys *和从机的keys *一样
> 		主机get name和从机get name值一样
> 		说明：一启动，数据就已经经过了主从复制，从机和主机的数据完全一致了
> 	3> 主机set name newname
> 		从机get name，发现值为newname，跟随主机一起改过了
> 	4> 进一步测试就可以用java代码连接主机，进行操作，自然从机从进行主从复制，自动备份主机数据
> 备注：
> 	主机：
> 		ip: 192.168.1.125
> 		port: 1111
> 		auth: 123456
> 	从机：
> 		ip: 192.168.1.126
> 		port: 2222
> 		auth: 123456	
> 来源：
> 	https://www.cnblogs.com/taijun/p/4583465.html
> ```
>
> #### 实战(两台机器+四个实例) -- 其中一台机器有三个实例，可见一机多实例的启动方法
>
> ```python
> 步骤：
>     1> /usr/local/redis/redis-4.0.9/redis.conf同级目录下，创建两个文件夹2221和2222
>         mkdir 2221 
>         mkdir 2222
>     2> 把redis.conf复制两份，新建文件夹每个一份
>         cp redis.conf 2221
>         cp redis.conf 2222
>     3> 修改配置文件
>         2221下的:
>             port 2221
>             slaveof 192.168.1.125  1111 
>             requirepass 123456 (可选)
>         	masterauth 123456 (可选)
>             #protected-mode yes (可选)
>         2222下的：
>             port 2222
>             slaveof 192.168.1.125  1111 
>             requirepass 123456 (可选)
>             masterauth 123456 (可选)
>             #protected-mode yes (可选)
>         redis.conf的：
>             port 2220
>             requirepass 123456 (可选)
>             #protected-mode yes (可选)
>     4> 防火墙给2220/2221/2222三个端口都放行
>     5> 测试主机192.168.1.125对192.168.1.126的三个端口都可以访问
>         方法是利用redis节点彼此互联(PING-PONG机制)，示例如下
>         【主机输入】./redis-cli -h 192.168.1.126 -p 2220 -a 123456 -r 3 -i 2 ping
>         【主机输入】./redis-cli -h 192.168.1.126 -p 2221 -a 123456 -r 3 -i 2 ping
>         【主机输入】./redis-cli -h 192.168.1.126 -p 2222 -a 123456 -r 3 -i 2 ping
>     6> 启动一主三从，共四个实例
>         【从机2220】./redis-server ../redis.conf
>         【从机2221】./redis-server ../2221/redis.conf
>         【从机2222】./redis-server ../2222/redis.conf
>         【主机1111】./redis-server ../redis.conf
>     7> 测试
>         第一：启动，就发现三个从机中都已经有数据了，而且和主机的一样
>         第二：主机执行flushdb，发现三个从机中数据也都空了
> 来源：	
> 	搭建一个简单的redis-sentinel(哨兵机制)集群
> 	https://blog.csdn.net/qq_37853817/article/details/78961462
> ```

#### 2、主从复制+哨兵机制

> #### 前言
>
> ```python
> https://blog.csdn.net/qq1137623160/article/details/79148613
> https://www.cnblogs.com/kerwinC/p/6069864.html
> https://blog.csdn.net/yyqq188/article/details/79220255 -- 术语 
> https://blog.csdn.net/ls1645/article/details/78931605 -- 有两种部署方式
> ```
>
> #### 实战
>
> ```python
> 准备工作：
> 	1> 台机器，我用的是虚拟机
> 	2> 每台机器都安装了redis，都开放了端口，可以互相联通
> 	3> CentOS6 + Redis4.x    
> 步骤：
> 	1> 每台机器，都是启动3个redis实例(进程)，1主2从。
> 		注：如果不知道同一机器启动多个实例，请参考主从配置(两台机器+四个实例)
> 	2> 192.168.1.125虚拟机配置两个sentinel.conf文件，192.168.1.126配置一个sentinel.conf文件
> 		注：文件内容详见备注
> 	3> 启动三个sentinel
> 		注：原理和同一机器启动多个redis一样，src文件下的redis-sentinel是工具，配合不同的.conf
> 	4> 查看启动是否成功
> 		注：启动失败的输出，成功的输出，原因，详见备注
> 	5> 测试哨兵模式的正确运行
> 		注：kill掉一个主机，查看控制台输出内容，即哨兵的投票等一系列自动化机制
> 来源：
> 	https://blog.csdn.net/qq_37853817/article/details/78961462
> ```
>
> #### 模拟主机宕机，观察配置文件变化
>
> ```python
> 步骤：
> 	1> 192.168.1.125 1110是主机，端口1111和1112是从机
> 	2> redis都启动，sentinel都启动
> 	3> kill -9 1110的进程ID
> 	4> 观察发现sentinel选取1111做了主机。
> 检查文件：
> 	1> 1111下的redis.conf的slaveof 192.168.1.125 1110和masterauth 123456都不见了
> 	2> 1112下的redis.conf的slaveof 192.168.1.125 1110变为了192.168.1.125 1111
> 	3> 1110对应的redis.conf，在文件末尾增加 slaveof 192.168.1.125 1111，但是masterauth没有加
> ```
>
> #### 备注
>
> ```python
> 0、网上的配置：sentinel.conf配置文件(后台运行，日志输入文件)，没有测试
>     bind 0.0.0.0
>     port 5000    #Sentinel 服务的端口
>     daemonize yes
>     logfile "/var/log/redis/sentinel.log"
>     sentinel monitor mymaster 127.0.0.1 6379 1  # Quorum取比总数/2大的最小整数即可，这里是1
>     sentinel down-after-milliseconds mymaster 5000
>     sentinel failover-timeout mymaster 60000
>     sentinel auth-pass mymaster toor  # Redis服务的密码
> 1、sentinel.conf文件内容
> 	port 26379
> 	dir /tmp 
> 	sentinel monitor s1 192.168.1.125 1110 2
> 	sentinel monitor s2 192.168.1.126 2220 2
> 
> 	sentinel auth-pass s1 123456 
> 	sentinel auth-pass s2 123456
> 
> 	sentinel down-after-milliseconds s1 30000
> 	sentinel down-after-milliseconds s2 30000
> 
> 	sentinel parallel-syncs s1 1
> 	sentinel parallel-syncs s2 1
> 
> 	sentinel failover-timeout s1 180000
> 	sentinel failover-timeout s2 180000
> 
> 	protected-mode no
> 	更多sentinel.conf配置信息：https://blog.csdn.net/u012441222/article/details/80751390
> 2、正常启动sentinel后控制台输出：
>     WARNING: The TCP backlog setting of 511 cannot be enforced because 							/proc/sys/net/core/somaxconn is set to the lower value of 128.
>     Sentinel ID is a205465e1f45a8fcacef281867ec4fbe878af04e
>     
>     +monitor master s1 192.168.1.125 1110 quorum 2
>     +monitor master s2 192.168.1.126 2220 quorum 2
>     
>     +slave slave 192.168.1.125:1111 192.168.1.125 1111 @ s1 192.168.1.125 1110
>     +slave slave 192.168.1.125:1112 192.168.1.125 1112 @ s1 192.168.1.125 1110
>     +slave slave 192.168.1.126:2221 192.168.1.126 2221 @ s2 192.168.1.126 2220
>     +slave slave 192.168.1.126:2222 192.168.1.126 2222 @ s2 192.168.1.126 2220
>     
>     +sentinel sentinel 5a23c4b855b70685ba15d22a3bc0aa8f8e0949af 192.168.1.125 26380 @ s1 		192.168.1.125 1110
>     +sentinel sentinel 5a23c4b855b70685ba15d22a3bc0aa8f8e0949af 192.168.1.125 26380 @ s2 		192.168.1.126 2220
>     +sentinel sentinel 07794ef8f9a5258a46d094b4a3e18af7c80871e4 192.168.1.125 26379 @ s1 		192.168.1.125 1110
>     +sentinel sentinel 07794ef8f9a5258a46d094b4a3e18af7c80871e4 192.168.1.125 26379 @ s2 		192.168.1.126 2220
> 	注：
> 		启动的时候，redis标识下面会有端口和进程号，这个启动的哨兵端口为：26379，ip是192.168.126
> 	注解：
> 		1> monitor监工两个
> 		2> slave从机共四个
> 		3> 列出另外两个哨兵，都监控着那两台主机
> 		4> 输出控制台所在的主机实例ID在Sentinel ID后面有
> ```
>
> #### 哨兵控制台输出内容详解
>
> ```python
> 备注：
> 	+sdown 信息加入监控系统
> 	-sdown 信息从监控系统中解除
> 步骤：
> 	第一步：停掉192.168.1.126 26379的哨兵
> 	第二步：重启192.168.1.126 26379的哨兵
> 	第三步：停掉192.168.1.126 2220的主机
> 	第四步：修改192.168.1.126的主机配置文件redis.conf，即打开masterauth的注释，并启动
> 输出：
>     #备注：本控制台窗口对应的是192.168.1.125 26379哨兵服务，一共三个哨兵，25两个，26一个
> -------------------------------------------------------------------------------------------
>     2007:X 18 Mar 12:08:52.977 # WARNING: The TCP backlog setting of 511 cannot be enforced 		because /proc/sys/net/core/somaxconn is set to the lower value of 128.
>     
>     #输出：本哨兵的ID
>     2007:X 18 Mar 12:08:53.090 # Sentinel ID is ff85a7e54cb318792cbe717a181b3a351a15df8b
>     
>     #输出：规则--两个监工，同时监控两个主机实例ip+port，法定人数2人才能投票生效
>     2007:X 18 Mar 12:08:53.090 # +monitor master s2 192.168.1.126 2220 quorum 2
>     2007:X 18 Mar 12:08:53.090 # +monitor master s1 192.168.1.125 1110 quorum 2
>     
>     #输出：所有从机+隶属于的主机 
>     2007:X 18 Mar 12:08:53.097 * +slave slave 192.168.1.126:2221 192.168.1.126 2221 @ s2 		192.168.1.126 2220
>     2007:X 18 Mar 12:08:53.100 * +slave slave 192.168.1.126:2222 192.168.1.126 2222 @ s2 		192.168.1.126 2220
>     2007:X 18 Mar 12:08:53.102 * +slave slave 192.168.1.125:1111 192.168.1.125 1111 @ s1 		192.168.1.125 1110
>     2007:X 18 Mar 12:08:53.105 * +slave slave 192.168.1.125:1112 192.168.1.125 1112 @ s1 		192.168.1.125 1110
>     
>     #输出：除了本哨兵外的其余哨兵+哨兵监控的主机 -- 本哨兵的信息，第一行有ID，redis-logo有PID和		port。监控对象当然也是这两个主机。如果想查看自己的+sentinel sentinel 信息，则跳转到另两个		哨兵的启动窗口。
>     #输出：哨兵125 26380 监控主机s1 125 1110
>     2007:X 18 Mar 12:08:53.461 * +sentinel sentinel 											19c83deac9d59b847356e43a3492ce47436fb96d 192.168.1.125 26380 @ s1 192.168.1.125 		1110
>     #输出：哨兵125 26380 监控主机s2 126 2220
>     2007:X 18 Mar 12:08:53.465 * +sentinel sentinel 											19c83deac9d59b847356e43a3492ce47436fb96d 192.168.1.125 26380 @ s2 192.168.1.126 		2220
> 	#输出：哨兵126 26379 监控主机s1 125 1110
>     2007:X 18 Mar 12:08:59.606 * +sentinel sentinel 											ca089181c5653475a1008c639841b8b33db1057e 192.168.1.126 26379 @ s1 192.168.1.125 		1110
> 	#输出：哨兵126 26379 监控主机s2 126 2220
>     2007:X 18 Mar 12:08:59.610 * +sentinel sentinel 											ca089181c5653475a1008c639841b8b33db1057e 192.168.1.126 26379 @ s2 192.168.1.126 		2220
> 	#备注：以上为启动信息 
> 	#操作：停掉192.168.1.126 26379的哨兵
> -------------------------------------------------------------------------------------------
> 	#输出：哨兵126 26379监控126 2220主机的服务宕机。+sdown sentinel表示(宕机发生)
>     2007:X 18 Mar 12:09:47.488 # +sdown sentinel ca089181c5653475a1008c639841b8b33db1057e 			192.168.1.126 26379 @ s2 192.168.1.126 2220
>     #输出：哨兵126 26379监控125 1110主机的服务宕机。+sdown sentinel表示(宕机发生)
>     2007:X 18 Mar 12:09:47.489 # +sdown sentinel ca089181c5653475a1008c639841b8b33db1057e 			192.168.1.126 26379 @ s1 192.168.1.125 1110
>  
> 	#操作：重启192.168.1.126 26379的哨兵
> -------------------------------------------------------------------------------------------
> 	#输出：哨兵126 26379监控126 2220主机的服务重启(对应上面ID)。-sdown sentinel表示(宕机解决)
>     2007:X 18 Mar 12:10:26.961 # -sdown sentinel ca089181c5653475a1008c639841b8b33db1057e 			192.168.1.126 26379 @ s2 192.168.1.126 2220
>     #输出：哨兵126 26379监控125 1110主机的服务重启(对应上面ID)。-sdown sentinel表示(宕机解决)
>     2007:X 18 Mar 12:10:26.961 # -sdown sentinel ca089181c5653475a1008c639841b8b33db1057e 			192.168.1.126 26379 @ s1 192.168.1.125 1110
>     
>     #原来的哨兵ID，地址失效
>     2007:X 18 Mar 12:10:28.284 * +sentinel-invalid-addr sentinel 								  ca089181c5653475a1008c639841b8b33db1057e 192.168.1.126 26379 @ s2 192.168.1.126 			2220
>     #重新对126 26379哨兵生成ID
>     2007:X 18 Mar 12:10:28.284 * +sentinel-address-update sentinel 								  ca089181c5653475a1008c639841b8b33db1057e 192.168.1.126 0 @ s2 192.168.1.126 2220 			 1 additional matching instances
>     #126 26379哨兵用新的ID监控主机126 2220
>     2007:X 18 Mar 12:10:28.284 * +sentinel sentinel 											  111ff1d8c93e49440013aa1dd7ac718f86ec857e 192.168.1.126 26379 @ s2 192.168.1.126   		  2220
> 	#126 26379哨兵用新的ID监控主机126 1110
>     2007:X 18 Mar 12:10:28.286 * +sentinel sentinel 											  111ff1d8c93e49440013aa1dd7ac718f86ec857e 192.168.1.126 26379 @ s1 192.168.1.125 			1110
> 	#停掉192.168.1.126 2220的主机             
> -------------------------------------------------------------------------------------------
> 	#输出：        
>     2007:X 18 Mar 12:10:57.937 # +sdown sentinel ca089181c5653475a1008c639841b8b33db1057e 			192.168.1.126 0 @ s2 192.168.1.126 2220
>     2007:X 18 Mar 12:10:57.937 # +sdown sentinel ca089181c5653475a1008c639841b8b33db1057e 			192.168.1.126 0 @ s1 192.168.1.125 1110
>     2007:X 18 Mar 12:20:29.537 # +sdown master s2 192.168.1.126 2220
>     2007:X 18 Mar 12:20:29.590 # +odown master s2 192.168.1.126 2220 #quorum 3/2
>     2007:X 18 Mar 12:20:29.590 # +new-epoch 1
>     2007:X 18 Mar 12:20:29.590 # +try-failover master s2 192.168.1.126 2220
>     2007:X 18 Mar 12:20:29.704 # +vote-for-leader ff85a7e54cb318792cbe717a181b3a351a15df8b 			1
>     2007:X 18 Mar 12:20:29.707 # 111ff1d8c93e49440013aa1dd7ac718f86ec857e voted for 			111ff1d8c93e49440013aa1dd7ac718f86ec857e 1
>     2007:X 18 Mar 12:20:30.381 # 19c83deac9d59b847356e43a3492ce47436fb96d voted for 			111ff1d8c93e49440013aa1dd7ac718f86ec857e 1
>     2007:X 18 Mar 12:20:31.282 # +config-update-from sentinel 									111ff1d8c93e49440013aa1dd7ac718f86ec857e 192.168.1.126 26379 @ s2 192.168.1.126 		2220
> 	
>     #主机从126 2220切换为126 2222
>     2007:X 18 Mar 12:20:31.282 # +switch-master s2 192.168.1.126 2220 192.168.1.126 2222
>     
>     #126 2221修改隶书关系，126 2220修改为从机，增加隶书关系
>     2007:X 18 Mar 12:20:31.284 * +slave slave 192.168.1.126:2221 192.168.1.126 2221 @ s2 		192.168.1.126 2222
>     
>     #修改192.168.1.126的主机配置文件redis.conf，即打开masterauth的注释，并启动
>     #注意：不能直接启动，因为哨兵已经把主从机的redis.conf文件都改过了
> -------------------------------------------------------------------------------------------
>     #系统增加一个从机126 2220
>     2007:X 18 Mar 12:20:31.284 * +slave slave 192.168.1.126:2220 192.168.1.126 2220 @ s2 		192.168.1.126 2222
>     2007:X 18 Mar 12:21:01.312 # +sdown slave 192.168.1.126:2220 192.168.1.126 2220 @ s2 		192.168.1.126 2222
>     2007:X 18 Mar 12:27:54.645 # -sdown slave 192.168.1.126:2220 192.168.1.126 2220 @ s2 		192.168.1.126 2222
> 测试借鉴：
> 	https://blog.csdn.net/u013820054/article/details/52036383
> ```
>
> #### 报错
>
> ```python
> 1、启动sentinel控制台输出：
>     错误：
>         2730:X 17 Mar 16:31:01.009 # WARNING: The TCP backlog setting of 511 cannot be 				enforced because /proc/sys/net/core/somaxconn is set to the lower value of 				128.
>         2730:X 17 Mar 16:31:01.009 # Sentinel ID is211cad3d91800a05c7a60b29afc63d6acbac15f2
>         2730:X 17 Mar 16:31:01.009 # +monitor master s1 192.168.1.125 1110 quorum 2
>         2730:X 17 Mar 16:31:01.009 # +monitor master s2 192.168.1.126 2220 quorum 2
>         2730:X 17 Mar 16:31:31.019 # +sdown master s1 192.168.1.125 1110
>         2730:X 17 Mar 16:31:31.019 # +sdown master s2 192.168.1.126 2220
>     错误原因：
>         +sdown master表示两台主机都没有连接成功
>         猜测是没有加密码验证，即：
>             sentinel auth-pass s1 123456 
>             sentinel auth-pass s2 123456
>         一开始配置：
>             port 26379
>             sentinel monitor s1 <ip地址> 6379 2
>             sentinel monitor s2 <ip地址> 6379 2
>             protected-mode no
>         后改为：
>             port 26379
>             dir /tmp 
>             sentinel monitor s1 192.168.1.125 1110 2
>             sentinel monitor s2 192.168.1.126 2220 2
> 
>             sentinel auth-pass s1 123456 
>             sentinel auth-pass s2 123456
> 
>             sentinel down-after-milliseconds s1 30000
>             sentinel down-after-milliseconds s2 30000
> 
>             sentinel parallel-syncs s1 1
>             sentinel parallel-syncs s2 1
> 
>             sentinel failover-timeout s1 180000
>             sentinel failover-timeout s2 180000
> 
>             protected-mode no
> 2、启动sentinel控制台输出：
>     错误：
>         +sdown sentinel 77e955bf8a8983618ee084d1023ff627090f1187 
>     错误原因：
>         猜测是防火墙或者端口的问题
>         25两个哨兵都正常启动
>         26一个哨兵老是错误。
>         区别：
>             26的三个从机端口也开放了，25只开放了主机端口 -- 端口猜测
>             26的防火墙配置和25的防火墙配置也不一样 -- 防火墙猜测
>         控制变量：
>             25和26的redis.conf和sentinel.conf都是一样的
>     解决：
>         开放了25的所有端口
>         关掉了26的防火墙和selinux
> ```

#### 3、集群模式(服务器分片)

> #### 前言
>
> ```python
> 来源：
> 	https://blog.csdn.net/qq_42815754/article/details/82912130
> ```
> #### 实战
>
> ```python
> 主备工作：
> 	1> 安装redis完成 -- 参考redis基础
> 	2> 各节点联通测试完毕，本地和redis节点联通测试完毕
> 步骤：
> 	1> 安装redis节点
> 		注* redis同级目录
> 		1、mkdir redis-cluster
> 		2、cd redis-cluster
> 		3、将redis目录下的安装内容给6个新建文件夹都考一份。命令参考：
> 			cp -r redis/redis-4.0.9/ redis-cluster/redis01  *如果没有redis01文件夹会自动创建
> 		4、将6个新建子文件夹中的快照文件dump.rdb删除。命令参考：
> 			rm -rf dump.rdb
> 		5、修改6个新建子文件夹中redis.conf，一共两处
> 			① port xxxx
> 			② cluster-enabled yes
> 			注* 我在搭建过程中，有两个端口号是3333和4444，搭建完成后，死活这两个连不上，改端口为
>             	3330和4440后，才可以连了。 
> 			注*此时redis.conf一定不要设置密码。否则redis-trib.rb创建集群会报错连不上节点。
> 				创建完成集群之后，再用命令设置密码。
> 		6、启动全部的6个节点
> 			① 方法1：手动挨个启动
> 			② 方法2：创建脚本文件，批量执行命令。
> 				1、touch start-all.sh。内容参考:
> 					cd redis01
> 					./src/redis-server ../redis.conf
> 					cd ..
> 					cd redis02
> 					...
> 					...
> 					cd redis06
> 					./src/redis-server ../redis.conf
> 				注* 如果start-all.sh是window新建的话，需要在linux中修改格式。
> 					vi start-all.sh
> 					: set ff=unix
> 					保存退出
> 				2、修改该脚本的权限：
> 					chmod +x start-all.sh
> 	2> 准备redis-trib.rb文件的运行环境：
> 		1、yum install ruby   -- 安装ruby语言运行环境
> 		2、gem install redis-3.0.0.gem -- 把ruby相关的包安装到服务器 参考备注
> 		3、安装RVM，如果没有curl，先安装curl。用RVM升级ruby到2.2.2以上 -- 参考安装RVM章节
> 		注* redis-trib.rb是一个ruby文件，所以需要ruby文件的运行环境。
> 		注* redis-trib.rb在redis安装文件中。
> 		注* CentOS7系统的话：安装完ruby之后，需要安装RVM，用RVM对ruby升级到v2.2.2以上，否则执行			redis-trib.rb命令创建集群的时候后报错。
> 		注*  把ruby相关的包安装到服务器
> 			https://rubygems.org/gems/redis/versions/4.1.0
> 			links --> download -- 需要将redis-3.0.0.gem单独下载下来，再上传服务器，再安装
> 	3> 操作防火墙：
>     	1、开放6个节点的端口，开放6个节点对一个的总线程端口 -- 参考整合Redis中的CentOS7防火墙操作 
> 		注*总线程端口是节点端口加10000，比如6个节点的端口是1111,2222,3333....6666，则对应总线程			端口为11111,12222,13333...16666
> 	4> 执行redis-trib.rb命令创建集群
> 		./redis-trib.rb create --replicas 1 39.105.32.104:1111 39.105.32.104:2222 				39.105.32.104:3330 39.105.32.104:4440 39.105.32.104:5555 39.105.32.104:6666
> 		1、--replicas 1的含义：从机数/主机数
> 		注：redis-trib.rb在redis的安装文件中。或者cp命令把该文件赋值一份到redis-cluster中
> ```
>
> #### 安装RVM
>
> ```python
> 步骤：
> 	1> 安装 curl 
> 		#  sudo yum install  curl
> 	2> 安装 RVM
> 		#  curl -L  get.rvm.io | bash -s stable
> 	注* 上面领命会报错，因为防火墙阻挡了安装
> 	3> 失败后会有提示：or if it failed:
>         command curl -sSL https://xxxxx    -- 获取公钥
> 	4> 执行上面提示命令，然后继续执行安装RVM命令：#  curl  -L  get.rvm.io |  bash -s  stable
> 	5> 提示：Thank you for using RVM!
> 		上面还有提示：To start using RVM you need to run 'source/etc/profile.d/rvm.d'
> 	6> 执行命令：source/etc/profile.d/rvm.d
> 	7> 下载RVM依赖
> 	8> 查看centos  下rvm管理的软件和版本
> 		#  rvm  list known
> 	9> 安装ruby-2.2
> 		rvm install ruby-2.2.0
> 	10> 查询当前使用的版本
> 		# rvm info
> 来源：
> 	安装RVM的正确姿势：https://cloud.tencent.com/developer/article/1151349
> 原则：
> 	按照失败之后的提醒，来操作，而不是按照网上的步骤来做
> RVM各种命令：
> 	https://blog.csdn.net/shaonian_wo/article/details/78007722
> ```
>
> #### 报错记录
>
> ```python
> 1、一直卡在Waiting for the cluster to join....的问题  
> 	https://blog.csdn.net/xianzhixianzhixian/article/details/82392172 
> 	解决：
> 		1> 打开集群总线端口   linux
> 		2> 打开集群总线端口   aliyun安全组
> 		或者
> 		1> 直接关掉防火墙
> 
> 2、报错slot xx已经被分配过了
> 	错误：
> 		ERR Slot 0 is already busy (Redis::CommandError)
> 	原因：
> 		已经执行过./redis-trib.rb create --replicas 1命令，再次执行的时候，后报该错误。
> 	解决：
> 		节点挨个连接，挨个执行flushall和redis reset
> 
> 3、配置参数含义  
> 	描述：
> 		集群的redis-1111.conf的配置含义
> 	来源：
> 		https://blog.csdn.net/bigtree_3721/article/details/78883857
> 
> 4、升级ruby问题
> 	--参考安装RVM
> 
> 5、.sh文件权限问题，ff=unix问题
> 	来源：https://blog.csdn.net/qq_28096687/article/details/79356173
> 	总结：
> 		在windows环境下任何工具编写sh脚本文件，在上传到linux环境后执行sh脚本前千万记得要
> 		set ff=unix，去掉每行尾部多余的\r。
> 
> 6、3333端口和4444端口无效
> 	错误：
> 		端口有毒
> 	原因：
> 		猜测是这两个端口被系统的某些服务占用了
>     解决：
>     	待解决
> 
> 7、集群搭建成功，但是不能存入值，一直卡在Redirected to slot [8949] 
> 	注意：redis-trib.rb执行创建集群命令，不能用127.0.0.1一定要用具体ip
> 		集群搭建完成之后，服务端redis-cli可以连接，其他地方都不能连接
> 	过程:
> 		1> window本地: 连接redis-cli -c -h 39.105.32.104 -p 1111   
> 			没有设置密码，不需要加-a
> 		2> 执行set方法，set name guozi
> 		3> 一直卡在： Redirected to slot [10138] located at 127.0.0.1:2222     
> 			查询并没有存进去，因为也没有输出+OK
> 	原因：
> 		Redirected to slot [8949] located at 127.0.0.1:2222   
> 		注意：
> 			ip是127.0.0.1  
> 			这个是执行./redis-trib.rb create replicas 1 127.0.0.1 1111  .....
> 			这个命令的时候，定的。
> 			执行set name guozi的时候，输出信息表明redis集群回去找127.0.0.1的2222端口，
> 			而window客户端的127.0.0.1是window本地的ip，所以找不到。
> 			redis集群所在机器的127.0.0.1正好是服务端所在的机器，所以可以找到，可以存进去。
> 	解决：
> 		按照 重新执行搭建集群命令 执行。将ip从127.0.0.1改为具体的iP
> 
> 
> 8、重新执行搭建集群命令
> 	1> 删除nodes.conf、删除dump.rdb
> 	2> 节点挨个连接，挨个执行flushall和redis reset
> 	3> 重新执行命令：./redis-trib.rb create --replicas 1
> 
> 9、redis版本、centos系统版本问题
> 	1> 不能随便跟着网上的执行步骤走，因为可能版本不一样，网上前面的几乎都是redis3.x的版本
> 	2> 安装ruby升级到工具，也是，网上的方法已经过时了。跟着安装出现的  错误后解决步骤走就可以自己解		决
> 	3> 网上说的redis安装目录下有bin目录，但是redis4.x是没有的。需要自己解决，
> 		cp redis4.0.9/ ../redis-cluster/redis01。把整个redis的安装目录移动到redis01下面
> 
> 10、集群密码：
> 	1> 搭建的时候，千万不要设置密码。否则会报连接ip:port失败(第一个子节点就连不上)
> 	2> 设置密码的时机：集群搭建完成
> 		1、命令行的方式，优点是不用重新启动服务
> 		2、简单粗暴，反正已经集群搭建完毕了。直接把每个节点的redis.conf改了，加上密码
> 			(masterauth 和 requirepass )。再把节点按新的redis.conf启动起来。
> 	3> 命令行方式：
> 		1、redis.cli -c -h 39.105.32.104  -p 1111(第一个节点)
> 		2、config set masterauth passwd123 
> 		3、config set requirepass passwd123 
> 		4、这时候再操作，已经要报错了，需要密码，所以，退出，重新加上密码连接一次
> 		5、redis.cli -c -h 39.105.32.104  -p 1111 -a 123456，这时可以重新连接成功了
> 		6、执行命令，把刚才的设置写入redis.conf配置文件：config rewrite 
> 		7、同样的步骤，把剩下的5个redis实例，都设置密码，不论主还是从
> 	4> 来源：https://www.cnblogs.com/linjiqin/p/7462822.html
>         
> 11、 创建集群报错
> 	在运行ruby的时候，一直报错>>> Creating cluster [ERR] Sorry, can't connect to node
> 	因为节点设置了密码，千万不能设置密码，而应该搭建集群完毕之后，再用命令设置密码
> ```
>
> #### 一路搜刮
>
> ```python
> 1> linux下gpg的加密解密说明
> 	https://www.linuxidc.com/Linux/2015-02/113015.htm
> 2> redis5.x工具文件是c写的，不再是ruby写的了
> 3> centos7需要ruby版本在2.2.2之上
> 4> RVM各种命令：
> 	https://blog.csdn.net/shaonian_wo/article/details/78007722
> 5> curl命令和yum命令的区别
> ```

#### 4、集群模式(客户端分片)

> ```python
> 
> ```

#### 5、集群模式(twenproxy)

> ```python
> https://www.cnblogs.com/crazylqy/p/7455633.html
> ```

#### 6、集群和主从+哨兵哪个好

> ```python
> https://q.cnblogs.com/q/109403/
> https://www.cnblogs.com/demingblog/p/10295236.html
> https://www.cnblogs.com/crazylqy/p/7455633.html -- 大牛
> ```

#### 7、一路搜刮

> #### 验证机器联通
>
> ```python
> 1、原本打算，我计算机部一个redis，我计算机上的虚拟机部一个redis，aliyun上部一个redis。但是好像		redis集群只能部署在同一个局域网内。因为你拿你的192.168的局域网段去ping阿里云的公网吗？
> 2、我计算机和计算机上的虚拟机，相互ping没有问题。
> 3、改变策略，我本地计算机部一个redis，虚拟机部一个，重新创建一个新的虚拟机部一个。
> 4、接着改变策略：
> 	1> redis集群有两种：一是redis-sentinel模式，二是redis-cluster模式
> 	2> 实例部署的时候有两种方式：一是不同机器，二是同一机器
> 	3> redis版本选择其中的两种，5.x和4.x
> 	决定：aliyun部署方式：
> 			1、是同一机器
> 			2、部署不同实例，
> 			3、用redis-sentinel模式，
> 			4、Redis版本5.x
> 			5、操作系统 CentOS7
>     	  我的虚拟机部署方式：
> 			1、三台不同虚拟机
> 			2、每个环境部署一个实例
> 			3、用redis-cluster模式
> 			4、Redis版本4.x
> 			5、操作系统 CentOS6
> ```
>
> #### 公网IP和私网IP的区别
>
> ```python
> 1、简介
> 	1> 在Internet网络上有上千百万台主机，为了能够将这些主机区分开来，于是就给每台主机都分别配了一个		专门的地址，称为IP地址。
>     2> 通过IP地址就可以访问到每一台主机。IP地址由4部分数字组成，ghost win7每部分数字对应于8位二制	    数字，各部分之间用小数点分开。如某一台主机的IP地址为：211.152.65.112 ，Internet IP地址由		  NIC(Internet Network Information Center)统一负责全球地址的规划、管理;同时由Inter NIC、		  APNIC、RIPE三大网络信息中心具体负责美国及其它地区的IP地址分配。
> 2、固定IP和动态IP区别
> 	1> 固定IP地址是长期固定分配给一台计算机使用的IP地址，一般是特殊的服务器才拥有固定IP地址。	
> 	2> 因为IP地址资源非常短缺，通过电话拨号上网或普通宽带上网用户一般不具备固定IP地址，而是由ISP动		态分配暂时的一个IP地址。普通人一般不需要去了解动态IP地址，这些都是计算机系统自动完成的。
> 4、公有地址和私有地址区别
> 	1> 公有地址(Public address)由Inter NIC(Internet Network Information Center 因特网信息中   			心)负责。这些IP地址分配给注册并向Inter NIC提出申请的组织机构。通过它直接访问因特网。
> 	2> 私有地址(Private address)属于非注册地址，专门为组织机构内部使用。
> 	   私网IP是专门给一些局域网内用的。也就是说在网络上是不唯一的，公网上是不能通这个私有IP来找到		   	  应的设备的。
> 	   以下范围内的IP地址属于内网保留地址，即不是公网IP，而是属于私有IP:
> 			10.0.0.0 - 10.255.255.255
> 			172.16.0.0 - 172.31.255.255
> 			192.168.0.0 - 192.168.255.255
> 	3> 最大区别是公网IP世界只有一个，私网IP可以重复，但是在一个局域网内不能重复访问互联网是需要IP地		址的，IP地址又分为公网IP和私网IP，访问互联网需要公网IP作为身份的标识，而私网IP则用于局域		 网，在公网上是不能使用私网IP地址来实现互联网访问的。公网IP在全球内是唯一的。也就是说在同一		时间一个IP(除了一些特别的IP，如：154.0.0.0等)只代表一能设备，所以通只要找得到IP，也就可以		 找到特定的设备了。如果A是公网IP，且没有防火墙等Ban连接的话，那么B电脑上的EM就可以找并连接		  上A了。
> 6、总结
> 	公网IP，是在互联网上使用的，在任何地方只有能连网都能访问公网IP。而私有IP是局域网所使用的，通过	  互联网是不能访问私有IP的。
> ```
>
> #### 阿里云公网IP理解
>
> ```python
> 我和下面这个网友的疑惑相同：
> 	  我也不太懂，能给我讲讲吗？，是我的ecs对应一个公网ip吗，公网ip不是很缺乏吗，内网里就只有我的一     个服务器吗，好难理解
> 
>   
> 找到答案了：https://bbs.csdn.net/topics/390933060
> 全世界公网IP有多少个：https://zhidao.baidu.com/question/586704140.html
> 为什么我没有公网IP，我是ADSL的：那是因为你通过NAT接入互联网的，具体情况你要咨询宽带运营商了
> 
> 
> 	整个网络课程才好
> 未完待续....
> ```
>
> #### 查看端口是否被占用
>
> ```python
> Windows 上使用命令 
> 	netstat -ano | findstr "6379" 
> Linux机器上用命令 
> 	netstat -tunlp | grep 6379
> ```
>
> #### telnet登录远端redis
>
> ```python
> https://yq.aliyun.com/articles/692132?spm=a2c4e.11155472.0.0.549b69dfZb6yP5
> 1、可以正常连接
> 2、可以进行set操作
> 3、可以进行get操作
> 实战1：redis没有密码
> 	1> telnet 12.168.1.125 9999  注：ip是本地虚拟机，9999是redis端口
> 	2> 出现空白的黑窗口
> 	3> 因为没有密码，直接键入命令：set name guozi
> 	4> 输出+OK
> 	5> 键入命令：get name
> 	6> 输出$12 guozi
> 实战2：redis设置了密码
> 	1> telnet 12.168.1.125 9999
> 	2> 出现空白的黑窗口
> 	3> auth 123456  #注123456是redis的密码
> 	4> 操作和上面一样，get和set等
> 注：连接redis服务端方法：
> 	1> 安装了redis-cli客户端   #redis-cli -h 12.168.1.125 -p 9999 -a 12345
> 	2> 安装了可视化界面redis-desktop-manager
> 	3> 使用telnet  #telnet 12.168.1.125 9999  #auth 123456
> 来源：https://www.cnblogs.com/eyesfree/p/9186363.html
> ```
>
> #### telnet远程登录的两种方式
>
> ```python
> 方式一：telnet
> 方式二：ssh
> 来源：https://www.cnblogs.com/chinas/p/4484409.html
> ```
>
> #### 浅谈CMD和PowerShell的区别
>
> ```python
> 1、PowerShell是微软推出的新一代命令行工具，与 .NET Framework框架无缝链接，功能较之cmd更加全面，命	  令更加丰富，完全用面向对象的思想编写，“Everything is object”。
> 2、https://www.jb51.net/article/72197.htm/
> 3、打开powershell的方式也是：win + R --> powershell
> ```
>
> #### netsh命令使用详解
>
> ```python
> 1、https://blog.csdn.net/zdhlwt2008/article/details/46737267
> 2、网卡什么的，要是有一个网络课程就好了。
> 3、netsh interface portproxy的微软帮助文档地址：
> 	https://technet.microsoft.com/zh-cn/library/cc776297(WS.10).aspx#BKMK_1
> ```
>
> #### DNS工作原理
>
> ```python
> https://www.cnblogs.com/codecc/p/dns.html
> DNS：DNS(Domain Name System)，域名系统
> ```
>
> #### tcmalloc，jemalloc和libc对应的三个内存分配器 
>
> ```python
> 1、malloc的全称是memory allocation，中文叫动态内存分配
> 	allocate 美[ˈæləˌket]  v.分配
> 	allocation  美[ˌæləˈkeɪʃn]  n.分配
> 	allocator  美['æləkeɪtə]  n.分配器
> 2、来源：https://blog.csdn.net/libaineu2004/article/details/79400357
> ```
>
> #### redis-cli命令参数大全
>
> ```python
> 1、-r命令重复执行多次
> 	redis-cli.exe -h 192.168.1.126 -p 8888 -a 123456 -r 3 ping
> 2、-i是命令重复执行多次时，每次返回响应的时间间隔
> 	redis-cli.exe -h 192.168.1.126 -p 8888 -a 123456 -r 3 -i 3 ping
> 	或者
> 	redis-cli.exe -h 192.168.1.126 -p 8888 -a 123456 -r 10 -i 1 info|findstr 				used_memory_human 注：如果是linux则把findstr改为grep
> 3、info查看服务端信息
> 	redis-cli.exe -h 192.168.1.126 -p 8888 -a 123456 info
> 4、-c
> 	连接集群结点时使用，此选项可防止moved和ask异常
>     
>     
> 缩写：
> 	-r   repeat
> 	-i   internal
> 来源：http://www.cnblogs.com/kongzhongqijing/p/6867960.html
> ```
>
> #### linux下创建文件的多种
>
> ```python
> 方法一：
> 	touch filename
> 	vi filename  -- 编辑内容
> 方法二：
> 	vi filename
> 	写完，保存退出的时候，如果没有该文件，会自动创建。
> ```
>
> #### screen命令用法
>
> ```python
> https://www.cnblogs.com/runtheworld/p/5659098.html
> ```
>
> #### rpm -qa的含义
>
> ```python
> yum install screen -y
> rpm -qa | grep screen
> ```

#### 8、java访问redis集群

> #### 报错：NOAUTH Authentication required
>
> ```python
> 问题：
> 	已经在application.yml中配置了spring.redis.password=yourpassword，
> 	但是这个配置在JedisConnectionFactory中没有被加载进去
> 解决：
> 	手动加载
> 	@Bean
>     JedisConnectionFactory jedisConnectionFactory() {
>         JedisConnectionFactory factory = new JedisConnectionFactory();
>         factory.setPassword("12345678....");
>         return factory;
>     }
> 来源：
> 	https://blog.csdn.net/shangyadongze/article/details/80371998
> ```
>
> #### 报错：timeout问题
>
> ```python
> application.yml中的spring.
> ```
>
> #### 报错：java代码问题
>
> ```python
> 1> 下面两个模板都能操作redis
> 	@Autowired  //操作字符串的template，StringRedisTemplate是RedisTemplate的一个子集
>     private StringRedisTemplate stringRedisTemplate;
> 
>     @Autowired  // RedisTemplate，可以进行所有的操作
>     private RedisTemplate<Object,Object> redisTemplate;
> 2> 但是结果：
> 	redisTemplate存入的是对象，redis中key为:"\xac\xed\x00\x05t\x00\x03age"
> 	stringRedisTemplate存入的是字符串，redis中key为："age"
> ```
>
> #### 注意：配置application.yml
>
> ```python
> spring:
>     redis:
>         password: 123456  #注意：password配置在redis下面
>         # 连接超时时间（毫秒）
>         timeout: 5000  #注意：超时时间不能为0
>         #采用哪个数据库
>         database: 0
> 
>         sentinel:
>           master: s1  #注意：主机名称，是sentinel.conf中配置的名称
>           #三个哨兵的端口
>           nodes: 192.168.1.125:26379,192.168.1.125:26380,192.168.1.126:26379 
> ```
>
> #### 报错：代码执行了，但是在redis中查找不到
>
> ```python
> 问题：
> 	1> java代码执行了，但是telent或者redis-cli连接192.168.1.125 1110之后，查找。没有存入的key
> 	2> application.yml中将sentinel下的master从s1改为s2之后，连接192.168.1.126 2220，可以找到
> 	3> 重新改回s1，重新执行代码，连接192.168.1.125 1111，可以找到
> 结论：
> 	1> 想起来了：搭建起来主从+哨兵模式后，为了测试，将192.168.1.125的主机，即1110端口的实例杀掉		了，测试哨兵是否按机制起作用。
> 	2> 疑问：1111是成功变为了主机，但是好像1110并没有变为从机。如果是从机了，就应该有主从复制成功
> 	3> 有时间再测试一下，哨兵是否起作用
> ```

#### 9、大牛知识扩展

> ```python
> 第一步：
> 	所有redis部署方式
>     1> 可以利用主从模式实现读写分离，主负责写，从负责只读，同时一主挂多个从。在Sentinel监控下，还可		以保障节点故障的自动监测。
>     2> 上面分别介绍了多Redis服务器集群的两种方式，它们是基于客户端sharding的Redis Sharding
>     3> 基于服务端harding的Redis Cluster。
>     4> twemproxy处于客户端和服务器的中间，将客户端发来的请求，进行一定的处理后(如sharding)，再转		发给后端真正的Redis服务器。也就是说，客户端不直接访问Redis服务器，而是通过twemproxy代理中		 间件间接访问。
>     来源：https://www.cnblogs.com/crazylqy/p/7455633.html
>     
> 第二步：
> 	集群开机自启动
> ```

