### 听课讲义--有舍才有得

#### 1、基本概念

​	1>	服务器：服务器就是一台电脑，只不过它的性能比较好。就是cpu比较高级，内存比较大，硬盘比较大，	

​		但是一般不装显卡。

​	2>	交换机：公司的服务器都是放在一个大的房子里，好多的服务器，但是我们都是在办公室办公，不可能

​			到服务器的房间工作。所以两边不直接连接，两边都放了交换机，再用xshell等工具连接服务器

​	3>	网卡：查看方式

​			电脑使用网卡：网络->属性->更改适配器选项->比如wifi连接->WLAN->右键属性->网络->连接时使用

​			虚拟机使用网卡：VMWare->编辑->虚拟网络编辑器->桥接模式->桥接到

​	4>	内核：就是现在用的Linux系统，就是用C写的代码

​	5>	shell：系统的用户界面，用户和内核打交道的一个中间层，一个界面

​			人和机器打交道，机器肯定不懂人的命令语言，所以shell就是一个解释器，把人的命令语言解释为

​			机器语言，机器执行后，再解释为人的语言，返回显示出来

​	6>	所有xshell自带python解释器，命令python就可以打开，只是版本比较老

#### 2、基本指令

​	http://man.linuxde.net/

​	1>	uname命令

​		uname -r   带-r参数  输出内核发行号

​		uname -m	带-m参数	输出内核版本号

​		uname --help   查看uname命令的所有参数

​	2>	bash	在原来的shell界面上，再打开一个shell进程

​	3>	vi xxx开始编辑某文件

​		光标移动：j下k上h右l左

​		删除：x

​		添加内容：a

​		退出不保存：esc-> : ->q!

​		退出保存：esc-> : ->wq!

​		查看：cat xxx查看某文件

​	4>	pwd	显示当前目录

​	5>	ls	显示子目录

​	6> 	ls -l或者ll	显示子目录的详细信息

​	7>	ifconfig	命令

​		ifconfig -a 把所有的网络接口都显示出来

​	8>	ping www.baidu.com	看是否ping的通，而且可以看到baidu只是域名，可以看到百度的真实ip地址

​		还可以ping  ip

​		还可以ping 网关

​	9>	cd - 回到上次的目录

​		cd ~回到用户的home目录

​	10>	tab键

​		①补全命令

​		②补全路径

​		如果路径有很多个，就按两下tab键，会分页显示所有匹配的内容，enter键下页

​	11>	service命令

​		service network restart	重启网络，重启xshell。

​		service iptables stop/start/restart	防火墙关闭、打开、重启

​			restart/start/stop都是service命令的参数，所以不

​			能用tab补全

​	12>	ctrl+l或者clear	清屏

​	13>	 hostname	主机名(安装linux系统的时候，自己起的名字)

​	14>	ssh 用户名@ip	远程连接服务器命令

​	15>	shutdown 命令

​		shutdown --help

​		shutdown now	马上关机

​		shutdown +5		5分钟后关机

​		shutdown +5 "xxxxx"	5分钟后关机并带有提示

​		ctrl+c	取消自己的定的关机进程

​		shutdown -c	取消所有的关机进程

​	16>	reboot	重启

​	17>	date命令

​		date	--help

​		date	显示当前时间

​		date -s	修改时间

​		date +%Y/%m/%d	格式化输出

​		date -s "20181002 14:28:50"	或者 date -s 20181002\14:28:50    设置时间

​	18>	cal命令

​		cal	显示当前月日历

​		cal 2018	显示2018年整年的日历

​	19>	ctrl+R	搜索历史命令

​	20>	history	显示历史记录，只有500行，默认配置500行

​	21>	witch xxx	显示可执行文件的路径位置

​	22>	last命令

​		last 显示都是谁登陆了这个服务器

​		last -2	显示最新两行

​		last root	显示root登陆的

​		last -2 root	显示最新两条root登陆的

​	23>	file命令

​		file xxx	查看文件的类型，比如file ls

​	24>	setenforce 0/1	关闭、打开linux安全策略

##### 	netstat命令

​	-l	listener监听

​	-n	number所有都按数字显示，包括域名、端口等等

​	-t	tcp所有tcp协议的进程

​	-u	udp所有udp协议的进程

​	-p	

##### 	sed命令

##### 	awk命令

##### 	压缩解压缩命令

​	tar只是打包

​		1>	tar -cvf	c是create创建 v是visual可视化 f是file文件

​		2>	tar -xvf	x是解压	v和f同上 v可视化是把压缩或者解压缩的文件名列出来	解压到哪个目录，需要		

​			先cd到该目录，再写解压命令，比如：cd /opt	然后tar -xvf /tmp/txt.tar

​	tar打包和zip压缩解压缩结合

​		1>	tar -zcvf	*.txt	打包并压缩

​		2>	tar -zxvf txt.tar.gz		打开包并解压缩

​	tar打包和zip2压缩解压缩结合

​		1>	tar -jcvf *.txt

​		2>	tar -jxvf txt.tar.gz2

##### yum命令

​	1>	yum install -y vim	从yum仓库中拿到vim包的资源并安装      -y是不用你在过程是输入yes，默认一路yes

​	2>	yum remove -y vim 从本地把vim包卸载掉

​		选项：

​			-y	一路默认yes

​			--downloadonly	只下载不安装

​			--downloaddir	下载的路径

​			比如：yum install -y --downloadonly --downloaddir=/tmp/vim vim

​	3>	yum list	把yum仓库中有的包都列出来

##### rpm命令

​	先用yum把包下载下来不安装

​	1>	rpm -ivh	包名	安装

​	2>	rpm -e wget	把wget卸载

​	3>	rpm -qa	查询所有安装的包	-qa是querry all的简写	比如：rpm -qa | grep wget

​	其他选项：

​		-ql	查询安装路径

​		-qa	列出系统的所有软件 querry all

​		-qi	显示包的详细信息	information

​		-qf	查询某个文件是属于哪个rpm包的

#### 3、shell编程语言

​	要学习，shell脚本，是另外一种语言

#### 4、目录

​	home目录是其他用户放在根目录下的home目录下

