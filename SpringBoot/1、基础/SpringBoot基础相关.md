### 不记文档，白忙一场

------

#### ***官网文档***

> ```python
> 进入springboot官网文档页面：
> 	spring.io --> 页面上方PROJECTS --> SPIRNG BOOT --> 右侧的Learn --> 
> 	选择一个版本，比如2.2.0 SNAPSHOT --> Reference Doc. --> Spring Boot Features -->
> 	比如查看自定义banner章节 --> 点击左侧的Customizing the Banner
> ```

#### 为什么使用SpringBoot

> ```python
> SpringBoot使配置变简单
> 	没有一大堆的XML配置文件
> SpringBoot使编码变简单
> 	POM.xml中引入一个jar包，代码中一个@RestController就可以完成hello world的输出
> SpringBoot使部署变简单
> 	不再是项目打成war包部署在web容器里，每个SpringBoot都内置一个web容器，打成的也变成了jar包
> SpringBoot使监控变简单
> 	有十几个路径可以直接可视化监控信息
> ```

#### 0、快速构建项目

> #### 手动创建HelloSpringBoot

> ```python
> 第一步：访问https://spring.io/guides/gs/rest-service/
> 第二步：在IDE中创建一个普通的MAVEN项目
> 第三步：肯定不是用Gradle而是用maven，所以在Build with maven中把依赖加入pom.xml文件中
> 第四步：我是2019-02-21看的Spring官网，
> 	1、Create a resource representation class创建了一个实例类
> 	2、Create a resource controller创建了一个Controller类
> 	3、Make the application executable创建了一个启动类
> 第五步：启动启动类，访问http://localhost:8080/greeting访问
> ```

> #### 自动创建HelloSpringBoot
>

> ```python
> 第一步：访问http://start.spring.io/
> 第二步：选择
> 	1、Genernate a maven project with java and Spring Boot 2.1.3
> 	2、填写Group、Artifact，Search for dependecies选择Web
> 	3、Generate Project
> 第三步：将下载的压缩包解压，将解压后的项目包import进入IDE
> 	比如IDEA，则File --> Open... --> 选择解压后的项目 --> 搞定
> 第四步：启动类已经自动生成了，直接写一个Controller类即可
> 	比如：
>     @RestController
>     public class HelloWorldController {
>         @RequestMapping("/greeting")
>         public String sayHello(){
>             return "hello spring boot!";
>         }
>     }
> 第五步：启动启动类，访问http://localhost:8080/greeting访问
> ```
>
> #### IDEA创建HelloSpringBoot
>
> ```python
> 第一步：file --> new --> project --> Spring Initializer(鼠标放上去显示Create Spring boot 		Applications using Spring boot Starters) --> JDK选择1.8，没有就New一个 --> Next
> 第二步：填写Group、Artifact --> 类型是Maven Project --> 打包方式jar --> java版本1.8 --> Next
> 第三步：选择依赖 --> 选择Web，右侧选择Web，选择Spring Boot版本 --> Next --> Finish
> 	因为Spring Boot项目内置了Web容器，所以需要选择Web相关的依赖
> 第四步：新建一个Controller类
> 	@RestController
>     public class HelloWorldController {
>         @RequestMapping("/greeting")
>         public String sayHello(){
>             return "hello spring boot!";
>         }
>     }
> 第五步：启动启动类，访问http://localhost:8080/greeting访问
> ```

#### 1、查看默认依赖jar包

> ```python
> 1、pom.xml文件中如果依赖包没有<version>信息，则版本就和<parent>的版本一直。如果想引用最新的，就自	己增加<version>信息，然后重新刷新导入jar包。
> 	比如可以自己加一个<version>信息
> 	<dependency>
>     	<groupId>org.springframework.boot</groupId>
>     	<artifactId>spring-boot-starter-web</artifactId>
> 		<version></version>
>     </dependency>
> 2、pom.xml文件中ctrl + 左键点击<parent>标签中内容，进入父.pom文件，发现还有<parent>标签，接着点击	标签中内容，又进入爷爷.pom文件，发现了各种的依赖包，以及版本
> ```

#### 2、特有注解

> ```python
> 1、@RestController and @RequestMapping是springMVC的注解，不是springboot特有的	
> 2、@RestController = @Controller+@ResponseBody	
> 3、@SpringBootApplication = @Configuration+@EnableAutoConfiguration+@ComponentScan
> 
> 【注1】测试@RestController注解，将@RestController注解改为@Controller，然后方法上加@ResponseBody		注解，可测试效果一样
> 【注2】测试@SpringBootApplication注解，将@SpringBootApplication注解改为@Configuration、		@EnableAutoConfiguration、@ComponentScan三个注解，可测试效果一样
> 【注3】具体原因，可ctrl + 点击@RestController注解和@SpringBootApplication注解进行查看
> ```

#### 3、请求方式

> #### 前言
>
> ```python
> 下面所有方法中的param变量，都是：
> 	private Map<String,Object> param = new HashMap<String,Object>();
> ```
>
> #### 测试GetMapping
>
> ```python
>     @GetMapping(value="/v1/page_user1")
>     public Object pageUser(int from,int size){
>         param.put("from",from);
>         param.put("size",size);
>         return param;
>     }
> 
> 	1> 测试：
>     	http://localhost:8080/v1/page_user1?from=0&size=100
> ```
>
> #### 测试PostMapping
>
> ```python
>     @PostMapping("/v1/login")
>     public Object login(String id,String pwd){
>         param.put("id",id);
>         param.put("pwd",pwd);
>         return param;
>     }
> 	
>     1> 笔记1：
>     	1、postman模拟post请求。只有两个参数，在Postman中，除了上面的方法中点raw，
>         	这儿点击Body中的x-wwww-from-urlencoded，是key-value形式
>     	2、选择之后，在Http的header中有一个key-value是：
>         	Content-type:application/x-www-form-urlencoded
> ```
>
> #### 测试PutMapping
>
> ```python
>     @PutMapping("/v1/put")
>     public Object put(String id){
>         param.put("id",id);
>         return param;
>     }
> 
> ```
>
> #### 测试DeleteMapping
>
> ```python
> @DeleteMapping("/v1/del")
> public Object del(String id){
>     param.clear();
>     param.put("id",id);
>     return param;
> }
> ```

#### 4、获取参数

> #### 简介
>
> ```python
> GET/POST/PUT/DELETE
> ```
>
> #### 前言
>
> ```python
> 下面所有方法中的param变量，都是：
> 	private Map<String,Object> param = new HashMap<String,Object>();
> ```
>
> #### 从restful路径中获取参数--@PathVariable
>
> ```python
>     @RequestMapping(path="/{city_id}/{user_id}",method= RequestMethod.GET)
>     public Object findUser(@PathVariable("city_id") String cityId,@PathVariable("user_id") 		String userId){
>         param.put("cityId",cityId);
>         param.put("userId",userId);
>         return param;
>     }
> 
>     1> 笔记1：
>     	@RequestMapping中的path参数值，按规则写成小写字母加下划线，不要写成驼峰
>     2>笔记2：
>     	方法findUser中的参数，可以写成@PathVariable，不加括号中的参数，但是这时候，就需要			    String user_id和路由中的参数一模一样。如果想下面的不一样，就需要在@PathVariable中加参数和         路由中参数映射，获取值。
>     3> 测试：
>     	http://localhost:8080/10010/12
> ```
>
> #### url参数：--@RequestParam
>
> ####       1 设置默认值；
>
> ####       2 设置是否为必须的参数
>
> ```python
>     @GetMapping(value="/v1/page_user2")
>     public Object pageUser2(@RequestParam(defaultValue = "0",name = "page") int from,                                   @RequestParam(required = true) int size){
>         param.put("from",from);
>         param.put("size",size);
>         return param;
>     }
> 
> 	1> 笔记1：
>     	路径中不是from而是@RequestParam中的name属性值，即page
>     2> 测试1：
>     	http://localhost:8080/v1/page_user2?page=100&size=50
>     2> 测试2：
>     	http://localhost:8080/v1/page_user2?size=50
>     3> 测试3：
>     	http://localhost:8080/v1/page_user2 
>         注意：提示"Required int parameter 'size' is not present"
> ```
>
> #### Bean对象传参--@RequestBody
>
> ```python
>     @PostMapping("/v1/save_user")
>     public Object saveUser(@RequestBody User user){
>         param.put("user",user);
>         return param;
>     }
> 
> 	1> 笔记1：
>     	注意需要指定http头为content-type为application/json。即在Postman填完url后点击body,		    在下一行最后有一个下拉选，默认是Text，选择JSON(application/json)
>     2> 笔记2：
>     	使用body传输数据。即:
>             在Postman填完url后点击body,点击raw,填一个json格式参数，比如
>             {
>             	"username":"guozi",
>             	"age":"26"
>             }
>     3> 测试：
>     	http://localhost:8080/v1/save_user
> 	4> 应用场景：
>     	当路由中参数过多的时候，比如表单post提交的注册功能。不能在方法参数中写全部的参数一个一个获		    取，最好定义一个Bean一次接受。
> ```
>
> #### 获取http请求的Header中的信息--@RequestHeader
>
> ```python
>     @GetMapping("/v1/get_header")
>     public Object getHeader(@RequestHeader("access_token") String accessToken,String id){
>         param.put("access_token",accessToken);
>         param.put("id",id);
>         return param;
>     }
> 
> 	1> 笔记1：
>     	比如设计token来进行会话管理，则需要获取Header中的token信息，在后台进行获取后判断
>     2> 笔记2：
>     	在Postman中填写路径之后，在第二行有一个Headers，点击，是key-value格式，key			           写"access_token"，value随便写一个标识
>     3> 测试：
>     	http://localhost:8080/v1/get_header?id=12
> 	4> 注意：
>     	如上面的请求路由，只有一个id参数，access_token是在header中设置的
> ```
>
> #### 使用原始的HttpServletRequest获取参数值
>
> ```python
>     @GetMapping("/v1/test_request")
>     public Object testRequest(HttpServletRequest req){
>         String id=req.getParameter("id");
>         param.put("id",id);
>         return param;
>     }
> 
> 	1> 测试：
>     	http://localhost:8080/v1/test_request?id=12
> ```

