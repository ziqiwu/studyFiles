### 不记文档，白忙一场

------

#### new一个package

> ```python
> 弹框出来是：
> 	Source folder --> cnafSelfControl/src
> 	Name --> selfControl.hbase
> 现在需求是心在hbase包下新建一个hbaseInter包：
> 	直接把Name后面的值改为selfControl.hbase.hbaseInter，即直接加了一个.hbaseInter
> ```

#### 只有src，没有src/main/java

> ```python
> 方法一：点击src包下面的package，右键build path --> Use As Source Folder即可
> 注意：比如在src下创建了main，在main下又分别创建了java和resource包，则应该在最里面的java和resource包上右键build path
> 
> 方法二：直接在项目上右键，new --> source folder --> src/main/java
> ```

#### 同时启动两个项目

> ```python
> 情景描述：两个maven项目，一个是接口项目，另一个是调用接口的项目
> Eclipse:两种方法
>     方法一：同时部署在一个tomcat中，启动，完事儿，没有试过，但应该可以。
>     方法二：通过配置JDK插件和tomcat插件，项目右键maven build --> 即可运行
>     	--> tomcat端口号可在插件的pom.xml中配置
>         示例：
>       		<!--JDK版本 -->
> 			<plugin>
> 				<groupId>org.apache.maven.plugins</groupId>
> 				<artifactId>maven-compiler-plugin</artifactId>
> 				<version>2.5.1</version>
> 				<configuration>
> 					<source>1.7</source>
> 					<target>1.7</target>
> 					<encoding>UTF-8</encoding>
> 					<showWarnings>true</showWarnings>
> 				</configuration>
> 			</plugin>
> 
> 			<!-- 配置Tomcat插件 ,用于启动项目 -->
> 			<plugin>
> 				<groupId>org.apache.tomcat.maven</groupId>
> 				<artifactId>tomcat7-maven-plugin</artifactId>
> 				<version>2.1</version>
> 				<configuration>
> 					<!-- 通过maven tomcat7:run运行项目时，访问项目的端口号 -->
> 					<port>8888</port>
> 					<!-- 项目访问路径  本例：localhost:9090,  如果配置的aa， 则访问路径为								localhost:9090/aa-->
> 					<path>/cnafInterfaceService</path>
> 					<uriEncoding>UTF-8</uriEncoding>
> 				</configuration>
> 			</plugin>
> IDEA：方法简单
> 	Run --> Edit Configurations --> Http port --> 配置tomcat的端口号，两个项目配置成不一样的
> 	--> JMX port --> 配置JDK的端口号，两个项目配置成不一样的
> 	注意：Http port默认是8080，JMX port默认是1099    	
> ```

