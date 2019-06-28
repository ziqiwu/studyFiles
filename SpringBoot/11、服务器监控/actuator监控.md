### 不记文档，白忙一场

------

#### 0、基础

> #### 介绍什么是actuator
>
> ```python
> 1> 官方介绍：
> 	Spring Boot包含许多附加功能，可帮助您在将应用程序投入生产时监视和管理应用程序。 可以选择使用	HTTP端点或JMX来管理和监控您的应用程序，自动应用于审计，健康和指标收集;
> 2> 一句话：
> 	springboot提供用于监控和管理生产环境的模块
> ```
>
> #### 官方文档
>
> ```python
> https://docs.spring.io/spring-boot/docs/2.1.0.BUILD-SNAPSHOT/reference/htmlsingle/#production-ready
> ```

#### 1、实战步骤

> ```python
> 1> 加入依赖
> 	<dependency>  
> 		<groupId>org.springframework.boot</groupId>  
> 		<artifactId>spring-boot-starter-actuator</artifactId>  
> 	</dependency> 
> 2> 加入上述依赖后，访问几个url
>     /actuator/health
>     /actuator/info
>     /actuator
> ```

#### 2、详细配置

> #### 访问全部监控功能
>
> ```python
> application.yml中配置management.endpoints.web.exposure.include=*
> 注* 官网说明：https://docs.spring.io/spring-boot/docs/current-								SNAPSHOT/reference/htmlsingle/#boot-features-security-actuator
> 原因：出于安全考虑，除/ health和/ info之外的所有执行器默认都是禁用的。 							management.endpoints.web.exposure.include属性可用于启用执行器
> ```
>
> #### 建议
>
> ```python
> 在设置management.endpoints.web.exposure.include之前，请确保暴露的执行器不包含敏感信息和/或通过将其放置在防火墙进行控制，不对外进行使用
> 
> 禁用的端点将从应用程序上下文中完全删除。如果您只想更改端点所暴露的技术，请改用 include和exclude属性 
> 		
> 例子：
>     开启全部：management.endpoints.web.exposure.include=*
>     开启某个：management.endpoints.web.exposure.include=metrics
>     关闭某个：management.endpoints.web.exposure.exclude=metrics
> ```

#### 3、常用模块url

> ```python
> /health 	查看应用健康指标
> /actuator/metrics	查看应用基本指标列表
> /actuator/metrics/{name}		通过上述列表，查看具体 查看具体指标
> /actuator/env		显示来自Spring的 ConfigurableEnvironment的属性
> ```

#### 4、所有监控方法

> ```python
> 1、自带actuator
> 2、用springadmin进行管理
> 	相关资料：https://www.cnblogs.com/ityouknow/p/8440455.html
> 3、或者用自己编写脚本监控
> 	CPU、内存、磁盘、nginx的http响应状态码200,404,5xx 
> 注* 建议为第三种，因为前两种还是要占用JVM资源的
> ```

#### 注意

> ```python
> exposure.include值为所有的时候，.properties格式直接写*，如果是.yml格式，则需要写"*"，如果不加双引号会报错。
> ```