#### 5、常用json框架

> #### 	简介
>
> ```python
> 常用json框架介绍和Jackson返回结果处理
> 简介：介绍常用json框架和注解的使用，自定义返回json结构和格式
> 
> 1、常用框架 阿里 fastjson,谷歌gson等
>     'JavaBean''序列化'为'Json'，性能：Jackson > FastJson > Gson > Json-lib 同个结构
>     Jackson、FastJson、Gson类库各有优点，各有自己的专长
>     空间换时间，时间换空间
> 
> 2、jackson处理相关自动
>     指定字段不返回：@JsonIgnore
>     指定日期格式：@JsonFormat(pattern="yyyy-MM-dd hh:mm:ss",locale="zh",timezone="GMT+8")
>     空字段不返回：@JsonInclude(Include.NON_NUll)
>     指定别名：@JsonProperty
> ```
>
> #### 	代码示例
>
> ```python
> @RestController
> public class SampleController {
>     @GetMapping("/testjson")
>     public Object testJson(){
>         return new User("guozi","abc.123456","25",null,"18210553849", new Date());
>     }
> }
> 
> 
> 
> public class User {
>     private String username;
>     //该字段不返回给前端，比如密码，返回给前端，随便的爬虫就暴露了
>     @JsonIgnore
>     private String psw;
>     private String age;
>     
>     //该字段是NULL就不反回给前端。即包含的条件是非空。
>     @JsonInclude(JsonInclude.Include.NON_NULL)
>     private String gender;
>     
>     //给该字段起别名。不想把真实的数据库字段映射名称返回给前端，也是爬虫和黑客防止他们。
>     @JsonProperty("account")
>     private String phone;
>     
>     //时间字段规定格式。
>     @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss",locale = "zh",timezone = "GMT+8")
>     private Date createTime;
> 
>     public User(String username, String psw, String age, String gender, String phone, Date 			createTime) {
>         this.username = username;
>         this.psw = psw;
>         this.age = age;
>         this.gender = gender;
>         this.phone = phone;
>         this.createTime = createTime;
>     }
> }
> ```

#### 6、静态资源加载

> #### 简介
>
> ```python
> 讲解SpringBoot目录文件结构和官方推荐的目录规范
> ```
>
> #### 目录讲解
>
> ```python
> src/main/java：存放代码
> src/main/resources
> 	static: 存放静态文件，比如 css、js、image, （访问方式 http://localhost:8080/js/main.js）
> 	templates:存放静态页面jsp,html,tpl
> 	config:存放配置文件,application.properties
> 	resources:
> ```
>
> #### 引入依赖 Thymeleaf  (html静态资源文件不在默认加载的目录中)
>
> ```python
> 注：thyme[taɪm]（用以调味的）百里香（草） ;  
> 需要路径跳转，不在Springboot可加载的目录下，默认可加载的目录是resources、static、public
> 
> <dependency>
> 	<groupId>org.springframework.boot</groupId>
> 	<artifactId>spring-boot-starter-thymeleaf</artifactId>
> </dependency>
> 注意：如果不引人这个依赖包，html文件应该放在默认加载文件夹里面，
> 比如resources、static、public这个几个文件夹，才可以访问。
> 如果是放在了template目录中，就需要添加下面笔记1中的内容，才可以访问得到。
> 
> 笔记1：创建一个testHtml.html放在template目录中，直接访问http://localhost:8080/testHtml.html，
> 	会发现报错。因为springboot框架不会默认到template目录中找，需要引入一个spring-boot-starter-       thymeleaf的jar包，然后写一个controller映射。
> 	@RequestMapping(value="/api/v1/gopage")
>     public Object index(){
>         return "testHtml";
>     }
>     访问http://localhost:8080/api/v1/gopage就可以访问了。
> 跟敲报错：
> 	输入http://localhost:8080/api/v1/gopage一直返回页面只有testHtml一个单词。
> 原因是：	
> 	参见"获取参数从Restful获取参数"：
> 	@RequestMapping(path="/{city_id}/{user_id}",method= RequestMethod.GET)
> 	我把这个路由方法放在了之前就有的一个返回json数据的类里面，类上面有注解@RestController，类里的	方法返回的都是json格式。return "testHtml"也变成json格式返回了。
> 解决是：
> 	新建立了一个类。当然也可以把类注解改为@Controller，原有的方法多加一个@ResponseBody注解
> ```
>
> #### 同个文件的加载顺序 (静态资源文件)
>
> ```python
> Spring Boot 默认会挨个从
> META/resources > resources > static > public  里面找是否存在相应的资源，如果有则直接返回。
> 
> 笔记1：在项目的目录结构中(参考上面的目录讲解)，每个目录中都存放一个testJs.js文件，内容写得有区分		点，然后在浏览器中直接访问http://localhost:8080/testJs.js，会发现输出的是resources中     		testJs.js的内容。删掉这个文件，再访问，会发现输出的是static目录中的内容。删掉这个文件，再访		问，会防线输出的是public目录中的内容。
> 笔记2：访问地址直接写http://localhost:8080/testJs.js，
> 	不需要写http://localhost:8080/resources/testJs.js等，
> 	因为springboot框架会默认顺序地从上面的目录中查找这些静态资源文件。
> 	但是如果是比如：static/js/testJs.js的话，就需要访问http://localhost:8080/js/testJs.js。
> 	不需要写static，因为默认会顺序访问，但是js文件夹需要写。
> ```
> #### js/css/image等静态资源文件不在默认加载的目录中
>
> ```python
> 背景：
> 	项目中的js/css/image都是跟着模块走的。不在spirngboot默认加载目录内。
> 	需要修改默认配置
> 默认配置
> 1）官网地址：
> 	https://docs.spring.io/spring-boot/docs/current/reference/html/boot-features-			developing-web-applications.html#boot-features-spring-mvc-static-content
> 
> 2）示例：
> 	spring.resources.static-locations = classpath:/META-									INF/resources/,classpath:/resources/,classpath:/static/,classpath:/public/ 
>                     
> 笔记1：比如因为业务需求，静态资源文件，并没有存放在默认加载的目录中，而是放在一个test目录中，路径为
> 	java/main/resources/test/testJs.js。
> 	这时候访问http://localhost:8080/test/testJs.js也不会访问到，
> 	因为/test/目录没有加在springboot加载的范围内。
> 	解决如下：
> 	在application.properties文件中(创建springboot项目时候已经生成)，然后粘贴进默认的配置
> 	spring.resources.static-locations = classpath:/META-									INF/resources/,classpath:/resources/,classpath:/static/,classpath:/public/ 
> 	然后再默认配置后面追加上/test/目录，即
> 	spring.resources.static-locations = classpath:/META-									INF/resources/,classpath:/resources/,classpath:/static/,classpath:/public/
> 	,classpath:/test/
> 	最后再访问http://localhost:8080/testJs.js就可以访问到了，都不用加/test/就像不用加/resources
> ```
>
> #### 未来趋势 (静态资源文件并不会放入java项目中)
>
> ```python
> 比如阿里，腾讯等，
> 1、都会把静态资源文件存储在CDN，就比如访问国外网站，需要从那么远的服务器上请求到资源，然后下载到本		地，很耗时间。所以会把静态资源文件，存放在CDN上。
> 2、前后端分离，在tomcat等上面请求'静态资源文件'，并没有nginx等这样的服务器性能高。
> 3、会专门搭建图片的服务器。
> ```

#### 7、文件上传

