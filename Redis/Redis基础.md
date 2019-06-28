### 不记文档，白忙一场

------

#### 0、Redis介绍

> #### redis官网
>
> ```python
> https://redis.io
> https://redis.io/download
> ```
>
> #### 官网推出的在线测试工具
>
> ```python
> http://try.redis.io/
> Redis官方已经在他那边部好了服务端，我们直接在页面进行命令测试就可以了。
> ```

#### 1、实战步骤

> ```python
> 第一步：源码编译安装Redis4.x
>     官网：https://redis.io/download#installation
>     下载：wget http://download.redis.io/releases/redis-4.0.9.tar.gz
>     解压：tar -zxvf redis-4.0.9.tar.gz
>     进入：cd redis-4.0.9
>     编译：make
> 
>     注意1：解压之后，进入解压后的目录，最重要的就是一个src的目录，这里面是它的源码。底层用c写的。
>     注意2：只需要make编译就可以了，不需要make install安装。
>     注意3：make、make install和configigure的区别详见linux笔记目录。
> 第二步：修改redis.conf配置文件
> 	开发环境：
> 		1> 注释掉bind 127.0.0.1
> 		2> 注释掉protected-mode yes
> 	生产环境：
> 		1> 注释掉bind 127.0.0.1 -- NETWORK
> 		2> 修改端口号 port 6379  --  NETWORK
> 		3> 保持protected-mode yes 
> 		4> 设置后台运行 -- GENERAL
> 		5> 添加密码 -- SECURITY
> 第三步：开放端口 (redis服务端所在服务器)
> 	详见CentOS7防火墙操作 --> 开放、关闭端口
> 第四步：指定IP访问端口 (aliyun的ESC页面)
> 	详见aliyun网络和安全组操作
> 第五步：指定IP访问端口 (redis服务端所在服务器)<生产环境>
> 	详见CentOS7防火墙操作 --> 指定IP对某端口访问
> 注意：之所以需要设置两道防火墙的原因
> 	安全组是脱离服务器的系统内部的一到防火墙，可以将安全组类比家里的路由器，服务器类比家里的电脑。
> 	来源：https://blog.csdn.net/opengps/article/details/81213591	
> ```

#### redis-conf配置文件

> #### 设置密码
>
> ```python
> 在SECURITY模块下，
> 	找到requirepass foobar，修改为requirepass 123456。你的密码就是123456了。
> 注意：其中foobar，没有任何意义，只是占位符
> ```
>
> #### 启动后台运行
>
> ```python
> 在GENERAL模块下，
> 	找到daemonize no，将值该为yes。
> 	则开启服务端之后，不需要一直保持窗口打开。当然redis标识什么的也不会出现。只是控制台打印三行输出
> ```

#### CentOS7防火墙操作

