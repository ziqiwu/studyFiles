### 不记文档，白忙一场

------

#### ***什么环境使用***

> ```python
> 在开发，测试的时候使用，生产不要使用。
> 不会来回变动
> ```

#### 0、消息总线概念

> ```python
> 讲解消息总线Bus介绍和使用场景
> 
> 1、什么是消息
> 	一个事件，需要广播或者单独传递给某个接口
> 2、为什么使用这个
> 	配置更新了，但是其他系统不知道是否更新
> ```

#### 1、rabbitmq基本介绍

> #### 简介
>
> ```python
> 1、消息队列介绍
> 	参考：https://www.cnblogs.com/linjiqin/p/5720865.html
> 
> 2、同类产品
>     ActiveMQ
>     RocketMQ
>     Kafka
>     等
>     
> 3、SpringCloud默认推荐使用RabbitMQ
> ```
>
> #### 官网
>
> ```python
> 官方文档：http://www.rabbitmq.com/getstarted.html
> 中文文档：http://rabbitmq.mr-ping.com/
> ```

#### 2、docker安装rabbitmq

> #### 安装步骤
>
> ```python
> 1> 拉取镜像：docker pull rabbitmq:management
> 2> 查看当前镜像列表：docker images
> 3> 删除指定镜像：docker rmi  IMAGE_ID  (如果需要强制删除加 -f)
> 			
> 4> 创建容器
> 	docker run -d --name="myrabbitmq" -p 5671:5671 -p 15672:15672 rabbitmq:management
> 
>     参数讲解: 
>     run: 创建一个新的容器并运行一个命令
>     -d: 后台运行容器，并返回容器ID
>     -p: 端口映射，格式为：主机(宿主)端口:容器端口
>     --name="rabbitmq": 为容器指定一个名称
> ```
>
> #### 管控台
>
> ```python
> RabbitMQ默认创建了一个 guest 用户，密码也是 guest, 如果访问不了记得查看防火墙，端口或者云服务器的安全组
> 管理后台：http://127.0.0.1:15672
> ```
>
> #### 其他安装方式
>
> ```python
> Linux安装：https://blog.csdn.net/qq_34021712/article/details/72567786
> windows安装：http://www.rabbitmq.com/install-windows.html
> https://blog.csdn.net/liyuejin/article/details/78410586
> ```
>
> #### 记录
>
> ```python
> 1> rabbitmq是spring cloud官网推荐使用的消息队列
> 2> docker pull rabbitmq:management其中版本号指的是，带有管控台的版本
> 3> -p 5671:5671 -p 15672:15672其中后面的端口映射指的是，管控台web页面的端口号，前面的端口映射指的	是应用的端口。
> 4> 管控台地址为http://localhost:15672，默认账号密码都是guest
> 5> 百度搜索"rabbitmq 管控台讲解"
> ```
> #### 报错
>
> ```python
> 原来百度云是好使的。是直接从docker hub拉的镜像。
> 用阿里云，安全组和linux防火墙把端口都开放了，还是不能访问管控台。是阿里云私有镜像仓库拉的镜像。
> 解决：
>     1> 最大可能，我上传到私有仓库的镜像是latest的，不是management版本的，这个版本才带有管控台。
>         1、不能启动的docker logs xxID日志：
>             started TCP listener on [::]:5672
>         2、可以启动的:management版本的docker logs xxID日志：
>             started TCP listener on [::]:5672
>             Management plugin: HTTP (non-TLS) listener started on port 15672
>     2> 是私有云仓库拉取时候的问题
> ```

#### 3、Bus实战

