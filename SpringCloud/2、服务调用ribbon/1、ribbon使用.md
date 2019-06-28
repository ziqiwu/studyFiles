### 不记文档，白忙一场

------

#### ***简介***

> ```python
> ribbon和feign都是发HTTP请求的一个客户端
> 客户端负载均衡。Client Side Load Balancing (Ribbon)
> Netflix提供的功能之一：
> The patterns provided include Service Discovery (Eureka), Circuit Breaker (Hystrix), Intelligent Routing (Zuul) and Client Side Load Balancing (Ribbon)..
> ```

#### 0、ribbon底层

> ```python
> 封装设计模式：
> ribbon封装了HttpClient，HttpClient封装了URLConnection。在基础上又增加了很多功能。
> 就好像BufferStream封装了InputStream等一样。
> ```

#### 1、ribbon使用方式一

> #### 前言
>
> ```python
> Eureka章节创建Eureka Server和Eureka Client。
> 其中Eureka Server是单纯的Eureka注册中心，Eureka Client是负责提供商品信息的服务，即provider。
> 本节开始写消费者，也是一个Eureka Client，负责订单。它需要从商品的Eureka Client获取商品信息。
> ```
>
> #### 实战截取
>
> ```python
> 第一步：
>     @Configuration
>     public class RestTemplateConfig {
>         @Bean
>         @LoadBalanced
>         public RestTemplate restTemplate() {
>             return new RestTemplate();
>         }
>     }
> 
> 
> 第二步：
>     @Service
>     public class ProductOrderServiceImpl implements ProductOrderService {
>         @Autowired
>         private RestTemplate restTemplate;
>         @Override
>         public ProductOrder save(int userId, int productId) {
>             Map<String,Object> productMap = restTemplate.getForObject(
>                     "http://product-service/api/v1/product/findById?									    username=guozi&id="+productId, Map.class);
> 
>             ProductOrder productOrder = new ProductOrder();
>             productOrder.setCreateTime(new Date());
>             productOrder.setUserId(userId);
>             productOrder.setTradeNo(UUID.randomUUID().toString());
> 
>             productOrder.setProductName(productMap.get("name").toString());
>             productOrder.setPrice(Integer.parseInt(productMap.get("price").toString()));
>             productOrder.setUserName("存量"+productMap.get("store").toString());
>             return productOrder;
>         }
>     }
> ```
>
> #### 实战
>
> ```python
> 第零步：创建order_service项目
> 	注* 选择依赖Dependencies，比如IDEA创建项目需要勾选三个地方，即需要增加三个dependencies：
>         WEB/Eureka Discovery（即Eureka Client）/Ribbon（在Cloud Routing中）
> 第一步：修改springboot和spring cloud版本
> 	注* 修改成和Eureka Server一样的版本
> 第二步：配置application.yml
>     server:
>     	port: 8781
>     #指定注册中心地址
>     eureka:
>       client:
>         serviceUrl:
>           defaultZone: http://localhost:8761/eureka/
>     #服务的名称
>     spring:
>       application:
>         name: order-service
> 第三步：开发配置类
> 	创建config包，在包下创建RestTemplateConfig类
> 	@Configuration
> 	public class RestTemplateConfig {
> 		@Bean
> 		@LoadBalanced
> 		public RestTemplate restTemplate() {
> 			return new RestTemplate();
> 		}
> 	}
> 第四步：开发订单模块，作为消费者
> 	1> domain包：
>         //商品订单实体类
>         public class ProductOrder implements Serializable {
>             private int id;
>             private String productName;
>             private  String tradeNo;
>             private int price;
>             private Date createTime;
>             private int userId;
>             private String userName;
>             ...
>             //所有get/set方法
>             ...
>         }
> 
> 	2> service包：
>         @Service
>         public class ProductOrderServiceImpl implements ProductOrderService {
>             @Autowired
>             private RestTemplate restTemplate;
>             @Override
>             public ProductOrder save(int userId, int productId) {
>                 //注* RestTemplate是Spring框架自带的类，底层封装了HttpClient，增加了功能
>                 Map<String,Object> productMap = restTemplate.getForObject(
>                     "http://product-service/api/v1/product/findById?									   username=guozi&id="+productId, Map.class);
> 
>                 ProductOrder productOrder = new ProductOrder();
>                 productOrder.setCreateTime(new Date());
>                 productOrder.setUserId(userId);
>                 productOrder.setTradeNo(UUID.randomUUID().toString());
> 
>                 productOrder.setProductName(productMap.get("name").toString());                             productOrder.setPrice(Integer.parseInt(productMap.get("price").toString()))
>                 productOrder.setUserName("存量"+productMap.get("store").toString());
>                 return productOrder;
>             }
>         }
> 	
>     3> controller包：
>         @RestController
>         @RequestMapping("/api/v1/order")
>         public class OrderController {
>             @Autowired
>             private ProductOrderService productOrderService;
>             @GetMapping("save")
>             public Object save(@RequestParam("user_id") int userId, 										@RequestParam("product_id") int productId) {
>                 return productOrderService.save(userId, productId);
>             }
>         }
>     
> 	4> 重构server-product项目的service类
>         @RestController
>         @RequestMapping("/api/v1/product")
>         public class ProductController {
>             @Autowired
>             private ProductDao dao;
>             //小知识点：属性值优先取IDEA设置的，然后才是application.yml中的
>             @Value("${server.port}")
>             private String port;
> 
>             @GetMapping("findById")
>             public Product findById(@RequestParam("id") int id) {
>                 Product product = dao.getById(id);
>                 Product copyProduct = new Product();
> 
>                 //小知识点：BeanUtils是Spring框架提供的工具类，copyProperties方法就是克隆
>                 BeanUtils.copyProperties(product,copyProduct);
>                 copyProduct.setName(product.getName()+"data from port="+port);
>                 return copyProduct;
>             }
>         }
> 	    注* 重构是为了server-product多节点启动的时候，测试RestTemplateConfig类加了@LoadBalanced
> 			之后软负载均衡的效果。
> 			BeanUtils是Spring提供的工具类，是克隆只用。
> 	5> 测试：
> 		启动server-eureka
> 		启动三个server-product节点，端口分别为8771/8772/8773
> 		启动server-order
> 		连续访问三次：http://localhost:8781/api/v1/order/save?															username=guozi&user_id=27&product_id=2
> 		结果摘录：
> 			{"id":0,"productName":"洗衣机data from port=8772"
> 			{"id":0,"productName":"洗衣机data from port=8773"
> 			{"id":0,"productName":"洗衣机data from port=8771"
> ```
>
> #### 注意报错
>
> ```python
> 1> 配置类中不加@LoadBalanced就报错，找不到product-service这个unknown host。
> 	网上解决办法：https://blog.csdn.net/zhangminemail/article/details/84849648
> 	多加了一个@Bean
> 2> 不编写RestTemplateConfig这个类，也报错，找不到这个类，可是这个类明明已经导入了，这儿只不过是重		新配置，重新而已。不明所以。
> ```

