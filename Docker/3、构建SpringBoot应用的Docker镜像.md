### 不记文档，白忙一场

------

#### 0、方法一：maven命令打包

> #### 简介
>
> ```python
> 加入maven插件，并使用mvn命令将springboot项目打包为镜像
> 注* 如果是mac系统的开发环境，则很简单。
> 	如果是window系统的开发环境，window环境下安装的docker，则会出现各种问题。
> 	我使用的是方法二。
> ```
>
> #### 步骤
>
> ```python
> 1> maven里面添加配置pom.xml
>     <properties>
>         <docker.image.prefix>xdclass</docker.image.prefix>
>     </properties>
> 
>     <build>
>         <finalName>docker-demo</finalName>
>         <plugins>
>             <plugin>
>                 <groupId>com.spotify</groupId>
>                 <artifactId>dockerfile-maven-plugin</artifactId>
>                 <version>1.3.6</version>
>                 <configuration>
>                     <repository>${docker.image.prefix}/${project.artifactId}</repository>
>                     <buildArgs>
>                         <JAR_FILE>target/${project.build.finalName}.jar</JAR_FILE>
>                     </buildArgs>
>                 </configuration>
>             </plugin>
>         </plugins>
>     </build>
> 	注* 配置讲解
>     	Spotify 的 docker-maven-plugin 插件是用maven插件方式构建docker镜像的。
>     	${project.build.finalName}是jar名称，缺省为${project.artifactId}-${project.version}
> 	    ${project}是maven自带的变量，直接适用就可以了。
> 2> 创建Dockerfile
> 	FROM openjdk:8-jdk-alpine
> 	VOLUME /tmp
> 	ARG JAR_FILE
> 	COPY ${JAR_FILE} app.jar
> 	ENTRYPOINT ["java","-jar","/app.jar"]
> 	
> 	注* 
> 	默认是根目录，可以修改为src/main/docker/Dockerfile，如果修改则需要制定路径
>     参数讲解：
>     1、FROM <image>:<tag> 需要一个基础镜像，可以是公共的或者是私有的， 后续构建会基于此镜像，如果		同一个Dockerfile中建立多个镜像时，可以使用多个FROM指令
> 	2、VOLUME  配置一个具有持久化功能的目录，主机 /var/lib/docker 目录下创建了一个临时文件，并链		   接到容器的/tmp。改步骤是可选的，如果涉及到文件系统的应用就很有必要了。/tmp目录用来持久化到 	    Docker 数据文件夹，因为 Spring Boot 使用的内嵌 Tomcat 容器默认使用/tmp作为工作目录 
> 	3、ARG  设置编译镜像时加入的参数， ENV 是设置容器的环境变量
> 	4、COPY : 只支持将本地文件复制到容器 ,还有个ADD更强大但复杂点
> 	5、ENTRYPOINT 容器启动时执行的命令
> 	6、EXPOSE 8080 暴露镜像端口
> 3、构建镜像
> 	点击项目，show in folder或者IDEA点击terminal进入项目终端操作
> 	mvn install dockerfile:build
>         
> 	注* 我的执行报错：
>         Caused by: com.spotify.docker.client.exceptions.DockerException: 					    java.util.concurrent.ExecutionException: com.spotify.docker.client.shaded.java
>         x.ws.rs.ProcessingException: org.apache.http.conn.HttpHostConnectException: 
>         Connect to localhost:2375 [localhost/127.0.0.1, localhost/0:0:0:0:0
>         :0:0:1] failed: Connection refused: connect
> 4、将镜像推送至阿里云的docker私有镜像仓库
> 	方法详见docker部署-linux之"构建自己的镜像仓库"
> 5、登录阿里云私有仓库地址，查看镜像版本，查看是否镜像推送成功
> ```
>
> #### 官方文档
>
> ```python
> https://spring.io/guides/gs/spring-boot-docker/
> ```
>
> #### 记录
>
> ```python
> 0、<build>标签中的<finalName>标签，代表项目打成jar包之后的名称。
> 1、${project}是maven自带的变量，直接适用就可以了。
> 2、Dockerfile里面的FROM之后的版本，可以到Docker官方仓库去搜索。
> 3、Docker是一个容器，里面的目录都是虚拟的。而我们有的东西需要让它持久化。
> 4、ARG即设置变量，然后后面直接使用这些定义好的变量。
> 5、COPY ${JAR_FILE}其中JAR_FILE是POM文件中已经有的标签名称。 -- 将本地文件复制到容器
> ```

