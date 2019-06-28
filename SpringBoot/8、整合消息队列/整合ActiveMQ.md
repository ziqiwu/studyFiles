### 不记文档，白忙一场

------

#### *版本*

> ```python
> 1、ActiveMQ 5.x
> ```

#### 0、介绍ActiveMQ5.x

> ```python
> 特点：
> 	1）支持来自Java，C，C ++，C＃，Ruby，Perl，Python，PHP的各种跨语言客户端和协议
> 	2）支持许多高级功能，如消息组，虚拟目标，通配符和复合目标
> 	3) 完全支持JMS 1.1和J2EE 1.4，支持瞬态，持久，事务和XA消息
> 	4) Spring支持，ActiveMQ可以轻松嵌入到Spring应用程序中，并使用Spring的XML配置机制进行配置
> 	5) 支持在流行的J2EE服务器（如TomEE，Geronimo，JBoss，GlassFish和WebLogic）中进行测试
> 	6) 使用JDBC和高性能日志支持非常快速的持久化
> 			...
> 快速开始：http://activemq.apache.org/getting-started.html
> ```

#### 1、下载安装

> ```python
> 0、下载地址：http://activemq.apache.org/activemq-5153-release.html
> 1、在官网的Download Link下的可点击的apache-activemq-5.15.3-bin.tar.gz
> 2、右键 --> Copy link address
> 3、在linux中执行wget xxxx
> 4、tar -zxvf 解压
> 5、cd bin  --> ./activemq start   -- 注* 该启动命令是需要jdk环境的
> 6、http://127.0.0.1:8161/  -- 注* 访问之前需要开放aliyun和linux的8161端口号
> 7、用户名和密码默认都是admin
> ```
>

#### 2、前提必做

> ```python
> 0、安装了jdk -- activemq的运行是依赖于jdk环境的
> 1、打开aliyun的8161的端口号
> 2、打开linux的8161的端口号
> ```

#### 3、管理面板

> ```python
> 面板：	
>     Name：队列名称。
>     Number Of Pending Messages：等待消费的消息个数。
>     Number Of Consumers：当前连接的消费者数目
>     Messages Enqueued：进入队列的消息总个数，包括出队列的和待消费的，这个数量只增不减。
>     Messages Dequeued：已经消费的消息数量。
> ```

#### 4、官方案例集合

> ```python
> https://github.com/spring-projects/spring-boot/tree/master/spring-boot-samples
> ```

#### 5、连接池简介

> ```python
> ActiveMQ需要连接
> Redis需要连接
> MySQL需要连接，
> 但是创建连接时很耗资源的，所以他们都有各自的连接池，原理都是一样的。
> ```

#### 6、整合之点对点消息

