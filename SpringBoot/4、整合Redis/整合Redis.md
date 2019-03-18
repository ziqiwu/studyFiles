### 不记文档，白忙一场

------

#### 1、源码编译安装+使用Redis

> #### 源码编译安装Redis4.x
>
> ```python
> 官网：https://redis.io/download#installation
> 下载：wget http://download.redis.io/releases/redis-4.0.9.tar.gz
> 解压：tar -zxvf redis-4.0.9.tar.gz
> 进入：cd redis-4.0.9
> 编译：make
> 
> 注意1：解压之后，进入解压后的目录，最重要的就是一个src的目录，这里面是它的源码。底层用c写的。
> 注意2：只需要make编译就可以了，不需要make install安装。
> 注意3：make、make install和configigure的区别详见linux笔记目录。
> ```
>
> #### 使用
>
> ```python
> 第一步：修改redis.conf。
> 	注释掉bind:127.0.0.1和protected yes。修改port 6379，随便改个端口号，比如port 6666
> 第二步：开放端口。
> 	1. 开放端口命令： /sbin/iptables -I INPUT -p tcp --dport 6666 -j ACCEPT
> 	2.保存：/etc/rc.d/init.d/iptables save
> 	3.重启服务：/etc/init.d/iptables restart
> 	4.查看端口是否开放：/sbin/iptables -L -n
> 第三步：启动服务端
> 	cd src --> ./redis-server ../redis.conf
> 第四步：客户端连接
> 	1) 比如redis-desktop-manager连接
> 	2) 比如服务器redis-cli连接：
> 		如果修改了端口，则./redis-cli -p 6666 -a 123456
> 		默认-h是127.0.0.1，不用写，-a是设置的密码
> 	   比如window上安装的redis的redis-cli连接：
> 		命令为redis-cli.exe -h 10.18.72.30 -p 6666 -a 123456
> ```
>
> #### 笔记
>
> ```python
> 1、是linux下的一种安装方式，下载源码到本地，make是编译，make install是安装
> 2、redis自身有一个限制，本地服务端，必须本地客户端连接，不开放给远程连接。
> 	我可安全起见，redis的配置文件中，默认绑定了本地的ip，只能127.0.0.1可以连接。
> 	有一个白名单限制。
> 3、守护进程启动redis服务端：nohup ./redis-server
> 4、redis.conf配置文件的NETWORK块下面，4.x需要改bind属性值，protected-mode属性值。
> 	如果是开发环境，直接注释掉bind属性，就不会只允许本地连接，或者把本地的ip绑定到上面，可以绑定多     个ip，之间用空格隔开。
> ```

#### 2、连接本地虚拟机redis出错

> #### 问题描述
>
> ```python
> 第一步：本地虚拟机，xshell连接，按照上一步步骤，安装，启动服务端，启动客户端，操作客户端，存取redis		中数据正常。
> 第二步：保持服务端启动状态，本地Redis Desktop Manager创建连接，测试连接，失败。
> 第三步：修改redis.conf配置文件，修改bind属性值为本地ip，重启服务端，测试连接，失败。
> 第四步：xshell连接虚拟机，开放端口6379，测试连接，失败。
> ```
>
> #### 问题分析
>
> ```python
> 解决问题一共两步，缺一不可。
> 第一步：修改redis.conf配置文件，修改bind属性值为本地ip。超重要的是，启动命令一定要加上配置文件。
> 第二步：开放端口，如果redis.conf的port属性值你没有修改，就开放6379，如果改了，就开放修改过后的值。
> ```
>
> #### 笔记
>
> ```python
> 1、带配置文件启动命令：cd src --> ./redis-server ../redis.conf
> 	如果不带配置文件的话，启动命令会默认使用默认的配置，而不会读取redis.conf配置文件。所以即使你修     改了配置文件，但是启动命令不带配置文件参数，也是不会生效的。
> 2、开放端口的两种方式：
> 	方式一：命令行方式
> 		1. 开放端口命令： /sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
> 		2.保存：/etc/rc.d/init.d/iptables save
> 		3.重启服务：/etc/init.d/iptables restart
> 		4.查看端口是否开放：/sbin/iptables -L -n
> 	方法二：直接编辑/etc/sysconfig/iptables文件
> 		1.编辑/etc/sysconfig/iptables文件：vi /etc/sysconfig/iptables。加入内容并保存：
> 		-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT
> 		2.重启服务：/etc/init.d/iptables restart
> 		3.查看端口是否开放：/sbin/iptables -L -n
> 	来源：https://www.cnblogs.com/jtestroad/p/8031850.html
> ```

#### 3、整合Redis

