### 不记文档，白忙一场

------

#### ***搭建流程***

> ```python
> git仓库服务器搭建
> config-server搭建
> config-client中的使用
> 注* 更重要是细读官方文档，视频也是跟着官网文档走的，但是很多细节地方并没有讲。
> ```

#### ***使用好处***

> ```python
> 配置中心server-config的好处：
> 	如果服务改换端口、改换rabbitmq等，只需要修改git仓库中的配置信息就可以，而不需要在项目中修改，
> 	再打包镜像了。
> 注* 生产环境不能使用钩子函数，自动触发，否则Cracker攻击的危险性大增。
> ```

#### 0、分布式配置中心基础

> #### 简介
>
> ```python
> 简介：讲解什么是配置中心及使用前后的好处 (画图)
> 1> 什么是配置中心：
> 	一句话：统一管理配置, 快速切换各个环境的配置
> 		
> 2> 相关产品：
> 	百度的disconf 
> 		地址:https://github.com/knightliao/disconf
> 	阿里的diamond
> 		地址：https://github.com/takeseem/diamond
> 	springcloud的configs-server:
> 		地址：http://cloud.spring.io/spring-cloud-config/
> 3> 推荐干货文章：
> 	http://jm.taobao.org/2016/09/28/an-article-about-config-center/
> 	注* 干货文章是阿里中间件的博客文章，强烈推荐，多开开眼界，了解前沿技术。
> ```
>
> #### 原理
>
> ```python
> 详见流程图.png
> ```

#### 1、实战(上)config-server

> #### 官网步骤
>
> ```python
> cloud.spring.io --> 左侧选择Spring Cloud Config
> ```
>
> #### 实战步骤
>
> ```python
> 第一步：新建项目server_config
> 	1> IDEA创建项目
> 	2> 选择的dependencies有Config Server(Cloud Config)和Eureka Discovery(Cloud Discovery)
> 第二步：配置application
>     server:
>       port: 8781
> 
>     #服务的名称
>     spring:
>       application:
>         name: config-service
> 
>     #指定注册中心地址
>     eureka:
>       client:
>         serviceUrl:
>           defaultZone: http://localhost:8761/eureka/
> 第三步：启动类加注解
> 	@EnableConfigServer
> 注* 启动之后报错：
> 	Caused by: java.lang.IllegalStateException: You need to configure a uri for the git 	repository
> ```

#### 2、实战(中)git服务器