​	root用户比较特殊，它单独放在了根目录下的root目录下

#### 5、day03命令--错误

​	1>	useradd xiaozuanfeng -g tangseng -u 666

​		useradd  -g tangseng -u 666 xiaozuanfeng 

​		-g   指定主组，组名或者组id
		-u   指定用户id    一般不指定
		-d   指定家目录    一般不指定

​	2>	ll grep.* notfound.txt 2>>error.log

​		2和>>之间不能有空格

​	3>	cat > 1.txt中，不能正常使用删除键

​		需要要ctrl+删除

​		保存不能用ctrl+c，那样就直接退出了

​		保存需要用ctrl+d，保存退出

#### 6、shell脚本中的正则表达式

​	重要

#### 7、挂载还没有敲实例

​	

#### 8、练习

​	**磁盘**

```python
整个磁碟盘上头好像有多个同心圆绘制出的圆形图，而由圆心以放射状的方式分割出磁碟的最小储存单
位，那就是磁区(Sector)， 在物理组成分面，每个磁区大小为512Bytes，这个值是不会改变的。
而磁区组成一个圆就成为磁轨(track)， 如果是在多碟的硬碟上面，在所有磁碟盘上面的同一个磁轨可以组成一个磁柱
(Cylinder)， 磁柱也是一般我们分割硬碟时的最小单位了！
```



```python
扇区：磁盘上的每个磁道被等分为若干个弧段，这些弧段便是磁盘的扇区，每个扇区可以存放512个字节的信息，磁盘驱动器在向磁盘读取和写入数据时，要以扇区为单位。1.44MB3.5英寸的软盘，每个磁道分为18个扇区。 
柱面：硬盘通常由重叠的一组盘片构成，每个盘面都被划分为数目相等的磁道，并从外缘的“0”开始编号，具有相同编号的磁道形成一个圆柱，称之为磁盘的柱面。
磁盘的柱面数与一个盘面上的磁道数是相等的。由于每个盘面都有自己的磁头，因此，盘面数等于总的磁头数。
所谓硬盘的CHS，即Cylinder（柱面）、Head（磁头）、Sector（扇区），只要知道了硬盘的CHS的数目，即可确定硬盘的容量，硬盘的容量=柱面数*磁头数*扇区数*512B。
```

​	**管理磁盘**

​		1>	du命令

​		2>	df命令

​	**给现有磁盘扩容**

```python
磁盘已成功扩展。您必须从客户机操作系统内部对磁盘重新进行分区和扩展文件系统。
```

​		1> fdisk -l 列出所有设备的信息，包括磁盘，光驱，缓存等等

​		2>	fdisk /dev/sda	查看磁盘分区表

​			其中sda是上一步列出来的其中一个，标识磁盘，/dev/mapper/root或		

​			者、/dev/mapper/swap表示的是光驱、缓存等。fdisk /dev/sda是列出磁盘的分区

​		3>	进入磁盘分区后，有命令：p是打印，n是新建分区，d是删除分区，l是列出已有分区

​			w保存并退出



​		注：df -h是查看挂载磁盘使用大小的情况

​			fdisk -l是查看磁盘分区的情况

​			每一个分区要使用，都必须要有文件系统，比如u盘能使用，它的属性可查看他的文件系统ext4等

​			mkfs.ext4 /dev/sda3 创建文件系统   其中sda3是新的分区  ext4是文件系统  mkfs:make filesystem

​			mount /dev/sda3 /mnt	挂载	其中/dev/sda3是要挂载的磁盘分区	/mnt是挂载的点

​			扩容步骤：写到磁盘分区表->创建文件系统->挂载

​			步骤完成reboot重启：分区还在，挂载就没有了，需要将挂载写入文件系统表中，让系统已启动就

​				自动去挂载这个分区

​				vi /etc/fstab	dev/sda3	/mnt	ext4	defaults	0 0	其中每个之间都是一个tab键

**添加新磁盘**

​		1>	lsblk	和fdisk -l的效果一样，只是fdisk -l更详细	它是list block的意思



#### 9、安装

​	有些包yum库里面没有，就需要源码安装

​	配置，编译，安装

​	比如window下载好nginx的.tar.gz的包，再拖入服务器中

#### 10、遇到问题

​	1、nginx 配置虚拟主机

​		按步骤都做了，就是访问不了，一开始www.haha.com还能访问，现在www.hehe.com和前面的都访问

​		不了。都把配置重新改了，不行，重启nginx不行。突然想到刚才编辑hehe/index.html，服务器卡了，	

​		没有退出编辑	模式，就重启了服务器，而前一天晚上做前面步骤，是关闭了防火墙和selinux的。

​		试着关了他俩，果然可以正常访问nginx服务器了











#### 11、基本常识

##### 连接服务器工具

> xshell、 putty、 secureCAT
>

##### 主流操作系统

> windows（收费）, linux（大部分免费）,macOS
>

##### 虚拟机

> virtualbox(oracle 免费) ，vmware, parallers
>
> win下确实vm是最好的.... 其他的虚拟机都感觉力不从心的感觉  
>
> 但是mac系统不一样哈...

##### 发行版本

> Debian（大便系列） http://www.debian.org/
> Gentoo（贱兔系列） http://www.gentoo.org/
> Ubuntu（乌班图），是大便系列的衍生版 http://www.ubuntu.com/ 
> RedHat（红帽系列） http://www.redhat.com
> CentOS  是红帽系列的发行版本（服务器使用较多） http://www.centos.org/  
> Federo  是红帽系列的测试版 http://fedoraproject.org/
> deepin 国内linux，界面很漂亮。
>

##### Linux Shell

> Linux Shell：Shell是系统的用户界面，提供用户与内核进行交互操作的一种接口。
> Shell是一个命令解释器，它解释由用户输入的命令并且把它们送到内核执行。
> Shell编程语言具有普通编程语言的很多特点，用这种编程语言编写Shell程序与其他应用程序具有同样的效果。
> 目前常见的Shell有Bourne Shell（sh）、Korn Shell（ksh）、C Shell（csh）、Bourne-again Shell（bash）。

##### ssh远程访问