> #### 简介
>
> ```python
> 讲解HTML页面文件上传和后端处理实战
> ```
>
> #### 前端
>
> ```python
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>首页标题</title>
> </head>
> <body>
>     <h1>首页--------------</h1>
>     <form method="post" action="upload" enctype="multipart/form-data">
>         文件名：<input type="file" name="upload_name">
>         姓名：<input type="text" name="user_name">
>         上传：<input type="submit" name="sub_button">
>     </form>
> </body>
> </html>
> 
> 笔记1：
> 	静态页面直接访问：localhost:8080/index.html
> 注意点：
> 	如果想要直接访问html页面，则需要把html放在springboot默认加载的文件夹下面：
> 	resources、static、public
> ```
>
> #### 后端
>
> ```python
> 注* 只有两点注意
> 	1> MultipartFile对象接收前端type=file的文件
> 	2> uploadFile.transferTo(filePathFile) --MultipartFile 对象的transferTo方法，用于文件保存
> @RestController
> public class UploadController {
>     @PostMapping("/upload")
>     public Object uploadHandler(@RequestParam("upload_name") MultipartFile 						uploadFile,@RequestParam("user_name") String username) {
>         String originalName = uploadFile.getOriginalFilename();
>         String suffixName = originalName.substring(originalName.indexOf("."));
>         String nowName = UUID.randomUUID() + suffixName;
> 
>         System.out.println("---文件是否为空："+ uploadFile.isEmpty());
>         System.out.println("---文件大小："+uploadFile.getSize());
>         System.out.println("---文件原始名称："+originalName);
>         System.out.println("---文件后缀名：" + suffixName);
>         System.out.println("---文件上传后名称："+nowName);
>         System.out.println("---参数user_name:"+username);
>         
>         try {
>             //MultipartFile 对象的transferTo方法，用于文件保存
>             //（效率和操作比原先用FileOutStream方便和高效）
>             uploadFile.transferTo(filePathFile);
>             return filePath;
>         } catch (IOException e) {
>             e.printStackTrace();
>         }
>         return null;
>     }
> }
> //笔记1：获取当前文件的绝对路径System.getProperty("user.dir")，其中的user.dir不是让自己			定义的，而是系统Sytem自己定义的属性
> //笔记2：System.getProperty("user.dir")后面跟着的路径，需要到工作空间的项目去一层一层看
> 	String filePath = System.getProperty("user.dir") +                                          "/src/main/resources/static/images/" + nowName;
> 	File filePathFile = new File(filePath);
> //笔记3:当文件上传成功后，直接访问http://localhost:8080/images/c7451ef5-54bf-424e-                  b603-a6d741647224.log，但是出现{"cityId":"images","userId":"c7451ef5-54bf-424e-              b603-a6d741647224.log"}。
> 	是因为自己的一个controller中测试restFull接口获取参数，
> 	需要注释掉@RequestMapping(path="/{city_id}/{user_id}",method=RequestMethod.GET)
> //笔记4：正常的应该返回的json应该是专门定义一个对象，字段有code，sucessdata，failmsg
> 	public class ReturnJson {
>         //返回状态，-1失败，0成功
>         private int code;
> 
>         //成功时候返回的数据
>         //注意：data值为null的时候不返回给前端
>         @JsonInclude(JsonInclude.Include.NON_NULL)
>         private Object data;
> 
>         //失败时候返回的错误原因信息
>         //注意：msg值为null的时候不返回给前端
>         @JsonInclude(JsonInclude.Include.NON_NULL)
>         private String msg;
>     }
> 	其中的两个@JsonInclude注释，可以不用像视频讲解那样定义两个构造器，只需要
> 	return new ReturnJson(0,filePath,null); -->
> 		{"code":0,"data":"H:\\desktop\\java\\springboot-										demo/src/main/resources/static/images/6ce4cc4e-5b6d-49b1-9e0c-5660f1f5b7de.log"}
> 	return new ReturnJson(-1,null,"transferTo方法执行时异常"); --> 							{"code":-1,"msg":"transferTo方法执行时异常"}
> ```
> #### 文件上传大小配置
>
> ```python
> 我的做法：
> 在和controller同级目录上，创建了一个名称为config的目录，里面创建了个类，名称为uploadConfig.java，
> @Configuration
> public class UploadConfig {
>     @Bean
>     public MultipartConfigElement multipartConfigElement() {
>         MultipartConfigFactory factory = new MultipartConfigFactory();
>         //单个文件最大
>         factory.setMaxFileSize("200KB");
>         //总上传数据总大小
>         factory.setMaxRequestSize("1024KB");
>         return factory.createMultipartConfig();
>     }
> }
> 
> 笔记1：文件上传大小配置的方法必须在有@Configuration注解的类中，才能生效。
> 笔记2：在Springboot启动类中写该配置方法也可以，	
> 	因为：
> 		@SpringBootApplication = @Configuration+@EnableAutoConfiguration+@ComponentScan
> 	ctrl + 点击@SpringBootConfiguration可以发现里面就有@Configuration注解。
> ```

#### 8、jar包启动

> #### 简介
>
> ```python
> 讲解SpingBoot2.x使用 java -jar运行方式的图片上传和访问处理
> 注* nohup java -jar yourapp.jar --server.port=8888 &
> 	可以启动命令指定port，所以机器上传一份项目，如果是nginx负载均衡，不同端口启动即可。
> 	来源：https://www.cnblogs.com/kedarui/p/6518723.html
> ```
>
> #### 打成jar包的方法
>
> ```python
> IDEA的右侧MAVEN --> Lifecycle --> install --> 第一次会downloading一堆jar包，很慢，第二次就     很快了 --> 在项目的target文件夹中可以找到已经打包好的jar包
> 	
> 注意：maven install会把clean、package、download都执行一遍。打包好的jar包会放在maven项目的target	
> 	文件夹下。
> 注意：也可以在cmd命令窗口中使用mvn install命令进行打包
> 	mvn clean package -Dmaven.test.skip=true
> ```
>
> #### 运行jar包 (没有加入maven依赖)
>
> ```python
> java -jar springboot-demo-0.0.1-SNAPSHOT.jar
> 我的报错：springboot-demo-0.0.1-SNAPSHOT.jar中没有主清单属性
> 视频报错：no main manifest attribute, in XXX.jar
> ```
>
> #### 运行jar包 (加入maven依赖)
>
> ```python
> 在pom.xml中加入以下的依赖：
>     <build>
>         <plugins>
>             <plugin>
>                 <groupId>org.springframework.boot</groupId>
>                 <artifactId>spring-boot-maven-plugin</artifactId>
>             </plugin>
>         </plugins>
>     </build>
> 然后：
> 	java -jar springboot-demo-0.0.1-SNAPSHOT.jar
> 成功！！
> ```
>
> #### 分析原因
>
> ```python
> manifest  美[ˈmænəˌfɛst]  显示，表明; 证明; 使显现;
>     
> 没有加入maven依赖打成的Jar包，生成的manifest文件，缺少一部分配置信息，插件spring-boot-maven-plugin就是帮我们生成这些信息。
>     
> 1、加入maven依赖的情况
>     解压jar包之后就可以看到。
>     把jar包springboot-demo-0.0.1-SNAPSHOT.jar解压springboot-demo-0.0.1-SNAPSHOT，会发现
> 	springboot-demo-0.0.1-SNAPSHOT\META-INF\MANIFEST.MF，这个就是manifest文件了。
>     
>     打开此文件MANIFEST.MF可以看到一堆配置文件:
> 	Manifest-Version: 1.0
> 	Implementation-Title: springboot-demo
> 	Implementation-Version: 0.0.1-SNAPSHOT
> 	Built-By: 起鹜
> 	Implementation-Vendor-Id: com.guozi.springboot
> 	Spring-Boot-Version: 2.2.0.BUILD-SNAPSHOT
> 	Main-Class: org.springframework.boot.loader.JarLauncher
> 	Start-Class: com.guozi.springboot.springbootdemo.SpringbootDemoApplication
> 	Spring-Boot-Classes: BOOT-INF/classes/
> 	Spring-Boot-Lib: BOOT-INF/lib/
> 	Created-By: Apache Maven 3.3.9
> 	Build-Jdk: 1.8.0_172
> 	Implementation-URL: https://projects.spring.io/spring-boot/#/spring-boot-starter-			parent/springboot-demo
> 	
> 	其中最重要的是
> 		1> Main-Class: org.springframework.boot.loader.JarLauncher，
> 			这个运行jar包的类在META-INF的同级目录下。
> 			jar包启动器
> 		2> Start-Class: com.guozi.springboot.springbootdemo.SpringbootDemoApplication
> 			指定了生成的项目Jar包的运行入口。
> 		注* 这些都在/META-INF/MANIFEST.MF
> 2、没有加入maven依赖的情况
> 	解压jar包，打开MANIFEST.MF，配置信息如下：
> 	Manifest-Version: 1.0
> 	Implementation-Title: springboot-demo
> 	Implementation-Version: 0.0.1-SNAPSHOT
> 	Built-By: 起鹜
> 	Implementation-Vendor-Id: com.guozi.springboot
> 	Created-By: Apache Maven 3.3.9
> 	Build-Jdk: 1.8.0_172
> 	Implementation-URL: https://projects.spring.io/spring-boot/#/spring-boot-starter-			parent/springboot-demo
>             
> 	可以看到其中并没有指定jar包启动器的类，也确实没有这个类的文件夹：							org.springframework.boot.loader.JarLauncher，
> 	也没有指定项目的入口类：com.guozi.springboot.springbootdemo.SpringbootDemoApplication
> ```
> #### 打成jar包运行，不能上传文件的解决 
>
> ```python
> jar包已经是压缩包了，不能往里存图片等，那就需要往项目之外的文件夹存放上传的文件。
> 
> 我在E:盘下新建了一个文件夹springboot_jar_images，即目录为E:\springboot_jar_images
> 第一步：
> 	UploadController.java原来文件存放路径代码为：
> 		String filePath = System.getProperty("user.dir") + 										"/src/main/resources/static/images/"+ nowName;
> 	现改为：
> 		String filePath = "E:/springboot_jar_images/"+nowName;
> 第二步：
> 	视频讲解，改完代码的上传文件路径后，这个路径并不能并springboot纳入加载范围，即静态资源加载路		径，需要在application.properties配置文件中加入该文件上传路径。如下：
> 		web.image-path= E://springboot_jar_images
> 		spring.resources.static-locations = classpath:/META-INF/resources/,classpath:
>          /resources/,classpath:/static/,classpath:/public/,
> 		classpath:/test/,file:${web.image-path}  
> 	访问http://localhost:8080/dd874828-55e9-4274-aaf7-0d5776eab40f.jpg是whitelabel error 		page页面。即这个不是springboot加载过的静态资源文件。
> 笔记1：
> 	如果只是把文件上传到某个项目之外的文件夹内，是不需要修改application.properties配置文件的。但是
> 	如果想在项目中直接访问，就需要把这个文件夹变为springboot的加载过的静态资源文件夹，即需要在配置	文件中配置该文件夹纳入springboot加载的范围。
> 报错1：
> 	我把代码中文件上传路径改为：String filePath = "E:/springboot_jar_images/"，然后运行一直报错
> 	java.io.IOException: java.io.FileNotFoundException: E:\springboot_jar_images (拒绝访		问。)。我以为是配置文件中，格式的错误获取是路径的斜杠的错误，改了半天，没有效果。
> 	然后又发现自定义的key高亮，点开发现是warning:
>     Inspection info: Checks Spring Boot application .properties configuration files.           Highlights unresolved and deprecated configuration keys and invalid values.
> 	但是发现这个根本不影响代码运行。
> 	解决：String filePath = "E:/springboot_jar_images/"+nowName。路径中少些了图片的名称。
> ```

#### 9、热部署

