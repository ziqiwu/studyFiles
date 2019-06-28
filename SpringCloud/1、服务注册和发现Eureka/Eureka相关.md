### 不记文档，白忙一场

------

#### ***前途未卜***

> ```python
> 学习原因：
> 	1> Eureka虽然官方不再维护了，但是一两年内还是主流的。
> 	2> 注册中心的迁移是非常简单容易的。我们的微服务中，都是一段配置，专门指向微服务，剩下的不改动。
> ```

#### 0、官方文档

> #### 步骤
>
> ```python
> 注* This section describes how to set up a Eureka server.
> https://cloud.spring.io --> 左侧目录选择Spring Cloud Netflix --> 选择Learn的tab页 -->
> 选择对应版本号的Reference Doc. --> 左侧目录选择Service Discovery:Eureka Server
> ```
>
> #### 一步到位
>
> ```python
> https://cloud.spring.io/spring-cloud-netflix/spring-cloud-netflix.html#spring-cloud-eureka-server
> ```

#### 1、创建项目

> #### 方法一：在线自动创建
>
> ```python
> https://start.spring.io/ --> Maven Project --> Java --> Spring Boot --> Project Metadata-->
> Dependencies --> Eureka Server
> ```
>
> #### 方法二：IDEA创建
>
> ```python
> File --> New --> Project --> Spring Initializr --> 选择JDK版本 --> Next --> 填写maven信息 -->
> Next --> 左侧目录选择Cloud Discovery --> 右侧选择Spring Boot版本 --> 右侧勾选Eureka Server --> Next --> Finish
> ```

#### 2、Boot和Cloud版本对应

> ```python
> 上述官方文档，左侧目录树，点击Spring Cloud，即Spring Cloud Netflix的上一级目录。出现页面最下面。
> ```

#### 3、官网没有最新v2.2.0.M1

> #### 前言
>
> ```python
> 查看Spring Cloud Netflix官网网页，版本号是有2.0.3 CURRENT GA的。视频讲解的Spring Boot版本号也是2.0.3.RELEASE。后来讲解zuul的时候，视频老是的IDEA默认是2.0.4，他也按2.0.4.RELEASE创建了。
> ```
>
> #### 注意
>
> ```python
> 1> 官网文档中有的最新Spring Cloud Netflix版本为：2.1.1 SNAPSHOT CURRENT
>     1、 Spring Cloud Netflix也就是一个Spring Boot项目，版本号也就是Spring Cloud Netflix使用的			Spring Boot版本号。
>     2、 而且Spring Cloud官网中的Spring Cloud Netflix组件章节是没有没有这个版本的。
>     3、 因为Spring Cloud Netflix也只是一个Spring Boot项目，说明Netflix项目组没有用19年03月刚出来         的最新Spring Boot创建自己的组件。
>     4、 所以创建Spring Cloud Netflix的Eureka Server项目的时候，应该按照Eureka Server官网上的版         本来选择创建项目的时候的Spring Boot版本。
> ```
>
> #### 所有版本号
>
> ```python
> 1> Springboot的2.2.1M1版本号解释：
> 	1、M是MILESTONE的简写，里程碑的意思。
> 	2、Spring Boot 2.2 首个里程碑版本 M1 已于昨天发布，可从里程碑仓库获取。官方表示该版本关闭了          140多个 issue 和 PR。 --2019年03月09日
> ```
>
> #### 官网上列举的版本号都不全
>
> ```python
> 比如：
> 	视频里使用的Spring Boot版本号为：2.0.3.RELEASE
> 	但是进入Spring Boot官网，点击右侧Overview跟前的Learn，发现版本号中没有2.0.3GA，
> 	随便点一个2.0.9GA的Reference Doc.
> 	然后在路径上把2.0.9.RELEASE改为2.0.3.RELEASE
> 	点击即可进入2.0.3GA的文档中	
> ```
>
> #### 列举
>
> ```python
> 1> start.spring.io创建
>     <parent>
>         <groupId>org.springframework.boot</groupId>
>         <artifactId>spring-boot-starter-parent</artifactId>
>         <version>2.2.0.M1</version>
>         <relativePath/> <!-- lookup parent from repository -->
>     </parent>
>     <properties>
>         <java.version>1.8</java.version>
>         <spring-cloud.version>Greenwich.BUILD-SNAPSHOT</spring-cloud.version>
>     </properties>
> 	创建的Eureka Server项目
> 
> 2> IDEA创建
> 	<parent>
>         <groupId>org.springframework.boot</groupId>
>         <artifactId>spring-boot-starter-parent</artifactId>
>         <version>2.1.4.RELEASE</version>
>         <relativePath/> <!-- lookup parent from repository -->
>     </parent>
>     <properties>
>         <java.version>1.8</java.version>
>         <spring-cloud.version>Greenwich.SR1</spring-cloud.version>
>     </properties>
>     创建的Eureka Server项目
> 
> 3> 解释
> 	Table 1. Release train Spring Boot compatibility
>         Release Train	 Boot Version
>         Greenwich        2.1.x
>         Finchley         2.0.x
>         Edgware          1.5.x
>         Dalston          1.5.x
> 	所以：Boot Version是2.2.0.M1和2.1.4.RELEASE，对应的Spring Cloud都是Greenwich。
>     	 而视频中的2.0.3.RELEASE对应的是Finchley.RELEASE
> ```

