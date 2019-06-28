### 不记文档，白忙一场

------

#### 0、基础学习

> ```python
> 1> 为什么使用solr
> 	传统的SQL语言实现方式效率低下（条件众多，排序需求）
> 	1 SQL语言会很长
> 	2 公网项目，搜索频繁，如果每一个搜索页面都绑定一个庞大的SQL，一旦并发上来，SQL执行很慢，用户体
> 		验差，服务器压力增大。
> 	3 所以需要需用搜索引擎来改造这个功能。
> 2> 工作原理
> 	1 原来交互模式是，用户发送请求，然后到数据库查询数据返回数据
> 	2 现在solr是，用户发送请求，然后到搜索引擎中查询数据返回数据。搜索引擎会定期查询数据库进行增量
>     	更新。
> 3> 什么是solr
> 	1 基于Lucence的java搜索引擎服务器程序
> 		注* Lucene和solr都是Apache开发的，之前Lucene是一堆的jar包，如果我们想使用搜索引擎，就引
> 			入这些jar包进行开发。Apache为了简化我们的工作，然后基于Lucene开发了solr，solr是服务
> 			器程序，所以它是一个war包。现在如果我们想从底层开发，也可以使用Lucene这种形式。
> 	2 输出多种格式（XML/JSON等）
> 		注* 数据已经从数据库中导入了，它可以以不同格式输出来。
> 	3 建立索引，维护索引
> 	4 数据检索（全文检索、高亮显示、精确搜索）
> 4> 目录解读
> 	1 Solr_home
> 		一系列配置文件的目录，通过core（collection）来对配置文件进行管理。
> 		注* 比如，爱旅行项目中，酒店的数据就单独建一个core，机票相关的就建另一个core。
> 5> 安装步骤
> 	完全按照视频走
> 	注* solr7和solr4部署流程有略微差别
> 	待.....
> 6> 新建core
> 	1 拷贝collection
> 	2 修改配置文件
> 	3 重启Tomcat
> 	注* 删除core之前，需要停掉tomcat
> 7> 删除core
> 	直接在solr_home下将对应core目录delete掉
> 	注* 删除core之前，需要停掉tomcat
> 8> 我window上安装了solr4.9.1，linux上安装了solr7.7.2
> 9> solr管理数据库步骤
> 	1 拷贝数据库连接jar包到tomcat的lib目录
> 		注* 比如mysql-connector-jar-5.1.1.8.jar
> 		注* 因为solr是用java写的，所以它连接数据库操作数据肯定是通过JDBC的。
> 	2 配置数据源
> 		注* 即配置数据库用户名、密码、url等
> 		注* 然后solr就可以成功连接到数据库，写sql
> 	3 配置字段
> 	4 执行数据导入
> 	5 测试数据导入结果
> 10> 需要data-config.xml和schema.xml两个文件的原因？	
> 	注* 凡是修改了schema.xml都需要对数据进行重新导入的操作
> 	1 data-config.xml
> 		配置数据源
> 		写出对应的SQL
> 		将对应的数据导入到搜索引擎当中
> 	2 schema.xml
> 		定义搜索引擎对导入进来的数据进行什么样的处理
> 		a. 保留哪个字段，不保留哪个字段
> 		b. 要给哪个字段建索引，不给哪个字段建索引
> 11> 实现数据导入solr
> 	来源（配置文件）：https://blog.csdn.net/slqgenius/article/details/71712450
> 	注* 报错某些类class not found
> 		solr-dataimporthandler开头的两个jar包，必须放入的是tomcat下的solr项目的lib包中，而不是
> 		tomcat的lib中。
> 	注* 报错 org.apache.solr.common.SolrException: Invalid Number: MA147LL/A
> 		找到core中的evaluate.xml文件，注释掉最后一行以下内容
> 		<!--
>  			<query text="ipod">
>    				<doc id="MA147LL/A" />  
>    				<doc id="IW-02" exclude="true" /> 
>  			</query>
>  		-->
> 		解释：这个是solr的bug，要求主键id必须是string，不能是int
> 	步骤：
> 		1 添加数据库驱动到tomcat的lib目录下
> 		2 修改solrconfig.xml文件（在core的conf下），增加如下内容：
> 			<requestHandler name="/dataimport" 
>                   class="org.apache.solr.handler.dataimport.DataImportHandler">
> 				<lst name="defaults">
> 	    			<str name="config">data-config.xml</str>
> 				</lst>
>   			</requestHandler>
> 		3 新建data-config.xml
> 			注* 在solrconfig.xml的同级目录下，并没有data-config.xml文件，所以新建需要
> 			注* 内容如下：（配置数据源，配置sql，配置字段）
> 				<?xml version="1.0" encoding="UTF-8"?>
> 				<dataConfig>
> 					<dataSource type="JdbcDataSource" driver="com.mysql.jdbc.Driver" 							url="jdbc:mysql://127.0.0.1:3306/solrdb" user="root" 									password="123456"/>
> 					<document name="hotel_doc">
> 						<entity name="hotel" pk="id" query="select id,hotelName,address 							from hoteltb">
> 							<field column="id" name="id"/>
> 							<field column="hotelName" name="hotelName"/>
> 							<field column="address" name="address"/>
> 						</entity>
> 					</document>
> 				</dataConfig>
> 		4 修改schema.xml文件
> 			a.删除field标签（只留name="_version_"）、dynamicField、copyField的所有标签
> 			b.增加以下内容：
> 				<field name="id" type="int" indexed="true" stored="true"/>
>    				<field name="hotelName" type="string" indexed="true" stored="true"/>
>    				<field name="address" type="string" indexed="true" stored="true"/>
>    				<field name="text" type="text_general" indexed="true" stored="false" 						multiValued="true"/>
> 		5 生成hotel这个core报错，错误日志在管控台看到
> 			参考上面的注*
> 12> 实现增量更新	
> 	概述：
> 		增量更新：
> 	注* apache-solr-dataimportscheduler.jar可以在CSDN上下载
> 	注* dataimport.properties的坑
> 		设置了值的后面不要加空格，否则会读取的时候连空格都读取到。
> 	注* dataimport.properties整个文件模板可以在CSDN上下载
> 	1 导入增量更新jar包
> 		apache-solr-dataimportscheduler.jar放入solr项目中
> 		注* 是solr项目中，不是tomcat的lib下。因为这个监听器是solr项目要用到的
> 	2 配置增量更新文件
> 		solr_home下新建conf，conf下新建文件dataimport.properties
> 	3 增加增量更新监听器
> 		solr的web.xml增加监听器配置内容：
> 		<listener>
> 			<listener-class>
> 				org.apache.solr.handler.dataimport.scheduler.ApplicationListener
> 			</listener-class>
> 		</listener>
> 		注* 如果导入jar包位置放错，比如放在了tomcat的lib目录下，会报错监听器创建失败
> 	4 编写增量更新SQL
> 		core的conf下的data-config.xml增加两个属性，内容如下
> 		<entity name="hotel" pk="id" 
> 			query="select id,hotelName,address from hoteltb"
> 			deltaImportQuery="select id,hotelName,address from hoteltb where 							id='${dih.delta.id}'"
> 			deltaQuery="select id from hoteltb where modifydate > 										'${dih.last_index_time}'">
> 		注* 原来entity标签中，只有query属性，现在新增deltaImportQuery和deltaQuery
> 		注* deltaQuery中'${dih.last_index_time}'是固定写法，查找出上一次导入solr的时间
> 		注* deltaQuery中的modifydate是我们mysql定义的一个字段，是判断数据是否为最新的标准
> 		注* deltaImportQuery是将查询到的数据执行导入
> 	5 测试
> 		新增一条数据，一直点查询，1分钟后，发现可以在solr中查看到了，即管控台可以看到该新增数据。
> 13> 实现全文检索
> 	概述：
> 		全文检索：分析用户输入，并对用户输入进行拆分，组合等转化操作，根据转化后的数据对数据源数据
> 			进行检索，并将检索结果返回给用户
> 		分词器：将用户输入根据语义拆分成多个词语
> 		常见的中文分词器：
> 			word分词器
> 			Ansj分词器
> 			IKAnalyzer分词器
> 	步骤：
> 		1 下载IK
> 			注* 官网：https://github.com/medcl/elasticsearch-analysis-ik
> 			注* csdn：https://download.csdn.net/download/tjcyjd/8420639
> 			注* solr版本和IKAnalyzer版本需要对应一致
> 		2 解压
> 			将解压后文件中的IKAnalyzer2012FF_u1.jar放入solr项目中
> 			将IKAnalyzer.cfg.xm和stopword.dic放入solr中新建的WEB-INF/classes中
> 		3 修改core下的schema.xml，增加内容
> 			注* text_ik是我们新定义的一个类型，即只要我们定义了字段为该类型，就表明我们需要对它进
> 				行分词管理
> 			<fieldType name="text_ik" class="solr.TextField">
> 				<analyzer type="index" isMaxWordLength="false" 												class="org.wltea.analyzer.lucene.IKAnalyzer"/>
> 				<analyzer type="query" isMaxWordLength="true" 											class="org.wltea.analyzer.lucene.IKAnalyzer"/>
> 			</fieldType>
> 		4 将schema.xml中两个查询字段类型改为text_ik，测试结果
> 			<field name="hotelName" type="text_ik" indexed="true" stored="true"/>
> 			<field name="address" type="text_ik" indexed="true" stored="true"/>
> 			注* 原来他俩类型为string
> 		5 在管控台，选择一个core后，会有Analysis按钮
> 			选择一个字段，进行分词测试
> 			a. schema.xml中将字段类型改为text_ik再测试
> 			b. schema.xml中将字段类型改为string再测试	
> 		6 重新导入数据
> 			测试：模糊查询，结果不对，如q输入"hotelName:酒店"
> 			结果：返回结果为空
> 			分析：因为schema.xml中对字段类型修改过，从string改为text_ik，数据需执行重新导入。
> 				现在还是以字段为string，即只会进行精确匹配进行查询。
> 				如果q输入"hotel:酒店1"，则可精确匹配到1条数据。
> 			执行：core下选择Dataimport，点击Execute执行重新导入，再次测试，所有酒店都出来了
> 14> solr应用
> 	q：模糊匹配
> 	fq：对q的查询结果进行过滤（filter query）
> 		比如q是hotelName:北京，会查询出6条结果，如果增加fq为id=3 OR id=4，则只有两条结果
> 		注* fq在solr中执行完成之后，会对数据进行缓存。所以id或者type等在fq中设置，性能会高。
> 			而q中只进行模糊匹配查询。
> 	sort：排序
> 		比如：设置为"id asc"，则会对结果进行id的正序排序
> 	start,rows：分页（相当于pageSize和pageNum）
> 		注* start从0开始
> 	fl：指定返回字段
> 		注* 比如设置"id hotelName"，则查询出来的结果只显示这两个字段
> 	wt：指定输出格式（writer type）
> 		有json/xml等
> 15> 多字段匹配
> 	应用场景：用户并不知道我们把数据存在hotelName还是address中，提供了一个keyWord，
> 		所以我们需要在这两个字段中，都检索一遍。
> 	步骤：
> 		1 增加core下的schema.xml内容
> 			<field name="keyword" type="text_ik" indexed="true" stored="true" 						multiValued="true"/>
>    			<copyField source="hotelName" dest="keyword"/>
>    			<copyField source="address" dest="keyword"/>
> 			注* name="keyword"是我们自己创出来的字段，相比其他field，多了一个multiValued属性
> 			注* copyFiled即使将一个字段复制进keyword联合字段中。dest是destination的意思。
> 		2 重启tomcat
> 		3 重新执行数据导入
> 		4 测试，比如q设置"keyword:自如"，则会对hotelName和address同时进行检索
> 16> 使用java调用solr	
> 	注* 在应用中，solrj访问solr，对应的是，JDBC访问DB
> 	1 solr针对java调用开放了接口
> 		SolrJ-To connect from Java
> 		调用方式是http
> 		Apache开发
> 		除了java，还有ruby,PHP,python等语言的接口调用
> 	2 创建maven项目，导入依赖jar包
> 		注* 视频中的jar版本是5.3.1报错导入不了，maven官网上找了一个5.3.2
> 			官网：https://mvnrepository.com/artifact/org.apache.solr/solr-solrj
> 		<dependency>
>             <groupId>org.apache.solr</groupId>
>             <artifactId>solr-solrj</artifactId>
>             <version>5.3.2</version>
>         </dependency>
>         <dependency>
>             <groupId>org.slf4j</groupId>
>             <artifactId>slf4j-api</artifactId>
>             <version>1.7.25</version>
>         </dependency>
>         <dependency>
>             <groupId>commons-logging</groupId>
>             <artifactId>commons-logging</artifactId>
>             <version>1.2</version>
>         </dependency>    
> 	3 编写代码
> 	    注* url为"http://localhost:8080/solr/hotel"，格式：访问solr项目路径+core名称
> 		public class HotelService {
>             public void testSolr(String url) {
>                 //1.创建HttpSolrClient
>                 HttpSolrClient httpSolrClient = new HttpSolrClient(url);
>                 //配置解析器
>                 httpSolrClient.setParser(new XMLResponseParser());
>                 //配置连接超时时间
>                 httpSolrClient.setConnectionTimeout(500);
>                 //2.设置查询参数 solrQuery
>                 SolrQuery solrQuery = new SolrQuery(); //还有一个带参数的构造器，参数是q
>                 //设置q的查询参数
>                 solrQuery.setQuery("*:*");
>                 //设置fq的查询参数 TODO
>                 solrQuery.setFilterQueries();
>                 //设置排序
>                 solrQuery.setSort("id", SolrQuery.ORDER.desc);
>                 //设置分页开始
>                 solrQuery.setStart(0);
>                 //设置分页跨度
>                 solrQuery.setRows(10);
> 
>                 try {
>                     //3.创建QueryResponse数据接收对象
>                     QueryResponse queryResponse = httpSolrClient.query(solrQuery);
>                     List<Hotel> hotelList = queryResponse.getBeans(Hotel.class);
>                     for (Hotel hotel : hotelList) {
>                         System.out.println("----:"+hotel.getHotelName());
>                     }
>                 } catch (SolrServerException e) {
>                     e.printStackTrace();
>                 } catch (IOException e) {
>                     e.printStackTrace();
>                 }
>             }
>         }
> 	    注* Hotel实体类
> 	    注* 实体类即是solr返回数据和java对象的对应转换
> 	    public class Hotel implements Serializable {
>             @Field("id")
>             private Integer id;
>             @Field("hotelName")
>             private String hotelName;
>             @Field("address")
>             private String address;
>         }
> 17> solr项目封装
> 	/**
>      * 注意：泛型的使用，在类上面，也要加上<T>
>      * @param <T>
>      */
>     public class BaseDao<T> {
>         private HttpSolrClient httpSolrClient;
>         private QueryResponse queryResponse;
> 
>         public BaseDao(String url) {
>             httpSolrClient = new HttpSolrClient(url);
>             httpSolrClient.setParser(new XMLResponseParser());
>             httpSolrClient.setConnectionTimeout(500);
>         }
> 
> 
>         public List<T> querySolr(SolrQuery solrQuery,Class clazz) {
>             List<T> clazzList = null;
>             try {
>                 queryResponse = httpSolrClient.query(solrQuery);
>                 clazzList = queryResponse.getBeans(clazz);
>             } catch (SolrServerException e) {
>                 e.printStackTrace();
>             } catch (IOException e) {
>                 e.printStackTrace();
>             }finally{
>                 return clazzList;
>             }
>         }
>     }
>     注* 泛型：在类名后面也要加<T>
>     注* 方法参数用Class clazz，返回类型用<T>
>     注* 面向对象的意识：HttpSolrClient和QueryResponse是对象所属有的，提取出来，不混在方法中
> 注*
> 1> 为什么需要把tomcat停掉之后，再来war包的后缀备份起来？
> 	因为如果在tomcat启动状态下，修改war包后缀，这个时候tomcat就会认为我们把这个war包删掉了，这个时
> 	候tomcat会报war包解压出来的文件夹一起删掉。
> 	所以，需要先停掉tomcat，再修改war包后缀。
> 	注* 为什么备份war包，因为要直接修改项目，所以修改内容再打war包部署，不如直接修改解压之后的文件
> 2> solr集群搭建
> 	https://www.cnblogs.com/dijia478/p/8124751.html
> ```

#### 1、多表查询

> ```python
> https://blog.csdn.net/MeiX505/article/details/78469874
> ```



