### 不记文档，白忙一场

------

#### 0、什么是网关

> ```python
> API Gateway，是系统的唯一对外的入口，介于客户端和服务器端之间的中间层，处理非业务功能 提供路由请求、鉴权、监控、缓存、限流等功能
> 注* zuul其实就是一系列的Filter过滤器的集合。
> 
> 1> 统一接入:
>     智能路由
>     AB测试、灰度测试
>     负载均衡、容灾处理
>     日志埋点（类似Nignx日志）
>     注* AB测试：一部分人看到百度黑色背景，一部分人看到百度白色背景，调查满意度
> 
> 2> 流量监控:
>     限流处理
>     服务降级
> 
> 3> 安全防护:
>     鉴权处理
>     监控
>     机器网络隔离
> 注* 优点：
> 	1、"机器网络隔离"就是后面的服务机器都用内网进行调用沟通，速度特别快。只把网关用公网IP暴露给外部
> 		访问。内外网隔离，见详zuul内外网隔离.png
> 	2、网关类似于过滤器，但是过滤器只能用在传统的单一项目里。微服务，每个项目分离。而且项目之间各司		其职，把用网关把每个项目中的过滤器作用抽取出来，统一管理。
> 	3、上接2，"限流处理"，"服务降级"
> ```

#### 1、主流网关

> ```python
> zuul：是Netflix开源的微服务网关，和Eureka,Ribbon,Hystrix等组件配合使用，Zuul 2.0比1.0的性能提高	很多很多。
> 	注* 容易学习，组件多。
> kong: 由Mashape公司开源的，基于Nginx的API gateway
> nginx+lua：是一个高性能的HTTP和反向代理服务器,lua是脚本语言，让Nginx执行Lua脚本，并且高并发、非阻
> 	塞的处理各种请求。
> 	注* 这种开发成本较大。淘宝中使用。性能很高。
> ```

#### 2、zuul实战