#### 1、方法二：docker命令打包

> #### 简介
>
> ```python
> 本地VMware创建虚拟机，或者直接用aliyun云服务器。
> 将springboot-app.jar和Dockerfile拖入服务器，执行docker命令，打包生成镜像。
> ```
>
> #### 步骤
>
> ```python
> 0> pom文件中的<build>标签下加入<finalname>标签
> 	<build>
>         <finalName>docker-demo</finalName>
> 		...
> 	</build>
> 1> 将springboot项目，打成jar包
> 2> 创建Dockerfile文件
>     FROM java:8
>     VOLUME /tmp
>     ADD docker-demo.jar app.jar
>     RUN sh -c 'touch /app.jar'
>     ENV JAVA_OPTS=""
>     ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar 			/app.jar" ]
> 	注* 
>         0、ADD docker-demo.jar中的docker-demo这个名称和<finalName>的名称一致。
>         1、FROM java:8 
>             是指含有jdk1.8的镜像
>         2、VOLUE /tmp 
>             /tmp目录并持久化到Docker数据文件夹，因为Spring Boot使用的内嵌Tomcat容器默认使			    用/tmp作为工作目录
>         3、ADD docker-demo.jar app.jar
>             添加自己的项目到到app.jar中
>             注意：这里的包名要和pom文件中的包名一致。项目设定了finalname是docker-demo
>         4、ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom 
>                       -jar /app.jar" ]
>             ENTRYPOINT是指容器运行后默认执行的命令。
> 3> 构建镜像
> 	docker build -t front:1.0-SNAPSHOT .
> 	注* 注意后面是有个点的。
> 4、将镜像推送至阿里云的docker私有镜像仓库
> 	方法详见docker部署-linux之"构建自己的镜像仓库"
> 5、登录阿里云私有仓库地址，查看镜像版本，查看是否镜像推送成功
> ```
>
> #### 来源
>
> ```python
> https://blog.csdn.net/why154285/article/details/81067772
> ```

#### 2、测试上传自己镜像到仓库

> ```python
> 1> 登录百度云，执行上诉方法二，进行自己镜像的打包
> 2> 将项目上传到自己的阿里云私有镜像仓库，方法详见docker部署-linux之"构建自己的镜像仓库"
> 3> 登录阿里云，执行拉取操作，然后运行该镜像，访问该镜像接口
> ```

#### 3、构建server-eureka的镜像

> #### 实战步骤
>
> ```python
> 注* 还是使用方法二
> 0> pom文件中的<build>标签下加入<finalname>标签
> 	<build>
>         <finalName>server-eureka</finalName>
> 		...
> 	</build>
> 1> 将springboot项目，打成jar包
> 	IDEA的terminal终端中keyin命令：mvn clean package -Dmaven.test.skip=true
> 2> 创建Dockerfile文件
>     FROM java:8
>     VOLUME /tmp
>     ADD server-eureka.jar app.jar
>     RUN sh -c 'touch /app.jar'
>     ENV JAVA_OPTS=""
>     ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar 		/app.jar" ]
> 3> 测试
> 	用命令curl "http://localhost:6781"
> 	因为是aliyun服务器，不能开放该端口，所以用curl测试即可。返回的是注册中心管控台的html代码。
> ```

#### 4、构建server-config的镜像

