### 不记文档，白忙一场

------

#### 1、导入了druid.jar包和ojdbc6.jar包，但是连接数据库报错：java.lang.NoSuchMethodError: org.slf4j.spi.LocationAwareLogger.log(

> ```python
> 于是百度，找到一篇大神文章，链接https://www.cnblogs.com/dongqingswt/p/3605373.html
> 上面说，是jvm加载jar包冲突的原因，他用的是maven，所以删掉一个jar包。
> 
> 我的是普通项目，查看之后，发现一个J2EE6的java libraries，以前没有。在project properties中的build path中删除，再运行，没问题了。
> 
> 确定是druid.jar中和J2EE6中的某个jar包在JVM加载的时候冲突了。
> ```

#### 2、创建了项目，只有src包，没有src/main/java、src/main/resource等目录包

> ```python
> 方法一：点击src包下面的package，右键build path --> Use As Source Folder即可
> 注意：比如在src下创建了main，在main下又分别创建了java和resource包，则应该在最里面的java和			resource包上右键build path、
> 
> 方法二：直接在项目上右键，new --> source folder --> src/main/java
> ```

#### 3、报错信息：java.lang.NoClassDefFoundError: org/apache/commons/lang/StringUtils 

> ```python
> 缺少commons-lang-2.5.jar，将此jar加入工程的Build Path或者WebRoot/WEB-INF/lib下。
> 注：从报错信息中就可以看出，org/apache/commons/lang --> StringUtils类
> ```
>
> 

