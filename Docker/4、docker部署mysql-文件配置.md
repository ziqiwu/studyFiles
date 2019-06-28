### 不记文档，白忙一场

------

#### 0、注意点

> ```python
> docker安装最新mysql 8.x版本，我现在的mysql navicat连接不了，显示协议不一致，需要更新mysql client。卸载重新装了我本地的版本5.7.20之后，连接正常。
> ```

#### 1、安装步骤

> ```python
> docker安装mysql	
> 	来源：最新
>     	http://www.fwhyy.com/2018/05/docker-installs-mysql-to-mount-external-data-and-			configuration/
> 	来源：https://www.runoob.com/docker/docker-install-mysql.html
> 	1 docker pull mysql  #默认是最新版本，8.xx -- 2019/5/16
> 	2 查看了本地我安装的mysql版本是5.7.20，所以需要docker pull mysql:5.7.20
> 	3 cd /opt
> 	4 mkdir -p docker_v/mysql/conf
> 	5 cd docker_v/mysql/conf
> 	6 touch my.cnf
> 	7 创建并启动容器（包括配置文件挂载，设置密码）
>     	docker run -p 3306:3306 --name mysql-xiaoguozi -v 										/opt/docker_v/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 -d imageID
> 		注* -v是挂载的意思，配置文件本地都写在了/opt/docker_v/mysql/conf下的my.cnf
> 	8 进入容器
> 		docker exec -it mysql-xiaoguozi bash
> 	9 登录mysql
> 		mysql -u root -p
> ```

#### 2、中文乱码

> ```python
> 解决docker中运行的MySQL中文乱码
> 	来源：https://www.cnblogs.com/nihaorz/p/10256116.html
> 	注* 网上是vim /etc/mysql/mysql.conf.d/mysql.cnf，但是我的是本地/opt/docker_v/mysql/conf挂		载到了docker上的/etc/mysql/conf.d。所以我是把本地的该目录下的my.cnf加了配置信息。然后重		  启容器。
> ```

#### 3、安装一主三送

> ```python
> https://www.cnblogs.com/baolong/p/5763412.html
> ```