> #### 实战
>
> ```python
> 1> 创建项目
> 	注* idea创建，添加dependencies有：cloud discovery(Eureka Discovery)、cloud routing(Zuul)
> 2> 启动类增加注解：
> 	@EnableZuulProxy
> 3> application.yml配置信息
>     #服务端口
>     server:
>       port: 9000
>     #指定注册中心地址
>     eureka:
>       client:
>         serviceUrl:
>           defaultZone: http://localhost:8761/eureka/
> 	#服务的名称
> 	spring:
>       application:
>         name: api-zuul
> 4> 直接启动，访问注册中心eureka server地址
> 	localhost://8761
> 	查看是否已经注册到了注册中心
> 5> 通过zuul网关默认方式，访问下单接口
> 	http://localhost:9000/order-service-feign/api/v1/order/save?user_id=2&product_id=3
> 	注* order-service-feign是下单服务的服务名称，因为历史原因，后来改为order-service。
> 		历史原因是：
> 		zuul:
>           routes:
>             order-service: /apizuul/order/**
> 		因为：order-service-feign是报错的，所以改成了order-service。
> 			对应的当然把下单服务的服务名称也改成了order-service。
> 6> 路径中order-service-feign名字难看，重新自定义
> 	增加applicaiton.yml配置：
> 	#自定义网关路由名称
> 	zuul:
>   		routes:
>     		order-service-feign: /apizuul/**
> 	以下两种都可以：
>     	http://localhost:9000/zuul/api/v1/order/save?user_id=2&product_id=3
> 		http://localhost:9000/order-service-feign/api/v1/order/save?user_id=2&product_id=3
> 7> ignored-services的使用
> 	注* 使接口不能使用路由（即接口不对外进行暴露）一条对一条
> 	application.yml中配置：
> 		zuul:
> 			routes:
>     			order-service-feign: /apizuul/**
> 		    	product-service: /apizuul/**
>   			ignored-services: order-service-feign
> 
> 	测试：
> 		http://localhost:8781/api/v1/order/save?user_id=2&product_id=3
> 		直接访问：成功
>     	http://localhost:9000/order-service-feign/api/v1/order/save?user_id=2&product_id=3
> 		路由访问：失败
> 8> ignored-patterns的使用
> 	注* 使接口不能使用路由（即接口不对外进行暴露）正则匹配
> 	application.yml中配置：
> 		zuul:
>   			routes:
>     			order-service-feign: /apizuul/**
> 		    	product-service: /apizuul/**
>   			ignored-patterns: /*-service*/**
> 	注* 看配置，可以知道，现在外网访问网关，可以有两种方式访问，一种是自定义别名，一种是默认名称，
>     	但是ignored-patterns忽略即屏蔽掉一种，就只剩一种访问方式了。
> 	测试：
> 		http://localhost:8781/api/v1/order/save?user_id=2&product_id=3
> 		直接访问：成功
> 		http://localhost:9000/zuul/
> 		自定义名称访问：成功
> 		http://localhost:9000/order-service-feign/
> 		网关默认访问：失败
> 9> 三种访问方式
> 	1> 直接访问微服务接口。
> 		因为都是微服务都是内网访问，不暴露给外网，忽略
> 	2> 通过服务名称，即spring.application.name
> 		通过配置，屏蔽掉。即ignored-patterns: /*-service*/**
> 	3> 通过网关定义的别名
> 		最后留下唯一方式
> ```
>
> #### 为什么要自定义路由别名，使配置复杂
>
> ```python
> 示例：
> 	zuul:
>   		routes:
>     		order-service-feign: /apizuul/**
> 		    product-service: /apizuul/**
> 原因：
> 	自定义别名的意义是，对外提供服务，名称要有统一规范。
> ```
>
> #### 两个ignore-配置的使用
>
> ```python
> 相同点：
> 	都是忽略服务，不走网关，不通过网关对外暴露。
> 	注* 那你会说，可以直接访问的方式访问啊。局域网向外网暴露，只能通过网关，所以直接访问的方式，外网		是不知道局域网架构的。所以只要忽略了网关，就不能被外网访问到。
> 不同点：
> 	ignored-services：需要一个一个列出来服务的名称
> 	ignored-patterns：用正则匹配的方式，一次匹配出来
> ```
>
> #### 记录
>
> ```python
> 1> 代码恢复，时间超时
> 2> 指定服务port，服务名称，eureka server信息
> 3> eureka server集群怎么搭建
> 4> @EnableZuulProxy点进去看到已经包含了@EnableCircuitBreaker。所以如果后期需要引用断路器，就不需	要单独加注解了。默认集成断路器  @EnableCircuitBreaker
> 5> 访问路径，原来直接访问，现在改为中间经过一层网关，再去访问。
> 6> 网关一般最后一个启动
> ```
>
> #### 三种访问方式，限制为只有网关一种
>
> ```python
> 1> 直接访问接口
> 	http://localhost:8781/api/v1/order/save?user_id=2&product_id=3
> 2> 通过zuul网关默认方式
> 	http://localhost:9000/order-service-feign/api/v1/order/save?user_id=2&product_id=3
> 3> 通过zuul网关自定义网关名称方式
> 	http://localhost:9000/apizuul/api/v1/order/save?user_id=2&product_id=3
> 注* 那你会说，可以直接访问的方式访问啊。局域网向外网暴露，只能通过网关，所以直接访问的方式，外网		是不知道局域网架构的。所以只要忽略了网关，就不能被外网访问到。	
> 	只要控制通过网关访问的两种方式，即可。
> 	详见zuul内外网流程.png
> ```

#### 3、zuul问题解决

