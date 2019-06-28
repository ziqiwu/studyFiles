### 不记文档，白忙一场

------

#### *版本*

> ```python
> SpringBoot2.x
> elasticsearch5.6.x
> ```

#### 0、搜索框架es基本介绍

> #### 简介
>
> ```python
> 1> 简介：通过京东电商 介绍什么是搜索引擎，和开源搜索框架ElasticSearch6.x新特性介绍
> 2> 前言：介绍ES的主要特点和使用场景，新特性讲解
> 3> 数据量很大的时候，不能使用mysql的like来查询的原因：
> 	mysql：like 模糊，性能问题，like也不能使用索引
> 4> 常用的企业级搜索框架
> 	solr:针对企业，GB级别
> 	elasticsearch：针对数据量特别大，PB,TB
> 	注* 这两个都底层都是用lucene编写的
> 		1、纯java开发，springboot使用，5.6版本
> 		2、es升级4->5版本，改动大，但是5版本后，改动不大
> 		3、springboot的pom依赖，我们要用data，但是springboot整合elasticsearch只到5.6版本，所以			我们先用5.6，等什么时候springboot整合完了6.x版本，我们再用6.x版本
> ```
>
> #### elasticSearch主要特点
>
> ```python
> 1、特点：全文检索，结构化检索，数据统计、分析，接近实时处理，分布式搜索(可部署数百台服务器)，处理PB	级别的数据，搜索纠错，自动完成
> 2、使用场景：日志搜索，数据聚合，数据监控，报表统计分析
> 3、国内外使用者：维基百科，Stack Overflow，GitHub
> ```
>
> #### elasticSearch新特性讲解
>
> ```python
> 1、6.2.x版本基于Lucene 7.x，更快，性能进一步提升,对应的序列化组件，升级到Jackson 2.8
> 	注* elasticsearch和mysql在一些概念上的区别：
> 		mysql： database   table                 rocord
> 		es   ： index	  type（只能存在一个)    document
> 
> 2、推荐使用5.0版本推出的Java REST/HTTP客户端，依赖少，比Transport使用更方便，在基准测试中，性能并	不输于Transport客户端，在5.0到6.0版本中，每次有对应的API更新, 文档中也说明，推荐使用这种方式进行	开发使用,所有可用节点间的负载均衡。在节点故障和特定响应代码的情况下进行故障转移,失败的连接处罚（失	败的节点是否重试取决于失败的连续次数;失败的失败次数越多，客户端在再次尝试同一节点之前等待的时间越   长）
> 3、(重要)不再支持一个索引库里面多个type，6.x版本已经禁止一个index里面多个type，所以一个index索引库	只能存在1个type
> ```
>
> #### 官方文档
>
> ```python
> 1、6.0更新特性
> 	https://www.elastic.co/guide/en/elasticsearch/reference/6.0/release-notes-					6.0.0.html#breaking-java-6.0.0
> 2、6.1更新特性 
> 	https://www.elastic.co/guide/en/elasticsearch/reference/6.1/release-notes-6.1.0.html
> ```

#### 1、下载安装