> #### 简介
>
> ```python
> 介绍什么是热部署，使用springboot结合dev-tool工具，快速加载启动应用。
> 
> 简介：
> 	spring-boot-devtools是一个为开发者服务的一个模块，其中最重要的功能就是热部署。
> 原理：
> 	在发现代码有更改之后，重新启动应用，但是速度比手动停止后再启动更快。
> 	其深层原理是使用了两个ClassLoader。
> 	一个Classloader加载那些不会改变的类(第三方Jar包)，
> 	另一个ClassLoader加载会更改的类，称为restart ClassLoader。
> 	
> 	这样在有代码更改的时候，原来的restart ClassLoader被丢弃，重新创建一个restart ClassLoader，
> 	由于需要加载的类相比较少，所以实现了较快的重启时间。
> 	即devtools会监听classpath下的文件变动，并且会立即重启应用（发生在保存时机）
> ```
>
> #### SpringBoot项目在IDEA中实现热部署
>
> ```python
> 第一步：开启idea自动make功能 
> 	Settings --> Build,Execution,Deployment --> Compiler --> 查找make project automatically      (或者build project automatically)--> 选中
> 	CTRL + SHIFT + A --> 查找Registry --> 找到并勾选compiler.automake.allow.when.app.running
> 第二步：添加MAVEN依赖
> 	1、加MAVEN依赖
> 		<dependency>
>             <groupId>org.springframework.boot</groupId>
>             <artifactId>spring-boot-devtools</artifactId>
>             <optional>true</optional>
>         </dependency>
> 	2、开启热部署
> 		<build>
>             <plugins>
>                 <plugin>
>                     <groupId>org.springframework.boot</groupId>
>                     <artifactId>spring-boot-maven-plugin</artifactId>
>                     <configuration>
>                         <fork>true</fork>  <!--该配置必须-->
>                     </configuration>
>                 </plugin>
>             </plugins>
>         </build>
> 第三步：Chrome禁用缓存(备用)
> 	F12（或Ctrl+Shift+J或Ctrl+Shift+I）--> NetWork --> Disable Cache(while DevTools is open) 
> ```
>
> #### 备注
>
> ```python
> 可以捎带取消IDEA的自动保存功能，标志修改文件为星号。
> 具体方式在studyFiles --> IDE --> IDEA --> Intellij IDEA的"自带功能设置"里面。
> ```
>
> #### 来源
>
> ```python
> https://www.cnblogs.com/winner-0715/p/6666579.html
> ```
> #### 指定不被热部署的目录
>
> ```python
> 1、/resources, /static, /public, /templates，application.propertie等静态资源文件修改之后，也会	  进行热部署，也会单独对这些文件进行重新加载。如果不想这些文件修改的时候热部署，则可以指定其不被热     部署。
> 2、指定文件不进行热部署：
> 	在application.properties文件中加spring.devtools.restart.exclude=static/**,public/**
> 	注意：等号右边是不被热部署的文件名称
> 	重启项目后，再进行这些指定文件的修改时，这些被修改的文件不会被重新加载
> 3、有时候，比如模板引擎，静态文件希望热更新，因为有时候你改了html文件，还是没有效果，就可以做相应的	配置，之后再讲，再来补充内容。
> ```
>
> #### 手工触发重启
>
> ```python
> 1、简介：改代码不重启，通过一个文本去控制
> 2、在application.properties配置文件中加spring.devtools.restart.trigger-file=trigger.txt
> 	注意：等号右边是触发器的文件。
> 	在src/main/resources下创建trigger.txt文件。
> 	trigger.txt文件中写version=1，当你修改差不多了，想对这些修改文件进行重新编译加载的时候，修改文	 件中的version的值，比如比上一次加1，ctrl + S保存，项目就会对刚才修改多的文件进行单独的编译加载
> ```
>

#### 10、application.yml

> #### 常见的配置文件 xml、yml、properties的区别和使用
>
> ```python
> xml、properties、json、yaml
> 		1、常见的配置文件 xx.yml, xx.properties，
> 			1)YAML（Yet Another Markup Language）
> 				写 YAML 要比写 XML 快得多(无需关注标签或引号)
> 				使用空格 Space 缩进表示分层，不同层次之间的缩进可以使用不同的空格数目
> 				注意：key后面的冒号，后面一定要跟一个空格,树状结构
> 			application.properties示例
> 				server.port=8090  
> 				server.session-timeout=30  
> 				server.tomcat.max-threads=0  
> 				server.tomcat.uri-encoding=UTF-8 
> 
> 			application.yml示例
> 				server:  
> 	  				port: 8090  
> 	  				session-timeout: 30  
> 	  				tomcat.max-threads: 0  
> 	  				tomcat.uri-encoding: UTF-8 
> ```
>
> #### SpringBoot默认配置
>
> ```python
> application.properties中所有的可以覆盖的默认配置
> 
> 1、Springboot2.1.0.BUILD-SNAPSHOT所有默认配置：	
> 	spring.io --> projects --> spring-boot --> Learn --> Reference Doc.（比如2.2.0 M4）-->
> 	页面检索"common-application-properties" --> 页面响应太慢，或者 -->
> 	在Url后拼接#common-application-properties
> 2、如果需要修改，直接复制对应的配置文件，加到application.properties里面
> 3、默认示例文件仅作为指导。 不要将整个内容复制并粘贴到您的应用程序中，只挑选您需要的属性。
> 笔记1：
> 	所有的配置，我们都没有写，但是系统就有了，是因为你没有在application.properties中写的，			Springboot就会使用默认的配置。比如server.port=8080你就可以在上面的地址页中找到。
> ```
>
> #### 把配置文件中的值 --> 映射到属性变量/实体类中
>
> #### 方法一
>
> ```python
> 配置方法：
> 	配置文件中的值 --> 映射到属性变量中
>     1、Controller上面配置
>     	@PropertySource({"classpath:resource.properties"})
>     2、增加属性
>     	@Value("${test.name}")
>     	private String name;
> 实战如下：
> 	第一步：
>         @RestController
>         @PropertySource({"classpath:resources/resource.properties"})
>         public class UploadController {
>             @Value("${web.image-path}")
>             private String filePath;
>             .....
>         }
> 	第二步：
> 		resource.properties文件内容：web.image-path= E://springboot_jar_images/
> 		resource.properties文件路径：src/main/resources
> 	
> 	笔记1 --> 之前都是硬编码，直接private String filePath="E://springboot_jar_images/";
> 	笔记2 --> @PropertySource注解必须放在@Controller下面，在加载这个ControllerBean之时，会去加		载这个.properties配置文件，把里面的内容变成Map。然后@("{web.image-path}")就是用				web.image-path这个key取对应的value，而不需要ResourceBundle.getKey()等操作。
> 	报错1 --> 把resource.properties放在static或者resources或者public文件夹下都不好使，只有放在
> 		src/main/resources下才有效，可是springboot默认加载的路径不是有这几个吗？
> 		而且必须是：@PropertySource({"classpath:resources/resource.properties"})
> 		如果写@PropertySource({"classpath:resource.properties"})都找不到文件
> ```
>
> #### 方法二
>
> ```python
> 配置方法：
> 	配置文件中的值 --> 映射到实体类中
> 	1、添加 @Component 注解；
> 	2、使用 @PropertySource 注解指定配置文件位置；
> 	3、使用 @ConfigurationProperties 注解，设置相关属性；
> 	4、必须 通过注入IOC对象Resource 进来 ， 才能在类中使用获取的配置文件值。
> 		@Autowired
> 		private ServerSettings serverSettings;
> 实战如下：
> 	实体类：
> 		@Component
> 		@PropertySource({"classpath:application.yml"})
> 		@ConfigurationProperties(prefix = "entity.person")
> 		public class Person {
>     		private String name;
>     		private String gender;
>     		private String age;
>         }
> 	controller类：
> 		@Autowired
> 		private Person person;
> 		@GetMapping("/entity_test")
> 		public Object entityTest() {
> 			return person;
> 		}
> 	application.yml配置文件：
> 		entity:
> 			person:
> 				age: 26
> 				name: guozi
> 				gender: 男
> 	笔记1：访问http://localhost:8082/entity_test，返回 
> 		{
>             "name": "guozi",
>             "gender": "男",
>             "age": "26"
>         }
> 	笔记2：application.yml放在src/main/resources目录下，但是同级目录下新建resource.yml，内容完		全一样。实体类的注解@PropertySource({"classpath:resource.yml"})会出现各种问题。
> 	笔记3：上接笔记2，我想知道，同名目录下新建resource.yml怎么用，放在static等目录下怎么用。
> 	报错1：注解报错Configuration Annotation Proessor not found in classpath，解决加入maven依赖
> 		https://blog.csdn.net/w05980598/article/details/79167826
> 	报错2：上接报错1，加入该maven依赖之后，原来用于配置文件上传大小的类报错
>     	@Configuration
>         public class UploadConfig {
>             @Bean
>             public MultipartConfigElement multipartConfigElement() {
>                 MultipartConfigFactory factory = new MultipartConfigFactory();
>                 //单个文件最大
>                 factory.setMaxFileSize(200KB);
>                 //总上传数据总大小
>                 factory.setMaxRequestSize("1024KB");
>                 return factory.createMultipartConfig();
>             }
>         }
> 		解决：直接在application.yml中配置
>         spring:			#文件上传大小
>           servlet:
>             multipart:
>               max-file-size: 200KB
>               max-request-size: 1000KB
> ```

#### 11、单元测试