> #### 路由名称定义问题
>
> ```python
> 描述：
> 	application.yml定义，
> 	zuul:
>   		routes:
>     		order-service-feign: /apizuul/**
>     		product-service: /apizuul/**
>   		ignored-patterns: /*-service*/**
> 	如上定义后，product-service生效了，order-service-feign没有生效
> 	即：
> 		访问http://localhost:9000/apizuul/api/v1/product/list成功，
> 		访问http://localhost:9000/apizuul/api/v1/order/save?user_id=2&product_id=3失败。
> 原因：
> 	ctrl + 点击routes:，进去查看源码，可知：
> 	public void setRoutes(Map<String, ZuulRoute> routes) {
> 		this.routes = routes;
> 	}
> 	其内部维护的是一个Map，所以key一样的时候，下面的就会把上面的覆盖
> 解决：
> 	名称粒度更细一点，比如/apizuul/order/**和/apizuul/product/**
> 	访问http://localhost:9000/apizuul/order/api/v1/order/save?user_id=2&product_id=3成功
> 	访问http://localhost:9000/apizuul/product/api/v1/product/list成功
> ```
>
> #### Http请求头过滤问题
>
> ```python
> 描述：
> 	通过网关之后，cookie信息不能返回，token信息可以返回
> 实战：
> 	在controller中加入获取cookie和token的代码
> 	String token = request.getHeader("token");
> 	String cookie = request.getHeader("cookie");
> 	System.out.println("token:"+token+";cookie"+cookie);
> 测试：
> 	postman中点击Headers添加：	
>         token:sssssssssssssssssssssss
>         Cookie:3333333333333333333
> 返回：
> 	token:sssssssssssssssssssssss;cookienull   
> 报错：
> 	com.netflix.hystrix.contrib.javanica.exception.FallbackDefinitionException: fallback 	 method wasn't found: saveOrderFail
> 	因为：@HystrixCommand(fallbackMethod = "saveOrderFail")熔断的方法增加了参数
>     	HttpServletRequest request，而saveOrderFail没有对应增加该参数，两个方法中的参数必须一模		   一样。
> 源码分析：
> 	ctrl + 点击application.yml中的zuul:routes，进入ZuulProperties.java，
> 	public void setRoutes(Map<String, ZuulRoute> routes) {
> 		this.routes = routes;
> 	}
> 	点击routes的value即ZuulRoute，可知里面有属性sensitiveHeaders，点击该属性，
> 	可知注释：
> 	/**
>     * List of sensitive headers that are not passed to downstream requests. Defaults
>     * to a "safe" set of headers that commonly contain user credentials. It's OK to
>     * remove those from the list if the downstream service is part of the same system
>     * as the proxy, so they are sharing authentication data. If using a physical URL
>     * outside your own domain, then generally it would be a bad idea to leak user
>     * credentials.
>     */
> 	private Set<String> sensitiveHeaders = new LinkedHashSet<>(
> 		Arrays.asList("Cookie", "Set-Cookie", "Authorization")
>     );
>     默认会把这三个Header中的信息，过滤掉。
> 解决：
> 	application.yml中增加
> 	zuul:
> 		sensitive-headers:
> 	即可。
> 再访问：token:sssssssssssssssssssssss;cookie3333333333333333333
> ```
>
> #### zuul执行顺序 
>
> ```python
> 找源码ZuulProperties.java中，可以找到ZuulFilter这个抽象类，里面有filterType，filterOrder等。
> ```

#### 4、zuul自定义过滤器--登录