> #### 简介
>
> ```python
> 上半部分，启动配置中心，报错，提醒没有git uri，所以实战下半部分，创建git，实现配置信息从git上获取
> ```
>
> #### 实战如下
>
> ```python
> 实战步骤
> 	1、在jitee上创建新repositories
> 		名称为config-cloud
> 	2、点击clone获取uri，配置在项目的application中 -- 写git.uri就会有全路径的提示信息
>         server:
>           port: 9100
> 
>         #服务的名称
>         spring:
>           application:
>             name: config-service
> 		 #配置连接git仓库信息
>           cloud:
>             config:
>               server:
>                 git:
>                   uri: https://gitee.com/guoshijie1994/config-cloud
>                   username: 842715417@qq.com
>                   password: 1314yuhongyi
>                   #超时时间
>                   timeout: 5
>                   #分支
>                   default-label: master
> 
>         #指定注册中心地址
>         eureka:
>           client:
>             serviceUrl:
>               defaultZone: http://localhost:8761/eureka/
>         注* timeout和default-label都可以点进入源码进行查看
> 	3、jitee上选择master分支，选择new file，新建一个file
> 		名称为:
>             product-service-dev.yml
> 		内容为：
>             branch: master
>             env: dev
>             eureka:
>               client:
>                 serviceUrl:
>                   defaultZone: http://localhost:8761/eureka/
>             server:
>               port: 8771
>             spring:
>               application:
>                 name: product-service
> 		注* branch和env两个配置属性是无用的，只是用来做测试使用。
> 	4、启动注册中心server_eureka，再启动配置中心server_config，可以发现不再报错了
> 		控制台打印信息：
> 			存在访问信息的规则
> 	5、访问路径：http://localhost:9100/product-service-dev.yml
> 	6、git上创建分支slave1，并且在master和slave1两个分支中都创建两个文件，各自的branch属性当然是		各自的分支属性，env在两个文件中分别是dev和pro。
> 	7、访问如下：
> 		http://localhost:9100/product-service-pro.yml
> 		http://localhost:9100/master/product-service-dev.yml
> 		http://localhost:9100/master/product-service-pro.yml
> 		http://localhost:9100/slave1/product-service-dev.yml
> 		http://localhost:9100/slave1/product-service-pro.yml
> ```
>
> #### 记录
>
> ```python
> 1> config的访问方式规则在项目启动时候，控制台就有输出
> 2> 访问规则
> 	/{name}-{profiles}.properties
>     /{name}-{profiles}.yml
>     /{name}-{profiles}.json
>     /{label}/{name}-{profiles}.yml
>     
> 	name 服务名称
> 	profiles 环境名称，开发、测试、生产
> 	lable 仓库分支、默认master分支
>     
> 	1、product-service.yml可成功
> 	2、product.yml失败
> 	3、product-service-a.yml成功
> 	4、master/product-service.yml成功
> 	5、properties、yml、json格式之间会自动转换
> 3> 补习
> 	git的分支概念
> 4> 分支
> 	从master分支，创建出一个新的分支test
> 	里面的内容，一模一样，可以看成是一个版本
> 	然后修改文件中branch属性的值，原来是master，现在修改为test
> 5> 环境的问题
> 	env 有两种值，一个test，一个dev
> 	branch 有两种值，一个是test，一个是master
> 	上接第2点
> 	/master/product-service-dev.yml和/master/product-service-test.yml
> 	/master/product-service-dev.yml和/test/product-service-dev.yml
> 6> 任何微服务都需要注意超时问题
> 7> 点击配置文件，进入源码，查看默认的配置都有哪些
> 8> 开源中国git
> 	https://gitee.com/
>         
> 9> 实战步骤
> 	1、jitee上创建新repositories
> 	2、点击clone获取uri，配置在项目的application中 -- 写git.uri就会有全路径的提示信息
> 	3、jitee上选择master分支，选择new file，新建一个file
> 	4、启动注册中心server_eureka，再启动配置中心server_config，可以发现不再报错了
> 	5、访问路径：http://localhost:9100/product-service.yml
> 	6、git上创建分支slave1，并且在master和slave1两个分支中都创建两个文件，各自的branch属性当然是		各自的分支属性，env在两个文件中分别是dev和pro。
> 	7、访问如下：
> 		http://localhost:9100/product-service-pro.yml
> 		http://localhost:9100/master/product-service-dev.yml
> 		http://localhost:9100/master/product-service-pro.yml
> 		http://localhost:9100/slave1/product-service-dev.yml
> 		http://localhost:9100/slave1/product-service-pro.yml
> ```

#### 3、实战(下)config-client

> #### 实战步骤
>
> ```python
> 1、加入依赖
>     <dependency>
>     	<groupId>org.springframework.cloud</groupId>
>     	<artifactId>spring-cloud-config-client</artifactId>
>     </dependency>
> 	注* 视频中只是对server_product服务做了改动，server_order_feign也是同理。
> 
> 2、修改对应服务的配置文件
> 	把application.yml 改为 bootstrap.yml
> 3、修改bootstrap.yml内容
>     #指定注册中心地址
>     eureka:
>         client:
>             serviceUrl:
>                 defaultZone: http://localhost:8761/eureka/
> 
>     #服务的名称
>     spring:
>         application:
>             name: product-service
>         #指定从哪个配置中心读取
>         cloud:
>             config:
>                 discovery:
>                     service-id: CONFIG-SERVER
>                 enabled: true
>                 profile: test
>                 #建议用lable去区分环境，默认是lable是master分支
>                 label: master
> 4、测试
> 	修改git上product-service-pro.yml文件的server.port端口号，启动server_product查看启动端口
> ```
>
> #### 记录
>
> ```python
> 1> 坑1
> 	需要将application.yml改名为bootstrap.yml
> 2> 坑2
> 	profile的位置
> 			#服务的名称
> 			spring:
> 			  application:
> 			    name: product-service   #++
> 			  #指定从哪个配置中心读取
> 			  cloud:
> 			    config:
> 			      discovery:
> 			        service-id: CONFIG-SERVER
> 			        enabled: true
> 			      profile: test  #++
> 			      #建议用lable去区分环境，默认是lable是master分支
> 			      #label: test
> 	注* 如上配置，将会到product-service-test中读取配置信息，而lable默认是master，源码可知。
>     	验证方法的话，将gitee上面的master下的product-service-test.yml中的server.port修改一个，
> 	    重启server_product服务，就可以看到端口号的改变。也可以改bootstrap.yml中的lable属性。
> 3> 坑3
> 	更建议用lable去区分不同的环境，而不是用后缀dev/pro。因为从控制台可以知道，后缀的配置文件，它都	 会读取，会把相同的部分抽取出来，当成一个独立的文件。所以会有删除其中一个配置文件信息，访问，这些	 信息还在的坑。
> 	
> 4> 本地和git上面配置不要重复
> 	比如bootstrap.yml中已经有了spring.application.name服务名称，则git上面就去掉这个配置
>     
> 5> 本地加很少的配置，大部分配置放在git服务器上
> 
> 6> 启动server_product会看到控制台有
> 	Fetching config from server at : http://R9LOMLJ7ILIFB69:9100/，
> 	就是从server_config拿值的，然后server_config又是从git上拿值。
>     
> 7> 步骤：
> 	1、修改配置文件名为bootstrap.yml
> 	2、修改配置文件内容
> 	3、增加依赖，所有config-client都加该依赖
>     
> 8、为什么使用config server
> 	统一管理，动态刷新配置
> 	需要webhook，钩子函数，js中的回调函数
>     
> 9、配置中心流程
> 	1> 读取bootstrap.yml中的注册中心，得到注册中心服务信息
> 	2> 再到注册中心，获取git中的配置信息
> ```

