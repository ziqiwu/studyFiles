### 不记文档，白忙一场

------

#### *版本*

> ```python
> RocketMQ4.x
> ```

#### 0、介绍RocketMQ4.x

> #### 简介
>
> ```python
> 简介：阿里开源消息队列 RocketMQ4.x介绍和新概念讲解
> 1、Apache RocketMQ作为阿里开源的一款高性能、高吞吐量的分布式消息中间件
> 2、特点
>     1）在高压下1毫秒内响应延迟超过99.6％。
>     2）适合金融类业务，高可用性跟踪和审计功能。
>     3）支持发布订阅模型，和点对点
>     4）支持拉pull和推push两种消息模式
>     5）单一队列百万消息
>     6）支持单master节点，多master节点，多master多slave节点
>     ...
> 3、概念
> 	Producer:消息生产者
> 	Producer Group:消息生产者组，发送同类消息的一个消息生产组
> 
> 	Consumer:消费者
> 	Consumer Group:消费同个消息的多个实例
> 
> 	Tag:标签，子主题（二级分类）,用于区分同一个主题下的不同业务的消息
> 
> 	Topic:主题
> 	Message：消息
> 	Broker：MQ程序，接收生产的消息，提供给消费者消费的程序
> 	Name Server：给生产和消费者提供路由信息，提供轻量级的服务发现和路由		
> ```
> #### 官网
>
> ```python
> 官网地址：http://rocketmq.apache.org/
> ```
>
> #### 学习资料
>
> ```python
> 1）http://jm.taobao.org/2017/01/12/rocketmq-quick-start-in-10-minutes/	--淘宝中间件干货
> 2）https://www.jianshu.com/p/453c6e7ff81c   -- 大神文章入门
> ```

#### 1、下载安装

> ```python
> 第一步：
> 	http://apache.org/ --> ctrl + F找rocketmq --> 可以定位到apache project list中点击进入官网
> 第二步：
> 	Getting started --> Download & Build from Release -->  download a binary release 
> 	--> Download the 4.4.0 release --> Binary
> 第三步：
> 	下载.zip --> 移入linux目录 --> yum install -y unzip zip安装压缩和解压命令
> 	--> unzip xx.zip
> 第四步：启动名称服务
> 	cd xx --> cd bin --> 
> 	nohup sh mqnamesrv &  （报错请参见整合RocketMQ报错）
> 		或者
> 	nohup ./mqnamesrv &
> 	注* 查看名称服务启动是否成功
> 		查看日志 tail -f nohup.out
> 		结尾：The Name Server boot success. serializeType=JSON 表示启动成功
> 第五步：启动broker
> 	nohup sh mqbroker -n 127.0.0.1:9876 &
> 		或者
> 	nohup ./mqbroker -n 127.0.0.1:9876 &
> 	注* 查看broker是否启动成功
> 		jps 或者 ps -ef
> 第六步：关闭两个服务
> 	cd bin --> 
> 	./mqshutdown namesrv
> 	./mqshutdown broker
> 		或者
> 	sh mqshutdown namesrv
> 	sh mqshutdown broker
> ```

#### 2、可视化控制台

