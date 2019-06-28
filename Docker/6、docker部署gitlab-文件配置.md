### 不记文档，白忙一场

------

#### 记录

> #### 启动命令
>
> ```python
> docker run -d --detach --publish 8443:443 --publish 8090:80 --publish 2222:22 --name xiaoguozigitlab --restart always --volume /data/gitlab/config:/etc/gitlab --volume /data/gitlab/logs:/var/log/gitlab --volume /data/gitlab/data:/var/opt/gitlab gitlab/gitlab-ce
> ```
>
> #### 来源
>
> ```python
> https://www.imooc.com/article/49032
> ```
>
> #### 步骤
>
> ```python
> 完全参照上面的来源步骤
> 1> 我们需要gitlab的镜像 gitlab-ce
> 	docker search gitlab --查看docker hub上关于gitlab的镜像
> 	docker pull gitlab/gitlab-ce  --使用pull命令获取查询结果的第一个镜像
> 2> 建立相关存储文件夹
> 	mkdir -p /data/gitlab/config
> 	mkdir -p /data/gitlab/logs
> 	mkdir -p /data/gitlab/data
> 3> 启动镜像
> 	docker run 
> 	--detach 
> 	--publish 8443:443 --publish 8090:80 --publish 2222:22 
> 	--name xiaoguozigitlab --restart always 
> 	--volume /data/gitlab/config:/etc/gitlab 
> 	--volume /data/gitlab/logs:/var/log/gitlab 
> 	--volume /data/gitlab/data:/var/opt/gitlab gitlab/gitlab-ce
> 	注* 这个过程会花费大量时间，占用大量资源，xshell会因为资源过少而自动断开，总之执行完成，
> 		baiduyun什么都做不了了。
> 4> 访问地址
> 	http://106.13.48.248:8090
> 	注* 106.13.48.248是我baiduyun的公网地址
> 5> 注册账户和密码，这个都是在gitlab的数据库保存的。所以第一次需要注册。
> 	如果之前在gitlab官网注册过，则直接登录。
> 6> 登录之后，就和gibhub上差不多了，创建project等。
> ```
>
> 

