### 不记文档，白忙一场

------

#### 0、zipkin部署

> #### 0、zipkin简介
>
> ```python
> 可视化链路追踪系统Zipkin部署
> 什么是zipkin?
> 大规模分布式系统的APM工具（Application Performance Management）,基于Google Dapper的基础实现，和sleuth结合可以提供可视化web界面分析调用链路耗时情况		
> ```
>
> #### 1、zipkin官网
>
> ```python
> https://zipkin.io/
> ```
>
> #### 2、同类产品
>
> ```python
> 鹰眼（EagleEye） -- 阿里链路追踪系统，没有开源
> CAT -- 大众点评开源
> twitter开源zipkin，结合sleuth
> Pinpoint，运用JavaAgent字节码增强技术
> StackDriver Trace (Google) 
> ```
>
> #### 3、开始使用 -- Quick Start
>
> ```python
> https://github.com/openzipkin/zipkin
> https://zipkin.io/pages/quickstart.html
>     
> 一共三种方式部署：
> 	1> docker -- 视频中使用的方式，简单
> 		docker run -d -p 9411:9411 openzipkin/zipkin
> 	2> git clone -- 比较复杂，还需要配置插件什么的
> 	3> 下载jar包
> 		curl -sSL https://zipkin.io/quickstart.sh | bash -s
> 		java -jar zipkin.jar
> 		注* 如果是window上面跑zipkin，则在linux上执行curl命令，然后把下载的jar包拖到window下
> 	注* There are three options: using Java, Docker or running from source.
> zipkin组成：Collector、Storage、Restful API、Web UI组成
> ```
>
> #### 4、知识拓展
>
> ```python
> OpenTracing
> OpenTracing 已进入 CNCF，正在为全球的分布式追踪，提供统一的概念和数据标准。 
> 通过提供平台无关、厂商无关的 API，使得开发人员能够方便的添加（或更换）追踪系统的实现。
> 
> 注* 就好像数据库连接接口，java和python连接的时候，数据库不会另外开接口，而是因为有统一的接口规范，所以厂商实现这个统一规范提供API。java和python再去实现这个API即可。
> ```
>
> #### 5、推荐阅读
>
> ```python
> http://blog.daocloud.io/cncf-3/
> https://www.zhihu.com/question/27994350
> https://yq.aliyun.com/articles/514488?utm_content=m_43347
> ```

#### 1、zipkin+sleuth实战

> #### 原理
>
> ```python
> sleuth收集跟踪信息通过http请求发送给zipkin server，zipkinserver进行跟踪信息的存储以及提供Rest API即可，Zipkin UI调用其API接口进行数据展示
> 
> 默认存储是内存，可也用mysql、或者elasticsearch等存储
> ```
>
> #### 实战记录
>
> ```python
> 第一步：启动zipkin的springboot项目
> 	因为我是在window上开发，也不想专门放在aliyun的linux上，所以用的是"zipkin部署"的第三种方式，
> 	在linux用curl命令下载jar包，拖到window上，用java命令启动。
> 第二步：所有相关项目加spring-cloud-starter-zipkin依赖
>     <dependency>
>     	<groupId>org.springframework.cloud</groupId>
>     	<artifactId>spring-cloud-starter-zipkin</artifactId>
>     </dependency>
> 	注*
> 	1> 因为这个依赖里面包含两个依赖：spring-cloud-starter-sleuth、spring-cloud-sleuth-zipkin，
> 		所以需要把之前加入的spring-cloud-starter-sleuth依赖注释掉，否则会重复。
> 	2> 需要把order和product两个项目中都加入spring-cloud-starter-zipkin依赖，否则在zipkin的控制		 台，查到的server，只有order一个（一开始我只在order项目中加入了依赖）。而且分析链路的时		候，分析不到product里面的耗时情况。
> 第三步：配置order_server的application
> 	spring:
> 		#zipkin服务所在地址 -- 也是一个springboot项目
> 		zipkin:
> 			base-url: http://localhost:9411/
> 
> 		#配置采样百分比
> 		sleuth:
> 			sampler:
> 				probability: 1
> 	注*
> 	1> ctrl + 点击probability进入源码，可以看到默认采样比例是0.1即百分之十。
> 		也就是说100次访问，会采样10次
> 	2> 建议，开发配置为1，生产配置默认的0.1就可以
> 第四步：访问order的下单接口
> 	http://localhost:9000/apizuul/order/api/v1/order/save?									user_id=2&product_id=3&token=safsfda
> 	注*
> 	1> 上面的地址，是因为加入了zuul和过滤之后的url样子
> 	2> save的下单接口，里面又调用了product的findById接口
> 第五步：访问zipkin界面
> 	访问http://localhost:9411/，查看链路的耗时情况。
> ```
>
> #### 官方文档
>
> ```python
> http://cloud.spring.io/spring-cloud-static/Finchley.SR1/single/spring-cloud.html#_sleuth_with_zipkin_via_http
>     
> http://cloud.spring.io/spring-cloud-static/Finchley.SR1/single/spring-cloud.html#_features_2
> ```
>
> #### 推荐资料
>
> ```python
> https://blog.csdn.net/jrn1012/article/details/77837710
> ```
>
> #### 记录
>
> ```python
> 1> 就是一个springboot项目，
> 	用java -jar启动，和用docker启动没有任何区别
> 2> 加入jar包之后，ctrl + 点击进入查看
> 3> zipkin的信息默认是存储在内存中的
> 4> 配置信息中的probability，点进去，可以看到对应方法，是0.1f，默认采样10%
> 5> 网关也有默认超时时间，断路器hystrix，服务调用feign
> ```