> #### 简介
>
> ```python
> activemq有一个web式界面。
> rocketmq也提供了，但是默认不在对应的程序里面，需要进行额外的安装。
> ```
>
> #### 步骤
>
> ```python
> 1> 打开rocketmq-externals所在github地址
> 	https://github.com/apache/rocketmq-externals	
> 2> 找到对应的git下载地址
> 	clone or download点击即可找到
> 3> 利用git.exe将远程项目下载到本地
> 	进入powershell
> 	cd G:\Git2.7.2\Git --> cd bin --> 
>      .\git.exe https://github.com/apache/rocketmq-externals.git H:\desktop\self
> 	注* H:\desktop\self即使要下载到本地的地址
> 4> 快速打开整个项目源码
> 	选中整个项目包拖动刀sublime，可清晰看到整个目录结构
> 5> 打开rocketmq-console目录
> 	整个微服务中只有这部分是需要的
> 6> 修改部分配置文件，否则会报错
> 	1、application.properties
> 		rocketmq.config.namesrvAddr=39.105.32.104:9876
> 			注* ip是rocketmq所在服务器的公网，9876是rocketmq的broker启动时候定义的
> 				//nohup sh mqbroker -n 127.0.0.1:9876 &
>                   nohup sh bin/mqbroker -n localhost:9876 -c conf/broker.conf &
> 				否则会报错，详见下面的第11点信息
> 	2、pom.xml
> 		修改<rocketmq.version>4.4.0-SNAPSHOT</rocketmq.version>
> 		变为<rocketmq.version>4.4.0</rocketmq.version>
> 			注* 否则会报错，详见下面的第6点信息
> 7> mvn命令编译打包jar
> 	powershell进入rocketmq-console --> mvn clean package -Dmaven.test.skip=true
> 	--> 在该目录下会生成target目录，在其中可以找到对应jar包
> 	注* powershell中命令需变为mvn clean package '-Dmaven.test.skip=true'，详见下第5点
> 8> 开放端口号
> 	我再rocketmq部署服务器的Linux和aliyun开放了9876和10909两个端口
> 	注* 9876肯定需要开，10909不知道是否为必须，因为报错了不能连接到xxx:10909，详见11点
> 9> 启动该springboot项目
> 	运行java -jar xxxx.jar
> 10> 访问可视化控制页面
> 	访问地址：http://localhost:8080
> 	注* 启动日志中可知，该springboot项目默认端口号为8080
>     	当然可以修改application.properties中的server.port=8080进行端口修改
> ```
>
> #### 知识点+报错解决
>
> ```python
> 1> git clone命令指定下载目录
> 2> cd rocketmq-console  进入可以看到这就是一个maven工程
> 3> mvn 打包
> 4> 可以在sublime中进行快速查看项目目录结构
> 5> maven编译打包
> 	因为是springboot项目，当然是maven项目，所以可以用mvn命令来编译打包为jar、war包
> 	powershell下：
> 	mvn clean install package '-Dmaven.test.skip=true'
> 	cmd下：
>     mvn clean install package -Dmaven.test.skip=true
> 	来源：https://blog.csdn.net/wushengjun753/article/details/78973618
> 6> 报错：
> 	 Failed to execute goal on project rocketmq-console-ng: Could not resolve dependencies 		for project org.apache:rocketmq-console-ng:jar:1.0.0: The following artifacts could 	 not be resolved: org.apache.rocketmq:rocketmq-tools:jar:4.4.0-SNAPSHOT, 				 org.apache.rocketmq:rocketmq-namesrv:jar:4.4.0-SNAPSHOT, org.apache.rocketmq:rocketmq-		broker:jar:4.4.0-SNAPSHOT: Could not find artifact org.apache.rocketmq:rocketmq-		 tools:jar:4.4.0-SNAPSHOT -> [Help 1]
> 	解决：https://blog.csdn.net/qq_30051265/article/details/87621948
>     	<rocketmq.version>4.4.0-SNAPSHOT</rocketmq.version>声明的版本应改为4.4.0。
> 	分析：认真看报错，看到问题是maven打包的时候，不能下载对应的jar包。
> 7> 打包完成后，在target目录中会生成对应的jar包，本来就是springboot项目，docker部署，属于微服务。
> 	用java -jar运行
> 8> rocketmq.config.namesrvAddr=可以看到namesrvAddr的地址是空的
> 9> mvn clean package '-Dmaven.test.skip=true'第一次运行就生成了jar包
> 10> 我的做法，并没有把生成的rocketmq-console-nq.jar在linux上启动，而是在本地启动，那就涉及到一个	连接linux上rocketmq的问题，配置文件在applicaion.properties中。然后就需要打开Linux和aliyun
> 	的各自端口，端口号是9876。
> 11> org.apache.rocketmq.remoting.exception.RemotingConnectException: connect to 			<172.17.237.103:10909> failed
> 	这是由于跨域问题造成的。因为：
>     	rocketmq服务器部署在服务器上，rocketmq-console控制台在本地打开，所以存在跨域问题，解决方		法为：	https://blog.csdn.net/q258523454/article/details/82716027
> 	即：修改broker.conf新增一行brokerIP1=xx.xx.xx.xx  # 你的公网IP
>     	公网指的是rocketmq所在服务器的公网，我的是阿里云服务器公网
> 		nohup sh bin/mqbroker -n localhost:9876 -c conf/broker.conf &用修改后的配置文件启动
> 	备注：我还把10909端口号在Linux和aliyun上打开了，不知道是否为必要的步骤。
> ```

#### 3、整合之生产者