> 远程访问协议
>  xshell, putty ，secureCRT都是集成了ssh协议的工具。
>  ssh 用户名@ip（或hostname）:22

##### linux        系统目录结构

> /bin	        存放系统指令（可执行文件）
> /boot      存放linux系统开机引导程序
> /dev	存放设备文件的地方
> /etc	        存放系统配置文件的地方
> /home	存放用户家目录的地方。
> /lib和/lib64		存放系统动态链接库的地方。
> /lost+found		linux文件系统下特有的目录
> /media			存放媒体相关的东西。
> /mnt		默认的挂载点。
> /opt		        安装第三方软件的地方
> /proc		存放进程相关的东西
> /root		root用户的home目录
> /sbin		超级用户执行的指令
>
> /selinux	linux安全策略相关的东西。
>
> /srv		主要用来存储本机或本服务器提供的服务或数据。（用户主动生产的数据、对外提供服务）
> /sys		存放系统设备的地方
> /tmp	保存在使用完毕后可随时销毁的缓存文件。（有可能是由系统或程序产生、也有可能是用户主				动放入的临时数据、系统会自动清理）
> /usr		unix system resource，存放unix系统相关的文件
>
> /var		系统产生的不可自动销毁的缓存文件、日志记录。（系统和程序运行后产生的数据、不对外提供服务、只能用户手动清理）（包括mail、数据库文件、日志文件）

##### 文件系统

> 文件系统就是文件管理系统的简称，它规定了数据的存储方式和读取方式，不同的文件系统存储和读取方式不同，不同的文件系统存的大小也都不一样。
>
> 常见的文件系统：
>
> windows
> 	fat （File Allocation Table）
> 	fat16
> 	fat32   目前很多u盘就是这个格式，存储的单个文件最大为4G
> 	ntfs  (New Technology File System)，是 WindowsNT 环境的文件系统。NTFS取代了老式的FAT文件系	
>
> ​		统。	
>
> ​	windows系统默认的文件系统格式，到mac电脑上只读，在mac上装一个插件，插件收费的。
> 	exfat  （全称Extended File Allocation Table File System，扩展FAT，即扩展文件分配表）
> 	fat64，mac下和windows下都能读写
> linux
> 	ext2
> 	ext3   相比ext2多了日志系统
> 	ext4   Ext4 是 Ext3 的改进版，主流这个。
> mac
> 	hfs： 分层文件系统Hierarchical File System
> 	hfs+： hfs的升级。
> 	apfs： Apple File System，最新一代苹果文件系统。

##### 软硬连接

> 为了解决文件共享的问题，以软连接居多（在ll显示详情的时候，在文件类型处会显示l的字样）.
> 硬链接：
>
> 指令格式：  ln  源文件  目标文件
> 相当于给文件起了一个别名，修改其中一个文件，本质上是修改的都是同一个文件，通过ll可以查看硬链接的个数
> 【注】硬链接不能给目录创建
> 【注】硬链接创建之后，用户和组信息不变
>
> 软连接：
>
> 就可以理解为windows下面的快捷方式
> 指令格式：  ln   -s    源文件   目标文件
> 修改其中一个文件，另外一个也改变
> 【注】软连接可以给目录创建
> 【注】当目标文件丢失的时候，该软连接就会变成一个死链接，当重新创建了一个和目标文件同名文件的时	候，该软连接原地满血复活
> 【注】新建的软连接，用户和组信息是创建时候的用户和组信息

##### 文件权限

r：可读	read	w：可写	wirte	x：可执行 execute		-：没有权限

权限的表示法：

​	---		000		0    没有权限
	--x		001		1    可执行
	-w-		010		2    可写
	-wx		011		3    可写可执行
	r--		100		4    只读
	r-x		101		5    可读可执行
	rw-		110		6    可读写
	rwx		111		7    可读可写可执行

ll显示权限内容为：

​	rwx    				r-x    					r-x
	该用户的权限        组内用户的权限			组外用户的权限

#### 12、linux指令

##### uname -r

> 版本号 如：2.6.32-642.el6.x86_64  2：内核主版本 6：奇数代表开发版，偶数代表稳定版，小版   
>
> 本号 32：该版本修复的次数

##### cd - 

> 返回之前路径

##### cd ~ 

> 快速切换到home目录

#####  ctrl + l /clear

> 清屏

##### ctrl + c 

> 取消当前正在执行的进程。比如取消shutdown的关机进程，取消安装软件进程等等    -c: cancel

##### ctrl + r

> 搜索历史命令   r: reverse i search

##### service netwrok restart

> 重启网卡

##### init

> init是所有进程的祖先，其进程号始终为1。init用于切换系统的运行级别，切换的工作是立即完成的。init 0命令用于立即将系统运行级别切换为0，即关机；init 6命令用于将系统运行级别切换为6，即重新启动

##### shutdown  

> 命令安全地将系统关机 
>
> shutdown now 马上关机
>
> shutdown +5 5分钟之后关机
>
> shutdown +5 '即将关机，做好准备'     加提示5分钟之后关机
>
> shutdown -r now 是立即停止然后重新启动     -r restart
>
> shutdown -h  关机后不重新启动  
>
> shutdown -c   取消shutdown关机命令    -c cancel

##### halt

> halt是最简单的关机命令，其实际上是调用shutdown -h命令。halt执行时，杀死应用进程，文件系统写操作完成后就会停止内核。 
>
> halt -p 关机时调用poweroff，此选项为缺省选项 

##### reboot

> reboot的工作过程与halt类似，其作用是重新启动，而halt是关机。其参数也与halt类似。reboot命令重启动系统时是删除所有的进程，而不是平稳地终止它们。因此，使用reboot命令可以快速地关闭系统，但如果还有其它用户在该系统上工作时，就会引起数据的丢失。所以使用reboot命令的场合主要是在单用户模式。 

##### poweroff

> Poeroff : 切断系统电源 
>
> poweroff就是halt的软链接而已。执行的还是halt命令。关于halt 命令，可以这样理解：halt就是调用shutdown -h。halt执行时﹐杀死应用进程﹐执行sync系统调用﹐文件系统写操作完成后就会停止内核。 