#### 4、缺少视频boot版本解决

> #### 问题
>
> ```python
> 1> 如上所述，各种版本不一致：
> 	1> springboot 2.2.0.M1 + cloud Greenwich.BUILD-SNAPSHOT
> 	2> springboot 2.1.4.RELEASE + cloud Greenwich.SR1
> 	注* 启动类
>     	new SpringApplicationBuilder(ServerEureka2Application.class).web(true).run(args);
> 		会报错。
> 2> 希望按照视频版本创建：即
> 	boot <version>2.0.3.RELEASE</version>
> 	cloud <spring-cloud.version>Finchley.RELEASE</spring-cloud.version>
> ```
>
> #### 解决
>
> ```python
> 第一步：pom.xml中<version>2.1.4.RELEASE</version>改为											<version>2.0.3.RELEASE</version>
> 第二步：pom.xml中<spring-cloud.version>Greenwich.SR1</spring-cloud.version>改为
> 	<spring-cloud.version>Finchley.RELEASE</spring-cloud.version>
> 第三步：Maven --> 刷新
> 第四步：右键 --> Maven --> Reimport
> 第五步：检查启动类
> 	new SpringApplicationBuilder(Application.class).web(true).run(args);不报错
> ```
>
> #### 备注
>
> ```python
> 希望指定的springboot版本，之前没有下载过，比如2.0.3.RELEASE的话，第一次需要刷新Maven等操作，第二次就不需要了，直接修改pom文件，就可以直接引用。因为不是SNAPSHOT版本，不会再去repository拉取了。
> ```

#### 5、Eureka Server实战

> ```python
> 第零步：创建项目
> 	注意sprinboot选择，会直接绑定springcloud的版本号，对应关系为
> 		Release Train	 Boot Version
> 		Greenwich        2.1.x
> 		Finchley         2.0.x
> 		Edgware          1.5.x
> 		Dalston          1.5.x
> 第一步：修改springboot和spring cloud版本
> 	<parent>
>         <groupId>org.springframework.boot</groupId>
>         <artifactId>spring-boot-starter-parent</artifactId>
>         <version>2.0.3.RELEASE</version>
>         <relativePath/> <!-- lookup parent from repository -->
>     </parent>
>     
>     <properties>
>         <java.version>1.8</java.version>
>         <spring-cloud.version>Finchley.RELEASE</spring-cloud.version>
>     </properties>
> 第二步：启动类添加注解 @EnableEurekaServer
> 第三步：增加配置application.yml
> 	server:
> 		port: 8761
> 	eureka:
> 		instance:
> 			hostname: localhost
> 		client:
> 			#声明自己是个服务端
> 			registerWithEureka: false
> 			fetchRegistry: false
> 			serviceUrl:
> 				defaultZone: http://${eureka.instance.hostname}:${server.port}/eureka/
> 第四步：访问注册中心页面http://localhost:8761
> ```

#### 6、Eureka Client实战

