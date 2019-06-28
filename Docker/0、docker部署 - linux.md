### 不记文档，白忙一场

------

#### 0、简介

> ```python
> 微服务必备技能Docker容器基础篇幅
> 1、什么是Dokcer
> 	百科:一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布	到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口；
> 2、通俗理解
> 	docker就是和vmware等一样的虚拟化技术，可以将服务器隔离开来，虚拟成很多小的机器。
> 3、使用go语言编写，在LCX（linux容器）基础上进行的封装
> 4、简单来说：
>     1）就是可以快速部署启动应用
>     2）实现虚拟化，完整资源隔离
>     3）一次编写，四处运行（有一定的限制，比如Docker是基于Linux 64bit的，无法在32bit的				linux/Windows/unix环境下使用）
> 5、为什么要用
>     1> 提供一次性的环境，假如需要安装Mysql，则需要安装很多依赖库、版本等，如果使用Docker则通过镜像		就可以直接启动运行   
>     2> 快速动态扩容，使用docker部署了一个应用，可以制作成镜像，然后通过Dokcer快速启动
>     3> 组建微服务架构，可以在一个机器上模拟出多个微服务，启动多个应用
>     4> 更好的资源隔离和共享
>     注* 一句话：开箱即用，快速部署，可移植性强，环境隔离
> ```

#### 1、安装Docker实战

> #### 简介
>
> ```python
> 讲解阿里云ECS服务安装Docker实战
> Linux Standard Base的缩写，lsb_release命令用来显示LSB和特定版本的相关信息
> 命令： lsb_release -a 
> 
> 阿里云安装手册：
> https://help.aliyun.com/document_detail/51853.html?spm=a2c4g.11186623.6.820.RaToNY
>     
> 常见问题：
> https://blog.csdn.net/daluguishou/article/details/52080250
> ```
>
> #### 安装步骤摘录
>
> ```python
> 1> 添加yum源
>     # yum install epel-release –y
>     # yum clean all
>     # yum list
> 2> 安装并运行Docker
>     # yum install docker-io –y
>     # systemctl start docker
> 3> 检查安装结果
> 	# docker info
> ```

#### 2、仓库、镜像、容器概念

> ```python
> 简介：快速掌握Dokcer基础知识，
> 概念：
> 	1> Docker 镜像 - Docker images：
>         容器运行时的只读模板，操作系统+软件运行环境+用户程序
>         class User{
>             private String userName;
>             private int age;
>         }
> 
> 	2> Docker 容器 - Docker containers：
> 		容器包含了某个应用运行所需要的全部环境
> 		User user = new User()
> 
> 	3> Docker 仓库 - Docker registeries： 
> 		用来保存镜像，有公有和私有仓库，好比Maven的中央仓库和本地私服
> 		镜像仓库：（参考）配置国内镜像仓库：														https://blog.csdn.net/zzy1078689276/article/details/77371782
> 
> 	注* 对比面向对象的方式
> 		Dokcer 里面的镜像 : Java里面的类 Class
> 		Docker 里面的容器 : Java里面的对象 Object
> 		通过类创建对象，通过镜像创建容器
> ```

#### 3、Docker命令