> #### 注意
>
> ```python
> 1> 生产者在连接broker，即连接rocketmq之前，需要先到nameserver拿对应的broker的连接信息，然后才能建	立连接。
> 2> @PostConstruct可以保证只调用一次
> ```
>
> #### 整合
>
> ```python
> 配置方法：
> 	1> 加入相关pom依赖
> 		<dependency>  
> 		    <groupId>org.apache.rocketmq</groupId>  
> 		    <artifactId>rocketmq-client</artifactId>  
> 		    <version>${rocketmq.version}</version>  
> 		</dependency>  
> 		<dependency>  
> 		    <groupId>org.apache.rocketmq</groupId>  
> 		    <artifactId>rocketmq-common</artifactId>  
> 		    <version>${rocketmq.version}</version>  
> 		</dependency>  
> 		注* 在pom.xml的
> 			<properties>
> 				<rocketmq.version>4.4.0</rocketmq.version>
> 			</properties>
> 	2> application.properties加入配置文件	
> 		# 消费者的组名
> 		apache.rocketmq.consumer.PushConsumer=orderConsumer
> 		# 生产者的组名
> 		apache.rocketmq.producer.producerGroup=Producer
> 		# NameServer地址
> 		apache.rocketmq.namesrvAddr=127.0.0.1:9876
> 		注* namesrvAddr中ip改为rocketmq所在服务器的公网ip
> 	3> 开发jms连接属性类
> 	4> 开发controller类进行生产者相关代码编写
> 实战如下：
> 	1> 加入相关pom依赖
> 	2> application.properties加入配置文件	
> 	3> 开发jms连接属性类
> 		/**
>          * jms 即连接信息
>          */
>         //增加注解，可以保证让Spring扫描到
>         @Service
>         public class MsgProducer {
> 		   //生产者的组名
>             @Value("${apache.rocketmq.producer.producerGroup}")
>             private String producerGroup;
> 		    
>             //NameServer 地址
>             @Value("${apache.rocketmq.namesrvAddr}")
>             private String namesrvAddr;
> 
>             private DefaultMQProducer producer ;
> 
>             public DefaultMQProducer getProducer(){
>                 return this.producer;
>             }
> 
>             //该注解可以保证只初始化一次
>             @PostConstruct
>             public void defaultMQProducer() {
>                 //生产者的组名
>                 producer = new DefaultMQProducer(producerGroup);
>                 //如过NameServer集群，指定NameServer地址，多个地址以 ; 隔开
>                 //如 producer.setNamesrvAddr("192.168.100.141:9876;192.168.100.142:9876;
>                 //                            192.168.100.149:9876");
>                 producer.setNamesrvAddr(namesrvAddr);
> 			   producer.setVipChannelEnabled(true);
>                 try {
> 				  //Producer对象在使用之前必须要调用start初始化，只能初始化一次
>                     producer.start();
>                 } catch (Exception e) {
>                     e.printStackTrace();
>                 }
>                 // producer.shutdown();  一般在应用上下文，关闭的时候进行关闭，用上下文监听器
>             }
>         }
> 	4> 开发controller类进行生产者相关代码编写
>         @RestController
>         @RequestMapping("/api/v1/rocketmq")
>         public class OrderController {
>             @Autowired
>             private MsgProducer msgProducer;
>             /**
>              * 功能描述：微信支付回调接口
>              * @param msg 支付信息
>              * @param tag 消息二级分类
>              * @return
>              */
>             @GetMapping("order")
>             public Object order(String msg, String tag) throws Exception {
>                 /**
>                  * 创建一个消息实例，包含 topic、tag 和 消息体
>                  */
>                 Message message = new Message("testTopic", tag, 											msg.getBytes(RemotingHelper.DEFAULT_CHARSET));
>                 SendResult result = msgProducer.getProducer().send(message);
>                 System.out.println("发送响应：MsgId:" + result.getMsgId() + "，发送状态:" + 					result.getSendStatus());
>                 return JsonData.buildSuccess();
>             }
>         }
> 	注* 测试地址
> 	http://localhost:8888/api/v1/rocketmq/order?username=guozi&msg=发布第7条数据&tag=第二分类
> ```
>
> #### 注意
>
> ```python
> 1> 报错RemotingTooMuchRequestException: sendDefaultImpl call timeout
> 	不能将信息存入队列中
>    1、网上解决办法：https://blog.csdn.net/wangmx1993328/article/details/81588217#RemotingTooMuchRequestException%3A%20sendDefaultImpl%20call%20timeout
> 	即关闭防火墙
>    2、我的解决办法
> 	将producer.setVipChannelEnabled(false);改为producer.setVipChannelEnabled(true);
> ```
>
> #### 疑问
>
> ```python
> 上面第三步，应该最好是放到上下文监听器中初始化和销毁，但是，我增加了之后，报错。删除，又对了，如下：
> @WebListener
> public class InitMQProducer implements ServletContextListener {
>     /**
>      * 生产者的组名
>      */
>     @Value("${apache.rocketmq.producer.producerGroup}")
>     private String producerGroup;
> 
>     /**
>      * NameServer 地址
>      */
>     @Value("${apache.rocketmq.namesrvAddr}")
>     private String namesrvAddr;
> 
>     private DefaultMQProducer producer ;
> 
>     public DefaultMQProducer getProducer(){
>         return this.producer;
>     }
>     @Override
>     public void contextInitialized(ServletContextEvent sce) {
>         System.out.println("--contextInit");
>         //生产者的组名
>         producer = new DefaultMQProducer(producerGroup);
>         producer.setNamesrvAddr(namesrvAddr);
>         producer.setVipChannelEnabled(true);
> 
>         try {
>             /**
>              * Producer对象在使用之前必须要调用start初始化，只能初始化一次
>              */
>             producer.start();
>         } catch (Exception e) {
>             e.printStackTrace();
>         }
>     }
> 
>     @Override
>     public void contextDestroyed(ServletContextEvent sce) {
>         System.out.println("--contextDestroy");
>         producer.shutdown();  //一般在应用上下文，关闭的时候进行关闭，用上下文监听器
>     }
> }
> 报错信息为：
> Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'articleController': Unsatisfied dependency expressed through field 'articleRepository'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'articleRepository': Cannot resolve reference to bean 'elasticsearchTemplate' while setting bean property 'elasticsearchOperations'; nested exception is org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'elasticsearchTemplate' defined in class path resource [org/springframework/boot/autoconfigure/data/elasticsearch/ElasticsearchDataAutoConfiguration.class]: Unsatisfied dependency expressed through method 'elasticsearchTemplate' parameter 0; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'elasticsearchClient' defined in class path resource [org/springframework/boot/autoconfigure/data/elasticsearch/ElasticsearchAutoConfiguration.class]: Bean instantiation via factory method failed; nested exception is org.springframework.beans.BeanInstantiationException: Failed to instantiate [org.elasticsearch.client.transport.TransportClient]: Factory method 'elasticsearchClient' threw exception; nested exception is java.lang.IllegalStateException: availableProcessors is already set to [4], rejecting [4]
>                                                 
>                                                 
> The web application [ROOT] appears to have started a thread named [AsyncAppender-Dispatcher-Thread-19] but has failed to stop it. This is very likely to create a memory leak. Stack trace of thread:
> ```