> #### 普通单元测试
>
> ```python
> 第一步：maven中引入相关依赖
> 	<dependency>
>         <groupId>org.springframework.boot</groupId>
>         <artifactId>spring-boot-starter-test</artifactId>
>         <scope>test</scope>
> 	</dependency>
> 	注：如果是IDE生成，或者官网生成器生成，则项目默认添加
> 第二步：test类中使用
>     @RunWith(SpringRunner.class)  //底层用junit  SpringJUnit4ClassRunner
>     @SpringBootTest(classes={XdclassApplication.class})//启动整个springboot工程
>     public class SpringBootTests { }
>     注：ctrl + 左键进入SpringRunner可以发现，这个类就是继承SpringMVC的SpringJUnit4ClassRunner
> 		@SpringBootTest中必须指定SpringBoot的启动类入口，即main方法入口
> 实战如下：
>     @RunWith(SpringRunner.class)
>     @SpringBootTest
>     public class SpringbootDemoApplicationTests {
>         @Test
>         public void test1() {
>             System.out.println("----test1---");
>         }
>         @Test
>         public void test2() {
>             System.out.println("----test2---");
>         }
>         @Before
>         public void testBefore() {
>             System.out.println("---before---");
>         }
>         @After
>         public void testAfter() {
>             System.out.println("---after---");
>         }
>     }
> 	笔记1：输出为
>         ----before---
>         ----test1---
>         ----after---
>         ----before---
>         ----test2---
>         ----after---
> 	笔记2：视频中@SpringBootTest注解必须指定项目的启动入口类，即有main方法的类，但是我这儿并没有指		定，也没有报错
> 	笔记3：如上，只运行test1的话，在test1方法名称上，右键run test1即可。只运行test2同理。如果想全         部运行测试的话，在类名称上右键run classname。
> ```
> #### 单元测试进阶MockMvc (模拟http请求)
>
> ```python
> 使用方式：
> 	1、和普通单元测试一样，只是注解多了一个@AutoConfigureMockMvc。
> 	2、模拟的是http请求。ctrl + 点击进入MockMvcRequestBuilders类，可以发现该类下有get、post、		delete、put等很多请求方式的对应方法。
> 	3、MockMvcRequestBuilders是RequestBuilders接口的一种实现类。可以点击						   mockMvc.perform(MockMvcRequestBuilders.get("/testjson")其中的perform方法查看，参数是	   RequestBuilders接口对象。
> 	4、相关API
> 			perform：执行一个RequestBuilder请求
> 			andExpect：添加ResultMatcher->MockMvcResultMatchers验证规则
> 			andReturn：最后返回相应的MvcResult->Response
> 实战如下：
>     @RunWith(SpringRunner.class)
>     @SpringBootTest
>     @AutoConfigureMockMvc
>     public class MockmvcTest {
>         @Autowired
>         private MockMvc mockMvc;
> 
>         @Test
>         public void testApi() throws Exception {
>     //        MvcResult mvcResult = 												       //				mockMvc.perform(MockMvcRequestBuilders.get("/testjson"))
>     //                .andExpect(MockMvcResultMatchers.status().isOk()).andReturn();
>             MvcResult mvcResult = mockMvc.perform(MockMvcRequestBuilders.get("/testjson"))
>                     .andReturn();
>             String resultStr = mvcResult.getResponse().getContentAsString();
>             System.out.println(resultStr);
>         }
>     }
> 	笔记1：链式调用的时候，最后加andReturn()方法，最终返回的才是MvcResult对象。
> 		连接调用中间加的andExpect()更像是一个检查条件(断言)，只有符合这个条件，程序才会往下执行。
> 		如上面代码所示，注释掉的代码加了断言andExpect()，没加注释的没有加，结果一样。
> 		断言就是，我笃定地说，这块儿肯定没问题，肯定不会影响我的后面运行。
> 	笔记2：注解相较于普通单元测试，只多了一个@AutoConfigureMockMvc
> 	笔记3："/testjson"是我的一个controller方法，返回的是一个对象的json格式，最后输出
> 		{"username":"guozi","age":"25","createTime":"2019-02-28 								13:38:24","account":"18210553849"}
> 	笔记4：debug的话，可以打断点在MvcResult上，右键debug方法名称。可以鼠标移动到MvcResult对象上，		可以看到它有很多属性。找到mockResponse属性，点开mockResponse，会发现mockResponse也有很多		 属性，其中之一就是content，就是我们返回的对象json。
> ```

#### 12、个性化启动banner

> #### 个性化设置启动banner
>
> ```python
> 官网地址：
> 	参照 "官网文档" 章节
> 设置方法：
> 	第一步：在类路径下增加一个banner.txt，里面是启动要输出的信息(即随便画点东西)
> 	第二步：在applicatoin.properties增加banner文件的路径地址 
> 		spring.banner.location=banner.txt
> 实战如下：
> 	1、src/java/resources路径下创建banner.txt，内容为
>                      ****               *
>           zz****   *          **z  z
>             * zz*** *       zz     *                 Spring Boot is starting.....
>               *  z*  *      *    z                   pay attention!!!!!
>                *      *    *     *                   Ready?
>               *zz*       *                           GO.....
>                   z*
>                   * *z       z   *
>                     *         z *
>                      *z     *
>                        zzz**
>                         * ******
>                        **z**z
> 
>      ........................................................................
> 	2、application.yml中增加内容：
>     	spring:
>           banner:
>             location: banner.txt
> 	笔记1：字符画的生成，可以借助python的PIL模块，(备注PIL不支持python3，可以用Pillow模块替代)
>     	from PIL import Image
>         import argparse
> 
> 
>         #命令行输入参数处理
>         parser = argparse.ArgumentParser()
>         parser.add_argument('file')
>         parser.add_argument('-o','--output')
>         parser.add_argument('--width',type=int,default=80)
>         parser.add_argument('--height',type=int,default=80)
> 
> 
>         #获取参数
>         args = parser.parse_args()
> 
>         IMG = args.file
>         WIDTH = args.width
>         HEIGHT = args.height
>         OUTPUT = args.output
> 
>         #字符画所使用的字符集，有70个，可变
>         ascii_char = list('*************************** ')
> 
>         def get_char(r,g,b,alpha=256):
>             if alpha ==0:
>                 return ' '
>             length = len(ascii_char)
>             gray = int(0.2126*r+0.7152*g+0.0722*b)
> 
>             unit = (256.0+1)/length
>             return ascii_char[int(gray/unit)]
> 
>         if __name__ == '__main__':
>             rgb_im = Image.open(IMG)
>             im = rgb_im.convert('RGB')
>             im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
> 
>             txt = ""
> 
>             for i in range(HEIGHT):
>                 for j in range(WIDTH):
>                     txt += get_char(*im.getpixel((j,i)))
>                 txt += '\n'
> 
> 
>             print(txt)
>             if OUTPUT:
>                 with open(OUTPUT,'w') as f:
>                     f.write(txt)
> 
>             else:
>                 with open('output.txt','w') as f:
>                     f.write(txt)
> 	笔记2：找一张图片，我找的是百度了一张简笔画的公鸡，把.py文件和图片文件放在同一目录下，cmd，
>     	敲命令行：python sponge.py guo.jpg --width 30 --height 15
> 		就会在该目录下生成一个output.py文件。其中就是字符画了。
> 	笔记3：源网址为https://blog.csdn.net/weixin_42079187/article/details/81277263
> ```
>

#### 12、日志级别+日志输出文件

> ```python
> 1、jar包启动的时候：
>     启动获取更多信息 java -jar xxx.jar --debug
>     positive   美[ˈpɑ:zətɪv]   肯定的
>     negative   美[ˈnɛɡətɪv]    否定的
> 2、application.yml中设置：
> 	logging:
>       file: springboot.log
>       level:
>           web: DEBUG
> ```

#### 13、Exception

> #### SpringBoot异常配置原理
>
> ```python
> 第一步：程序运行出现异常
> 第二步：SpringBoot监听到该异常发生
> 第三步：SpringBoot使程序进入带有注解@ControllerAdvice或者@RestControllerAdvice的类中
> 第四步：在该类中找和@ExceptionHandler中value值对应的异常，然后按照方法体内容处理该异常信息。
> ```
>
> #### 配置处理全局异常
>
> ```python
> 设置方法：
> 	第一步：单独写一个类，类上配置注解@RestControllerAdvice
> 	第二步：配置某一个异常如ArithmeticException，或者最高级异常Exception。							注解为@ExceptionHandler(value = Exception.class)
> 实战如下：
> 	1、异常的controller:
>         @RestController
>         public class ExceptionController {
>             @GetMapping("/api/v1/test_exception")
>             public Object testException() {
>                 int a = 1/0;
>                 return new User("guozi","12340","12","南","123456",new Date());
>             }
>         }
> 		注：在postman中访问http://localhost:8082/api/v1/test_exception，会报错
>                 ArithmeticException的/by zero
> 	2、处理全局异常的类
>     	@RestControllerAdvice
>         public class TestExceptionHandler {
>             @ExceptionHandler(value = Exception.class)
>             public Object handlerAllException(Exception e, HttpServletRequest req) {
>                 Map<String,String> exceptionMap = new HashMap<String,String>();
>                 exceptionMap.put("code","404");
>                 exceptionMap.put("msg",e.getMessage());
>                 exceptionMap.put("url",req.getRequestURL().toString());
>                 return exceptionMap;
>             }
>         }
> 	笔记1：@ControllerAdvice注解从名称上就能直观看出，是Controller类通知处理的类。当Controller中		有报错的时候，就会自动进入该类里面。
> 	笔记2：当前后端分离，需要返回json的时候，注解有@ControllerAdvice+@ResponseBody或者			   @RestControllerAdvice
> ```
>
> #### 配置处理自定义异常
>
> ```python
> 设置方法：
> 	第一步：自定义一个异常类比如MyException，使其继承自RuntimeException
> 	第二步：在可能出错的代码中，手动抛出自定义的异常，比如throw new MyException()
> 	第三步：在带有@RestCntrollerAdvice或者@ControllerAdvice的类中，定义一个方法，加					@ExceptionHandler(value="MyException.class")
> 实战如下：
> 	1、自定义异常类
>         public class MyException extends RuntimeException{
>             private String code;
>             private String msg;
> 
>             public MyException(String code,String msg) {
>                 this.code = code;
>                 this.msg = msg;
>             }
>             //......这儿需要get/set方法，因为处理异常的时候，需要获取这些异常信息。
>         }
> 	2、在代码中手动抛出自定义异常类
> 		   @GetMapping("/api/v1/test_myexception")
>             public Object testMyException() {
>                 throw new MyException("500","自定义错误");
>             }
> 	3、在带有@RestControllerAdvice注解或者@ControllerAdvice注解的类中处理该异常
> 		       @ExceptionHandler(value=MyException.class)
>                 public Object handleMyException(MyException e,HttpServletRequest req){
>             //        ModelAndView modelAndView = new ModelAndView();
>             //        modelAndView.setViewName("error.html");
>             //        modelAndView.addObject("msg",e.getMessage());
>             //        return modelAndView;
>                     Map<String,String> msgMap = new HashMap<String,String>();
>                     msgMap.put("url",req.getRequestURL().toString());
>                     msgMap.put("code",e.getCode());
>                     msgMap.put("msg", e.getMsg());
>                     return msgMap;
>                 }
> 	笔记1：如果是返回页面，就用注释掉的ModelAndView，addObject()中内容怎么在模板引擎中获取，等之		  后学习了thymelead模板引擎之后再补充。
> 	笔记2：如果是前后端分离开发，则使用没有注释的json数据返回形式。特别注意，方法中参数不是				Exception，而是MyException，然后可以获取该自定义异常对象的所有属性，比如这儿定义的code和		msg
> ```

