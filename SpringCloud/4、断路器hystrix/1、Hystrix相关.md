### 不记文档，白忙一场

------

#### 0、简介

> ```python
> Netflix开源组件断路器（circuit breaker）Hystrix介绍
> 简介：介绍Hystrix基础知识和使用场景
> 
> 什么是Hystrix？
> 	1> hystrix对应的中文名字是“豪猪”
> 	2> hystrix 美[haɪs'trɪks]
> 什么是Netflix?
> 	1> 是一家在线影片租赁提供商
> 	2> netflix [net'fliks] 网飞公司
> ```

#### 1、官方文档精读

> ```python
> 文档地址：
> 	https://github.com/Netflix/Hystrix
> 	https://github.com/Netflix/Hystrix/wiki
> ```
>

#### 2、为什么要用

> ```python
> 1> 在一个分布式系统里，一个服务依赖多个服务，可能存在某个服务调用失败，
> 	比如超时、异常等，如何能够保证在一个依赖出问题的情况下，不会导致整体服务失败，
> 	通过Hystrix就可以解决
> 2> 提供了熔断、隔离、Fallback、cache、监控等功能
> 3> spring官网中相关地址：
> 	cloud.spring.io --> spring cloud netflix --> learn --> 2.0.3 GA --> References Doc.
> 	--> circuit breaker:hystrix clients
> ```
>

#### 3、熔断后怎么处理

> ```python
> 出现错误之后可以 fallback 错误的处理信息
> 兜底数据 -- 备份假数据，以备不时之需
> ```

#### 4、hystrix实战

> #### 实战
>
> ```python
> 1> 添加依赖
>     <dependency>
>     	<groupId>org.springframework.cloud</groupId>
>     	<artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
>     </dependency>
> 2> 启动类增加注解
>     启动类里面增加注解
>     @EnableCircuitBreaker
> 	注* 注解越来越多 --> SpringCloudApplication注解替代一部分注解，点进去看替代项
> 3> 代码编写
> 	controller层：
>     @GetMapping("save")
>     @HystrixCommand(fallbackMethod = "saveOrderFail")
>     public Object save(@RequestParam("user_id") int userId, @RequestParam("product_id") int 					productId) {
>         return JsonData.buildSuccess(productOrderService.save(userId, productId),0);
>     }
> 
> 	//编写fallback方法实现，方法签名一定要和api方法签名一致（注意点！！！）
> 	private Object saveOrderFail(int userId, int productId) {
>     	return JsonData.buildError("用户太多，您被挤出来了！", -1);
> 	}
> 	注* 如果save方法出现异常，就会执行fallbackMethod对应的方法，获取兜底数据。
> ```
>
> #### 备注
>
> ```python
> 1> 在项目中指定maven仓库repository，而不是settings.xml中指定 -- 记在maven章节
> 2> 用@SpringCloudxx注解替代 
> 3> 可以自定义注解
> 4> 报错问题：provider还没有完全启动成功，consumer启动了，肯定拿不到对应结果的信息，就会报错。
> 	要么重新启动consumer就是order_server，要么就等会儿再执行接口，因为它会不定期到注册中心去拿信息
> 5> hystrix的方法参数一定要和api的参数一模一样，即使用不上，也要一模一样，否则它会找不到这个方法。
> 6>	补充： 修改maven仓库地址
> 	pom.xml中修改
> 
> 	<repositories>
>         <repository>
>             <id>nexus-aliyun</id>
>             <name>Nexus aliyun</name>
>             <layout>default</layout>
>             <url>http://maven.aliyun.com/nexus/content/groups/public</url>
>             <snapshots>
>                 <enabled>false</enabled>
>             </snapshots>
>             <releases>
>                 <enabled>true</enabled>
>             </releases>
>         </repository>
>     </repositories>
> ```

#### 5、hystrix实战报错

> #### 报错描述
>
> ```python
> @Autowired
> private ProductClient productClient;
> productClient是定义的feign，
> 程序到String strResult = productClient.findById(productId);这儿的时候，就报错。
> 当然因为用到了hystrix，程序就会执行fallbackMethod。
> ```
>
> #### 原因
>
> ```python
> provider即server_product中使用了线程睡眠。
> try {
>     TimeUnit.SECONDS.sleep(2);
> } catch (InterruptedException e) {
>     e.printStackTrace();
> }
> 将这一段注释掉之后，hystrix正常使用了。
> ```
>
> #### 分析
>
> ```python
> 断路器hystrix里面定义了获取超时时间，应该是1s。
> 即使consumer的applicaiton中，重新定义了feign的连接和获取超时时间，都不管用。如下：
> feign:
>   client:
>     config:
>       default:
>         connectTimeout: 11000
>         readTimeout: 11000
> ```

#### 6、feign-hystrix实战