> #### 实战
>
> ```python
> 步骤如下：
> 	1、新建一个filter包
> 	2、新建一个类，实现ZuulFilter，重写里面的方法
> 	3、在类顶部加注解，@Component,让Spring扫描
> 实战如下：
>     /**
>      * 登录过滤器
>      */
>     @Component
>     public class LoginFilter extends ZuulFilter {
>         /**
>          * 过滤器类型 -- 主要有前置，后置，登录肯定是前置。位置详见zuul内部过滤器.png(流程图片)
>          * 比如要在请求结束返回的时候做一个处理，增加请求头或者修改里面的信息，就可以加一个post的类            型
>          * @return
>          */
>         @Override
>         public String filterType() {
>             return PRE_TYPE;  //FilterConstants.java中全是过滤器的常量
>         }
> 
>         /**
>          * 过滤器的order值越小，越先执行。
>          * 在FilterConstants.java中可以看到各种order值，但是自定义的不能放在太靠前，因为数据拿过			来之后，会执行编解码之类的
>          * 所以应该先让这些顺序先执行。
>          * @return
>          */
>         @Override
>         public int filterOrder() {
>             return 4;
>         }
> 
>         /**
>          * 过滤器是否生效
>          * 本实例中，判断如果是order服务下单save接口，return true拦截器生效，则进入run执行业务逻            辑
>          * @return
>          */
>         @Override
>         public boolean shouldFilter() {
>             //共享RequestContext，上下文对象
>             RequestContext requestContext = RequestContext.getCurrentContext();
>             HttpServletRequest request = requestContext.getRequest();
>             //拦截器生效 -- 执行下面的run方法
>             //这儿的匹配写死了，硬编码，应该ACL使用
>             if ("/apizuul/order/api/v1/order/save"
>                 .equalsIgnoreCase(request.getRequestURI())) {
>                 return true;
>             }
>             //拦截器不生效
>             return false;
>         }
> 
>         /**
>          * 业务逻辑 -- 这儿应该用JWT ，控制token
>          * @return
>          * @throws ZuulException
>          */
>         @Override
>         public Object run() throws ZuulException {
>             RequestContext requestContext = RequestContext.getCurrentContext();
>             HttpServletRequest request = requestContext.getRequest();
>             //token对象
>             //导入包，org.apache.common.lang
>             String token = request.getHeader("token");
>             if (StringUtils.isBlank(token)) {
>                 token = request.getParameter("token");
>             }
> 
>             if (StringUtils.isBlank(token)) {
>                 //不再往下游执行
>                 requestContext.setSendZuulResponse(false);
>                 //org.springframework.http   点进去HttpStatus可以看到所有的状态信息
>                 requestContext.setResponseStatusCode(HttpStatus.UNAUTHORIZED.value());
>                 //注* 可在在页面访问的时候，看到页面的HTTP ERROR 401 ，即自己定义的								HttpStatus.UNAUTHORIZED
>                 System.out.println("---------不具有token信息，到此结束");
>             }else{
>                 //访问http://localhost:9000/apizuul/order/api/v1/order/save?									user_id=2&product_id=3&token=11111111
>                 //或者访问postman，header中加入token
>                 System.out.println("---------具有token信息，放行");
>             }
>             return null;
>         }
>     }
> ```
>
> #### 注意对比
>
> ```python
> postman访问：
> 	http://localhost:9000/apizuul/order/api/v1/order/save?user_id=2&product_id=3
> 	并且header中加了token参数。
> 结果：
> 	zuul上获取了cookie或者token
> 	server_order_feign的controller中也获取了key，在上面的第3节。
> 	是zuul中获取了，然后传给了order
> 	debug可以清晰地看到先走的zuul，再走的order
> ```
>
> #### 记录
>
> ```python
> 0> 共享RequestContext，上下文对象
> 1> JWT--生成token
> 2> 可以定义很多个Filter，只要filterOrder不一样就可以了
> 3> ACL使用，现在是直接写死了，是硬编码。ACL是记录在redis里面。做权限的列表。redis-list
> ```

#### 5、zuul自定义过滤器--限流