> #### 一直报错
>
> ```python
> 报错信息：
> 	No route to host (Host unreachable)
> 问题描述：
> 	Docker容器相连时出现"no route to host"错误
> 	之后我重新写Dockerfile和修改配置文件中连接注册中心的ip地址，localhost、内网ip都不行
> 问题解决：
>     docker 解决容器内访问宿主机“No route to host”的问题
>     修复方式请顺序运行以下命令：
>         nmcli connection modify docker0 connection.zone trusted
>         systemctl stop NetworkManager.service
>         firewall-cmd --permanent --zone=trusted --change-interface=docker0
>         systemctl start NetworkManager.service
>         nmcli connection modify docker0 connection.zone trusted
>         systemctl restart docker.service
> 来源：
> 	https://www.cnblogs.com/cdmakunjie/p/8182654.html
> 下有评论：
> 	你好，我按照这个来修改，虽然能访问了，但是出现新的问题了，eureka集群，向某一个节点注册服务的时      候报错，找不到另外两个节点（会同步注册到这两个节点），请问你有遇到过么？
> ```
>
> #### ***关于docker之间的通信--IP***
>
> ```python
> 0> 前提 -- 怎么查询各个docker的IP地址
> 	来源：https://blog.csdn.net/sannerlittle/article/details/77063800
> 	方法1：docker inspect --format '{{ .NetworkSettings.IPAddress }}' <container-ID> 
> 		上述只需要修改<container-ID>即容器ID
> 	方法2：docker inspect <container id> 
>     	在最后的NetworkSettings下的IPAddress即为该Docker的IP地址，和方法1一样
> 	方法3：docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 			container_name_or_id
> 1> 配置中心server-config是eureka-client，需要连接注册中心eureka-server，配置连接信息为：
> 	defaultZone: http://172.17.0.2:8761/eureka/可以
> 	defaultZone: http://172.16.0.4:8761/eureka/可以
> 	其中172.16.0.4是宿主机的IP，172.17.0.2是这个Docker的IP -- 配置中心的Docker
> 2> 注册中心server-eureka的管控台地址
> 	http://172.17.0.3:8761可以
> 	http://172.16.0.4:8761可以
> 	其中172.16.0.4是宿主机的IP，172.17.0.3是这个Docker的IP -- 注册中心的Docker
> ```
>
> #### 实战步骤
>
> ```python
> 注* 还是使用方法二
> 0> pom文件中的<build>标签下加入<finalname>标签
>     <build>
>         <finalName>server-config</finalName>
>         ....
>     </build>
> 1> 修改applicaiton.yml
> 	将制定注册中心的配置信息改为：defaultZone: http://172.16.0.4:8761/eureka/
> 	原来是：defaultZone: http://localhost:8761/eureka/
> 	注* 这儿是模拟有自己机房的情况下，注册中心和配置中心放在两台机器上的情况。
> 		一般情况下注册中心和配置中心，肯定不会再一台机器上。
> 		所以配置中心的applicaiton.yml中配置注册中心的信息，把localhost换为同一机房的内网地址。
> 2> 将springboot项目，打成jar包
> 	IDEA的terminal终端中keyin命令：mvn clean package -Dmaven.test.skip=true
> 	不能直接用IDEA的MAVEN的install是因为有TEST，会尝试连接注册中心，肯定连不上会报错。
> 	所以用mvn命令手动打包Jar，跳过test环节。
> 3> 创建Dockerfile文件
>     FROM java:8
>     VOLUME /tmp
>     COPY server-config.jar app.jar
>     ENTRYPOINT ["java","-jar","/app.jar"]
> 4> 测试
> 	用命令curl "http://localhost:9100/order-service-dev.yml"
> ```
>
> #### 记录
>
> ```python
> 1> 一般情况下注册中心和配置中心，肯定不会再一台机器上。
> 	所以配置中心的applicaiton.yml中配置注册中心的信息，把localhost换为同一机房的内网地址。
> 2> 验证rabbitmq是否启动成功
> 	curl "http://localhost:15672"
> 3> 验证server-config配置中心是否启动成功
> 	curl "http://localhost:9100/product-server-pro.yml"
> 注* curl的时候，要么localhost要么写内网即阿里云的私有网络。写公网是不能生效的。
> 注* 所有对外都要经过网关才可以，应用见通信（除非跨机房）都用内网通信
> 
> 4> 部署redis：
> 	是因为下单服务中，有这样的一个依赖，（报警功能）
> 5> docker启动rabbitmq
> 	docker run -d --name "xdclass_mq" -p 5672:5672 -p 15672:15672 rabbitmq:management
> 	因为配置中心，依赖到了该消息队列
> 	注* 配置中心的时候，先不启动rabbitmq，等到商品服务和下单服务的时候，再启动
> ```

#### 5、Docker安装redis镜像