> #### 常用命令摘录
>
> ```python
> 常用命令（安装部署好Dokcer后，执行的命令是docker开头）,xxx是镜像名称
> 注* 镜像名称，镜像版本，容器名称等都可以用Tab键补全
> 0> 列出当前系统存在的所有镜像：
> 	docker images
> 1> 列出当前系统存在的所有容器：
> 	docker ps -a
> 2> 搜索镜像：
> 	docker search xxx
> 	注* 是从docker hub上搜索对应的镜像
> 3> 拉取镜像：
> 	docker pull xxx
> 	xxx是具体某个镜像名称(格式 REPOSITORY:TAG)
> 	REPOSITORY：表示镜像的仓库源,TAG：镜像的标签
> 4> 创建（运行）一个容器：
> 	docker run -d --name "xdclass_mq" -p 5672:5672 -p 15672:15672 rabbitmq:management
> 	或者
> 	docker run -d --name "xdclass_mq" -p 5672:5672 -p 15672:15672 5c0e9749ca78
> 	
> 	docker run - 运行一个容器
> 	-d 后台运行
> 	-p 端口映射
> 	rabbitmq:management  (格式 REPOSITORY:TAG)，如果不指定tag，默认使用最新的。或者ID号
> 	--name "xxx"
> 	注* 
> 		1、上面示例的docker run命令中有两个-p参数是因为，消息队列有两个端口号，一般都是一个-p
> 		2、-d是deamnize，使变成守护线程的意思
> 		3、docker run是第一次使用，会创建容器，然后启动。第二次之后，直接用docker start运行即可
> 5> 检查容器内部信息：
> 	docker inspect 容器名称
> 6> 删除镜像：
> 	docker rmi IMAGE_NAME
> 	强制移除镜像不管是否有容器使用该镜像 增加 -f 参数
> 	注* 
> 		0、-rm是remove是删除，-rmi是remove image是删除镜像
> 		1、删除镜像的时候，先docker images，可以查到镜像的IMAGE ID，
> 		2、然后进行删除，如果不能删除，则加-f强制删除，比如：
> 		3、docker rmi -f 5c0e9749ca78
> 7> 停止某个容器：
> 	docker stop 容器名称
> 8> 启动某个容器：
> 	docker start 容器名称
> 9> 移除某个容器：
> 	docker rm 容器名称 （容器必须是停止状态）
> 10> 查看容器日志
> 	docker logs mysql4SXD
> 	注* 后面的mysql4SXD可以是标签名，或者是ID
> 附录：docker各参数
> 	1 --detach   当我们启动容器的时候一定要加上--detach或者-d来保持容器在后台持续运行
> 		注* attach是附着，detach是使分离
> 	2 --publish  指定容器暴露的端口，也可写为-v
> 	3 --volume  给容器挂载'存储卷'，挂载到容器的某个目录，也可写为-v
> 来源：（全部参数nb）https://www.cnblogs.com/JesseSong/articles/7921170.html
> ```
>
> #### 文档
>
> ```python
> https://blog.csdn.net/permike/article/details/51879578
> ```

#### 4、实战：Docker部署Nginx

> #### 实战步骤
>
> ```python
> 1、搜索镜像
> 	docker search nginx
> 	或者
> 	在docker官网查看所有nginx版本：hub.docker.com，在首页搜索nginx
> 2、列举
> 	docker images
> 	列举本地所有镜像，查看是否已经有了nginx镜像
> 3、拉取
> 	docker pull nignx
> 	不写tag，则默认是latest最新版本。从docker中央仓库拉取最新的nginx版本
> 4、启动
> 	docker run -d --name "xdclass_nginx" -p 8088:80 nginx
> 	docker run -d --name "xdclass_nginx2" -p 8089:80 nginx
> 	docker run -d --name "xdclass_nginx3" -p 8090:80 nginx
> 	快速启动好几个nginx服务
> 5、测试
> 	方法1：
> 		打开安全组，配置端口8088/8089/8090，
> 		访问
> 			http://106.13.48.248:8088/，
> 			http://106.13.48.248:8089/，
> 			http://106.13.48.248:8090/
> 			都可以返回nginx首页页面
> 	方法2：
> 		直接在百度云控制平台，不用打开安全组端口自，
> 		命令执行
> 			curl "http://localhost:8088"，
> 			curl "http://localhost:8088"，
> 			curl "http://localhost:8088"
> 			都可以返回nignx首页的html代码文本
> ```

#### 5、公司使用Docker镜像仓库

> #### 简介
>
> ```python
> 官方公共镜像仓库和私有镜像仓库
> 	公共镜像仓库：
> 		官方：https://hub.docker.com/，基于各个软件开发或者有软件提供商开发的
> 		非官方：其他组织或者公司开发的镜像，供大家免费试用
> 
> 	私有镜像仓库：
> 		用于存放公司内部的镜像，不提供给外部试用； 
> 		SpringCloud 开发了一个支付系统 -》做成一个镜像 （操作系统+软件运行环境+用户程序）
> ```

#### 6、构建自己的镜像仓库

