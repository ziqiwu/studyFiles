### 不记文档，白忙一场

------

#### 0、注意点

> ```python
> nginx.conf配置文件详解
> 来源（太tm详细了）：https://www.cnblogs.com/zhang-shijie/p/5428640.html
>     
> ```

#### 1、安装步骤

> ```python
> docker安装nginx	
> 	来源：https://www.cnblogs.com/wwzyy/p/8337965.html（我实践过的）
> 	来源：https://www.runoob.com/docker/docker-install-nginx.html（参数详细，没有实践过）
> 	1 正常docker安装nignx
> 	2 本地修改一个nginx.conf文件，执行命令复制到docker容器中
> 		注* nginx在docker中的安装目录，参见来源1
> 	3 修改nginx.conf文件如下
> 		#注* upstream配合location可以设置多个
> 		upstream xiaoguozi_server{
> 			#注1* 写成http://172.17.237.103:8080报错，百度去掉了http://
> 			server 172.17.237.103:8080;
> 		}
>         upstream xiaoguozi_solor{
> 			#注1* 写成http://172.17.237.103:8080报错，百度去掉了http://
> 			server 172.17.237.103:8082;
> 		}
>         server {
>             listen       80 default_server;
>             listen       [::]:80 default_server;
>             server_name  xiaoguozi.com.cn;
> 		    #注2* 这个使用默认配置文件启动nginx容器，docker exec -it 容器id bash就可进入容器
> 		    #进行nginx在docker中安装目录的查看
>             root         /usr/share/nginx/html;
> 
>             # Load configuration files for the default server block.
>             include /etc/nginx/default.d/*.conf;
> 			
>             #注3* location是/，代表xiaoguozi.com.cn，访问的是首页
> 		   #我一开始一直报错，就是把下面location /biz/*的内容写在了location /里面
> 			#结果，我访问xiaoguozi.com.cn它直接给我跳到了upstream里面。
>             location / {
> 				root   /data/xiaoguozi/projectfront;
> 				index  xiaoguozi.html index.htm;
>             } 
> 		    #注4* 这儿表示的是代理到Tomcat服务器
>             #xiaoguozi.com.cn/biz/xxx
>             location /biz {
>                    proxy_set_header Host $host;
>                    proxy_set_header X-Real_IP $remote-addr;
>                    proxy_pass http://xiaoguozi_server;
>             }
>             #xiaoguozi.com.cn/solor/xxx
>             location /solor {
>                    proxy_set_header Host $host;
>                    proxy_set_header X-Real_IP $remote-addr;
>                    proxy_pass http://xiaoguozi_solor;
>             }
> 
>             error_page 404 /404.html;
>                 location = /40x.html {
>             }
> 
>             error_page 500 502 503 504 /50x.html;
>                 location = /50x.html {
>             }
>         }
> 	4 使用默认nginx.conf启动容器
> 	5 将nginx.conf复制到docker容器中
> 		docker cp nginx.conf xiaoguozinginx://etc/nginx/
> 	6 进入docker容器中，进行配置文件检测
> 		docker exec -it xiaoguozinginx bash
> 		nginx -t
> 		
> 		或者一条命令执行
> 		
> 		docker exec -it xiaoguozinginx nginx -t
> 	7 检测成功之后，重启容器
> 		docker restart xiaoguozinginx
> 	8 进行访问测试
> 		xiaoguozi.com.cn
> 		xiaoguozi.com.cn/index.html
> 		xiaoguozi.com.cn/xiaoguozi.html
> 	9 随便写一个springboot项目
> 		放在和nginx一台机器上
> 		nohup java -jar xxx.jar &启动
> 	10 nginx.conf中配置反向代理
> 		详细配置信息见"报错"章节
> 	11 xiaoguozi.html内容如下：
> 		<!DOCTYPE html>
> 		<html lang="en">
> 		<head>
>     		<meta charset="UTF-8">
>     		<title>小郭子网站</title>
> 		</head>
> 		<body>
>     		<h1><a href="/nginx/data/">小郭子，小郭子，呱呱呱</a></h1>
> 			<a href="/nginx/data/"><img src="https://txx.jpg" width="500"/></a
> 		</body>
> 		</html>
> 	12 不同端口启动
> 		nohup java -jar yourapp.jar --server.port=8888 &
> ```

#### 2、报错

> ```python
> 1> 只能实现处理静态内容，不能实现反向代理
> 	location块写错了两个地方
> 	原始：
> 	location /biz/* {
> 		proxy_set_header Host $host;
> 		proxy_set_header X-Real_IP $remote_addr;
> 		proxy_pass http://xiaoguozi_server;
> 	}
> 	正确：
> 	应该是/biz/，不能加*
> 	应该是X-Real-IP，不是X-Real_IP。导致nginx日志中，client地址总是和ip.taobao.com中看到的不一致2> 上面还有一点错
>     location /biz/之后，访问反向代理，发现，
> 	访问xiaoguozi.com.cn/nginx/data，但是日志为：
> 	http://172.17.237.103:8080/biz/nginx/data，所以，应该配置为：
> 	location /nginx/
> 3> 最后成型的nginx.conf整体配置信息为：
> 	upstream xiaoguozi_server{
> 		#注* 172.17.237.103是我aliyun服务器的内网ip，和docker的ip是在可以在内网访问的。
>         server 172.17.237.103:8080;
>     }
> 
>     server {
>         listen       80 default_server;
>         listen       [::]:80 default_server;
>         server_name  xiaoguozi.com.cn;
>         root         /usr/share/nginx/html;
> 
>         include /etc/nginx/default.d/*.conf;
> 
>         #注* http://xiaoguozi.com.cn/nginx/data访问就会匹配进入该location
> 	    location /nginx/ {
>                proxy_set_header Host $host;
>                proxy_set_header X-Real-IP $remote_addr;
>                proxy_pass http://xiaoguozi_server;
>         }
> 
> 
>         location / {
> 			root   /data/xiaoguozi/projectfront;
>              index  xiaoguozi.html index.htm;
>         } 
>   
> 
>         error_page 404 /404.html;
>             location = /40x.html {
>         }
> 
>         error_page 500 502 503 504 /50x.html;
>             location = /50x.html {
>         }
>     }
> 
> 4> docker容器中无法通过IP访问宿主机
> 	来源：https://segmentfault.com/a/1190000017829320
> 	1 用docker inspect xiaoguozinginx，可以看到docker容器的ip为172.18.0.2
> 	2 在宿主机上ping 172.18.0.2是可以ping通的，
> 		执行curl "http://172.17.237.103:8080/nginx/data"也没问题，
> 		查看日志，docker中的nginx反向代理访问的也是http://172.17.237.103:8080/nginx/data，
> 		但是报错no route for host。
> 		百度上面的来源地址，说是docker中已知的bug，需要修改防火墙文件。
> 		注* 简单粗暴的方法，关闭防火墙，systemctl stop firewalld，
> 			访问xiaoguozi.com.cn/nginx/data可以发现，正常访问。
> 	3 在/etc/firewalld/zones中，增加
> 		<rule family="ipv4">
> 			<source address="172.18.0.0/16" />
> 			<accept/>
> 		</rule>
> 		注* 增加172.18.xx.xx是不行的。我的docker的ip是172.18.0.2，所以包含在0/16中。
> 		注* 修改完后，需要重启防火墙systemctl restart firewalld
> ```