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
> 2、为了达到redis的高可用，有两种部署方式
> 	主从复制+哨兵机制；集群模式。
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
>             #protected-mode yes (可选)
>         2222下的：
>             port 2222
>             slaveof 192.168.1.125  1111 
>             requirepass 123456 (可选)
>             #protected-mode yes (可选)
>         redis.conf的：
>             port 2220
>             slaveof 192.168.1.125  1111 
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
> #### 备注
>
> ```python
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
>         
> 2、启动sentinel控制台输出：
> 错误：
> 	2730:X 17 Mar 16:31:01.009 # WARNING: The TCP backlog setting of 511 cannot be enforced 		because /proc/sys/net/core/somaxconn is set to the lower value of 128.
>     2730:X 17 Mar 16:31:01.009 # Sentinel ID is 211cad3d91800a05c7a60b29afc63d6acbac15f2
>     2730:X 17 Mar 16:31:01.009 # +monitor master s1 192.168.1.125 1110 quorum 2
>     2730:X 17 Mar 16:31:01.009 # +monitor master s2 192.168.1.126 2220 quorum 2
>     2730:X 17 Mar 16:31:31.019 # +sdown master s1 192.168.1.125 1110
>     2730:X 17 Mar 16:31:31.019 # +sdown master s2 192.168.1.126 2220
> 正确：
>     3869:X 18 Mar 07:42:54.044 # WARNING: The TCP backlog setting of 511 cannot be enforced 		because /proc/sys/net/core/somaxconn is set to the lower value of 128.
>     3869:X 18 Mar 07:42:54.047 # Sentinel ID is db2a019c614318639e2afdc86fab1f5b0d1ba5f3
>     3869:X 18 Mar 07:42:54.047 # +monitor master s2 192.168.1.126 2220 quorum 2
>     3869:X 18 Mar 07:42:54.047 # +monitor master s1 192.168.1.125 1110 quorum 2
>     3869:X 18 Mar 07:42:54.049 * +slave slave 192.168.1.126:2221 192.168.1.126 2221 @ s2 		192.168.1.126 2220
>     3869:X 18 Mar 07:42:54.051 * +slave slave 192.168.1.126:2222 192.168.1.126 2222 @ s2 		192.168.1.126 2220
>     3869:X 18 Mar 07:42:54.053 * +slave slave 192.168.1.125:1111 192.168.1.125 1111 @ s1 		192.168.1.125 1110
>     3869:X 18 Mar 07:42:54.055 * +slave slave 192.168.1.125:1112 192.168.1.125 1112 @ s1 		192.168.1.125 1110
> 错误原因：
> 	猜测是没有加密码验证，即：
>         sentinel auth-pass s1 123456 
>         sentinel auth-pass s2 123456
> 	一开始配置：
> 		port 26379
> 		sentinel monitor s1 <ip地址> 6379 2
> 		sentinel monitor s2 <ip地址> 6379 2
> 		protected-mode no
> 	后改为：
> 		port 26379
> 		dir /tmp 
> 		sentinel monitor s1 192.168.1.125 1110 2
> 		sentinel monitor s2 192.168.1.126 2220 2
> 
> 		sentinel auth-pass s1 123456 
> 		sentinel auth-pass s2 123456
> 
> 		sentinel down-after-milliseconds s1 30000
> 		sentinel down-after-milliseconds s2 30000
> 
> 		sentinel parallel-syncs s1 1
> 		sentinel parallel-syncs s2 1
> 
> 		sentinel failover-timeout s1 180000
> 		sentinel failover-timeout s2 180000
> 
> 		protected-mode no
> ```
>
> 

#### 3、集群模式

> ```python
> http://www.cnblogs.com/kerwinC/p/6611634.html
> ```

#### 4、集群开机自启动

> ```python
> 
> ```

#### 5、集群 3主机0从机--待测试

> #### 简介
>
> ```python
> 前言：
> 	目的：
> 		如果使用redis集群只是为了容量扩展，则不需要从机。
> 	原因：
> 		从机是用来主从复制的。
>         
> 测试redis部署模式：
> 	集群模式
> 	主从复制+哨兵机制，本来就是依赖于从机自动替换主机的，如果没有从机，还部署个什么劲儿。
> ```
>
> #### 实战
>
> ```python
> 
> ```

#### 6、集群和主从+哨兵哪个好

> ```python
> https://q.cnblogs.com/q/109403/
> https://www.cnblogs.com/demingblog/p/10295236.html
> ```





#### 

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