>  有些用户会使用直接断掉电源的方式来关闭linux，这是十分危险的。因为linux与windows不同，其后台运行着许多进程，所以强制关机可能会导致进程的数据丢失﹐使系统处于不稳定的状态﹐甚至在有的系统中会损坏硬件设备 

##### --help 参数

> 查找命令的用法

##### date

> 显示当前时间（格式化显示时间）
>
> date -s 修改时间
>
> 分两步：①date -s 2018-10-28先改日期 ②date -s 19:41:00再改时间

##### cal 

> 显示日历

##### which 

> 查找可执行文件所在位置   比如：which python/which pip

##### last 

> 显示近期用户或终端的登录情况
>
> last -5 root    显示root登陆的最近的5条

##### service iptables stop/start 

> 防火墙的关闭和开启

##### setenforce 0 

> 关闭selinux

##### ls

>   -a/A   :显示隐藏文件或目录
>   -i     :显示文件的inode号。即index node，索引节点。
>   -k	   :使用--block-size=1K来显示文件大小。
>   -l	   :使用较长格式列出信息
>   -R	   :递归显示目录下的所有文件及目录       -R:recursion  递归
>   -t     : 按照修改时间排序
>   -r     :排序时保留顺序 （逆序）                       -r:reverse 反转
>   ll   ls -l 的别名，也是简写。
>
>   
>
>   r：可读	read	w：可写	wirte	x：可执行 execute		-：没有权限
>
>   权限的表示法：
>
>   ​	---		000		0    没有权限
>   	--x		001		1    可执行
>   	-w-		010		2    可写
>   	-wx		011		3    可写可执行
>   	r--		100		4    只读
>   	r-x		101		5    可读可执行
>   	rw-		110		6    可读写
>   	rwx		111		7    可读可写可执行
>
>   ll显示权限内容为：
>
>   ​	rwx    				r-x    					r-x
>   	该用户的权限        组内用户的权限			组外用户的权限
>
>   ll显示内容：
>
>   ​	第一列 ：文件类型
>   			-  表示普通文件
>   			d  表示目录
>   			b  表示block，块文件
>   			c  表示字符文件
>   			l  表示链接
>   	第二列到第十列表示文件或目录的权限。
>   	第十一列表示selinux标志，如果开启则有"."
>   	第十二列表示硬链接的次数或者子目录的个数。
>   	第十三列表示文件的属主
>   	第十四列表示文件所属的group，属组。     
>   	第十五列表示文件的大小。单位是byte
>   	第十六到十八列表示文件的修改时间。
>   	第十九列表示文件或目录名。

##### vi

> 编辑完成按esc，进入指令模式，输入冒号，进入底行模式，输入wq！,保存并退出。
>
> 指令模式 进入 编辑模式：
>
> ​	i ： 在光标前插入
>   	I ： 让光标回到行首进行插入。
>   	a :  在光标之后追加输入。
>   	A :  让光标定位到行尾进行插入。
>   	o ： 另起下一行，进行输入。
>   	O ： 另起上一行，进行输入。
>   	s ： 删除光标所在位置的字符，并进入编辑模式。
>   	S ： 删除光标所在那一行，并进入编辑模式。
>
>  指令模式下的快捷键：
>
> ​	gg： 让光标回到文件的开头位置。
>   	G：  让光标回到最后一行的开头位置。
>   	ngg ：让光标回到指定的n行的开头位置。
>   	^ :  让光标回到该行行首。
>   	$ :  让光标定位到该行行尾。
>   	dd： 删除光标所在行
>   	ndd ：删除从当前光标开始的n行。
>   	yy：  复制当前行。
>   	p：   打印复制的内容。
>   	nyy   复制当前行开始的n行内容
>   	np：   从当前行开始打印n次复制的内容
>   	u：	  回退操作。
>   	n0000dd： 删除从光标开始的n0000行。
>   	ctrl+f ： 翻页显示
>   	ctrl+b ： 往上翻页
>   	ctrl+d ： 往下翻半页
>   	ctrl+u ： 往上翻半页。
>   	zt：     把当前行当做当前页的第一行。
>   	zb：     zt的逆操作。
>   	zz：	     把当前光标所在的行定位该页的中间。
>
> 底行模式下的指令:
>   	:wq 保存并且退出。
>   	:q  不保存直接退出。
>   	:q! 不保存，强制退出。
>   	:x  保存修改并退出。
>   	shift+zz 退出的快捷键。
>
> ​	:set nu 设置显示行号。
>   	:set nonu  取消行号显示。
>   	查找字符串  从光标所在位置往文件尾查找。/字符串 ,n代表往下翻，N代表往上翻。
>   			？字符串。
>
> ​	字符串替换  替换光标所在行的指定的字符串, 语法：s/被替换的字符串/替换后的字符串， 可以在s前加
>
> ​			上要替换的行号范围，用逗号分割。
>
> 异常：
>
> ​	如果vi编辑到一半终端异常退出了。再次进入vi编辑同一个文件时，按enter可以进入编辑。vi -r <文件名	
>
> ​	>可以恢复到上次未保存的内容。删除.<文件>.swp文件可不再出现vi的错误提示。
>
> vi配置文件：
>
> ​	.vimrc ，放在root home目录下。

##### rm

> 删除文件
>
> rm -r 删除目录
>
> rm -f 强制删除(无确认提示)
>
> 模式匹配，不是正则表达式，*代表任意多个字符

##### rmdir

> 只能删除空目录

##### mv 

> 可以移动，可改名，甚至可移动中改名。不区分目录还是文件。
>
> mv source(源) detination(目标)   移动

##### cp

> 拷贝
>
> cp -p源文件的属性一起拷过去。      -p:property
> cp -r 拷目录

##### 查看

> cat  显示所有内容。
> tac  倒着显示。
> head head -n 显示头部的n行
> tail tail -n 显示尾部的n行。-f 
> more 分页显示内容，空格表示下一页。回车表示下面一点点内容。
> less 也是分页显示内容，可前后回退显示。pageup pagedown
> wc   输出一个文件的行数，单词数，字节数。也可通过-l -w -c 来精确指定显示内容

##### useradd 