#### 2、ribbon使用方式二

> #### 官方文档步骤如下
>
> ```python
> cloud.spring.io --> 左侧菜单栏选择Spring Cloud Netflix --> 右侧选择Learn --> 选择2.0.3版本 -->
> Reference Doc. --> Single HTML --> 选择Using the Ribbon API Directly
> ```
>
> #### 官方文档如下
>
> ```python
> You can also use the LoadBalancerClient directly, as shown in the following example:
>     
> public class MyClass {
>     @Autowired
>     private LoadBalancerClient loadBalancer;
> 
>     public void doStuff() {
>         ServiceInstance instance = loadBalancer.choose("stores");
>         URI storesUri = URI.create(String.format("http://%s:%s", instance.getHost(), 				instance.getPort()));
>         // ... do something with the URI
>     }
> }
> ```
>
> #### 实战如下
>
> ```python
> @Service
> public class ProductOrderServiceImpl implements ProductOrderService {
>     @Autowired
>     private LoadBalancerClient loadBalancer;
>     @Override
>     public ProductOrder save(int userId, int productId) {
>         ServiceInstance instance = loadBalancer.choose("product-service");
>         URI productServiceUri = 																	URI.create(String.format("http://%s:%s/api/v1/product/findById?							username=guozi&id="+productId, instance.getHost(), instance.getPort()));
>         RestTemplate restTemplate = new RestTemplate();
>         Map<String,Object> productMap = 															restTemplate.getForObject(productServiceUri,Map.class);
> 
>         ProductOrder productOrder = new ProductOrder();
> 
>         productOrder.setCreateTime(new Date());
>         productOrder.setUserId(userId);
>         productOrder.setTradeNo(UUID.randomUUID().toString());
> 
>         productOrder.setProductName(productMap.get("name").toString());
>         productOrder.setPrice(Integer.parseInt(productMap.get("price").toString()));
>         productOrder.setUserName("存量"+productMap.get("store").toString());
>         return productOrder;
>     }
> }
> ```
>
> #### 备注(方式一)
>
> ```python
> 第一步：
>     @Configuration
>     public class RestTemplateConfig {
>         @Bean
>         @LoadBalanced
>         public RestTemplate restTemplate() {
>             return new RestTemplate();
>         }
>     }
> 
> 
> 第二步：
>     @Service
>     public class ProductOrderServiceImpl implements ProductOrderService {
>         @Autowired
>         private RestTemplate restTemplate;
>         @Override
>         public ProductOrder save(int userId, int productId) {
>             Map<String,Object> productMap = restTemplate.getForObject(
>                     "http://product-service/api/v1/product/findById?									    username=guozi&id="+productId, Map.class);
> 
>             ProductOrder productOrder = new ProductOrder();
>             productOrder.setCreateTime(new Date());
>             productOrder.setUserId(userId);
>             productOrder.setTradeNo(UUID.randomUUID().toString());
> 
>             productOrder.setProductName(productMap.get("name").toString());
>             productOrder.setPrice(Integer.parseInt(productMap.get("price").toString()));
>             productOrder.setUserName("存量"+productMap.get("store").toString());
>             return productOrder;
>         }
>     }
> ```