> #### 释义
>
> ```python
> 点对点(p2p)：一个消息只能被一个消费者消费。
> ```
>
> #### 官方网址
>
> ```python
> https://docs.spring.io/spring-boot/docs/2.1.0.BUILD-SNAPSHOT/reference/htmlsingle/#boot-features-activemq
> ```
>
> #### 整合步骤
>
> ```python
> 配置方法：
> 	1> 加入依赖
> 		<!-- 整合消息队列ActiveMQ -->
> 		<dependency>  
>             <groupId>org.springframework.boot</groupId>  
>             <artifactId>spring-boot-starter-activemq</artifactId>  
>         </dependency>  
>         
>         <!-- 如果配置线程池则加入 -->
>         <dependency>  
>             <groupId>org.apache.activemq</groupId>  
>             <artifactId>activemq-pool</artifactId>  
>         </dependency>
> 	2> 配置application.properties
> 		#整合jms测试，安装在别的机器，防火墙和端口号记得开放
> 		spring.activemq.broker-url=tcp://127.0.0.1:61616
> 
> 		#集群配置
> 		#spring.activemq.broker-url=failover:(tcp://localhost:61616,tcp://localhost:61617)
> 
> 		spring.activemq.user=admin
> 		spring.activemq.password=admin
> 		#下列配置要增加依赖
> 		spring.activemq.pool.enabled=true
> 		spring.activemq.pool.max-connections=100
> 	3> springboot启动类加@EnableJms，开启支持jms
> 	4> 编写生产者
> 	5> 编写消费者
> 实战如下：
> 	1> 加入依赖
> 		没什么好说的
> 	2> 配置application.properties
> 		注* 8161是activemq的http默认端口，61616是activemq的tcp的默认端口。
> 			就像9200是elasticsearch的http默认端口，9300是java连接的默认端口一样。
> 	3> 启动类开启支持jms
> 		@SpringBootApplication
> 		@EnableJms //开启支持Jms
> 		public class SpringbootDemoApplication {
>             public static void main(String[] args) {
>                 SpringApplication.run(SpringbootDemoApplication.class, args);
>             }
> 		}
> 	4> 编写生产者
> 		1、controller类
>             @RestController
>             @RequestMapping("/api")
>             public class ActiveMQController {
>                 @Autowired
>                 private ProducerService producerService;
>                 //存入order.queue消息队列
>                 @GetMapping("/v1/activemq/produce")
>                 public Object produceMQ(String msg) {
>                     Destination destination = new ActiveMQQueue("order.queue");
>                     producerService.sendMessage(destination,msg);
>                     System.out.println("---order.queue入列消息为："+msg);
>                     return JsonData.buildSuccess(msg);
>                 }
>             }
>     
> 		2、service类
>             @Service
>             public class ProducerServiceImpl implements ProducerService {
>                 @Autowired
>                 private JmsMessagingTemplate jmsTemplate;
>                 @Override
>                 public void sendMessage(Destination destination, String msg) {
>                     jmsTemplate.convertAndSend(destination,msg);
>                 }
>             }
> 	5、编写消费者
> 		@Service
> 		public class ConsumerServiceImpl implements ConsumerService {
>             @JmsListener(destination = "order.queue")
>             public void consumerOrder(String text) {
>                 System.out.println("----order.queue出列的消息为："+text);
>             }
> 		}
> ```
>
> #### 注意
>
> ```python
> 1> 点对点，消费者可以是多个，相同的代码，赋值两份，都加@JmsListener(destination = 				"order.queue")，则可以快速消费消息队列中的数据，达到分布式的效果。
> 2> application.yml中配置spring.activemq.pool.enabled=true会报错，配置为false，则不再报错。原因		未知。
> ```

#### 7、整合之发布订阅消息