> useradd 用户名   创建新用户
>
> -g   指定主组，组名或者组id
> -u   指定用户id    一般不指定
> -d   指定家目录    一般不指定
>
> 在创建用户的时候，如果没有指定这个用户的主组，那么系统会自动的为这个用户创建一个和用户名一样的组作为该用户的主组（一般都不指定）
>
> cat /etc/passwd  查看用户和密码
>
> cat /etc/group   查看组的信息在
>
> groups  查看组
>
> 给用户添加密码:
> 	passwd 用户名
> 	在root下面，你可以修改其它用户的密码
> 	但是在普通用户下面，只能修改自己的密码，不能别的用户的密码。

##### usermod

> -g(修改主组)  
>
> -u(修改用户id) 
>
> -l(修改用户名)  
>
> -d(修改家目录)

##### userdel

> userdel  用户名     仅仅删除用户信息，不删除家目录
> userdel  -r 用户名   同时删除家目录
>
> 【注】同时删除的家目录必须符合和用户名的名字一模一样才行，而且删除的时候，会一并将和用户名相同的组一块删除掉

##### groupadd  

> -g   指定组id

##### groupmod

> -g  修改组id
> -n  修改组名   groupmod -n tangke tang   将tang组名字修改为tangke

##### groupdel

> 如果一个组是某个用户的主组，那么这个组不允许被删除，你需要首先删除这个用户
> 如果一个组是系统自动为用户创建的，那么删除用户的时候会自动将这个同名的组给删除掉

##### su

> 切换用户
>
> root用户切换到普通用户   su bajie   不用输入密码
> 普通用户切换到root用户   su       需要输入密码
> 切换完之后，使用exit退出那个用户即可
> whoami   查看当前用户名 id 查看当前用户的用户id和组id

##### sudo  

> 临时使用root用户执行这条命令，需要输入密码。

##### chmod

修改权限

格式：  chmod   权限   文件路径

chmod 755 1.txt     注意：7是111，5是101。755三个数分别代表：该用户的权限、组内用户的权限、			

​	组外用户的权限

​	7:user	5:group		5:other

​	chmod u+x 1.txt
	chmod g-x 2.txt
	chmod o+w 1.txt
	chmod u-x,g-w,o-w 1.tx

​	chmod -R 777 mimi/
	修改目录权限的时候，添加-R选项，递归的修改子文件的权限和该目录权限一致

##### chown

> 修改用户和组
>
> chown  用户名  文件路径
> chown bajie 1.txt             修改用户
> chown bajie:bajie 1.txt       修改用户和组
> chown :bajie 1.txt            修改组

##### chgrp   

> chgrp    组名   文件路径
> chgrp bajie 1.txt             仅仅修改组

##### umask

> 决定文件或者目录的默认权限是什么
>
> umask -S  查看默认权限
>
> 如果想修改默认权限  umask 
>
> 文件的默认权限是   644  （文件默认都没有执行权限）
> 目录的默认权限是   755
> 777-022 = 755

##### find    

> 文件搜索
>
> 格式：  find  \[目录] \[选项][选项值]
>
> 目录：去哪找，可以不写，默认代表当前目录
>
> 选项：怎么找
>
> ​	-name   按照名字找(常用)    可以使用通配符
> 	-size   按照大小找  单位为  kmg   10k（等于10k）   +10k（大于10k）   -10k（小于10k）
> 	-user   按照用户名
> 	-group  按照组名
> 	-maxdepth  -mindepth   限制查找的目录层级，默认递归查找所有
> 	-ctime  按照创建时间查找   单位是天
> 	-type 文件类型 f表示普通文件。d表示目录，l表示链接。
>
> 选项值：找什么
> 	find / -name 1.txt 
> 	find / -name \*.txt
> 	find / -size +10k
> 	find / -user bajie
> 	find / -group bajie
> 	find / -mindepth 4 -name \*.txt
> 	find / -mindepth 3 -maxdepth 5 -name \*.txt
> 	find / -ctime -1

##### grep