#### 3、客户端负载均衡源码

> ```python
> 负载均衡策略
> 	a loadbalancing strategy
> 第一步：
>     @Configuration
>     public class RestTemplateConfig {
>         @Bean
>         @LoadBalanced
>         public RestTemplate restTemplate() {
>             return new RestTemplate();
>         }
>     }	
> 	点击@LoadBalanced注解
> 第二步：
> 	进入了@interface LoadBalanced，注释用法为：
> 	Annotation to mark a RestTemplate bean to be configured to use a LoadBalancerClient。
> 	可知，注解@LoadBalanced是为了使用LoadBalancerClient。
> 第三步：
> 	shift + shift --> 查找LoadBalancerClient类，或者直接写出来，点击进入
> 第四步：
> 	进入了public interface LoadBalancerClient extends ServiceInstanceChooser。
> 	Represents a client side load balancer（客户端的负载均衡器）。
> 	接口定义了三个方法，execute/execute/reconstructURI（重构URI）
> 第五步：
> 	查看接口LoadBalancerClient的所有实现类 --> ctrl + alt + B
> 第六步：
> 	进入了public class RibbonLoadBalancerClient implements LoadBalancerClient。
> 	可知，接口LoadBalancerClient就一个实现类，就是RibbonLoadBalancerClient类。
> 第六步：
> 	1> 因为我代码调用为：
>         @Autowired
>         private LoadBalancerClient loadBalancer;
>         ServiceInstance instance = loadBalancer.choose("product-service");
>         第一步就是调用了LoadBalancerClient对应实现类的对象的一个choose方法，所以找该方法。
> 	2> 查看public ServiceInstance choose(String serviceId) {方法。
>            
> 	3> 因为choose方法，调用了getServer()
> 		查看protected Server getServer(String serviceId) {方法。
> 		拿到一个服务的列表。从定义的服务名称，相同的服务名称中，获取所有的服务节点。
>                                                         
> 	4> 拿服务列表是从参数ILoadBalancer接口拿的，所以进入接口。
> 		接口定义方法很多，choose方法中调用的是getAllServers()获取所有服务列表。
> 		在该接口实现类BaseLoadBalancer中找到getAllServers()方法，查看实现过程。
> 第七步：
> 	在源码中打断点，一步一步测一下。
> ```

#### 4、负载均衡策略实现原理

> ```python
> 分析@LoadBalanced
>     1）首先从注册中心获取provider的列表
>     2）通过一定的策略选择其中一个节点
>     3）再返回给restTemplate调用
> ```

#### 5、自定义负载均衡策略

> #### 官方文档步骤如下
>
> ```python
> cloud.spring.io --> 左侧菜单栏选择Spring Cloud Netflix --> 右侧选择Learn --> 选择2.0.3版本 -->
> Reference Doc. --> Single HTML --> 选择Customizing the Ribbon Client by Setting Properties
> ```
>
> #### 官方文档如下
>
> ```python
> The following list shows the supported properties>:
>     <clientName>.ribbon.NFLoadBalancerClassName: Should implement ILoadBalancer
>     <clientName>.ribbon.NFLoadBalancerRuleClassName: Should implement IRule
>     <clientName>.ribbon.NFLoadBalancerPingClassName: Should implement IPing
>     <clientName>.ribbon.NIWSServerListClassName: Should implement ServerList
>     <clientName>.ribbon.NIWSServerListFilterClassName: Should implement ServerListFilter
> To set the IRule for a service name called users, you could set the following properties:
> application.yml. 
>     users:
>       ribbon:
>         NIWSServerListClassName: com.netflix.loadbalancer.ConfigurationBasedServerList
>         NFLoadBalancerRuleClassName: com.netflix.loadbalancer.WeightedResponseTimeRule
> ```
>
> #### 注意
>
> ```python
> 比如：<clientName>.ribbon.NFLoadBalancerRuleClassName: Should implement IRule
> 	clientName是服务名称，我的代码中是product-service
> 	后面的值是类名全路径
> 	这儿只讲负载均衡策略的类：
> 		在BaseLoadBalancer类中有 protected IRule rule = DEFAULT_RULE;
> 		ctrl + alt + B查看接口IRule的所有实现类，可以看到其所有的实现类。
> ```

#### 6、传参

> ```python
> 百度 -- ribbon复杂传参
> ```