#### 14、war包启动

> #### springboot项目所有启动方式
>
> ```python
> 1、IDE启动
> 	在idea中的话，右键run，或者ctrl + shift + f10
> 2、打成jar包，用java -jar spring-demo.jar命令启动
> 	备注1：maven插件:
> 		<build>
>             <plugins>
>                 <plugin>
>                     <groupId>org.springframework.boot</groupId>
>                     <artifactId>spring-boot-maven-plugin</artifactId>
>                 </plugin>
>             </plugins>
> 		</build>
> 		如果没有加，就执行jar包 ，java -jar spring-boot-demo-0.0.1-SNAPSHOT.jar
> 		会报如下错误：
> 		no main manifest attribute, in spring-boot-demo-0.0.1-SNAPSHOT.jar
> 	备注2：
>     	java -jar jar_path --param
> 		jar_path: 指代将项目打包为jar打包之后的存储路径
> 		--param: 为需要在命令行指定的参数。例如: 
> 		java -jar emample.jar --server.port=8081
> 		该命令通过在启动行指定了项目启动后绑定的端口号，因为该命令行参数，将会覆盖						application.properties中的端口配置
> 	备注3：
> 		在maven项目的根目录下，执行mvn clean package -Dmaven.test.skip=true
> 		会在maven安装目录的maven-repository中找到该jar包，其中是有jarLoader和manifest中也是指明		了启动类的。
> 		
> 3、如果有安装maven，用 mvn spring-boot:run
> 	备注1：
> 		mvn spring-boot:run -Drun.arguments="--server.port=8888"
> 	备注2：
> 		我们需要进入项目的根目录，执行mvn sprint-boot:run。
> 		idea中的话，直接点击项目名称，在terminal中运行该命令。
> 		cmd的话，cd进入项目名称目录下，运行该命令。
> 	备注3：
> 		来源https://blog.csdn.net/u011425751/article/details/79507386
> 4、war包方式启动
> 	修改方式：
>         1> 修改pom.xml文件，打包方式改为war<packaging>war</packaging>
>         2> 修改pom.xml文件，构建项目名称<finalName>xdclass_springboot</finalName>
>             注意：在<build>标签里面第一行添加<fialName>标签
>         3> 修改启动类
> 	实战如下：
> 		1> 修改pom.xml文件，打包方式改为war
> 			<project>
>                 <modelVersion>4.0.0</modelVersion>
>                 <packaging>war</packaging>
>                 <parent>...</parent>
> 			   <groupId>com.guozi.springboot</groupId>
>                 <artifactId>springboot-demo</artifactId>
>                 <version>0.0.1-SNAPSHOT</version>
>                 <name>springboot-demo</name>
>                 <description>Demo project for Spring Boot</description>
> 				.....
> 				.....
>             </project>
> 	
> 		2> 修改pom.xml文件，构建项目名称
> 			<build>
> 				<finalName>springboot-demo</finalName>
>                   <plugins>
>                       <plugin>
>                           <groupId>org.springframework.boot</groupId>
>                           <artifactId>spring-boot-maven-plugin</artifactId>
>                           <configuration>
>                               <fork>true</fork>
>                           </configuration>
>                       </plugin>
>                   </plugins>
>               </build>
> 		3> 修改启动类
>             public class XdclassApplication extends SpringBootServletInitializer {
>                 @Override
>                 protected SpringApplicationBuilder configure(SpringApplicationBuilder 						application) {
>                     return application.sources(XdclassApplication.class);
>                 }
> 
>                 public static void main(String[] args) throws Exception {
>                     SpringApplication.run(XdclassApplication.class, args);
>                 }
>             }
> ```
>
> #### 笔记
>
> ```python
> 1、springboot一般都是打成jar包启动，如果特殊情况的话，可以用war包部署在外部的tomcat上
> 2、用IDE打包的话，用maven --> install，
> 	如果是用cmd命令的话，就用mvn clean package -Dmaven.test.skip=true命令打包
> 3、pom.xml文件中把打包方式改为war包后，因为之前是jar包方式打包，导致target目录下有很多的其他文件，
> 	执行maven clean，默认直接删除target目录，可以，很强，mmp。控制台输出：
> 		INFO:--- maven-clean-plugin:3.1.0:clean (default-clean) @ springboot-demo ---
> 		INFO:Deleting H:\desktop\java\springboot-demo\target
> 	然后会出来一个新的target文件，里面少很多东西。其实不需要专门执行maven clean。因为maven 			install不是就是执行clean + compile + package吗
> 4、window下安装了tomcat，如果点击start.bat之后窗口闪退，则编辑start.bat文件，在最后一行加pause;，
> 	保存退出，则运行到最后，不会闪退，我们就可以查看到错误信息了
> 5、Tomcat、Jetty、undertow三种启动容器的压测比较
> 	使用Jmter测试工具测试性能，QPS,TPS，RT
> 	https://examples.javacodegeeks.com/enterprise-java/spring/tomcat-vs-jetty-vs-undertow-	  comparison-of-spring-boot-embedded-servlet-containers/
> 	结论：测试比较的指标有，performance(性能)、load(负载)、memory footprint(内存占用)，undertow	     是性能最好的。
> ```
>

#### 15、启动类

> #### 查看源码
>
> ```python
> 1、查看源码的能力很重要
> 2、切入点是启动类的run方法SpringApplication.run(SpringbootDemoApplication.class, args);
> 3、自我小收获之一：
> 	查看SpringApplication源码，类上面的注释有一段为：
> 	  <pre class="code">
>      * public static void main(String[] args) {
>      *   SpringApplication application = new SpringApplication(MyApplication.class);
>      *   // ... customize application settings here
>      *   application.run(args)
>      * }
>      * </pre>
> 	可以知道，默认用的启动方法SpringApplication.run(SpringbootDemoApplication.class, args);
> 	是使用默认配置的，如果要自定义配置，则可以用他的实例方法
> 	public static void main(String[] args) {
>     	SpringApplication application = new SpringApplication(MyApplication.class);
>         // ... customize application settings here   
>         application.run(args);
>         // SpringApplication.run(MyApplication.class, args);
>     }
> 	启动成功！
> ```
>
> #### 查看源码的几点
>
> ```python
> 1、点进去run()方法，查看项目启动的整个流程
> 2、点进去 SpringApplication.run(SpringbootDemoApplication.class, args)这个run，而不是
> 	new SpringApplication().run()的run方法，看到new SpringApplication(primarySources)
> 	一个参数的构造器，再点进去，可以看到这个构造器初始化的内容。
> 	其中最后一个执行过程是this.mainApplicationClass = deduceMainApplicationClass();
> 	是推断应用的main class，
> ```
> #### 启动所有方法
>
> ```python
> 方法一：目前默认方法
> 	SpringApplication.run(ServerProductApplication.class, args);
> 方法二：创建SpringApplication对象
> 	SpringApplication application = new SpringApplication(SpringbootDemoApplication.class);
> 	// ... customize application settings here   
> 	application.run(args)
> 	注* 比如上面注释的地方用 application.setWebApplicationType(WebApplicationType.REACTIVE);
> 方法三：过期方法
> 	new SpringApplicationBuilder(ServerProductApplication.class).web(true).run(args);
> 	注* 我是在spring boot 2.0.3上运行的，出现warn信息：
>     	Warning:(12, 69) java: org.springframework.boot.builder.SpringApplicationBuilder中         的web(boolean)已过时
>         猜测这个方法是springboot 1.x的方法。
> ```

#### 16、自定义Filter