> #### 释义
>
> ```python
> 1> 发布订阅(pub/sub)：一个消息可以被多个消费者消费。
> 	pub: publish
> 	sub: subscribe
> 2> springboot默认只支持点对点
> 3> 默认不能同时支持两种模式，需要修改它的容器工厂containerFactory
> ```
>
> #### 整合步骤 -- 使用发布订阅
>
> ```python
> 前言
> 	配置了发布订阅，则点对点不能再使用。存入队列中的消息，并不能被消费掉，而是停在了队列中
> 配置方法
> 	1> 加入依赖 -- 没有变动
> 	2> application.yml开启对发布订阅的支持
> 	3> 启动类加注解 -- 没有变动
> 	4> 编写发布者
> 	5> 编写订阅者
> 实战如下
> 	1> 加入依赖 -- 没啥好说
> 	2> application.yml增加支持发布订阅的配置
> 		spring.jms.pub-sub-domain=true
> 	3> 启动类加注解 -- 没啥好说
> 	4> 编写发布者
> 		1、controller类
>             @RestController
>             @RequestMapping("/api")
>             public class ActiveMQController {
>                 @Autowired
>                 private ProducerService producerService;
>                 @GetMapping("/v1/activemq/video")
>                 public Object produceMQVideo(String msg) {
>                     producerService.publishMessage(msg);
>                     System.out.println("---发布消息："+msg);
>                     return JsonData.buildSuccess(msg);
>                 }
>             }
> 		2、service类
>             @Service
>             public class ProducerServiceImpl implements ProducerService {
>                 @Autowired
>                 private JmsMessagingTemplate jmsTemplate;
>                 //默认的主题
>                 private static Topic topic = new ActiveMQTopic("video.topic");
>                 @Override
>                 public void publishMessage(String msg) {
>                     this.jmsTemplate.convertAndSend(this.topic,msg);
>                 }
>             }
> 	5> 编写订阅者
>         @Service
>         public class ConsumerServiceImpl implements ConsumerService {
>             @JmsListener(destination = "video.topic")
>             public void subscribeVideo1(String text) {
>                 System.out.println("-------订阅1："+text);
>             }
>             @JmsListener(destination = "video.topic")
>             public void subscribeVideo2(String text) {
>                 System.out.println("-------订阅2："+text);
>             }
>             @JmsListener(destination = "video.topic")
>             public void subscribeVideo3(String text) {
>                 System.out.println("-------订阅3："+text);
>             }
>         }
> ```
>
> #### 整合步骤 -- 同时使用发布订阅和点对点
>
> ```python
> 前言
> 	前提：springboot默认只支持点对点消息模式。
> 	原来的开启发布订阅消息模式的方法是，application中配置spring.jms.pub-sub-domain=true。
> 	现在改为：
> 		重新修改JmsListenerContainerFactory的方法，然后再消息订阅的方法配置上调用。
> 		具体为：
> 			1> @Bean
> 			   public JmsListenerContainerFactory<?> jmsListenerContainerTopic
> 			2> @JmsListener(destination = "video.topic",containerFactory = 							  "jmsListenerContainerTopic")
> 配置方法
>     1> 加入依赖 -- 没有变动
>     2> application.yml注释掉spring.jms.pub-sub-domain=true
>     3> 启动类加注解 -- 没有变动
>     4> 增加@Configure类，重写containerFactory方法
>     5> 编写发布者
>     6> 编写订阅者 -- 订阅者配置containerFactory="jmsListenerContainerTopic"
> 实战如下
> 	1> 加入依赖 
> 	2> application.yml注释掉spring.jms.pub-sub-domain=true
> 	3> 启动类加注解
> 	4> 增加@Configure类，重写containerFactory方法
>         @Configuration
>         public class ActiveMQConfig {
>             @Bean
>             public JmsListenerContainerFactory<?> jmsListenerContainerTopic(
>                 ConnectionFactory activeMQConnectionFactory) {
>                 DefaultJmsListenerContainerFactory bean = new                                                                               DefaultJmsListenerContainerFactory();
>                 bean.setPubSubDomain(true);
>                 bean.setConnectionFactory(activeMQConnectionFactory);
>                 return bean;
>             }
>         }
> 	5> 编写发布者 -- 没有改变
> 	6> 编写订阅者 -- 订阅者配置containerFactory="jmsListenerContainerTopic"
>         @Service
>         public class ConsumerServiceImpl implements ConsumerService {
>             @JmsListener(destination = "video.topic",containerFactory = 								"jmsListenerContainerTopic")
>             public void subscribeVideo1(String text) {
>                 System.out.println("-------订阅1："+text);
>             }
>             @JmsListener(destination = "video.topic",containerFactory = 								"jmsListenerContainerTopic")
>             public void subscribeVideo2(String text) {
>                 System.out.println("-------订阅2："+text);
>             }
>             @JmsListener(destination = "video.topic",containerFactory = 								"jmsListenerContainerTopic")
>             public void subscribeVideo3(String text) {
>                 System.out.println("-------订阅3："+text);
>             }
>         }
> ```
>
> #### 注意
>
> ```python
> 1> 默认消费者并不会消费订阅发布类型的消息，这是由于springboot默认采用的是p2p模式进行消息的监听修改	配置：spring.jms.pub-sub-domain=true
> 		
> 2> @JmsListener如果不指定独立的containerFactory的话是只能消费queue消息修改订阅者container：	    containerFactory="jmsListenerContainerTopic"
> ```