#### 4、整合之消费者

> #### java8的lanbda表达式
>
> ```python
> 我们一直在强调，如果要实现lambda表达式，那么必须有一个前提，这个前提就是接口里面的抽象方法只能够存在一个。所以为了严格这样的语法要求。可以使用函数式的接口定义。
> 来源：https://jingyan.baidu.com/article/eb9f7b6d569699869364e8b4.html
> ```
>
> #### 视频笔记
>
> ```python
> 问题：
> 		1、Caused by: org.apache.rocketmq.remoting.exception.RemotingConnectException: connect to <172.17.42.1:10911> failed 
> 
> 		2、com.alibaba.rocketmq.client.exception.MQClientException: Send [1] times, still failed, cost [1647]ms, Topic: TopicTest1, BrokersSent: [broker-a, null, null]
> 
> 		3、org.apache.rocketmq.client.exception.MQClientException: Send [3] times, still failed, cost [497]ms, Topic: TopicTest, BrokersSent: [chenyaowudeMacBook-Air.local, 	chenyaowudeMacBook-Air.local, chenyaowudeMacBook-Air.local]
> 		解决：多网卡问题处理
> 		1、设置producer:  producer.setVipChannelEnabled(false);
> 		2、编辑ROCKETMQ 配置文件：broker.conf（下列ip为自己的ip）
> 			namesrvAddr = 192.168.0.101:9876
> 			brokerIP1 = 192.168.0.101
> 
> 
> 
> 		4、DESC: service not available now, maybe disk full, CL:
> 		解决：修改启动脚本runbroker.sh，在里面增加一句话即可：		
> 		JAVA_OPT="${JAVA_OPT} -Drocketmq.broker.diskSpaceWarningLevelRatio=0.98"
> 		（磁盘保护的百分比设置成98%，只有磁盘空间使用率达到98%时才拒绝接收producer消息）
> 
> 
> 		常见问题处理：
> 			https://blog.csdn.net/sqzhao/article/details/54834761
> 			https://blog.csdn.net/mayifan0/article/details/67633729
> 			https://blog.csdn.net/a906423355/article/details/78192828
> ```
>
> #### 未完待续
>
> ```python
> 生产者可以正常塞入队列消息，消费者不能正常消费，控制台界面不知道如何使用。
> 以后，有机会，再深入了解解决。
> ```

#### 5、整合rocketmq集群

> ```python
> 以后，有机会，深入了解，部署集群使用
> https://blog.csdn.net/sqzhao/article/details/54834761 -- 含有集群部署的知识点
> ```