> #### 简介
>
> ```python
> 1> 高并发情况下接口限流
> 2> 谷歌guava框架介绍，网关限流使用
> 	1、nginx层限流
> 	2、网关层限流
> 3> zuul网关层限流原理
> 	详见zuul网关限流令牌.png
> ```
>
> #### 实战
>
> ```python
> /**
>  * 限流过滤器
>  */
> @Component
> public class RateLimiterFilter extends ZuulFilter {
>     //每秒产生1000个令牌
>     //import是com.google.common.util.concurrent.RateLimiter;   -- springcloud已经继承了			google的gauva
>     private static final RateLimiter RATE_LIMITER = RateLimiter.create(1000);
> 
>     @Override
>     public String filterType() {
>         return PRE_TYPE;
>     }
> 
>     //限流过滤器在所有过滤器里最先执行。源码中的最小值order是-3
>     @Override
>     public int filterOrder() {
>         return -4;
>     }
> 
>     /**
>      * 过滤器是否生效
>      * @return
>      */
>     @Override
>     public boolean shouldFilter() {
>         RequestContext requestContext = RequestContext.getCurrentContext();
>         HttpServletRequest request = requestContext.getRequest();
>         //拦截器生效
>         if ("/apizuul/order/api/v1/order/save".equalsIgnoreCase(request.getRequestURI())) {
>             return true;
>         }
>         //拦截器不生效
>         return false;
>     }
> 
>     /**
>      * 业务代码
>      * @return
>      * @throws ZuulException
>      */
>     @Override
>     public Object run() throws ZuulException {
>         RequestContext requestContext = RequestContext.getCurrentContext();
>         if (!RATE_LIMITER.tryAcquire()) {
>             //不再往下游执行
>             requestContext.setSendZuulResponse(false);
>             requestContext.setResponseStatusCode(HttpStatus.TOO_MANY_REQUESTS.value());
>             System.out.println("----超过了最大限流值，不再往下执行");
>         }else{
>             System.out.println("----在最大限流值内，放行");
>         }
>         return null;
>     }
> }
> ```
>
> #### 记录
>
> ```python
> 1> 限流过滤器在所有过滤器里最先执行
> 2> aquire()是阻塞的方式，拿一个令牌，如果拿不到的话，会进行阻塞。
> 	tryaquire()是非阻塞的方式去拿一个令牌
>     	timeout是0，非阻塞去拿，没有拿到的话，不等待，马上返回
> 3> TOO_MANY_REQUEST状态是469
> 4> 目前没有办法进行测试，如果有兴趣的话，可以自己用jmeter进行压测，使令牌桶到达1000
> 5> 线上部署肯定是集群部署。现在做的只是本地单节点限流方式，集群的话，需要redis等方式。但是一通百通
> 6> 目前只是对一个接口进行限流，也可以对整个项目进行限流
> ```

#### 6、zuul集群搭建+nignx

> #### 前言
>
> ```python
> 1> 首先查看zuul内外网隔离.png，
> 2> 下游的服务都是集群搭建，那么zuul也必须集群搭建，否则，网关服务挂了，后端再性能厉害，也白搭。下游	的节点都是集群，就是怕节点挂了。那zuul就是一个springboot应用，没有什么特别，它就很可能挂，所以必	  须集群。
> ```
>
> #### 实战
>
> ```python
> idea中使用，修改-Dserver.port=9001，之后第二个节点启动。
> 然后访问eureka server的网址，可以看到就是两个节点了，在API-ZUUL就是两个节点了，两个port一个是9000一个是9001
> ```
>
> #### 记录
>
> ```python
> 1、nginx+lvs+keepalive 
> 	https://www.cnblogs.com/liuyisai/p/5990645.html
> 2、整个流程图中网关之前，又加入了nginx，'nginx高可用，即keepalived，用的是ip映射'。	
> 	因为nignx性能超强大，所以建议使用。
> 	详见nginx加入之后的流程图.png
> ```
>
> #### 集群之后限流的问题
>
> ```python
> //每秒产生1000个令牌
> //import是com.google.common.util.concurrent.RateLimiter;   springcloud已经继承了google的gauva
> private static final RateLimiter RATE_LIMITER = RateLimiter.create(1000);
> 解决：
> 	如果是两个节点，就在配置文件中，配置是几个令牌，比如两个节点，每个的令牌个数就变为500.
> ```

#### 待学

> ```python 
> 1> JWT--生成token
> 2> ACL使用，现在是直接写死了，是硬编码。ACL是记录在redis里面。做权限的列表。redis-list
> 3> gauva框架，线下一定要学一下。
> ```

 