> #### 简介
>
> ```python
> 方法一：
> 	使用阿里云搭建自己的镜像仓库
> 方法二：
> 	待学。
> 	使用docker提供的方法，构建自己本地的镜像仓库。
> 	代价大，过程复杂。
> ```
>
> #### 步骤
>
> ```python
> 1> 阿里云镜像仓库：https://dev.aliyun.com/search.html --> 点击"镜像搜索"，页面跳转至自己的镜像页
> 2> 点击管理控制台 -> 初次使用会提示开通，然后设置密码
> 3> 如果第一次，则点击创建镜像仓库，一直下一步，创建好自己的仓库。
> 4> 如果之前已经创建过，则，点击"管理"，会有详细的"操作指南"
> ```
>
> #### 步骤摘录
>
> ```python
> 使用阿里云私有镜像仓库
> 	1> 登录： 
> 		docker login --username=ziqiwu18210553849 registry.cn-beijing.aliyuncs.com
> 		输入密码：
> 	2> 给自己的镜像打tag：
> 		docker tag [ImageId] registry.cn-beijing.aliyuncs.com/2019-04-27/docker-learn:
>             [镜像版本号]
> 		注* 
> 		  1、[ImageId]是用docker images命令就可以得到的镜像ID
> 		  2、[镜像版本号]是自己随便起的名称。
> 	3> 推送本地镜像：
> 		docker push registry.cn-beijing.aliyuncs.com/2019-04-27/docker-learn:[镜像版本号]
> 	3> 拉取镜像
> 		线上服务器拉取镜像：
> 		docker pull registry.cn-beijing.aliyuncs.com/2019-04-27/docker-learn:[镜像版本号]
> 	4> 创建容器并启动
> 		docker run -d --name "xdclass_mq" -p 5672:5672 -p 15672:15672 
>                 registry.cn-beijing.aliyuncs.com/2019-04-27/docker-learn:rabbitmq_images1
> 	5> 查看阿里云镜像仓库所有镜像		
> 		https://q.cnblogs.com/q/94364/
> ```

#### 7、查看私有仓库所有镜像

> ```python
> 1> 进入阿里云私有仓库
> 	https://dev.aliyun.com/search.html
> 2> 点击左侧"镜像版本"
> 	可以看到右侧列表中所有的镜像，上传到私有仓库中的所有镜像
> ```

#### 8、报错+难题

> #### rabbitmq不能登录管控台
>
> ```python
> 原来百度云是好使的。是直接从docker hub拉的镜像。
> 用阿里云，安全组和linux防火墙把端口都开放了，还是不能访问管控台。是阿里云私有镜像仓库拉的镜像。
> 1> 最大可能，我上传到私有仓库的镜像是latest的，不是management版本的，这个版本才带有管控台。
> 	1、不能启动的docker logs xxID日志：
> 		started TCP listener on [::]:5672
> 	2、可以启动的:management版本的docker logs xxID日志：
> 		started TCP listener on [::]:5672
> 		Management plugin: HTTP (non-TLS) listener started on port 15672
> 2> 是私有云仓库拉取时候的问题
> ```
> ####  Docker启动，则容器启动
>
> ```python
> --restart=always
> ```
>
> #### 创建容器后修改其属性
>
> ```python
> 来源：https://blog.51cto.com/12053992/2393104
> 方法：docker container update --restart=always 容器名字   
> 	eg.添加属性--restart=always 
> ```

#### 9、Docker间网络通信

> #### 来源
>
> ```python
> Docker的四种网络模式Bridge模式:
> 	https://www.cnblogs.com/yy-cxd/p/6553624.html
> ```
>
> #### 记录
>
> ```python
> 1> 命令brctl show
> 	并命名为eth0（容器的网卡），另一端放在主机中，以vethxxx这样类似的名字命名
> 2> iptables -t nat -vnL
> ```

#### 记录

> ```python
> 1> docker官方仓库或者docker官网查找相关镜像
> 	比如，查找nginx相关镜像，可以docker search nginx。
> 		也可以直接登录docker.io官网，ctrl+f查找nginx，官网有各种版本说明。
> 2> 实战为：
> 	1、CentOS7 安装docker
> 	2、拉取安装rabbitmq
> 	3、拉取安装nginx
> 3> curl命令新使用
> 	curl "http://127.0.0.1:8088"，默认返回nginx的html代码
> 4> 好处：
> 	使用高可用、集群很方便。
> 	docker run -d...映射端口号改一下，name名称改一下
> 	docker run -d...映射端口号改一下，name名称改一下
> 	很快可以启动很多个nginx服务
> ```
>