> #### 前提
>
> ```python
> 配置JDK1.8 -- 详情见linux 软件安装 JDK
> 官网：https://www.elastic.co/products/elasticsearch
> ```
>
> #### 下载安装
>
> ```python
> 方法1：官网下载安装包，上传到服务器
>     1、https://www.elastic.co/
>     2、点击download
>     3、点击elasticsearch
>     4、在最新的版本下面找到past version
> 方法2：wget下载安装包
> 	使用wget 下载elasticsearch安装包
> 	wget  https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.6.8.tar.gz
> ```
>
> #### 外网访问配置	
>
> ```python
> config目录下面elasticsearch.yml
> 修改为 network.host: 0.0.0.0
> ```
>
> #### 常见错误
>
> ```python
> 备注：
> 	常见配置问题资料：https://www.jianshu.com/p/c5d6ec0f35e0
> 配置es出现相关问题处理（阿里云、腾讯云，亚马逊云安装问题集合）：
> 1、问题一
> 	Java HotSpot(TM) 64-Bit Server VM warning: INFO: os::commit_memory(0x00000000c5330000, 		986513408, 0) failed; error='Cannot allocate memory' (errno=12)
> 	#
> 	# There is insufficient memory for the Java Runtime Environment to continue.
> 	# Native memory allocation (mmap) failed to map 986513408 bytes for committing reserved 	memory.
> 	# An error report file with more information is saved as:
> 	# /usr/local/software/temp/elasticsearch-6.2.2/hs_err_pid1912.log
> 	
>     解决：内存不够，购买阿里云的机器可以动态增加内存
> 2、问题二
> 	[root@iZwz95j86y235aroi85ht0Z bin]# ./elasticsearch
> 	[2018-02-22T20:14:04,870][WARN ][o.e.b.ElasticsearchUncaughtExceptionHandler] [] 			uncaught exception in thread [main] org.elasticsearch.bootstrap.StartupException: 
>         java.lang.RuntimeException: can not run elasticsearch as root
> 		at org.elasticsearch.bootstrap.Elasticsearch.init(Elasticsearch.java:125) ~				[elasticsearch-6.2.2.jar:6.2.2]
> 		at org.elasticsearch.bootstrap.Elasticsearch.execute(Elasticsearch.java:112) ~			[elasticsearch-6.2.2.jar:6.2.2] at 										                org.elasticsearch.cli.EnvironmentAwareCommand.execute
>         (EnvironmentAwareCommand.java:86) ~[elasticsearch-6.2.2.jar:6.2.2]
> 		at org.elasticsearch.cli.Command.mainWithoutErrorHandling(Command.java:124) ~			[elasticsearch-cli-6.2.2.jar:6.2.2]
> 		
>         解决：用非root用户
> 			添加用户：useradd -m 用户名  然后设置密码  passwd 用户名
> 3、问题三
> 	./elasticsearch
> 	Exception in thread "main" java.nio.file.AccessDeniedException: 			               /usr/local/software/temp/elasticsearch-6.2.2/config/jvm.options
> 	
>     解决：权限不够 chmod 777 -R 当前es目录
> ```
>
> #### 新错误1
>
> ```python
> [qiwu@iz2ze82l26n5rq314e106gz bin]$ ./elasticsearch ../config/elasticsearch.yml 
> Exception in thread "main" 2019-03-24 22:55:36,514 main ERROR No log4j2 configuration file found. Using default configuration: logging only errors to the console. Set system property 'log4j2.debug' to show Log4j2 internal initialization logging.
> 2019-03-24 22:55:36,623 main ERROR Could not register mbeans java.security.AccessControlException: access denied ("javax.management.MBeanTrustPermission" "register")
> 	at java.security.AccessControlContext.checkPermission(AccessControlContext.java:472)
> 	at java.lang.SecurityManager.checkPermission(SecurityManager.java:585)
> 	at com.sun.jmx.interceptor.DefaultMBeanServerInterceptor.checkMBeanTrustPermission(DefaultMBeanServerInterceptor.java:1848)
> 	at com.sun.jmx.interceptor.DefaultMBeanServerInterceptor.registerMBean(DefaultMBeanServerInterceptor.java:322)
> 	at com.sun.jmx.mbeanserver.JmxMBeanServer.registerMBean(JmxMBeanServer.java:522)
> 	at org.apache.logging.log4j.core.jmx.Server.register(Server.java:389)
> 	at org.apache.logging.log4j.core.jmx.Server.reregisterMBeansAfterReconfigure(Server.java:167)
> 	at org.apache.logging.log4j.core.jmx.Server.reregisterMBeansAfterReconfigure(Server.java:140)
> 	at org.apache.logging.log4j.core.LoggerContext.setConfiguration(LoggerContext.java:556)
> 	at org.apache.logging.log4j.core.LoggerContext.reconfigure(LoggerContext.java:617)
> 	at org.apache.logging.log4j.core.LoggerContext.reconfigure(LoggerContext.java:634)
> 	at org.apache.logging.log4j.core.LoggerContext.start(LoggerContext.java:229)
> 	at org.apache.logging.log4j.core.impl.Log4jContextFactory.getContext(Log4jContextFactory.java:242)
> 	at org.apache.logging.log4j.core.impl.Log4jContextFactory.getContext(Log4jContextFactory.java:45)
> 	at org.apache.logging.log4j.LogManager.getContext(LogManager.java:174)
> 	at org.apache.logging.log4j.LogManager.getLogger(LogManager.java:648)
> 	at org.elasticsearch.common.logging.ESLoggerFactory.getLogger(ESLoggerFactory.java:54)
> 	at org.elasticsearch.common.logging.ESLoggerFactory.getLogger(ESLoggerFactory.java:62)
> 	at org.elasticsearch.common.logging.Loggers.getLogger(Loggers.java:101)
> 	at org.elasticsearch.ExceptionsHelper.<clinit>(ExceptionsHelper.java:46)
> 	at org.elasticsearch.ElasticsearchException.toString(ElasticsearchException.java:663)
> 	at java.lang.String.valueOf(String.java:2994)
> 	at java.io.PrintStream.println(PrintStream.java:821)
> 	at java.lang.Throwable$WrappedPrintStream.println(Throwable.java:748)
> 	at java.lang.Throwable.printStackTrace(Throwable.java:655)
> 	at java.lang.Throwable.printStackTrace(Throwable.java:643)
> 	at java.lang.ThreadGroup.uncaughtException(ThreadGroup.java:1061)
> 	at java.lang.ThreadGroup.uncaughtException(ThreadGroup.java:1052)
> 	at java.lang.Thread.dispatchUncaughtException(Thread.java:1959)
> 
> SettingsException[Failed to load settings from /usr/local/elasticsearch/elasticsearch-5.6.8/config/elasticsearch.yml]; nested: AccessDeniedException[/usr/local/elasticsearch/elasticsearch-5.6.8/config/elasticsearch.yml];
> 	at org.elasticsearch.node.InternalSettingsPreparer.prepareEnvironment(InternalSettingsPreparer.java:102)
> 	at org.elasticsearch.cli.EnvironmentAwareCommand.createEnv(EnvironmentAwareCommand.java:75)
> 	at org.elasticsearch.cli.EnvironmentAwareCommand.execute(EnvironmentAwareCommand.java:70)
> 	at org.elasticsearch.cli.Command.mainWithoutErrorHandling(Command.java:134)
> 	at org.elasticsearch.cli.Command.main(Command.java:90)
> 	at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:91)
> 	at org.elasticsearch.bootstrap.Elasticsearch.main(Elasticsearch.java:84)
> Caused by: java.nio.file.AccessDeniedException: /usr/local/elasticsearch/elasticsearch-5.6.8/config/elasticsearch.yml
> 	at sun.nio.fs.UnixException.translateToIOException(UnixException.java:84)
> 	at sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:102)
> 	at sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:107)
> 	at sun.nio.fs.UnixFileSystemProvider.newByteChannel(UnixFileSystemProvider.java:214)
> 	at java.nio.file.Files.newByteChannel(Files.java:361)
> 	at java.nio.file.Files.newByteChannel(Files.java:407)
> 	at java.nio.file.spi.FileSystemProvider.newInputStream(FileSystemProvider.java:384)
> 	at java.nio.file.Files.newInputStream(Files.java:152)
> 	at org.elasticsearch.common.settings.Settings$Builder.loadFromPath(Settings.java:1039)
> 	at org.elasticsearch.node.InternalSettingsPreparer.prepareEnvironment(InternalSettingsPreparer.java:100)
> 	... 6 more
> 
>     
> 解决：
> 	1、创建新用户
> 	2、把整个安装目录的chown -R qiwu /usr/local/elasticsearch/elasticsearch-5.6.8
> 	3、修改配置项
> 		vi /usr/local/elasticsearch/config/elasticsearch.yml
> 		network.host:0.0.0.0 #可以让其它ip也能访问
> 		http.port: 9200 #端口
> 解决：https://blog.csdn.net/u010189918/article/details/54632143
> ```
>
> #### 新错误2
>
> ```python
> 错误：
> 	max virtual memory areas vm.max_map_count [65530]is too low, increase to at least 		[262144]
> 解决：
> 	https://blog.csdn.net/qq_21387171/article/details/53577115
> ```
>
> #### 新错误3
>
> ```python
> 错误：
> 	max file descriptors [65535] for elasticsearchprocess is too low, increase to at least 		[65536]
> 解决：
> 	https://blog.csdn.net/liyantianmin/article/details/81589795
> ```
>
> #### 新错误4 -- 成功启动，但是访问错误
>
> ```python
> [qiwu@iz2ze82l26n5rq314e106gz bin]$ ./elasticsearch
> [2019-03-24T23:19:09,714][INFO ][o.e.n.Node               ] [] initializing ...
> [2019-03-24T23:19:09,824][INFO ][o.e.e.NodeEnvironment    ] [PSIf5YK] using [1] data paths, mounts [[/ (rootfs)]], net usable_space [34gb], net total_space [39.2gb], spins? [unknown], types [rootfs]
> [2019-03-24T23:19:09,824][INFO ][o.e.e.NodeEnvironment    ] [PSIf5YK] heap size [1015.6mb], compressed ordinary object pointers [true]
> [2019-03-24T23:19:09,825][INFO ][o.e.n.Node               ] node name [PSIf5YK] derived from node ID [PSIf5YKoTYGMWT-OiYmljA]; set [node.name] to override
> [2019-03-24T23:19:09,826][INFO ][o.e.n.Node               ] version[5.6.8], pid[1724], build[688ecce/2018-02-16T16:46:30.010Z], OS[Linux/3.10.0-693.2.2.el7.x86_64/amd64], JVM[Oracle Corporation/Java HotSpot(TM) 64-Bit Server VM/1.8.0_192/25.192-b12]
> [2019-03-24T23:19:09,826][INFO ][o.e.n.Node               ] JVM arguments [-Xms1g, -Xmx1g, -XX:+UseConcMarkSweepGC, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -Djdk.io.permissionsUseCanonicalPath=true, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Dlog4j.skipJansi=true, -XX:+HeapDumpOnOutOfMemoryError, -Des.path.home=/usr/local/elasticsearch/elasticsearch-5.6.8]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [aggs-matrix-stats]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [ingest-common]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [lang-expression]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [lang-groovy]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [lang-mustache]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [lang-painless]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [parent-join]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [percolator]
> [2019-03-24T23:19:11,458][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [reindex]
> [2019-03-24T23:19:11,459][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [transport-netty3]
> [2019-03-24T23:19:11,459][INFO ][o.e.p.PluginsService     ] [PSIf5YK] loaded module [transport-netty4]
> [2019-03-24T23:19:11,459][INFO ][o.e.p.PluginsService     ] [PSIf5YK] no plugins loaded
> [2019-03-24T23:19:14,333][INFO ][o.e.d.DiscoveryModule    ] [PSIf5YK] using discovery type [zen]
> [2019-03-24T23:19:15,307][INFO ][o.e.n.Node               ] initialized
> [2019-03-24T23:19:15,308][INFO ][o.e.n.Node               ] [PSIf5YK] starting ...
> [2019-03-24T23:19:15,571][INFO ][o.e.t.TransportService   ] [PSIf5YK] publish_address {172.17.237.103:9300}, bound_addresses {0.0.0.0:9300}
> [2019-03-24T23:19:15,581][INFO ][o.e.b.BootstrapChecks    ] [PSIf5YK] bound or publishing to a non-loopback address, enforcing bootstrap checks
> [2019-03-24T23:19:18,698][INFO ][o.e.c.s.ClusterService   ] [PSIf5YK] new_master {PSIf5YK}{PSIf5YKoTYGMWT-OiYmljA}{bTb_pQv4SdWbcNNCHyMD_A}{172.17.237.103}{172.17.237.103:9300}, reason: zen-disco-elected-as-master ([0] nodes joined)
> [2019-03-24T23:19:18,767][INFO ][o.e.h.n.Netty4HttpServerTransport] [PSIf5YK] publish_address {172.17.237.103:9200}, bound_addresses {0.0.0.0:9200}
> [2019-03-24T23:19:18,767][INFO ][o.e.n.Node               ] [PSIf5YK] started
> [2019-03-24T23:19:18,779][INFO ][o.e.g.GatewayService     ] [PSIf5YK] recovered [0] indices into cluster_state
> 
> 
> 错误：
> 	但是访问：http://39.105.32.104:9200/失败，是空白页面   
> 解决：
> 	开放aliyun的9200端口
> 	开放CentOS7的9200端口
> ```
> #### 测试
>
> ```python
> 使用Postman
> 1> 访问：http://39.105.32.104:9200/
> 2> 访问：http://39.105.32.104:9200/_cat/health?v  -- 集群健康状态检查
> ```