> #### 原因简述
>
> ```python
> 因为服务中对redis存在依赖
> 下单服务中的熔断降级是有告警功能的，此功能的实现需要依赖redis服务，所以在部署server-order-feign之前需要先安装redis镜像
> ```
>
> #### 步骤
>
> ```python
> 1、搜索镜像 
> 	docker search redis
> 2、拉取 
> 	docker pull docker.io/redis
> 	注* docker.io/redis是第一步搜索出来的第一行，可以看到OFFICIAL是OK，是官方推出来的
> 3、启动 
> 	docker run --name "redis-xiaoguozi" -p 6379:6379 -d 4e8db158f18d
> 	注* 启动的是redis的服务端，最后一句日志 Ready to accept connections
> 	注* 如果需要配置密码等信息，则
> 	docker run --name "redis-xiaoguozi" -p 6379:6379 -d 4e8db158f18d --requirepass "123456" 	-v 	$PWD/data:/data
> 4、访问redis容器里面，进行操作
> 	docker exec -it 295058d2b92e redis-cli
> 	注* 启动的是redis的客户端
> 	注* docker exec -it是进入某个容器，执行命令
> 5、测试
> 	第4步，启动完客户端之后，可以执行set name guozi
> 	执行docker inspect redis-xiaoguozi
> 	可以得到安装redis的docker的IP，172.17.0.4
> 	进入redis的安装包中，./redis-cli -h 172.17.0.4
> 	再执行get name可以得到guozi
> 	证明是redis服务端是正确的
> ```

#### 6、Docker安装rabbitmq镜像

> #### 原因简述
>
> ```python
> 因为服务中对rabbitmq存在依赖
> 下单服务和商品服务的消息总线Bus对动态刷新配置文件功能的实现，需要依赖rabbitmq，所以在部署server-order-feign和server-product之前需要先安装rabbitmq镜像。
> ```
>
> #### 步骤
>
> ```python
> docker run -d --name "rabbitmq-xiaoguozi" -p 5672:5672 -p 15672:15672 rabbitmq:management
> ```

#### 7、解决注册非ip:port问题

> ```python
> 问题描述：
> 	1> 问题1：
>         之前，在本地启动注册中心服务端和各个客户端，进入注册中心管控台，可以看到，
>         各个eureka-client的
>         标识为：UP (1) - R9LOMLJ7ILIFB69:config-service:9100
>         这样部署到生产环境的docker上是肯定有问题的，因为docker之间不能通过ip：port相互通信。
>         在本地的IDEA上通信没问题，但是生产环境是各个机器间的docker进行通信
> 	2> 问题2：
> 		比如启动server-order和server-product的时候，控制台输出springboot的logo，然后第一行是：
> 		Fetching config from server at：从配置中心，拉取对应的配置信息
> 		如果不是ip:port的格式，就是一串数字加字母，肯定在生产环境下是访问不到的。
> 问题解决：
> 	在每个eureka-client的配置文件中，关于注册中心的信息，都增加instance属性描述。如：
>  	instance:
> 		#实例ID，格式为ip:port
> 	    instance-id: ${spring.cloud.client.ip-address}:${server.port}
> 		#偏好是ip地址
> 		prefer-ip-address: true
> 	和eureka.client平级
> 解决之后：
> 	标识为：UP (1) - 192.168.42.1:9100
> ```

#### 8、构建server-product镜像

> ```python
> 下同server-zuul
> ```

#### 9、构建server-order镜像

> ```python
> 下同server-zuul
> ```

#### 10、构建server-zuul镜像

> ```python
> 1> pom中增加<finalName>标签
> 	如果是maven插件打包的话，则增加插件依赖，详见方法一：maven命令打包
> 2> bootstrap.yml配置文件
> 	1、注册中心配置信息，ip修改为部署eureka-server的docker的ip
> 	2、增加instance属性描述
> 3> 增加Dockerfile文件
> 4> mvn clean package -Dmaven.test.skip=true
> 	window上打jar包
> 5> docker build -t xxxx:xxxx .
> 	linux机器上构建镜像
> ```

#### 11、其余修改