> #### 防火墙命令
>
> ```python
> 1、安装
> 	yum install firewalld
> 	yum install firewall-config   --如果需要使用图形化配置工具
> 	注意：wget只是获取源码的压缩包。yum是直接安装。
> 2、启动
> 	systemctl start firewalld
> 3、停止
> 	systemctl stop firewalld
> 4、停止
> 	systemctl restart firewalld
> 5、查询状态
> 	systemctl status firewalld
> 	或
> 	firewall-cmd --state
> 6、启用开机自动启动
> 	systemctl enable firewalld
> 7、禁用开机自动启动
> 	systemctl disable firewalld
> 8、查看自动启动状态
> 	systemctl is-enabled firewalld
> 注意：来源https://www.cnblogs.com/bldly1989/p/7209632.html
> ```
>
> #### 开放、关闭端口
>
> ```python
> 1、查看端口开启状态
> 	firewall-cmd --query-port=6666/tcp
> 2、开启端口
> 	firewall-cmd --add-port=6666/tcp --permanent
> 3、关闭端口
> 	firewall-cmd --remove-port=6666/tcp --permanent
> 4、重新加载配置
> 	firewall-cmd --reload
> 5、查看端口是否开放
> 	firewall-cmd --query-port=6379/tcp
>     
> 注意1：--permanent表示永久生效，重启不会丢失配置。需要firewall-cmd --reload之后才会生效
> 注意2：关闭端口会有提示 -- Warning: NOT_ENABLED: 9998:udp
> 注意3：重启防火墙，也可以使配置生效 -- systemctl restart firewalld.service
> ```
>
> #### 指定IP对某端口访问
>
> ```python
> 第一步：添加允许
> 	firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source 						address="192.168.1.118" port protocol="tcp" port="6666" accept"
> 第二步：添加拒绝
> 	firewall-cmd --permanent --add-rich-rule="rule family="ipv4" source 						address="192.168.1.119" port protocol="tcp" port="6666" drop"
> 第三步：查看配置结果，验证配置
> 	firewall-cmd --list-all
> 第三步：重新加载使生效
> 	firewall-cmd --reload
>    
> 追加1：删除规则
> 	firewall-cmd --permanent --remove-rich-rule="rule family="ipv4" source 						address="192.168.1.118" port protocol="tcp" port="6666" accept"
> 追加2：批量操作规则
> 	firewall-cmd --permanent --list-rich-rule
> 		rule family="ipv4" source address="139.130.99.0/24" port port="22" protocol="tcp" 		  accept
> 		rule family="ipv4" source address="139.129.0.0/24" port port="22" protocol="tcp"   		   accept
> 		rule family="ipv4" source address="58.218.198.159" port port="22" protocol="tcp" 		 drop
> 追加3：必须--reload才能生效的原因：
> 		直接使用firewall-cmd修改的规则是不需要更新就可以直接生效的，但是如果加了--permanent参数，	或者直接编辑xml文件之后就需要我们手动reload了，firewall-cmd提供了两个更新规则的参数：--reload	 和--complete-reload，前者只是更新需要更新规则，而且更新的过程中不会影响现有的连接，而后者在更	新时会将所有的规则清除掉然后重建，而且为了安全考虑，在更新之前首先会将策略设置为DROP，等更新完	 成之后再恢复为ACCEPT，这样就会对现有连接造成影响，所以如果没有特殊需求我们应该尽量使用前者。具		体命令如下：
> 		[root@excelib.com ~]# firewall-cmd --reload
> 		[root@excelib.com ~]# firewall-cmd --complete-reload
> 	来源：https://www.cnblogs.com/bldly1989/p/7209632.html
> 追加4：permanent 美[ˈpɜ:rmənənt]  adj.永久（性）的，永恒的，不变的	
> ```
>

#### CentOS6防火墙操作