> #### SpringBoot2.x过滤器Filter
>
> ```python
> 查看springboot源码
> 1、IDEA中写Ordered.HEIGEST_PRECEDENCE，ctrl+点击Ordered接口
> 2、同样的方法，查看FilterRegistrationBean，它是注册Filter的bean。
> 	找到package org.springframework.boot.web.servlet;快速进入该目录。
> 	找到该目录下的filter目录，里面的5个Filter类就是系统启动默认加载的5个过滤器。
> 	查看OrderedCharacterEncodingFilter，查看其继承的CharacterEncodingFilter。
> 	可以知道最后一行中的filterChain.doFilter(request, response);
> 3、在启动日志中查看加载的几个过滤器，前提是在application.yml中把logging的级别改为debug
> 4、官网网址：
> 	参考 "官网文档" 章节
> 	#boot-features-embedded-container-servlets-filters-listeners
> ```
>
> #### 使用Servlet3.0配置自定义Filter实战
>
> ```python
> 设置方法：
>     第一步：新建一个Filter类，implements Filter，并实现对应的接口，加注解@WebFilter
>     第二步：启动类里面增加 @ServletComponentScan，进行扫描
> 实战如下：
> 	1、新建Filter类
> 		@WebFilter(urlPatterns = "/api/*",filterName = "loginFilter")
> 		public class LoginFilter implements Filter {
> 
>             @Override
>             public void init(FilterConfig filterConfig) throws ServletException {
>                 System.out.println("--初始化filter");
>             }
> 
>             @Override
>             public void doFilter(ServletRequest servletRequest, ServletResponse 							servletResponse,FilterChain filterChain) throws IOException, 							ServletException {
>                 HttpServletRequest req = (HttpServletRequest) servletRequest;
>                 HttpServletResponse res = (HttpServletResponse) servletResponse;
>                 String username = req.getParameter("username");
>                 System.out.println("--doFilter");
>                 if ("guozi".equals(username)) {
>                     filterChain.doFilter(servletRequest, servletResponse);
>                 } else {
>                     res.sendRedirect("/index");
>                 }
>             }
> 
>             @Override
>             public void destroy() {
>                 System.out.println("--销毁destroy");
>             }
>         }
> 	2、启动类加@ServletComponentScan
> 		@SpringBootConfiguration
> 		@EnableAutoConfiguration
> 		@ComponentScan
> 		@ServletComponentScan
> 		public class SpringbootDemoApplication {
>             ...
> 		}
> 	3、controller中类
> 		   @Autowired
>             private Person person;
>             @GetMapping("/api/entity_test")
>             public Object entityTest() {
>                 return person;
>             }
> 	笔记1：
> 		doFilter是放行的意思
> 	笔记2：
> 		@ServletComponentScan会对Servlet3.0的注解进行扫描
> 	笔记3：
> 		init()是容器启动的时候进行加载。容器会创建一个实例来调用该方法；
> 		doFilter()请求被拦截的时候，进行调用；
> 		destroy()容器被销毁的时候进行调用。热部署的时候，可以看到。
> 			不过我想，打成war包应该在关闭容器的时候，也能看到
> 	笔记4：
> 		@WebFilter是Servlet3.0中的一个注解。只有加上该注解，
> 		标记一个类为filter，被filter进行扫描
> 		urlPatterns：拦截规则，支持正则
> 		@WebFilter(urlPatterns="/api/*")中的urlPatterns规定了，哪些请求时需要进入过滤器的。
> 		根据层级划分的api，比如/api/user/*，/api/user/admin 
> ```
>
> #### 报错
>
> ```python
> public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, 			FilterChain filterChain) throws IOException, ServletException {
>     HttpServletRequest req = (HttpServletRequest) servletRequest;
>     HttpServletResponse res = (HttpServletResponse) servletResponse;
>     String username = req.getParameter("username");
>     System.out.println("--doFilter");
>     if ("guozi".equals(username)) {
>         filterChain.doFilter(servletRequest, servletResponse);
>     } else {
>         res.sendRedirect("/index"); ///index.html
>     }
> }
> 注意：	
> 	其中的重定向，不能写成/index.html，因为我的index.html文件放在了templates文件夹下，这是默认扫
> 	不到的，默认是static/resources/public。
> 	但是我有一个controller，路由是/index，return "index"，而且我加了Thymleaf的jar包。
> 	所以可以写成sendRedircet("index")
> ```
>
> #### 注意
>
> ```python
> 1、Filter必须依赖Servlet容器，它的机制就是基于一个回调机制
> 2、快速进入依赖jar包的某个类的目录，比如spring-boot的jar包中的FilterRegistrationBean类
> 	在文件的第一行，找到package org.springframework.boot.web.servlet;，
> 	然后ctrl+点击最后一个单词servlet，就可以快速进入该目录中。
> ```

#### 17、自定义Servlet

> #### 使用Servlet3.0新特性自定义Servlet
>
> ```python
> 设置方法：
> 	第一步：新建一个MyServlet，继承自HttpServlet，重写doGet()和doPost()，MyServlet类上加			@WebServlet注解
> 	第二步：SpringBoot的启动类中上@ServletComponentScan注解
> 实战如下：
> 	1、新建一个MyServlet
> 	    @WebServlet(name = "myServlet",urlPatterns = "/v1/user/test")
>         public class MyServlet extends HttpServlet {
>             @Override
>             protected void doGet(HttpServletRequest req, 
>                     HttpServletResponse resp) throws ServletException, IOException {
>                 resp.setCharacterEncoding("utf-8");
>                 resp.getWriter().print("这儿是自定义的Servlet");
>                 resp.getWriter().flush();
>                 resp.getWriter().close();
>             }
> 
>             @Override
>             protected void doPost(HttpServletRequest req, 
>                       HttpServletResponse resp) throws ServletException, IOException {
>                 this.doGet(req, resp);
>             }
>         }
> 	2、SpringBoot启动类加注解@ServletComponentScan
> 	   @SpringBootConfiguration
>         @EnableAutoConfiguration
>         @ComponentScan
>         @ServletComponentScan
>         public class SpringbootDemoApplication {
>             ...
>         }
> 	笔记1：使用SpringBoot或者SpringMVC的时候，框架给我们封装了好多功能，节省了我们的代码量
> 		比如：从req获取参数，原生servlet需要req.getParameter("xx")，每个参数都需要获取。
> 			框架的话，直接给我们封装成了对象，映射关系也有
> 			@PostMapping("/v1/save_user")
> 			public Object saveUser(@RequestBody User user){
>                     param.put("user",user);
>                     return param;
> 			}
> 		比如：返回json，原生的需要获取getWriter()，需要关闭，对象的话，还需要因为jar包，把对象转			换为json。框架的话只需要加一个@ResponseBody注解。如果加了@RestController的话，都不用			 加注解了方法上面。
> 	笔记2：@WebServlet、@WebFilter、@WebListener注解，都是Servlet3.0中的新特性，在SpringBoot中			都需要和@ServletComponentScan注解一起使用(启动类中)
> ```

#### 18、自定义Listener

> #### 使用Servlet3.0新特性自定义Listener
>
> ```python
> 注* 常见监听器
> 	常用的监听器 servletContextListener、httpSessionListener、servletRequestListener
> 设置方法：
> 	第一步：新建一个MyRequestListener，实现ServletRequestListener接口，实现requestDestroyed和		requestInitialized方法，MyRequestListener类上加@WebListener注解
> 	第二步：SpringBoot的启动类中上@ServletComponentScan注解
> 实战如下：
> 	1、新建一个监听器类
>     MyRequestListener(实战1)
> 	@WebListener
>     public class MyRequestListener implements ServletRequestListener {
>         @Override
>         public void requestDestroyed(ServletRequestEvent sre) {
>             System.out.println("--requestDestroy");
>         }
> 
> 
>         @Override
>         public void requestInitialized(ServletRequestEvent sre) {
>             System.out.println("--requestInit");
>         }
>     }
> 		
>         或者
>         
>     MyContextListener(实战2)
> 	@WebListener
>     public class MyContextListener implements ServletContextListener {
>         @Override
>         public void contextInitialized(ServletContextEvent sce) {
>             System.out.println("--contextInit");
>         }
> 
>         @Override
>         public void contextDestroyed(ServletContextEvent sce) {
>             System.out.println("--contextDestroy");
>         }
>     }
> 	2、SpringBoot启动类加注解@ServletComponentScan
> 		@SpringBootApplication
> 		@ServletComponentScan
> 		public class SpringbootDemoApplication {
>             ...
> 		}
> ```
>
> #### 项目实战 --> 使用上下文监听器
>
> ```python
> 实战1：	
> 	航油项目之'天气采集系统'
> 	描述：
> 		1> 项目自己写了生产者和消费者模式，肯定需要项目一启动就启动消费者，生产者在程序适当时间启			 动。所以消费者最好放在上下文监听器中启动。
> 		2> 第一次失败，原因，启动类中忘了加@ServletComponentScan
> 		3> 第二次失败，找不到javax.servlet.annotation这个目录所在jar包，即servlet-api这个jar		   包。pom中手动加入：
>             <groupId>javax.servlet</groupId> 
>                <artifactId>javax.servlet-api</artifactId> 
>                <version>3.0.1</version> 
>                <scope>provided</scope>
>             </dependency>
> 
> 
>             <dependency> 
>                <groupId>javax.servlet.jsp</groupId> 
>                <artifactId>jsp-api</artifactId> 
>                <version>2.1</version> 
>                <scope>provided</scope>
>             </dependency>
> 		    引入的注解都不报错，但是项目启动不了
> 		4> 第三次失败，改引入spring-boot-starter-web，而不是spring-boot-starter。
> 		   因为@WebListener注解所在Jar包不在spring-boot-starter的jar包中，在spring-boot-                 starter-web的jar包中。
> 		   还是报错
> 		5> 第四次成功。
> 		   将启动类中的new SpringApplicationBuilder().sources(
>                CnafWeatherApplication.class).web(false).run(args);改为
>             SpringApplication.run(CnafWeatherApplication.class, args);
> 		   端口占用，可以从控制台看到是8080
> 	分析：
> 	    原始上下文监听器如下：
>         package com.web.system.listener;
> 
>         import java.util.ArrayList;
>         import javax.servlet.ServletContextEvent;
>         import javax.servlet.ServletContextListener;
>         /**
>          * 自定义的ServletContext监听器，可以在ServletContext加载时做一些初始化的工作
>          *
>          */
>         public class MyServletContextListener implements ServletContextListener {
>                  @Override
>                  public void contextDestroyed(ServletContextEvent arg0) {
>                            System.out.println("MyServletContextListener Destoryed");
>                  }
> 
>                  /**
>                   * servletContext初始化
>                   */
>                  @Override
>                  public void contextInitialized(ServletContextEvent arg0) {
> 					System.out.println("MyServletContextListener Init");
>                  }
>             }
> 		
> 		web.xml配置如下：
>         <listener>
> 		<listener-class>com.web.system.listener.MyServletContextListener</listener-class>
>  	    </listener>
> 
> 			所以啊，总而言之，annotation并没有那么玄乎，并不是打个标记就会帮你做什么事情，这个要
> 		做的事情还是要在后续配套的'反射函数'来自己实现。
> 			也是需要web.xml里面的配置信息，当然必须是web项目。
> ```
>
> #### @WebListener注解所在Jar包
>
> ```python
> 不在spring-boot-starter的jar包中，在spring-boot-starter-web的jar包中。
> ```
>
> #### 笔记
>
> ```python
> 0、自定义Listener(常用的监听器 servletContextListener、httpSessionListener、					servletRequestListener)
> 1、继承ServletRequestLisener，需要重写里面的两个方法，一共也就两个方法，init和destroy，一个是进去	一个是离开。过程就是，先Init初始化，再进入我们的controller，然后再destroy进行销毁。
> 3、ServletContextListener可以用在，服务器一启动的时候，就用来连接数据库、redis等。而且这个工程，最	  好是重新启动给一个线程来做，因为不能阻塞主线程。
> 4、应用场景，可以百度，一个是用来做资源加载，一个是用来做统计。
> 5、context的listener最先加载，最后销毁，因为其他的一切都是需要上下文环境的。
> 6、从打印日志，查看过滤器、监听器的初始和销毁的时间
> 	当启动服务器的时候：
> 		--contextListener Init
> 		--filter Init
> 	当请求一个url的时候：
> 		--requestListener Init
> 		--requestListener Destroy
> 	当触发器热加载的时候：
> 		--filter destroy
>     	--contextListener Destroy
> 7、需要在启动类上加@ServletConponentScan注解，才能生效
> ```