#### 4、遗留问题，下节解决

> ```python
> 我们通过gitee的页面，进行配置信息的更改管理，但是我们更改了之后，config-server并不能感知到，自然下面一层的所有微服务，也不能及时去拉取更新后的信息。
> 
> 目前的状况，server_product和server_order_feign如果重启，是可以从server_config拉取最新配置的，遗留问题就是解决：是否不重启各微服务，也可以让他们从配置中心拉取最新的配置信息。
> 
> 解决方法：
> 	消息总线Bus的单播和广播
> ```

#### 5、所有项目改造为配置中心

> #### 实战步骤
>
> ```python
> 1> git里面新增对应项目的配置文件，都要添加下面的配置
>     #服务的名称  
>     #注* 服务的名称在bootstrap里面配置，配合profile定为git配置文件名称
>     #注* 这个是为了bus消息总线的配置
>     spring:
>         rabbitmq:
>             host: localhost
>             port: 5672
>             username: guest
>             password: guest
> 
>     #暴露全部的监控信息
>     management:
>         endpoints:
>             web:
>                 exposure:
>                     include: "*"
>                         
> 2> 项目里面添加maven依赖
>     <!--配置中心客户端-->
>     <dependency>
>         <groupId>org.springframework.cloud</groupId>
>         <artifactId>spring-cloud-config-client</artifactId>
>     </dependency>
> 
>     <!--Bus+actuator消息总线-->
>     <dependency>
>         <groupId>org.springframework.boot</groupId>
>         <artifactId>spring-boot-starter-actuator</artifactId>
>     </dependency>
> 
>     <dependency>
>         <groupId>org.springframework.cloud</groupId>
>         <artifactId>spring-cloud-starter-bus-amqp</artifactId>
>     </dependency>
> 3> 修改application.properties为bootstrap.yml 并拷贝配置文件
> 	注* bootstrap中只保留两个配置项，剩下的都放在git中
>     #指定注册中心地址
>     eureka:
>         client:
>             serviceUrl:
>                 defaultZone: http://localhost:8761/eureka/
> 
>     #执行配置中心的对心位置
>     spring:
>         application:
>             name: order-service
>         #指定从哪个配置中心读取
>         cloud:
>             config:
>                 discovery:
>                     service-id: CONFIG-SERVER
>                     enabled: true
>                 profile: test
>                     
> 4> 各个项目启动顺序
>     1）注册中心
>     2）配置中心
>     3）对应的服务：商品服务、订单服务。。。
>     4）启动网关
> ```
>
> #### 记录
>
> ```python
> 1> 将git上相同应用的配置，只留一份，比如-dev和-pro，只留-dev。目前是三个应用有三个配置文件
> 2> server_order_feign的服务名称需要改了，原来是order-service-feign，但是从git上读取配置文件信	息，文件命名是有规范的，所以改为order-service，对应网关服务中的配置信息，改为：
> 	order-service: /apizuul/order/**，而不是order-service-feign
> 3> 记得改完配置信息之后，要都加入config-client的jar包，否则server.port在git上配置，服务启动8080了
> ```