> #### 官网
>
> ```python
> 官网：https://docs.spring.io/spring-boot/docs/2.1.0.BUILD-									SNAPSHOT/reference/htmlsingle/#boot-features-redis
> 集群文档：https://docs.spring.io/spring-data/data-redis/docs/current/reference/html/#cluster
> ```
>
> #### 整合redis
>
> ```python
> 配置方法：
> 	第一步：springboot整合redis相关依赖引入
> 		<dependency>
> 			<groupId>org.springframework.boot</groupId>
> 			<artifactId>spring-boot-starter-data-redis</artifactId>
> 		</dependency>
> 	第二步：相关配置文件配置
> 		注：即使不加这些配置信息，也会使用默认的配置，不影响使用
> 		#=========redis基础配置=========
> 		spring.redis.database=0
> 		spring.redis.host=127.0.0.1
> 		spring.redis.port=6390
> 		# 连接超时时间 单位 ms（毫秒）
> 		spring.redis.timeout=3000
> 
> 		#=========redis线程池设置=========
> 		# 连接池中的最大空闲连接，默认值也是8。
> 		spring.redis.pool.max-idle=200
> 
> 		#连接池中的最小空闲连接，默认值也是0。
> 		spring.redis.pool.min-idle=200
> 			
> 		# 如果赋值为-1，则表示不限制；pool已经分配了maxActive个jedis实例，则此时pool的状态为			exhausted(耗尽)。
> 		spring.redis.pool.max-active=2000
> 
> 		# 等待可用连接的最大时间，单位毫秒，默认值为-1，表示永不超时
> 		spring.redis.pool.max-wait=1000
> 	第三步：controller中调用
> 实战如下：
> 	1、springboot整合redis相关依赖引入。没有什么好说的。
> 	2、相关配置文件配置。暂时我只在application.yml中配置了host的port
>         spring:
>           redis:
>             host: 192.168.1.115
>             port: 9999
> 	3、在controller中调用
> 		@RestController
> 		@RequestMapping("/api")
> 		public class RedisController {
>             @Autowired
>             StringRedisTemplate redisTemplate;
> 
>             @GetMapping(value = "/v1/redis/add")
>             public Object redisAdd() {
>                 Map<String,Object> map = new HashMap<String,Object>();
>                 map.put("sdlf", "sfas");
>                 redisTemplate.opsForValue().set("gender", "不男不女");
>                 return JsonData.buildSuccess(map);
>             }
> 
>             @GetMapping(value = "/v1/redis/get")
>             public Object redisGet() {
>                 String gender = redisTemplate.opsForValue().get("gender");
>                 return JsonData.buildSuccess(gender);
>             }
>         }
> ```
>
> #### 报错
>
> ```python
> controller上注解@RequestMapping("/api")，方法上注解为@GetMapping(value = "/v1/redis/add")，
> 	RedisController类上面注解是@RequestMapping("/api")的时候，直接返回的是Thymeleaf的			index.html页面。改为@RequestMapping("/guozi")的时候，即只要不是api的其他路由名称的时候，成功	 返回了正确信息。
> ```
>
> #### 报错原因
>
> ```python
> 1、我原来加过一个过滤器：
> 
> @WebFilter(urlPatterns = "/api/*",filterName = "loginFilter")
> public class LoginFilter implements Filter {
> 
>     @Override
>     public void init(FilterConfig filterConfig) throws ServletException {
>         System.out.println("--filter init");
>     }
> 
>     @Override
>     public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, 			FilterChain filterChain) throws IOException, ServletException {
>         HttpServletRequest req = (HttpServletRequest) servletRequest;
>         HttpServletResponse res = (HttpServletResponse) servletResponse;
>         String username = req.getParameter("username");
>         System.out.println("--doFilter");
>         if ("guozi".equals(username)) {
>             filterChain.doFilter(servletRequest, servletResponse);
>         } else {
>             res.sendRedirect("/index"); ///index.html
>         }
>     }
> 
>     @Override
>     public void destroy() {
>         System.out.println("--filter destroy");
>     }
> }
> 2、如果想让过滤器放行，其实在后面加一个参数username，给其赋值为guozi就可以了
> 3、记住，以后所有/api开头的路由，都在路径后面加username=guozi
> ```
>
> #### 笔记
>
> ```python
> 常见redistemplate种类讲解和缓存实操(使用自动注入)
> 1、注入模板
> 	@Autowired
> 	private StringRedisTemplate strTplRedis
> 
> 2、类型String，List,Hash,Set,ZSet
> 	对应的方法分别是opsForValue()、opsForList()、opsForHash()、opsForSet()、opsForZSet()
> ```

#### 4、Redis工具类封装

> #### 注意
>
> ```python
> redis的key值的命名规范：按层级用冒号分开。比如basic:user:11，则在可视化工具中，将按层级生成文件夹，basic是一个文件夹，展开，user是一个文件夹。而且这样的命名，查询的效率更高。
> ```