#### 2、简单使用

> ```python
> 1> 创建索引：http://39.105.32.104:9200/test_index?pretty -- Put请求方式
> 	出现："acknowledged": true表示成功！
> 2> 查看索引：http://39.105.32.104:9200/_cat/indices?v
> 3> 插入数据：http://39.105.32.104:9200/test_index/external/1?pretty --Put请求方式
>         Postman --> Body --> 输入{"name":"guozi"} --> send --> 查看返回的信息pretty
>         --> 可以看到"created": true
> 	其余信息：
> 		"_index": "test_index",  -- 相当于数据库
>     	"_type": "external",   --相当于表
>     	"_id": "1",   --相当于主键
> 4> 查看数据：http://39.105.32.104:9200/test_index/external/1?pretty --Get请求方式
>         注* 和插入数据的URL一模一样，只是请求方式变为了Get
> ```

#### 3、springboot整合

> #### Spring Data Elasticsearch文档地址
>
> ```python
> https://docs.spring.io/spring-data/elasticsearch/docs/3.0.6.RELEASE/reference/html/
> ```
>
> #### 版本说明：SpringBoot整合elasticsearch
>
> ```python
> https://github.com/spring-projects/spring-data-elasticsearch/wiki/Spring-Data-Elasticsearch---Spring-Boot---version-matrix
> ```
>
> #### QueryBuilder使用的官方说明
>
> ```python
> https://www.elastic.co/guide/en/elasticsearch/client/java-api/1.3/query-dsl-			queries.html
> ```
>
> #### 整合步骤
>
> ```python
> 1、添加maven依赖					
> 	<dependency>  
> 		<groupId>org.springframework.boot</groupId>  
> 		<artifactId>spring-boot-starter-data-elasticsearch</artifactId>  
> 	</dependency>  
> 	注意：版本号，参考上一个版本说明
> 2、新建实体对象article
> 	1> 加上类注解 @Document(indexName = "blog", type = "article")
> 	2> 实体类表示document，注解是该document属于哪个index(相当于数据库)，哪个type(相当于表)
> 3、接口继承ElasticSearchRepository,里面有很多默认实现
> 	注意点：索引名称记得小写，类属性名称也要小写
> 4、配置文件：
> 	注* 找的步骤：(官方文档配置)
>         1> https://spring.io/
>         2> projects
>         3> springboot
>         4> Learn
>         5> Reference Doc
>         6> 全文检索spring.data.elasticsearch
> 	配置信息示例：
>         spring.data.elasticsearch.cluster-name=elasticsearch 
>         spring.data.elasticsearch.cluster-nodes=localhost:9300 
>         spring.data.elasticsearch.repositories.enabled=true 
> 5、QueryBuilder使用
> 	官方文档地址：	
> 		https://www.elastic.co/guide/en/elasticsearch/client/java-api/1.3/query-dsl-			queries.html
> 	使用：
> 		//单个匹配，搜索name为jack的文档  
> 		QueryBuilder queryBuilder = QueryBuilders.matchQuery("title", "搜"); 
> 6、查看es数据
> 	查看索引信息：http://localhost:9200/_cat/indices?v
> 	查看某个索引库结构：http://localhost:9200/blog
> 	查看某个对象：http://localhost:9200/blog/article/1
> ```
>
> #### 实战如下：
>
> ```python
> 1、添加maven依赖：没什么好说的
> 2、新建实体对象article
> 	@Document(indexName = "blog", type = "article")
> 	public class Article implements Serializable {
>         private static final long serialVersionUID=1;
> 
>         private long id;
>         private String title;
>         private String summary;
>         private String content;
>         private int pv;
> 	    
>         ...属性的get/set方法  
>     }
> 3、接口继承ElasticSearchRepository,里面有很多默认实现
>     @Component
>     public interface ArticleRepository extends ElasticsearchRepository<Article,Long> {
>     }
> 4、配置文件(application.yml):
>     spring:
>       data:
>         elasticsearch:
>           # 在conf/elasticsearch.yml中有此属性
>           cluster-name: guozi
>           # es的http端口是9200，但是java连接端口默认是9300
>           cluster-nodes: 39.105.32.104:9300
>           repositories:
>             enabled: true
> 5、QueryBuilder使用
> 	@RestController
>     @RequestMapping("/api/v1/article")
>     public class ArticleController {
>         @Autowired
>         private ArticleRepository articleRepository;
> 
>         //注意：如果没有save方法的
>         @GetMapping("save")
>         public Object save(long id,String title){
>             Article article = new Article();
>             article.setId(id);
>             article.setPv(124);
>             article.setContent("今天天气风和日丽，万里无云，外出踏春赏景的绝佳天气");
>             article.setTitle(title);
>             article.setSummary("天气");
>             articleRepository.save(article);
>             return JsonData.buildSuccess();
>         }
> 
>         @GetMapping("search")
>         public Object search(String title){
>             //QueryBuilder queryBuilder = QueryBuilders.matchAllQuery(); //搜索全部文档
>             QueryBuilder queryBuilder = QueryBuilders.matchQuery("title", title);
>             Iterable<Article> list =  articleRepository.search(queryBuilder);
>             return JsonData.buildSuccess(list);
>         }
>     }
> 	#加入数据：
> 		http://localhost:8888/api/v1/article/save?username=guozi&id=3&title=美食节目
> 	#查询数据：
>     	http://localhost:8888/api/v1/article/search?username=guozi&title=美食
> ```
>
> #### 笔记
>
> ```python
> 1、elasticsearch和spring-data是两个不同的开发团队在维护，所以版本肯定不能保持一致。
> 	因为需要es的团队在es版本发布到maven仓库之后，spring-data团队再进行开发。
> ```
> #### java连接报错原因
>
> ```python 
> 1、保证telnet port可以通
> 	不通的话，apliyun没有开，或者linux防火墙没有开
> 2、es版本和spring-data版本没有对应上
> 3、es配置文件中cluster-name问题，
> 4、es的http端口是9200，但是java连接端口默认是9300
> ```
>
> #### 我的错误原因
>
> ```python
> 1、打开aliyun的9300端口，打开linux防火墙的9300端口
> 2、配置文件，修改cluster-name，没啥用
> 3、修改ip地址为0.0.0.0
> 4、springboot的application.yml中：
> 	cluster-name: guozi   -- 注意是自己改的cluster-name
> 	cluster-nodes: 39.105.32.104:9300   -- 注意是公网IP，注意是9300端口
> 5、之前只是测试http://39.105.32.104:9200/health?v等，所以只打开了9200端口
> 6、明天尝试：
> 	把es配置文件的ip改为，服务器公网ip和私网ip
> ```