> #### 开放、关闭端口
>
> ```python
> 1. 开放端口命令： /sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
> 2. 保存：/etc/rc.d/init.d/iptables save
> 3. 重启服务：/etc/init.d/iptables restart
> 4. 查看端口是否开放：/sbin/iptables -L -n
> ```
>
> #### 指定IP对某端口访问
>
> ```python
> 【注意】：大牛来源https://blog.csdn.net/hel12he/article/details/46911159
>     不能通过bind属性值来完成该限定
> 第一步：注释掉原来的bind 127.0.0.1可以放开访问权限，然后再用防火墙进行限制
> 第二步：通过iptables 允许指定的外网ip访问
> 	1> iptables -A INPUT -s 127.0.0.1 -p tcp --dport 6379 -j ACCEPT	//只允许127.0.0.1访问		6379
> 	2> iptables -A INPUT -p TCP --dport 6379 -j REJECT //其他ip访问全部拒绝
> 	
> 注意1：大牛来源https://blog.csdn.net/hel12he/article/details/46911159
> 注意2：centos7之后，防火墙不再是iptables，而是firewalld
> 注意3：在redis.conf中配置bind属性纯属扯淡，这个在网上是错误的解释。详情见大牛来源地址
> 结论：方法只有一个，就是redis.conf配置文件修改 + 防火墙设置。redis.conf修改有两种方法：
> 	1>注释掉bind 127.0.0.1
> 	2>修改bind属性值为redis所在服务器的ip地址<但是我试了，不好使，不知道是否ip拿错了>
> 笔记1：iptables中参数含义
>     1.INPUT　　　　——进来的数据包应用此规则链中的策略
>     2.OUTPUT　　   ——外出的数据包应用此规则链中的策略
>     3.FORWARD　　——转发数据包时应用此规则链中的策略
>     4.PREROUTING  ——对数据包作路由选择前应用此链中的规则
>     	（记住！所有的数据包进来的时侯都先由这个链处理）
>     5.POSTROUTING ——对数据包作路由选择后应用此链中的规则
>     	（所有的数据包出来的时侯都先由这个链处理）
> 
>     -A  在指定链的末尾添加（append）一条新的规则
>     -D  删除（delete）指定链中的某一条规则，可以按规则序号和内容删除
>     -I  在指定链中插入（insert）一条新的规则，默认在第一行添加
>     -R  修改、替换（replace）指定链中的某一条规则，可以按规则序号和内容替换
>     -L  列出（list）指定链中所有的规则进行查看
>     -E  重命名用户定义的链，不改变链本身
>     -F  清空（flush）
>     -N  新建（new-chain）一条用户自己定义的规则链
>     -X  删除指定表中用户自定义的规则链（delete-chain）
>     -P  设置指定链的默认策略（policy）
>     -Z 将所有表的所有链的字节和数据包计数器清零
>     -n  使用数字形式（numeric）显示输出结果
>     -v  查看规则表详细信息（verbose）的信息
>     -V  查看版本(version)
>     -h  获取帮助（help）
> 	来源：https://www.cnblogs.com/lemon-flm/p/7608029.html
> ```

#### aliyun网络和安全组操作

> ```python
> 步骤：ESC页面 --> 实例 --> 更多 --> 网络和安全组 --> 安全组配置 --> 配置规则 --> 快速创建规则
> 注意1：自定义端口，需要写成6666/6666，不能只写6666，因为指定的是端口号的范围。否则会报错。
> 注意2：授权对象，如果是全部，写成0.0.0.0/0
> 	0.0.0.0/0的含义：https://www.cnblogs.com/hnrainll/archive/2011/10/13/2210101.html
> 示例：我的redis端口号改为了6666，需要对所有Ip放开这个端口号，则
> 	自定义端口：6666/6666
> 	授权对象：0.0.0.0/0
> 	协议类型：自定义TCP
> 注意3：阿里云ESC安全组规则
> 	https://help.aliyun.com/document_detail/51324.html?											spm=5176.11065259.1996646101.searchclickresult.168239e7m3ZP9d
> 注意4：阿里云服务器端口不能访问的原因：安全组
> 	https://blog.csdn.net/opengps/article/details/81213591
> ```

#### 报错：远程连接统一问题

> ```python
> 1、如果是保护模式，且注释掉bind属性，即没有绑定特定的ip，那么远程连接，就必须设置密码。
>    保护模式的作用定义如下：
> 	Redis is running in protected mode because protected mode is enabled, no bind address 	  was specified, no authentication password is requested to clients. In this mode             connections are only accepted from the loopback interface.
>    解决办法如下：
> 	1> protected-mode yes + requirepass 123456 + #bind 127.0.0.1
> 	2> protected-mode no + #requirepass 123456 + #bind 127.0.0.1
> 2、有客户端的地方，就可以远程连接，不论是可视化界面还是命令行窗口的客户端。eg.window下的命令行窗口
> 	redis-cli.exe -h 39.105.32.104 -p 6666 -a 123456。其中
> 	redis-cli.exe是命令行
> 	-h是host，即远程服务器ip。默认是127.0.0.1
> 	-p是redis端口。默认是6379
> 	-a是redis的连接密码
> ```

#### 报错：远程连接虚拟机redis