> 文件内容查找
>
> 格式：grep   查找的内容   文件路径
> grep movie 1.txt
> grep that ~/*
> grep that ~/*.txt
>
> -v 翻转
> -n 显示匹配的行数
> --color=auto   将颜色高亮显示
> 		给 grep 指令起一个别名   vi ~/.bashrc
> 		添加一行                 alias grep='grep --color=auto'
> 		让配置文件立即生效       source ~/.bashrc
> -c         得到内容的个数
> -i         不区分大小写的查找
> -r         递归查找，但是不能限制后缀，只能遍历所有   grep -r that ~/*
> -l	    只显示文件名，不显示内容

##### ssh-keygen

> 生成公钥和私钥
>
> keygen: key genernate

##### ls > lala.txt / ll >> lala.txt

> 注意：这部分需要重新听
>
> 重定向
> 标准输入（stdin，键盘就是其标准输入）、标准输出（stdout，屏幕就是标准输出）
> 标准错误（stderr,屏幕也是默认标准错误输出）
> 输出重定向
> 	ls > lala.txt   先清空，再写入
> 	ll >> lala.txt  追加
> 错误重定向
> 	将指令错误提示信息写到文件中
> 	ls 100 2> error.txt   
> 	ls 300 2>> error.txt
> 输入重定向（不常用）
> 	linux默认从键盘获取输入
> 	cat > 1.txt
> 		从键盘获取输入，完毕之后，敲 ctrl+d  结束输入
> 	重定向
> 		cat > 1.txt < 2.txt
> 	标准输出和错误信息都重定向到一个文件中
> 		command >out.file 2>&1 

##### fdisk -l

> 注意：挂载
>
> 查找设备
>
> /dev/sda    这是你的第一块硬盘
> 		/dev/sda1   第一个分区
> 		/dev/sda2   第二个分区
> /dev/sdb    这是你的第二块硬盘
> 		/dev/sdb1   第一个分区

##### mount

> 注意：挂载/分区/扩展磁盘/加磁盘/设置开机挂载的过程，需要重新听
>
> 挂载
>
> 格式   mount [参数] 设备 挂载点
> 	-t   指定文件系统格式
> 		msdos===>fat16
> 		vfat====>fat32
> 		nfs=====>网络文件系统格式
> 		auto====>自动识别
> 		ntfs====>ntfs
> 	-o
> 		iocharset=utf8
> 	mount -o iocharset=utf8 /dev/sdb1 /mnt/usb
> 	mount -t vfat -o iocharset=utf8 /dev/sdb1 /mnt/usb/

##### umount

> 解除挂载
>
> umount /dev/sdb1 /mnt/usb
> umount /dev/sdb1
> umount /mnt/usb

##### lsblk

> 列出系统上的所有磁盘列表

##### mkfs.ext4

> 格式化分区
>
> mkfs.ext4 /dev/sdb1   将分区1格式化为ext4格式的

##### gzip

> gzip、gunzip
> gzip 文件名
> （1）不保存源文件
> （2）不能打包压缩

##### bzip2

> bzip2、bunzip2
> bzip2 文件名
> （1）不能打包压缩
> -k：保留源文件并且压缩

##### tar

> tar（解压和压缩一块承包）
> 	比gzip和bzip2功能强大的就是打包压缩
> 	（1）如果使用tar指令对文件进行打包并且使用gzip压缩，那么文件后缀名为.tar.gz
> 	（2）如果使用tar指令对文件进行打包并且使用bzip2压缩，后缀名为.tar.bz2
> 	参数：
> 	-c : 打包文件或者文件夹
> 	-z ：使用gzip格式进行压缩
> 	-j : 使用bzip2格式进行压缩
> 	-f : 放到最后面，来指定压缩后的文件名
> 	-v : 压缩或者解压缩的时候显示过程
> 	-x : 解压缩
>
> 1、打包并且使用gzip压缩和解压
> 	压缩： tar -zcvf haha.tar.gz 1.txt 2.txt 3.txt
> 	解压缩： tar -zxvf haha.tar.gz .tgz
> 2、打包并且使用bzip2压缩和解压
> 	压缩： tar -jcvf haha.tar.bz2 1.txt 2.txt 3.txt
> 	解压缩：tar -jxvf haha.tar.bz2

##### init 

> 切换等级
>
> init 等级号
> init 0      关机
> init 6      重启
>
> linux的用户等级   vi /etc/inittab
> 	0 : 关机模式
> 	1 : 单用户模式
> 	2 : 无网络的多用户模式
> 	3 : 有网络的多用户模式
> 	4 : 保留模式
> 	5 : 带图形界面的多用户模式
> 	6 : 重启模式

##### runlevel / who -r

>  查看当前等级

##### chkconfig --list

>  查看随开机启动的服务

##### service

> 控制服务的开启与关闭
>
> 你现在自己安装了一个软件，是nginx，你想通过service这个指令控制服务的开启与关闭，你需要将nginx的启动	
>
> ​	脚本放到  /etc/init.d/ 这个文件夹中，并且修改权限
>
> 所以：/etc/init.d/iptables start是等价于service iptables stop | start | restart

##### top

> 可以实时的查看系统的运行状态，尤其是内存的使用情况
> 输入大写的M  将进程按照内存利用率排序
> 按q退出查看
> w，查看当登录该系统的所有用户
> free，查看当前系统内存使用情况   -h 以人性化的方式显示

##### ps

> 查看进程相关信息
> 	ps -ef | grep ssh
> 	ps aux | grep ssh
> kill，杀死一个进程，根据进程id号杀死进程
> 	kill -9 进程id号
> 	service sshd start
>  在linux里面，随开机启动的服务，我们称之为守护进程（daemon）

##### netstat

> 用于显示linux中各种网络相关信息。如网络链接 路由表  接口状态链接 多播成员等等
>
> 参数介绍：
>
> -a (all)显示所有选项，默认不显示LISTEN相关
> -t (tcp)仅显示tcp相关选项
> -u (udp)仅显示udp相关选项
> -n 拒绝显示别名，能显示数字的全部转化成数字。
> -l 仅列出有在 Listen (监听) 的服務状态
>
> -p 显示建立相关链接的程序名
> -r 显示路由信息，路由表
> -e 显示扩展信息，例如uid等
> -s 按各个协议进行统计
> -c 每隔一个固定时间，执行该netstat命令。
>
> 提示：LISTEN和LISTENING的状态只有用-a或者-l才能看到
>
> 常用实例：
>
> 列出所有端口：netstat -a
>
> 列出所有tcp端口：netstat -ta
>
> 列出所有udp端口：netstat -au
>
> 列出所有监听端口：netstat -l
>
> 只显示tcp的监听端口：netstat -lt
>
> 显示所有端口的统计信息:netstat -s
>
> 显示tcp进程的id信息：netstat -pt
>
> 显示路由信息：netstat -r
>
> 显示网络接口信息:netstat -i
>
> 每隔3秒输出一次tcp监听端口信息： netstat -ntplc 3

##### 软件下载及安装

> **安装包下载：**
>
> ①curl（自带的）
>   	curl -O https://mirrors.tuna.tsinghua.edu.cn/apache/httpd/httpd-2.2.34.tar.bz2
> ②wget（是一个软件，需要安装）
>   	wget 地址
>   	-c：断点续传，通俗的理解，就是下载一半，网络断了，要不要接着上次的继续下载
>
> **软件安装：**
>
> ① yum安装
>   	说明：
>   	yum是什么，yum就是你电脑上的电脑管家里面的软件管理，就是小米手机里面的应用商店，就是苹果手机	
>
> ​		appstore，就是一个软件中心
>   	在linux里面，很多软件之间都存在着依赖关系，如果安装软件的依赖关系来安装是一项非常复杂的工作，
>
> ​		yum源的出现就很好的解决了这个问题
>   	常见的yum源：
>   		网易源，清华源，阿里源，搜狐源，中科大源
>   	配置yum源	
>   		cd /etc/yum.repos.d/
>   		mv CentOS-Base.repo CentOS-Base.repo.back
>   		curl -O http://mirrors.aliyun.com/repo/Centos-6.repo
>   		mv Centos-6.repo CentOS-Base.repo
>   		
>   		配置好之后
>   		yum clean all    清空所有
>   		yum makecache    生成缓存
>   	常见yum指令
>   		yum install -y wget   安装
>   		yum remove -y wget    卸载
>   		yum list              显示所有
>   		yum search vim        搜索
>   	常用选项
>   		-y   过程全部yes
>   		--downloadonly   只下载不安装
>   		--downloaddir    指定下载的目录
>   		yum install -y --downloadonly --downloaddir=./ wget
> ②rpm安装
>   	redhat系列的包后缀名为 .rpm，yum安装的也是rpm包，只不过yum为你解决了依赖问题，如果你想自己通
>
> ​		过rpm指令安装，你需要手动解决依赖关系
>   	安装
>   		rpm -ivh 包名
>   		rpm -ivh * 
>   	卸载
>   		rpm -e 包名
>   		rpm -e wget-1.12-10.el6.x86_64    【不带后缀】
>   		rpm -e wget
>   	其它选项
>   		-ql : 查询包安装路径
>   			rpm -ql wget
>   		-qa : 列出系统所有的软件
>   			rpm -qa | grep wget
>   		-qi : 显示包的详细信息
>   		-qf ：查询某个文件是属于哪个rpm包的。
>   			rpm -qf /usr/share/vim/vim74/vimrc_example.vim
>
> ③源码安装
>
>   	在linux里面，几乎所有的软件都是c或者c++来编写的，这种语言写的程序，首先得自己编译一下，生成一个
>
> ​		可执行文件，然后再执行这个文件
>   	要写编译代码，你得有编译器，在linux里面编译器就是gcc，gcc-c++
>   	yum install -y gcc gcc-c++
>   	
>   	源代码从网上下载，下载下来之后一般都是  .tar.gz  .tar.bz2 .tgz
>   	源码安装三部曲
>   	首先解压下载的源码包。
>   	1、配置
>   		./configure [--prefix=安装路径]
>   	2、编译
>   		使用里面自带的Makefile，   make
>   	3、安装
>   		make install
>   	安装过程中，查看上一步是否成功，输入 echo $?  输出0表示成功，其它失败
>   	make && make install

##### screen

> 在linux中，管理员通常会通过ssh协议远程登录服务器，然后去安装一些软件，执行一些程序等工作，但是有时候安装软件过程非常的长，或者程序就是死循环，这时候管理员什么也做不了，只能干等着，所以出现了screen这个软件，解决了这种问题。
>
> 安装
>
> ​	yum install -y screen
>
> 使用
>
> ​	新建会话   screen -S baobao
> 	去往会话   screen -r baobao
> 	查看会话   screen -ls
>
> 在baobao会话中的快捷键(ctrl + a)
>
> ​	退出会话   ctrl + a + d
> 	新建窗口   ctrl + a + c
> 	显示所有窗口   ctrl + a + w
> 	上一个窗口  ctrl + a + p
> 	下一个窗口  ctrl + a + n
> 	杀死窗口    ctrl + a + k   (找准那个点)
>
> 窗口全部关闭之后，这个会话就会结束



#### 13、Linux一些配置

##### 网络配置：

> 使虚拟机可以连接上网络
>
> /etc/sysconfig/network-scripts/ifcfg-eth0
> 把ONBOOT=no改成yes

##### 搭建主机信任

> 配置ssh免密码登录，操作步骤：
> 	1.1 在主机1上面生成公钥和私钥
>   		ssh-keygen   敲回车生成即可
>   		在 ~/.ssh 中生成两个文件   id_rsa(私钥)   id_rsa.pub(公钥)
>   	1.2 将公钥粘贴到主机2中
>   		复制主机1的公钥
>   		在主机2中
>   			vi ~/.ssh/authorized_keys
>   			将公钥粘贴进来
>   	1.3 在主机1再次通过ssh登录实现免密码
>
> 备注：
>
> ​	密码学：加密，解密
>   	加密和解密的时候，用到一个东西，密钥
>   	加密和解密的时候，密钥是否相同，如果相同，称之为对称加解密，如果不相同，非对称加解密
>   	公钥：公开的，你们都能拿到
>   	私钥：私有的，只有我知道
>   	这一对，成对出现

##### 挂载

> 查找设备   fdisk -l
> 	/dev/sda    这是你的第一块硬盘
> 		/dev/sda1   第一个分区
> 		/dev/sda2   第二个分区
> 	/dev/sdb    这是你的第二块硬盘
> 		/dev/sdb1   第一个分区
>
> mount
> 	格式   mount [参数] 设备 挂载点
> 	-t   指定文件系统格式
> 		msdos===>fat16
> 		vfat====>fat32
> 		nfs=====>网络文件系统格式
> 		auto====>自动识别
> 		ntfs====>ntfs
> 	-o
> 		iocharset=utf8
> 	mount -o iocharset=utf8 /dev/sdb1 /mnt/usb
> 	mount -t vfat -o iocharset=utf8 /dev/sdb1 /mnt/usb/
>
> umount
>
>   	umount /dev/sdb1 /mnt/usb
>   	umount /dev/sdb1
>   	umount /mnt/usb
>
> 设置开机挂载
>
> ​	vi /etc/fstab
>   	添加一行
>   	/dev/sdb1      /mnt/usb      ext4        defaults        0 0
>   	设备名         挂载点        系统格式     默认           默认
>   	
>   	让配置文件立即生效
>   	mount -a
>
>  删除分区
>   	fdisk /dev/sdb
>   	d  分区号
>   	挨个删除即可

##### SCP拷贝

> scp
> xmanager
>   基于ssh协议copy
>   格式：   scp    源路径   目的路径
>   10.0.142.84   root   123456
>   scp dapian.avi root@10.0.142.84:/root/kong
>   scp -r root@10.0.142.84:/root/exmple ./     拷贝目录需要加上-r选项
>   如果配置了免密码的登录，scp的时候就不用输入密码了
>   winscp
> 	安装一下
> 	通过这个软件可以将windows里面的东西直接发送给linux

##### 将linux目录共享给windows

> samba服务
>
> 搭建之前：关闭防火墙和selinux
>
> ​	service iptables stop
> 	setenforce 0
>
> 安装samba软件
>
> ​	yum install -y samba samba-client
>
> (1)不带密码的方式访问
> 	vi /etc/samba/smb.conf
> 	来到第101行
> 		#security = user
> 		#passdb backend = tdbsam
> 		security = share
> 	来到第248行
> 		[xiaoji]        
> 			browseable = yes
> 			writable = yes
> 			public = yes
> 			path = /smb
> 	cd /
> 	mkdir smb
> 	vi smb/goudan.txt
> 	chmod -R o+w smb
> 	
>
> 	开启服务
> 	service smb start
> 	
> 	来到windows下面，在cmd中输入  \\10.0.142.34 （用自己的ip替换）
> 	就会看到 xiaoji
> (2)带密码的方式访问
> 	vi /etc/samba/smb.conf
> 	来到101行
> 		        security = user
> 				passdb backend = tdbsam
> 				#security = share 
> 	添加用户
> 		useradd test
> 	给用户添加密码
> 		pdbedit -a test
> 	重启samba服务：service smb restart
> 	来到windows下面，在cmd中输入  \\10.36.133.80
> 	输入用户名和密码即可
> 	就会看到 xiaoji

##### 将windows目录共享给linux

> (一般用上一个，因为把自己的共享出去，其他人也能看到)
>
> windows下面新建一个目录
> 	右键===》属性===》共享===》共享===》添加everone读写===》完成
> 	右键===》属性===》高级共享===》共享此文件夹
> 	共享===》密码保护===》关闭  密码保护的共享
> 来到你的linux服务器中
> 	yum install -y cifs-utils
> 将windows下面共享的目录挂载到linux里面
> 	mount -t cifs //10.0.142.88/baby /mnt/usb

##### 将linux目录共享给linux(nfs搭建)

> **准备**
>
> nfs：网络文件系统
> 搭建nfs至少需要两台linux，linux1作为nfs客户端，linux2作为nfs服务器
> 主机1（10.0.142.34，nfs服务器）    主机2（10.0.142.23   nfs客户端）
> **nfs服务器**
>
> 1、yum install -y nfs-utils
> 2、编辑配置文件
> 	vi /etc/exports
> 	/test   			10.36.133.0/24(rw,sync)
> 	要共享的目录        网段
> 3、启动服务
> 	nfs服务是基于rpc协议的
> 	service rpcbind start
> 	service nfs start
>
> **nfs客户端**
>
> 1、yum install -y nfs-utils
> 2、查看对应的ip地址上面共享的目录
> 	showmount -e 10.36.131.133(nfs服务器ip地址)
> 3、将共享的目录挂载到本地
> 	mount -t nfs 10.0.142.34:/test/ /root/bajie
> 4、设置开机挂载
> 	vi /etc/fstab
> 	10.0.142.34:/test/   /root/nfs   nfs   defaults  0   0
> 	设备                 挂载点      格式   默认
>
> **nfs搭建完毕**

##### nginx服务搭建

> apache和nginx都是服务器
> 安装nginx
> 1、关闭防火墙和selinux
> 2、安装一些依赖的软件
>
> ​	yum install -y gcc gcc-c++ autoconf automake zlib zlib-devel openssl openssl-devel pcre pcre-devel
>
> 3、创建www用户，但是不允许www用户登录系统
>
> ​	useradd www -s /sbin/nologin
>
> 4、安装
>
> ​	tar -zxvf nginx-1.11.5.tar.gz
> 	cd nginx-1.11.5
> 	./configure --prefix=/usr/local/nginx --without-http_memcached_module --user=www --group=www   --	
>
> ​		with-http_stub_status_module --with-http_ssl_module
> 	make && make install
>
> 5、设置nginx开机启动
>
> ​	cp nginx /etc/init.d
> 	chmod 755 /etc/init.d/nginx
> 	chkconfig nginx on
> 	chkconfig --list    查看是否开机启动
> 	service nginx start | stop | restart
>
> 6、配置虚拟主机
>
> ​	ip地址找到服务器的
> 	域名====》ip对应着呢
> 	www.baidu.com====>DNS====>得到真实的ip地址
> 	然后再根据ip地址再来访问服务器
>
> ​	解决多个网站同时放到同一台服务器上
> 	www.hehe.com===>10.0.142.34
> 	www.lala.com===>10.0.142.34
> 	www.haha.com===>10.0.142.34
>
> ​	vi /usr/local/nginx/conf/nginx.conf
> 	37gg   给一个server_name
> 	service nginx restart
>
> ​	windows下面hosts文件
> 		C:\Windows\System32\drivers\etc\hosts
> 		10.0.142.34  www.lala.com
>
> ​	配置虚拟主机步骤
> 	1、vi /usr/local/nginx/conf/nginx.conf
> 	2、最后一个大括号的上面
> 		include vhost/*.conf;
> 	3、mkdir /usr/local/nginx/conf/vhost
> 	4、vi /usr/local/nginx/conf/vhost/www.hehe.com.conf
> 		server
> 		{
> 			server_name www.hehe.com;    
> 			root html/hehe;
> 			index index.html;
> 		}
>
> ​		server_name   域名
> 		root          站点目录，网站的目录
> 		index         网站默认的首页
>
> ​	5、mkdir /usr/local/nginx/html/hehe
>
> ​	6、vi /usr/local/nginx/html/hehe/index.html
> 		这是我的hehe网站
> 	7、service nginx restart

#### 14、注意

> 1、~ 家目录，所有用户都有一个家目录。
>
> 2、扩展阅读：http://www.ruanyifeng.com/blog/2012/02/a_history_of_unix_directory_structure.html  目	
>
> ​	录结构
>
> 3、扩展阅读：http://www.ruanyifeng.com/blog/2011/12/inode.html   索引节点
>
> 4、扩展阅读：http://www.cnblogs.com/chengmo/archive/2010/10/10/1847287.html    grep的三种正则
>
> ​	正则是面试会用到的
>
> 4、linux命令查询网站：http://man.linuxde.net/
>
> 5、新建文件的方式：
>
> ​	①vi <文件名> 如果文件存在则打开文件，如果不存在，则新建。
>
> ​	②touch <文件名>
>