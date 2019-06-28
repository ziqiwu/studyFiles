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