> #### 前言
>
> ```python
> 1> 查看pom依赖，feign中也整合了hystrix依赖，名称feign-hystrix，只是这个整合依赖不能使用				@HystrixCommond注解
> 2> 其实feign中已经整合了hystrix，但是不能用@HystrixCommond注解，所以建议两个依赖都加入进去。
> ```
>
> #### 实战
>
> ```python
> ProductClient接口:
> 	@FeignClient(name="product-service",fallback = ProductClientFallback.class)
> 	public interface ProductClient {
>     	//或者@RequestMapping(value="",method="GET")
>     	@GetMapping("/api/v1/product/findById")
>     	String findById(@RequestParam(value="id") int id);
> 	}
> fallback对应类：
> 	@Component
> 	public class ProductClientFallback implements ProductClient{
>     	@Override
>     	public String findById(int id) {
>         	System.out.println("--------feign调用product server出现异常！");
>         	return null;
>     	}
> 	}	
> 	注* 必须实现@FeignClient注解对应的接口。
> 		如果feign调用错误，会执行对应fallback指定方法，获取兜底数据。
> ```
>
> #### 备注
>
> ```python
> 1> 查看feign依赖spring-cloud-starter-openfeign，里面已经有了
>     <dependency>
>     	<groupId>io.github.openfeign</groupId>
>     	<artifactId>feign-hystrix</artifactId>
>     </dependency>
> 2> 查看@FeignClient注解
> 	里面有：
> 	/**
> 	 * Fallback class for the specified Feign client interface. The fallback class must
> 	 * implement the interface annotated by this annotation and be a valid spring bean.
> 	 */
> 	Class<?> fallback() default void.class;
> 	即：使用注解的时候，@FeignClient(name="xxx", fallback=xxx.class)，有fallback属性，属性值为		   类名称。
> 	注* 认真阅读注释，这个属性的fallback calss必须继承加了@FeignClient注解的接口，而且必须加注解		让Spring可以扫描到。
> 3> 需要放在applicaiton.class的同级包下
> 4> 模拟product_server宕机，直接关掉服务，feign调用不成功。再模拟服务恢复，启动product_server服	务，立马调用接口，还是不成功。
>    原因是：product_server启动的时候，会向注册中心eureka server发送自己的网络信息。order_server会		定期去eureka server拿，拿到之后，它才能进行调用。hystrix会尝试开放部分流量去调用，如果调用		  还不成功，则后续都不能调用。
> ```

#### 7、feign_hystrix实战测试

> ```python
> 第一步：Fallback class没有加@Component
> 	结果：报错Spring bean之类的错误，因为没有让Spring扫描
> 第二步：加@Component注解
> 	结果：调用正常，模拟成功的情况
> 第三步：模拟product_server宕机，关闭服务
> 	结果：返回@HystrixCommond注解方法中的数据，feign_hystrix生效，自定义Fallback `class`中错误				信息输出。
> 第四步：模拟product_server服务恢复，重启服务
> 	结果：立马访问接口，还是错误的情况。过10s左右，访问成功。原因如下：
> 		product_server启动的时候，会向注册中心eureka server发送自己的网络信息。order_server会			定期去eureka server拿，拿到之后，它才能进行调用。hystrix会尝试开放部分流量去调用，如果调		  用还不成功，则后续都不能调用。
> ```

#### 8、hystrix预警报警功能

> #### 前言
>
> ```python
> 做微服务，监控特别重要，一定要加进去
> ```
>
> #### 实战
>
> ```python
> 1> 加入redis依赖
>     <dependency>
>     	<groupId>org.springframework.boot</groupId>
>     	<artifactId>spring-boot-starter-data-redis</artifactId>
>     </dependency>
> 2> 配置redis链接信息
>     spring:  
>         redis:
>             database: 0
>             host: 127.0.0.1
>             port: 6379
>             timeout: 2000
> 3> 报警位置代码编写：
> 	注* 报警代码可以写在hystrix处，也可写在feign_hystrix处
> 	注* 以下代码出处，可见"hystrix实战" 章节
> 	本实例写在hystrix的fallbackMethod方法中：
>     @Autowired
>     StringRedisTemplate redisTemplate;
>     private Object saveOrderFail(int userId, int productId) {
>         //监控报警
>         String redisKey = "save:order";
>         String redisVal = redisTemplate.opsForValue().get(redisKey);
>         //新建线程，执行报警，线程池亦可 -- 
>         //此处用java8的lambda表达式创建线程， -- 详见java线程池
>         new Thread(()->{
>             if (StringUtils.isEmpty(redisVal)) {
>                 System.out.println("-----服务报警，请您尽快处理！");
>                 //短信报警 TODO
>                 //redis存值，过期时间20s
>                 redisTemplate.opsForValue().set(redisKey, "saveOrderFail", 20, 								TimeUnit.SECONDS);
>             } else {
>                 System.out.println("-----redis有效期20s内不再发送短信！");
>             }
>         }).start();
>         //返回兜底数据
>         return JsonData.buildError("用户太多，您被挤出来了！", -1);
>     }
> ```
>
> #### 记录
>
> ```python
> 使用redis的原因，是因为部署肯定是集群部署，一定时间过期的key肯定是每个节点都是访问的相同的key。
> ```