> ```python
> 注* 客户端只需要增加applicaiton.yml配置，而不需要在启动类加注解@EnableEurekaClient的原因：
> 	官方文档说明如下
> 	By having spring-cloud-starter-netflix-eureka-client on the classpath, your application 	automatically registers with the Eureka Server. Configuration is required to locate the 	Eureka server, as shown in the following example
> 	1> 只要classpath就是jar包路径下有，spring-cloud-starter-netflix-eureka-client这个jar包就可         以自动注册到服务中心。
> 	2> 配置文件applicaiton.yml是必要的，用来定为Eureka Server。
> 第零步：创建项目
> 	注* 选择依赖Dependencies，比如start.spring.io中，在Search dependencies to add中，选择
>     	Web和Eureka Discovery
> 第一步：修改springboot和spring cloud版本
> 	注* 修改成和Eureka Server一样的版本
> 第二步：增加配置application.yml
>     server:
>     	port: 8771
> 
>     #指定注册中心地址
>     eureka:
>       client:
>         serviceUrl:
>           defaultZone: http://localhost:8761/eureka/
> 
>     #服务的名称
>     spring:
>       application:
>         name: product-service
> 第三步：编写类代码
> 	Domain层：
>         @Component
>         public class Product implements Serializable {
>             public Product() {}
> 
>             public Product(int id, String name, int price, int store) {
>                 this.id = id;
>                 this.name = name;
>                 this.price = price;
>                 this.store = store;
>             }
> 
>             private int id;
>             private String name;
>             private int price;
>             private int store;
> 
>             public int getId() {return id;}
>             public void setId(int id) {this.id = id;}
>             public String getName() {return name;}
>             public void setName(String name) {this.name = name;}
>             public int getPrice() {return price;}
>             public void setPrice(int price) {this.price = price;}
>             public int getStore() {return store;}
>             public void setStore(int store) {this.store = store;}
>         }
>     
>     
>     Dao层：
>         @Repository
>         public class ProductDao {
>             private static Map<Integer, Product> productMap = 
>             									new HashMap<Integer,Product>();
>             static {
>                 Product p1 = new Product(1,"电视",523,14);
>                 Product p2 = new Product(2,"洗衣机",43,234);
>                 Product p3 = new Product(3,"冰箱",546,14);
>                 Product p4 = new Product(4,"计算机",234,23);
>                 Product p5 = new Product(5,"电磁炉",4653,63);
>                 Product p6 = new Product(6,"手机",2345,355);
> 
>                 productMap.put(p1.getId(), p1);
>                 productMap.put(p2.getId(), p2);
>                 productMap.put(p3.getId(), p3);
>                 productMap.put(p4.getId(), p4);
>                 productMap.put(p5.getId(), p5);
>                 productMap.put(p6.getId(), p6);
>             }
> 
>             /**
>              * 通过id获取对应Product
>              * @param id
>              * @return
>              */
>             public Product getById(int id) {
>                 return productMap.get(id);
>             }
> 
>             /**
>              * 列出所有的Product对象
>              * @return
>              */
>             public List<Product> listProduct() {
>                 return (List<Product>) productMap.values();
>             }
>         }
> 	Controller层：
>         @RestController
>         @RequestMapping("/api/v1/product")
>         public class ProductController {
>             @Autowired
>             private ProductDao dao;
> 
>             @GetMapping("findById")
>             public Product findById(@RequestParam("id") int id) {
>                 return dao.getById(id);
>             }
> 
>             @GetMapping("list")
>             public List<Product> listProduct() {
>                 return dao.listProduct();
>             }
>         }	
> 	第四步：访问controller接口，访问Eureka Server控制页面
> 		注* Eureka Client使用IDEA平行运行的特性，改变端口，运行同一个项目。同时启动三个进程，端口			  分别为8771/8772/8773。
> ```

#### 7、Eureka Server控制台

> #### 问题
>
> ```python
> 内容：
> 	EMERGENCY! EUREKA MAY BE INCORRECTLY CLAIMING INSTANCES ARE UP WHEN THEY'RE NOT. 		RENEWALS ARE LESSER THAN THRESHOLD AND HENCE THE INSTANCES ARE NOT BEING EXPIRED JUST 	  TO BE SAFE.
> 解释：
> 	eureka管理后台出现一串红色字体：是警告，说明有服务上线率低
> ```
>
> #### 去除报警信息
>
> ```python
> 方法：
> 	关闭检查方法：eureka服务端配置文件加入
> 步骤：application.yml中增加配置
> 	eureka:
>     	server:
> 			enable-self-preservation: false
> 注意：
> 	生产环境下自我保护模式禁止关闭，默认是开启状态true
> 报警原因：
> 	当a和b都连接到注册中心的时候，b因为网络等原因，暂时不能连通注册中心。可是注册中心以为a挂掉了，	 如果自我保护模式关闭，则注册中心会把b从注册中心列表剔除。
> 	这是很危险的在生产环境中，因为其实现在b还是可以正常工作的，给a提供服务，只是不能联通中间的注册中     心而已，所以一般禁止关闭自我保护模式。
> ```

#### 8、服务不定时到注册中心拉取

> #### 示例
>
> ```python
> 当a和b都连接到注册中心的时候，b一方增加节点，因为是集群，那新加的节点就会把注册信息注册进入Eureka Server注册中心。但是a这个时候，即使做了负载均衡，也还是请求不到b一方新增的节点，因为a也是不定时到服务中心拉取配置信息的。等一会儿之后，再访问，就发现可以访问b一方新增节点了。说明a已经到Eureka Server拉取到配置信息了
> ```