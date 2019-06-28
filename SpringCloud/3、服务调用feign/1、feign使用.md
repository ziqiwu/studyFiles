### 不记文档，白忙一场

------

#### 0、官方文档

> #### 查找步骤
>
> ```python
> cloud.spring.io --> 左侧目录查找Spring Cloud OpenFeign点击进入 --> 
> 右侧查找Lean的Tab页点击进入 --> 找到对应版本2.0.3 CURRENT GA --> 点击Reference Doc.
> ```

#### 1、简介

> ```python
> Feign： 伪RPC客户端(本质还是用http)
> ```

#### 2、feign实战

> ```python
> 第零步：创建项目
> 	比如用IDEA创建项目，勾选的dependecies如下：
> 	1> 因为有controller等对外服务，所以Web --> Web
> 	2> 因为要连接Eureka注册中心，自己是Eureka客户端，所以Cloud Discovery --> Eureka Discovery
> 	3> 因为用的是feign，所以Cloud Routing --> Feign
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
> 	注* boot和cloud对照为：
> 		注意* sprinboot选择，会直接绑定springcloud的版本号，对应关系为
> 		Release Train	 Boot Version
> 		Greenwich        2.1.x
> 		Finchley         2.0.x
> 		Edgware          1.5.x
> 		Dalston          1.5.x
> 第二步：启动类添加注解 @EnableFeignClients //开启feign客户端
> 第三步：增加配置application.yml
>     server:
>       port: 8782
>     #指定注册中心地址
>     eureka:
>       client:
>         serviceUrl:
>           defaultZone: http://localhost:8761/eureka/
>     #服务的名称
>     spring:
>       application:
>         name: order-service-feign
> 第四步：编写实现代码
> 	1> utils.JsonUtils:
>         public class JsonUtils {
>             private static final ObjectMapper objectMapper = new ObjectMapper();
>             /**
>              * json字符串转JsonNode对象方法
>              * 注* JsonNode一定引用成Jackson的
>              */
>             public static JsonNode str2JsonNode(String str) {
>                 try {
>                     return objectMapper.readTree(str);
>                 } catch (IOException e) {
>                     return null;
>                 }
>             }
>         }
> 	2> domain.ProductOrder
>         public class ProductOrder implements Serializable {
>             private int id;
>             private String productName;
>             private  String tradeNo;
>             private int price;
>             private Date createTime;
>             private int userId;
>             private String userName;
>             //----各get/set方法
>         }
> 	3> service.ProductClient
>         @FeignClient(name="product-service")
>         public interface ProductClient {
>             //或者@RequestMapping(value="",method="GET")
>             @GetMapping("/api/v1/product/findById?username=guozi")
>             String findById(@RequestParam(value="id") int id);
>         }
> 	    注* 这个接口加上注释，就可以和server-product通信，@GetMapping必须和通信接口一模一样，
>         	@RequestParam参数必须和通信接口一模一样。如果是POST请求方式，则@PostMapping和
> 		    @RequestBody注解
> 	4> service.ProductOrderService
>         @Service
>         public class ProductOrderService {
>             @Autowired
>             private ProductClient productClient;
>             public ProductOrder save(int userId, int productId) {
>                 //使用注入的productClient
>                 String strResult = productClient.findById(productId);
>                 //这个工具类的对象是Jackson
>                 JsonNode jsonNode = JsonUtils.str2JsonNode(strResult);
> 
>                 ProductOrder productOrder = new ProductOrder();
>                 productOrder.setCreateTime(new Date());
>                 productOrder.setUserId(userId);
>                 productOrder.setTradeNo(UUID.randomUUID().toString());
> 
>                 productOrder.setProductName(jsonNode.get("name").toString());
>                 productOrder.setPrice(Integer.parseInt(jsonNode.get("price").toString()));
>                 productOrder.setUserName("存量"+jsonNode.get("store").toString());
>                 return productOrder;
>             }
>         }
> 	5> controller.OrderController
>         @RestController
>         @RequestMapping("/api/v1/order")
>         public class OrderController {
>             @Autowired
>             private ProductOrderService productOrderService;
> 
>             @GetMapping("save")
>             public Object save(@RequestParam("user_id") int userId, 													@RequestParam("product_id") int productId) {
>                 return productOrderService.save(userId, productId);
>             }
>         }
> ```

#### 3、feign实战注意

> ```python
> 1> 新旧版本依赖名称不一样：
> 	新版本：
>     <dependency>
>         <groupId>org.springframework.cloud</groupId>
>         <artifactId>spring-cloud-starter-openfeign</artifactId>
>     </dependency>
> 	旧版本：
> 	<dependency>
>         <groupId>org.springframework.cloud</groupId>
>         <artifactId>spring-cloud-starter-feign</artifactId>
>     </dependency>
> 	旧版本没有@EnableFeignClients注解，在它的源码中没有该注解。启动类中加的。
> 2> 方法中取参数
> 	String findById(@RequestParam(value="id") int id);
> 	注* 是@RequestParam而不是@Param，否则会报错不支持POST请求方式。
> ```