> ```python
> 问题描述：
> 	第一步：本地虚拟机，xshell连接，按照上一步步骤，安装，启动服务端，启动客户端，操作客户端，存取		redis中数据正常。
> 	第二步：保持服务端启动状态，本地Redis Desktop Manager创建连接，测试连接，失败。
> 	第三步：修改redis.conf配置文件，修改bind属性值为本地ip，重启服务端，测试连接，失败。
> 	第四步：xshell连接虚拟机，开放端口6379，测试连接，失败。
> 解决问题：
> 	解决问题一共两步，缺一不可。
> 	第一步：修改redis.conf配置文件，修改bind属性值为本地ip。超重要的是，启动命令一定要加上配置文			件。
> 	第二步：开放端口，如果redis.conf的port属性值你没有修改，就开放6379，如果改了，就开放修改过后的		值。
> 笔记：
> 	1、带配置文件启动命令：cd src --> ./redis-server ../redis.conf
> 		如果不带配置文件的话，启动命令会默认使用默认的配置，而不会读取redis.conf配置文件。所以即使		  你修改了配置文件，但是启动命令不带配置文件参数，也是不会生效的。
> 	2、开放端口：
> 		系统1：CentOS6
> 			1. 开放端口命令： /sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
> 			2. 保存：/etc/rc.d/init.d/iptables save
> 			3. 重启服务：/etc/init.d/iptables restart
> 			4. 查看端口是否开放：/sbin/iptables -L -n
> 		系统2：CentOS7
> 			1. 开放端口：firewall-cmd --add-port=6379/tcp --permanent
> 			2. 使生效：firewall-cmd --reload
> 			3. 查看端口是否开放：firewall-cmd --query-port=6379/tcp
> ```

#### 报错：远程连接阿里云redis

> ```python
> 环境：
> 	CentOS 7.4
> 	redis-4.0.9
> 经过：
> 	1、开放端口：CentOS7的防火墙不再是iptables，而是firewalld，使用新命令开放端口
> 	2、阿里云开放端口：放开所有
> 	3、设置远程连接密码
> 结论：
> 	
> ```

#### 报错：找不到.redis.conf.swp

> ```python
> 问题：上一次修改redis.conf文件的时候，没有正好退出，比如ctrl + z，导致生成.redis.conf.swp文件。
> 	但是在文件中并没有找到这个文件，执行find / -name .redis.conf.swp可以找到该文件路径。进入路		径，还是没有找到。
> 解决：执行命令 ll -a
> ```

#### Redis键命令

> ```python
> 0-15：redis默认有16个数据库，默认是在第0个数据库中操作
> select num:切换数据库
> keys *：所有键
> del key:删除键
> EXPIRE key seconds:给指定的key添加过期时间，单位是s
> ttl key:以秒为单位，返回这个键剩余的时间秒数
> exists key:判断一个键是否存在
> flushdb: 删除当前数据库中所有的键
> flushall:删除所有数据库中的键
> ```

#### telnet相关

> ```python
> 1、全称
>     ftp：file transfer protocol，文件传输协议。
>     Telnet：telecom munication net work protocol，电信网络协议。
>     BBS：Bulletin Bard System，电子公告牌系统。
>     Usenet：User's Net，属于所有网络使用者的逻辑网络。
>     
>     TCP/IP分为两部分：
>     TCP：Transmission Control Protocol，传输控制协议。
>     IP：Internet Protocol，互联网协议。
>     DNS：Domain Name System，域名命名系统。
>     HTTP：HyperText Transfer Protocol，超文本传输协议。
> 	来源：https://zhidao.baidu.com/question/15049823.html
> 2、使用
> 	ping ip地址 ：可以确认两边网络通着
> 	telnet 39.105.32.104 22 ：可以确认端口是否对自己开放
> 3、telecom 
> 	美['telɪkɒm]  n.telecommunication 电信
> 4、配置、使用、远程访问
> 	https://jingyan.baidu.com/article/ae97a646b22fb6bbfd461d19.html
> 	成功的标志：在windows下按下win+R键，输入cmd，运行命令(需开启telnet)，如果变成空界面表示成功
> 	来源：https://blog.csdn.net/zx110503/article/details/78787483
> 5、格式为：telnet 192.168.1.1 135，ip和端口中间没有冒号
> ```
>
> 