> #### 修改
>
> ```python
> 1> git上的rabbitmq连接信息，ip由localhost修改为rabbitmq镜像所在的docker的ip
> 2> 网关server-zuul是有一个坑的，演示错误，因为网关服务中，也有rabbitmq的连接配置信息，host的信息为
> 	localhost，所以一直warn警告：Attempting to connect to: [localhost:5672]。
> 	警告尝试连接rabbitmq，但是就是连接不上。
> 	所以网关服务对应的git配置信息，也需要修改。
> 	注* 商品服务、订单服务、网关服务的git配置信息都需要修改。
> 3> 正式部署的时候，只有网关的9000端口开放，剩余的端口全部关闭。公司的话，会做内外网隔离。
> 4> 同第一点，redis的连接信息，在server-order-feign的项目对应的git配置文件中，
> 	也需要修改redis的连接信息中的host
> 5> 测试：
> 	直接访问下单接口
> 	通过网关访问下单接口
> ```
>
> #### 记录
>
> ```python
> 注* 
> 	server-eureka：172.17.0.2
> 	server-config：172.17.0.3
> 	redis-xiaoguozi：172.17.0.4
> 	rabbitmq-xiaoguozi：172.17.0.5
> 	server-order-feign：172.17.0.6
> 1> 官方解释：
> 	首次访问下单接口，会报错
> 2> 用到redis的地方，测试：
> 	地址的参数product_id赋值一个没有的数值，会报错，触发熔断降级和报警，会存一个标识进入redis，防	  止不停报警。
> 3> 先不要启动网关，测试访问：
> 	http://106.13.48.248:8781/api/v1/order/save?user_id=2&product_id=3&token=2423
> 	注* 需要百度云的安全组开放8781端口
> 4> 启动网关，测试一下网关的使用
> 	http://106.13.48.248:9000/apizuul/order/api/v1/order/save?								user_id=2&product_id=3&token=2423
> 	所以，生产环境上只需要开放网关端口，其余端口全部关闭。更加安全。
> 	注* 需要百度云的安全组开放9000端口
> ```

#### 12、构建出错

> ```python
> 1> 原来的时候，server-eureka所在的docker的ip是172.17.0.4，到了单位再查看的时候，
> 	变成了172.17.0.2。然后停掉了所有容器，删掉了镜像。重新打包镜像，涉及连接注册中心的配置信息都改	为172.17.0.2。
> 2> 网关报错：（机器性能不够）
>     报错信息：
>         Caused by: com.netflix.client.ClientException: Load balancer does not have 				available server for client: order-service
>     问题分析：
>         1、以为是order-service命名出错了，将网关在git上对应的配置信息修改成order-servcie-feign，
>         	一样报错。
>         2、然后发现是server-order-feign-xiaoguozi服务挂掉了。停掉server-zuul，然后重启
>         	server-order，访问网关对应下单接口，还是报错，再查看server-order又挂掉了。
>         3、free -m查看机器性能，内存只剩不到100m了。好吧，问题找到到了。
>         4、停掉了server-redis，启动server-order和server-zuul，访问网关对应下单接口，成功。
>         5、因为redis只有在熔断降级后报警的时候，才会访问，所以停掉也暂时没有影响。
>     问题解决：
>         暂时弹性伸缩1G内存，只买一周
> 	得到经验：
>     	我们经常说的，服务器宕掉了，其实都是硬件的问题，性能不够用了。
> ```

#### 13、只开放网关端口给外网

> ```python
> 做内外网隔离
> 两个地址都可以访问：
> 	1> http://106.13.48.248:8781/api/v1/order/save?user_id=2&product_id=3&token=2423
> 	2> http://106.13.48.248:9000/apizuul/order/api/v1/order/save?								user_id=2&product_id=3&token=2423
> 但是：
> 	8781端口是不会开放给外网的，所以不可能访问得到，
> 	指挥开放9000这个网关的端口号给外网。
> ```

#### 记录

> ```python
> 0、测试是否项目启动成功，用curl命令，访问即可
> 1、server-eureka的管控台界面不会开放给外网访问的。8761
> 2、rabbitmq的管控台也是不会开放给外网访问的。15672端口
> 3、不增加eureka.instance下面的instance-id和prefer-ip-address的情况下，现在本地测试：
> 	eureka-server的管控台，有一个Status的数据显示，在本地测试的时候，格式不是ip:port的。
> 	先不用放到生产上面测试。
> 4、配置中心server-config的好处：
> 	如果服务改换端口、改换rabbitmq等，只需要修改git仓库中的配置信息，然后重启对应服务就可以，而不需	 要在项目中修改，再打包镜像了。重启服务，就是docker stop xxx，然后docker start xxx即可
> 注* 如果公司有自己机房，是用内网访问。如果是阿里云服务器，则不能访问，一般也不会访问这个管控台。
> 注* 阿里云机器的话，是否可以租一个内网是相同网段的，然后这台机器装window，就是为了访问，好像不行。
> ```