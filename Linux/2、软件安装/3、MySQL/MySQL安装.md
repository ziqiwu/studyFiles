### 不记文档，白忙一场

------

#### 0、备注

> ```python
> 1> mysql老版本安装：
> 	来源：https://www.cnblogs.com/fnlingnzb-learner/p/5830622.html
> 
>     /usr/local/mysql-5.7.26/mysql-5.7.26-linux-glibc2.12-x86_64/bin
>     [root@guozi1 bin]# ./mysql_install_db --user=mysql
>     2019-05-29 11:23:19 [WARNING] mysql_install_db is deprecated. Please consider switching 		to mysqld --initialize
>     2019-05-29 11:23:19 [ERROR]   The data directory needs to be specified.
> 2> 错误：mysql.socket丢失
> 	来源：https://www.cnblogs.com/super-lucky/p/superlucky.html
> 3> mysql5.7版本安装	
> 	来源：https://www.cnblogs.com/zero-gg/p/8875598.html
> 4> chown -R 用户名:组名 ./ 及 chown用法介绍
> 	来源：https://www.cnblogs.com/puppey/p/9712192.html
> 5> 初始随机密码
> 	A temporary password is generated for root@localhost: sebyshO_s2iY
> 6> 出错解决：
> 	https://blog.csdn.net/laokaizzz/article/details/78904422
> 7> 启动报错
> 	service mysqld start
> 	The server quit without updating PID file (/usr/local/mysql[FAILED]ozi1.pid).
> 	解决：
> 		chown -R mysql:mysql  /var/lib/mysql
> 		chmod -R 775 /var/lib/mysql
> 	来源：
> 		https://www.cnblogs.com/super-lucky/p/superlucky.html
> 8> 进入mysql，执行show databases;报错
> 	You must reset your password using ALTER USER statement before executing this 			statement.
> 	解决：
> 		alter user user() identified by "123456";
> 		此时，就可以执行数据库命令了，exit命令退出后，用123456为命令即可以登录。
> 		注* 不知道user()是什么的，试着执行
> 			select user();和select version();就可以明白了。
> 	来源：
> 		https://blog.csdn.net/hj7jay/article/details/65626766
>             
>             
> 8、百度云从阿里云服务器远程复制文件
> 	来源：https://www.cnblogs.com/zongfa/p/8391837.html
> 	1> 将本地文件拷贝到远程
> 		scp /root/install.* root@192.168.1.12:/usr/local/src
> 	2> 从远程将文件拷回本地
> 		scp root@192.168.1.12:/usr/local/src/*.log /root/
> 	注* scp 源文件名 目标文件名
> 9、报错解决：
> 	错误：
> 		执行scp命令：scp root@39.105.32.104:/etc/my.cnf /etc/my.cnf
> 		报错：ssh_exchange_identification: read: Connection reset by peer
> 	原因：
> 		39.105.32.104是阿里云服务器
> 		它的/etc/hosts.allow文件中，只允许一个ip访问
> 	解决：
> 		将百度云服务器ip也加在阿里云的/etc/hosts.allow文件中
> 		注* 多个ip之间是用逗号隔开的，如下
> 			sshd:111.201.151.210,106.13.48.248:allow
> 		注* 并不需要如网上所说，改完/etc/hosts.allow文件还要service sshd restart才生效。
> 			直接在重新执行scp命令发现已经可以执行成功了。
> 10> 百度云随机密码
> 	A temporary password is generated for root@localhost: yMTBimrla2;O
> 11> 百度云启动mysql服务报错
> 	报错：
> 		Starting MySQL...The server quit without updating PID file 								[FAILED]cal/mysql/data/instance-ocarq1p8.pid).
> 	尝试：
> 		按阿里云的方法
> 		chown -R mysql:mysql  /var/lib/mysql
> 		chmod -R 775 /var/lib/mysql
> 		没有效果
> 	解决：
> 		ps -ef | grep mysql
> 		发现有一个mysqld的进程在运行，果断杀掉
> 		再次启动mysql服务，成功
> ```

#### 1、报错解决

> ```python
> 1> grant执行赋值权限，需要重启服务
> 	linux:systemctl restart mysql
> 	window:net start mysql
> 2> 给root用户修改密码后，需要重启服务
> 3> 问题：解决Navicat 出错:1130-host . is not allowed to connect to this MySql server,MySQL
> 	解决：navicat所在机器没有权限
> 	来源：https://www.cnblogs.com/q149072205/p/7411097.html
> 	注* 赋值权限后，navicat登录出现密码错误，所以还需要修改一次密码
>     
> 	解决：
> 		1 /etc/my.cnf设置skip-grant-tables;
> 		2 navicat远程连接，查看mysql数据库中的user表，可以看到host是xxx.xxx.xxx.xxx的ip
> 			用户名是myuser。
> 		3 去掉skip-grant-tables，用myuser在navicat上登录成功。
> 		
>     
> 4> 修改密码
> 	mysql5.7之后，mysql.user表中字段都变了
> 	mysql -uroot -p登录
> 	show databases; --> use mysql  #进入mysql数据库
> 	show tables; --> show create table user\G; #用户名：user，密码authentication_string
> 	修改密码update user set authentication_string=password('888888') where user='root';
> 	注* 修改密码后，需要重启服务
> 5> 完全登录不上，不知道密码
> 	修改/etc/my.cnf，最后一行增加skip-grant-tables  #跳过密码核验
> 	mysql -uroot -p 回车不需要输入密码 --> 登录成功，再进行密码sql修改运行
> 	注* window的话是my.ini
> ```
>
> 