#### 19、自定义Interceptor

> #### 旧拦截器 (SpringBoot2.x之前)
>
> ```python
> 设置方法：
> 	第一步：定义。自定义一个拦截器
> 	第二步：注册。在Configurer配置器中addInterceptor注册该拦截器
> 实战如下：
> 	1、定义
> 		@Configuration
>         public class OneInterceptor implements HandlerInterceptor {
>             @Override
>             public boolean preHandle(HttpServletRequest request, HttpServletResponse 						response, Object handler) throws Exception {
>                 System.out.println("--oneInterceptor preHandle");
>                 return HandlerInterceptor.super.preHandle(request,response,handler);
>             }
> 
>             @Override
>             public void postHandle(HttpServletRequest request, HttpServletResponse 						response, Object handler, ModelAndView modelAndView) throws Exception {
>                 System.out.println("--oneInterceptor postHandle");
>                 HandlerInterceptor.super.postHandle(request,response,handler,modelAndView);
>             }
> 
>             @Override
>             public void afterCompletion(HttpServletRequest request, HttpServletResponse 					response, Object handler, Exception ex) throws Exception {
>                 System.out.println("--oneInterceptor afterCompletion");
>                 HandlerInterceptor.super.afterCompletion(request,response,handler,ex);
>             }
>         }
> 	2、注册
> 		@Configuration
>         public class CustomOldWebMvcConfigurer extends WebMvcConfigurerAdapter {
>             @Override
>             public void addInterceptors(InterceptorRegistry registry) {
>                 registry.addInterceptor(new OneInterceptor()).addPathPatterns("/api/*/**");
>                 super.addInterceptors(registry);
>             }
>         }
> 笔记1：
> 	ctrl + 点击进入抽象类WebMvcConfigurerAdapter，可以看到如下注释：
>     @deprecated as of 5.0 {@link WebMvcConfigurer} has default methods (made
>     possible by a Java 8 baseline) and can be implemented directly without the
>     need for this adapter
> 笔记2：
> 	preHandle:进入controller方法之前
> 	postHandle:调用完controller之后，视图渲染之前
> 	afterCompletion:整个方法完成之后，通常用于资源清理
> ```
>
> #### 新拦截器 (SpringBoot2.x)
>
> ```python
> 设置方法：
> 	第一步：定义。自定义一个拦截器
> 	第二步：注册。在Configurer配置器中addInterceptor注册该拦截器
> 实战如下：
> 	1、定义
> 		和就拦截器用的完全是同一个拦截器
> 	2、注册
> 		@Configuration
> 		public class CustomWebMvcConfigurer implements WebMvcConfigurer {
>     		@Override
>     		public void addInterceptors(InterceptorRegistry registry) {
>         		registry.addInterceptor(new 																OneInterceptor()).addPathPatterns("/api2/*/**");
>         		WebMvcConfigurer.super.addInterceptors(registry);
>     		}
> 		}
> 	笔记1：只记录postman请求之后的执行顺序
> 		--requestListener Init
> 		--oneInterceptor preHandle
> 		--oneInterceptor postHandle
> 		--oneInterceptor afterCompletion
> 		--requestListener Destroy
> 	笔记2：还是记录一下容器启动时候的执行顺序
> 		--contextListener Init
> 		--filter init
> ```
>
> #### 两个拦截器
>
> ```python
> 设置方法：
> 	第一步：定义。定义两个拦截器。OneInterceptor、TwoInterceptor
> 	第二步：注册。分别对两个拦截器进行注册。
> 实战如下：
> 	1、OneInterceptor和上面的完全一样
> 		TowInterceptor如下：
> 		@Configuration
> 		public class TwoInterceptor implements HandlerInterceptor {
>     		@Override
>     		public boolean preHandle(HttpServletRequest request, HttpServletResponse 					response, Object handler) throws Exception {
>         		System.out.println("--twoInterceptor preHandle");
>         		return HandlerInterceptor.super.preHandle(request,response,handler);
>     		}
> 
>     		@Override
>     		public void postHandle(HttpServletRequest request, HttpServletResponse 						response, Object handler, ModelAndView modelAndView) throws Exception {
>         		System.out.println("--twoInterceptor postHandle");
>         		HandlerInterceptor.super.postHandle(request,response,handler,modelAndView);
>     		}
> 
>     		@Override
>     		public void afterCompletion(HttpServletRequest request, HttpServletResponse 				response, Object handler, Exception ex) throws Exception {
>         		System.out.println("--twoInterceptor afterCompletion");
>         		HandlerInterceptor.super.afterCompletion(request,response,handler,ex);
>     		}
> 		}
> 	2、分别对两个拦截器进行注册
> 		@Configuration
> 		public class CustomWebMvcConfigurer implements WebMvcConfigurer {
>     		@Override
>     		public void addInterceptors(InterceptorRegistry registry) {
>         		registry.addInterceptor(new 															OneInterceptor()).addPathPatterns("/api2/*/**");
>         		registry.addInterceptor(new 															TwoInterceptor()).addPathPatterns("/api2/*/**");
>         		WebMvcConfigurer.super.addInterceptors(registry);
>     		}
> 		}
> 	笔记1：两个拦截器的执行顺序
> 		--requestListener Init
> 		--oneInterceptor preHandle
> 		--twoInterceptor preHandle
> 		--twoInterceptor postHandle
> 		--oneInterceptor postHandle
> 		--twoInterceptor afterCompletion
> 		--oneInterceptor afterCompletion
> 		--requestListener Destroy      
> ```
>
> #### 注意
>
> ```python
> 1、拦截器不生效的常见的原因
> 	1）是否有加@Configuration。定义和注册的时候，都需要加这个注解
> 	2）拦截路径是否有问题 **  和 * 
> 	3）拦截器最后路径一定要 "/**"， 如果是目录的话则是 /*/
> 2、注册的时候新旧版本的区别
> 	@Configuration
> 	继承：WebMvcConfigurationAdapter(SpringBoot2.X之前旧版本)
> 	实现：SpringBoot2.X 新版本配置拦截器 implements WebMvcConfigurer
> 3、Filter和Interceptor的区别
> 	☆Filter是基于函数回调 doFilter()，而Interceptor则是基于AOP思想
> 	Filter在只在Servlet前后起作用，而Interceptor够深入到方法前后、异常抛出前后等
> 	Filter依赖于Servlet容器即web应用中，而Interceptor不依赖于Servlet容器所以可以运行在多种环境。
> 	☆在接口调用的生命周期里，Interceptor可以被多次调用，而Filter只能在容器初始化时调用一次。
> 	Filter和Interceptor的执行顺序
> 		过滤前->拦截前->action执行->拦截后->过滤后
> ```
>
> #### 笔记
>
> ```python
> 1、拦截器的应用场景：微服务都是用的token来进行会话管理，拦截器就可以从redis缓存中拿到token，进行判
> 	断，如果有，则放行，如果没有，而且是前后端分离，则返回json；如果没有，而且是不分离的话，返回	html错误页面。
>     .excludePathPatterns("/api2/xxx/**");
> 2、笔记2：拦截的匹配规则
> 	拦截匹配方法，最后一级要用**，匹配到的是方法。/**的话就是拦截所有
> 	也可以用链式匹配，registry.addInterceptor(new
> 	LoginInterceptor()).addPathPatterns("/api2/*/**");。如果在这个匹配规则下，有一部分不想
> 	拦截，则可以链式上加LoginInterceptor()).addPathPatterns("/api2/*/**")
> 3、笔记：
> 	preHandle:进入controller方法之前
> 	postHandle:调用完controller之后，视图渲染之前
> 	afterCompletion:整个方法完成之后，通常用于资源清理
> 4、学习回调函数怎么写
> 5、自定义的这些，各自的应用场景是什么
> ```
>

#### 20、SpringBoot Starter

> #### 官网地址
>
> ```python
> 参考 "管网文档" 章节
> #using-boot-starter
> ```
>
> #### 简介
>
> ```python
> 就是一个工具包，是一个jar包集合。里面把我们要用到的jar包都放进去
> ```
>
> #### 几个常用的starter
>
> ```python
> spring-boot-starter-freemarker
> spring-boot-starter-thymeleaf
> mybatis-spring-boot-starter
> spring-boot-starter-data-redis
> spring-boot-starter-data-elasticsearch
> spring-boot-starter-data-solr
> spring-boot-starter-activemq
> spring-boot-starter-webflux
> spring-boot-starter-actuator
> 
> spring-boot-starter-aop
> ```

#### 21、多环境配置

> #### application.yml
>
> ```python
> 配置方法：
>     spring:
>       profiles:
>         active: dev
>     ---
>     spring:
>       profiles: dev
>     server:
>       port: 8888
>     ---
>     spring:
>       profiles: pro
>     server:
>       port: 9999
> 注意：
> 	1> 三部分之间要有---分割
> 	2> 通过第一部分的active来控制选用那种环境配置
> 	3> 还可以通过---增加其他环境配置，比如开发、测试、预上线、生产、灰度
> ```
>
> #### application.properties
>
> ```python
> 配置方法：
> 	application-dev.properties配置文件内容：
> 		server.port=8888
> 	application-pro.properties配置文件内容：
> 		server.port=9999
> 	application.properties配置文件内容：
> 		spring.profiles.active=dev
> 注意：
> 	1> 多种环境，则多个配置文件
> 	2> 配置文件命名规范是固定的，application-后面的名称是active后面的名称
> 	3> 选用哪个配置文件，有application.properties中的active决定
> ```

