> #### 消息总线整合配置中心架构流程图
>
> ```python
> 详见流程图.jpg
> ```
>
> #### 官方文档
>
> ```python
> 官方文档：
> 	http://cloud.spring.io/spring-cloud-bus/single/spring-cloud-bus.html
> 	#_bus_refresh_endpoint
> ```
>
> #### 实战步骤
>
> ```python
> 在配置文件中增加关于RabbitMQ的连接
> 步骤：
> 	1> 启动rabbitmq
> 	2> config-client加入依赖
> 		本实例中是server_product
> 		<!--配置中心结合消息队列-->
> 		<dependency>
>             <groupId>org.springframework.boot</groupId>
>             <artifactId>spring-boot-starter-actuator</artifactId>
> 		</dependency>
> 
> 		<dependency>
>             <groupId>org.springframework.cloud</groupId>
>             <artifactId>spring-cloud-starter-bus-amqp</artifactId>
> 		</dependency>
> 	3> 在配置文件中增加关于RabbitMQ的连接
> 	    #rabbitmq连接信息
>         spring:
> 			rabbitmq:
> 				host: localhost
> 				port: 5672
> 				username: guest
> 				password: guest
> 			
> 		#暴露全部的监控信息
> 		management:
> 			endpoints:
> 				web:
> 					exposure:
> 						include: "*"
> 		注* 文档里面 暴露端点 management.endpoints.web.exposure.include=bus-refresh。
>         	本实例是暴露所有端点
> 	4> 需要刷新配置的地方，增加注解@RefreshScope 
>         @RestController
>         @RequestMapping("/api/v1/product")
>         @RefreshScope
>         public class ProductController {
>             private final Logger logger = LoggerFactory.getLogger(getClass());
> 
>             @Autowired
>             private ProductDao dao;
>             //小知识点：属性值优先取IDEA设置的，然后才是application.yml中的
>             @Value("${server.port}")
>             //为了测试消息总线Bus是否生效增加，该配置在git中
>             private String port;
>             @Value("${env}")
>             ....
> 		注* server_product中env是git上面配置的，这儿是测试修改git上面env然后看结果
> 	5> 手动触发webhook钩子函数
> 		http://localhost:8773/actuator/bus-refresh
>             1> post请求方式
>             2> 手动触发
>             3> 端口号是product应用服务的端口号  
> 	6> 查看结果
> 		0、修改git配置env值
> 		1、通过配置中心，拉取git配置
> 			http://localhost:9100/master/product-service-pro.yml
> 		2、访问product接口，查看配置是否读取最新的
> 			http://localhost:8777/api/v1/product/findById?id=1
> 		3、product启动两个节点
> 			查看是否修改配置，手动触发一个节点的钩子函数，所有连接mq的节点都会重新拉取配置
> 			http://localhost:8777/api/v1/product/findById?id=1
> 			http://localhost:8778/api/v1/product/findById?id=1
> 			方法详见下面的测试章节
> 测试：
> 	1> 需要启动的应用有：注册中心、配置中心、server_product
> 	2> 因为，server_product不需要调用其他微服务，而它首先需要到注册中心拿到配置中心信息，再通过配			置中心到git拿上面的配置信息。
> 		不用启动网关应用，是因为，走网关的配置是server_zuul中配置的，它不启动，就没有走网关。
> 	3> 最先启动注册中心，因为剩下两个都是注册发现应用。然后是配置中心，因为product应用通过注册中心
>     	找到配置中心后，才能通过配置中心到git拿信息了。
> 	4> 重启product服务，确实可以更新配置。也是废话，重启它肯定会去配置中心拿最新的配置信息。
> 	5> 启动两个product节点，不能在IDEA加-Dserver.port了，因为它要优先去读取git上面的配置。
> 		解决办法是，先启动一个节点，然后修改git上面的端口，再启动一次。 -- 验证广播
> 	6> 其他节点连接到这个消息队列，只要一个refresh一个节点，消息队列产生消息，其他都会重新拉取
> 	7> post请求refresh的时候，在rabbitmq管控台，才可以看到曲线的变动。说明消息推送到mq中。
> ```
>
> #### 生产建议
>
> ```python
> 生产环境不建议使用，原因如下：
> 	1> 黑客攻击，入口点改配置就可以了
> 	2> 实际项目，组件用的越多，越分散，风险就越大。核心组件用起来就可以了，不要用那么多。
> 	3> 把全家桶几十个组件都用上，那这个项目将超级庞大。杀鸡用牛刀，没必要。
> 	4> 开发和测试用，生产不要用。
> ```
>
> #### 记录
>
> ```python
> 1> 测试漏一步的访问结果
> 	config-server可以从git上读取最新的配置信息
> 	但是server_product还是不可以
> 2> @RefreshScope需要加的类，是里面有需要动态更新的配置新信息的类。
> 3> 最终达到的效果：
>    应用重启，动态更新配置
> 4> 测试单播和广播，启动product两个应用，测试是否连接上rabbitmq的应用，到时候触发了，都会去拉最新的	 配置
> 5> rabbitmq只是一个中转站，其他用处不大。解耦
> 6> 手动触发bus-refresh，就会产生一个消息，推送到消息队列，其他应用接收到这个消息，就会去拉取最新的    配置。
> ```