#### 9、hystrix策略源码+官网

> #### 官网
>
> ```python
> github --> 详细资料:
> 	https://github.com/Netflix/Hystrix/wiki/Configuration
> 	找execution.isolation.thread.timeoutInMilliseconds
> jar包源码：
> 	shift + shift --> HystrixCommandProperties
> 	注* Properties for instances of {@link HystrixCommand}
> 		@HystrixCommand注解示例的属性
> ```
>
> #### 查看源码
>
> ```python
> 1> shift + shift --> HystrixCommandProperties，查找以下配置项
>     1）execution.isolation.strategy   隔离策略
>     	1、THREAD 线程池隔离 （默认）
>     	2、SEMAPHORE 信号量
>     	3、信号量适用于接口并发量高的情况，如每秒数千次调用的情况，导致的线程开销过高，通常			       只适用于非网络调用，执行速度快
>     2）execution.isolation.thread.timeoutInMilliseconds  超时时间
>     	默认 1000毫秒
>     3）execution.timeout.enabled 是否开启超时限制 （一定不要禁用）
>     4）execution.isolation.semaphore.maxConcurrentRequests 隔离策略为 信号量的时候，如果达到最		大并发数时，后续请求会被拒绝，默认是10
> 	注* 如果要手动修改这些配置属性，则注意默认固定的前缀为
>         hystrix:
>           command:
>             default:
> 2> 访问官网https://github.com/Netflix/Hystrix/wiki/Configuration
> 	里面有详细的信息。
> ```
>
> #### 实战 --> 自定义hystrix过期时间
>
> ```python
> 1> server_production的provider中增加线程睡眠3s
> 2> 查看源码可知，hystrix的默认过期时间是1s
> 3> 直接访问order_server接口，返回fallback信息
> 4> application.yml增加配置，手动定义过期时间
> 	hystrix:
> 	  command:
> 	    default:
> 	      execution:
> 	        isolation:
> 	          thread:
> 	            timeoutInMilliseconds: 4000
> 	再次访问接口，正常访问。
> 	注* 虽然application.yml手动配置关闭hystrix的过期时间这个属性，也可正常，但是这一定不能做。
> ```
>
> #### 记录
>
> ```python
> 1> 只调整feign中的ribbon的过期时间是不够的。
> 	因为我们又使用了hystrix，它也有一个过期时间。
> 2> hystrix降级策略，如果响应超过1s，就会返回一个fallback，做一个降级处理
> 3> hystrix:common:default是默认的key
> 4> 网页勾选preserve log
> 5> 查看源码类，搜索就可以
> ```

#### 10、hystrix的dashboard

> #### 前言
>
> ```python
> 原理是sse，即:
>     服务端主动推送:SSE (Server Send Event)
> 生产环境，一般不建议加进入，一般做好“hystrix预警报警功能”就可以了
> ```
>
> #### 实战
>
> ```python
> 1> 加入依赖：
>     <dependency>
>     	<groupId>org.springframework.cloud</groupId>
>     	<artifactId>spring-cloud-starter-netflix-hystrix-dashboard</artifactId>
>     </dependency>
> 
>     <dependency>
>     	<groupId>org.springframework.boot</groupId>
>     	<artifactId>spring-boot-starter-actuator</artifactId>
>     </dependency>
> 2、启动类增加注解
> 	@EnableHystrixDashboard
> 3、配置文件增加endpoint
>     management:
>       endpoints:
>         web:
>           exposure:
>             include: "*"
> 4、访问入口
> 	http://localhost:8781/hystrix
> 	Hystrix Dashboard输入： http://localhost:8781/actuator/hystrix.stream 
> ```
>
> #### 记录
>
> ```python
> 1> 生产环境，一般就是报警预警，不会加dashboard
> 2> 现在网上的相关博客文章，问题很大，因为新旧版本很不一样。
> 3> 新旧版本监控路径不一样
> ```
>
> #### 参考资料
>
> ```python
> 默认开启监控配置
> 	https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle/
> 	--> #boot-features-security-actuator
> 配置文件类：
> 	spring-configuration-metadata.json
> ```

#### 11、dashboard参数讲解

> ```python
> 注* 使用的时候，重听视频，讲的很多，但是暂时用不上。
> 机制：
> 	断路器就是provider和comdumer中间的一层，状态由close，open，half-open
> 资料：
> 	https://github.com/Netflix/Hystrix/wiki/Dashboard
> ```

#### 附录：hystrix大牛查看源码

> ```python
> http://www.devzxd.top/2017/05/05/feign-hystrix-problem.html
> ```