#### 4、feign源码解读

> #### 源码查看步骤
>
> ```python
> 1> shift + shift --> 查找LoadBalancerFeignClient --> 
> 	这个类实现了Client接口，所以它的作用点击Client接口可以看到 
> 2> 进入Client接口 --> 查看execute方法 
> 	--> Executes a request against its {@link Request#url()url} and returns a response. 
> 	--> 就是一个HTTP请求
> 3> 进入LoadBalancerFeignClient类，查看execute方法
> 	--> public Response execute(Request request, Request.Options options)
> 4> 查看参数Request --> 它有5个属性：
> 		method 请求方式，url 请求url，headers 请求头，body请求体，charset 编码格式
> 	--> 和一个普通的HTTP请求一模一样
> 5> 查看参数Request.Options参数 --> 它有2个属性：
> 		connectTimeoutMillis 连接超时时间，readTimeoutMillis 读取超时时间
> 		默认分别是10s和60s
> 6> 注* 在execute方法体中：
> 	FeignLoadBalancer.RibbonRequest ribbonRequest = new FeignLoadBalancer.RibbonRequest(
> 					this.delegate, request, uriWithoutHost);
> 	表明feign底层是调用了ribbon的。
> ```
>
> #### debug测试
>
> ```python
> 在execute方法第一行代码处打断点：
> 	URI asUri = URI.create(request.url());
> 	调用一个feign的controller
> ```

#### 5、feign连接和读取超时

> #### 前言
>
> ```python
> 1> LoadBalancerFeignClient 类中定义了默认的连接和读取超时时间，分别是10s和60s。
> 2> 其内部自带的hystrix熔断器中定义了读取的超时时间是1s。
> 3> 综合以上情况：
> 	如果读取超过1s就会报错
> ```
>
> #### 测试前言
>
> ```python
> 原理：
> 	因为是server_order_feign用feign调用server_product的接口，如果调用长时间没有回应，比如		provider集群的所有节点都挂掉了，这时候就是读取超时了。
> 	模拟，在server_product的接口中，加入线程睡眠2s，已经超过了超时的1s，测试报错。
> 实战：
> 	1> server_product的ProductController类的findById方法中，加入
>         try {
>             TimeUnit.SECONDS.sleep(2);
>         } catch (InterruptedException e) {
>             e.printStackTrace();
>         }
> 	2> 重启provider和consumer，调用接口，报错：
> 		java.net.SocketTimeoutException: Read timed out
> 		正是读取超时了。
> ```
>
> #### 自定义超时时间
>
> ```python
> 如果有特殊需求，需要自定义超时时间，则在application.yml中定义：
> 	feign:
>         client:
>             config:
>                 default:
>                     connectTimeout: 2000
>                         readTimeout: 2000
> 注* 1> 客户端server_order判断server_product是否一直没有回应，当然加在consumer项目中
>     2> 如忘记配置项，官网查询：
> 		cloud.spring.io --> ... --> Spring Cloud OpenFeign过程不再赘述
> 		--> 选择Overriding Feign Defaults --> 可以找到application.yml配置内容
> ```
>
> #### 测试自定义超时时间
>
> ```python
> 1> server_product中的线程睡眠，模拟provider集群所有节点挂掉，不变
> 2> server_order_feign中的application.yml中加
> 	feign:
>         client:
>             config:
>                 default:
>                     connectTimeout: 3000
>                     readTimeout: 3000
> 3> 重启，访问接口，正确返回
> ```

#### 6、feign和ribbon选用

> ```python
> 工作当中，最好用feign，而不是ribbon。原因：
>     1、feign集成了ribbon，代码更简单
>     2、feign更好地集成hystrix
> ```

#### 7、知识点

> ```python
> 0> 走一遍源码
> 1> 线程睡眠：
> 	TimeUnit.SECONDS.sleep(3);
> 2> 设置连接超时时间和读取超时时间
> 3> feign源码中默认读取超时时间是10s，但是外面还有一层判断，是熔断器hystrix默认超时时间是1s。
> 	所以想自定义超时时间的话，需要自己设置在application.yml中。
> 	application.yml中的设置会取到hystrix中的默认设置。
> 4> 关系，feign包含ribbon
> 	验证方式1：先把客户端的，自定义的随机负载均衡策略注释掉，调用几次。
> 		再打开注释，再调用几次，看一下效果。
> 	验证方式2：看源码
> 5> debug的放行标识是：resume program
> 	resume 美[rɪ'zu:m] v 恢复  n.简历   名词的时候，读音改变 're 
> ```