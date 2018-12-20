### 不记文档，白忙一场

------

#### 下载破解

```python
下载：idea官网：https://www.jetbrains.com/idea/
注意：32-bit的jdk在安装的时候，需要勾选，否则启动IDEA的时候有问题
激活：http://www.pydyun.com/idea-activation-localization.html#respond
方法一：注册码激活
	下载安装完成IDEA(安装过程不需要安装javax86)，弹出激活窗口，选择注册码，在lanyu网址
	http://idea.lanyus.com/最下方点击获取注册码，添加即可，到2019年5月
方法二：本地搭建激活服务器
	尝试未果
方法三：破解补丁激活
	我之所以卸载之前的IDEA就是应为，运行大项目idea会闪退，网友提供的原因，可能是补丁破解的后遗症。
	所以也就不尝试第二遍了。
```

#### eclipse项目迁移

```python
第一步：导入
1、如果怕搞坏eclipse项目，复制一份该项目到一个目录
2、一路Next
	File --> New --> Project from Existing Sources --> Import project from external model 
	--> Eclipse --> Next --> Keep project and moduals files in --> 复制到的那个目录 --> Next --> 	Open Project Struture after import(打勾都行) --> Next --> Use default project code style 
    --> Next --> Name -->JDK 1.7 --> JDK home path --> 自己的JDK安装路径 --> Finish
第二步：设置项目属性
1、注意：在Libraries中可以看到爆红的项，删除掉，点加号，重新导入，不是maven管理也可以。
2、项目右键 --> Open Module Settings --> 
	project --> Project compilter output --> H:\desktop\cnafSelfControl\out(项目名后面加out，表
	示out目录存放编译后的文件) -->
	
    Modules --> Dependencies --> 爆红的选中删掉，即点右侧的减号
    (org.eclipose.jst.j2ee.internal.web.container和		
	org.eclipose.jst.j2ee.internal.module.container) --> 剩余的全部勾选 --> Apply
    
    Libraries --> 中可以看到爆红的项，删除掉，点加号，重新导入，不是maven管理也可以。
	如果在设置里面，maven设置里面，设置了会下载jar包的Classes、Sources、JavaDocs，则Libraries里		面的后两项有的jar包没有，就会后两项爆红，删掉后两项即可，不会影响使用。
	如果后续build项目有报错找不到jar包，则再返回来导入
    
    Facets --> 加号 --> Web --> 选中项目 --> Deployment Descriptors --> path --> 点铅笔 --> 项目中
    选到web.xml --> Web Resource Directories --> H:\desktop\cnafSelfControl\WebContent -->
    source root --> create Artifacts --> Name --> 改成项目名称，这个名称是"http://ip:port/项名/"中
    的项目名 --> Available Elements --> 项目右键 --> put into output root --> Apply 
第三步：设置服务器属性
1、Run --> Edit Configurations --> Name --> 起一个名字 --> Deployment --> 加号 --> Artifacts -->
	Server --> URL中可以看到http://localhost:8082/cnafSelfControl/ --> 其中的canfSelfControl
	就是Open Module Settings的Artifacts中的Name --> Apply --> Run

注意：
1、新加一个jar包，在Artifacts的Avalible Elements下的项目，右键，Put into Output Root，新加的jar包就	会加入到左侧的output root下的WEB-INF下的lib中
2、跑起来tomcat，报错没有找到zookeeper的包里面的类，我打开lib下面确实没有，则：
	项目右键 --> Open Module Settings --> Modules --> 右侧加号 --> 单独把zookeeper.jar放到桌面导入
3、Tomcat 配置时点加号，不要点templates
4、run --> edit configurations --> deployment --> 加号 --> artifacts
5、项目 --> 右键 --> open models settings是重点，根据网友博客内容走 --> 				
	https://blog.csdn.net/eaphyy/article/details/72513914
	https://blog.csdn.net/pzasdq/article/details/52537337
6、搞了半天，网上百度了半天，误打误撞出来了
	(1)访问地址：http://localhost:8082/xjymHandle_war_exploded/index.html，而不是		
            http://localhost:8082/xjymHandle_war_exploded/index.html
	(2)我重新run --> tomcat server --> local --> 加号 --> name --> tomcat7.0.65_2
		deployment --> 加号 --> artifacts
		server --> url --> 自动生成的http://localhost:8082/xjymHandle_war_exploded/
	(3)比如想把路径改成http://localhost:8082/xjymHandleWar/则需要：
		第一步：项目右键 --> open models settings
		第二步：artifacts --> Name --> 改为xjymHandleWar
		第三步：新建一个本地的tomcat server --> deploymnet --> 加号 --> artifacts --> 名字已改变 
        	--> server --> 默认路径已改变
7、eclipse项目导入idea一共两步：
	第一步：项目右键 --> open models settings配置项目
	第二步：run --> edit configurations 配置tomcat server
```

#### eclipse的maven项目迁移

```python
https://blog.csdn.net/xzjayx/article/details/83142167
注意：
    maven中install的作用
    解释一：
    install与idea无关，它是maven的一个生命周期。
    maven常用生命周期：
    clean: 清除target目录
    install: 工程打包到本地仓库，这时本地项目可以依赖，别人是依赖不了的
    deploy: 将打包的jar文件上传到私服(如果有私服)，此时连接私服的人才可以下载依赖
    
    解释二：
    mvn install 将项目打成一个jar包，自动存放在了tomcat下，然后上传到服务器上去跑。
    
    解释三：
    install是将项目打成了jar包，和其他外部下载下来的jar包没有两样，在maven-repository中可以找到打成的		jar包。比如在idea中执行了install后，输出的信息有：Installing H:\desktop\新建文件夹				\serviceHandle\pom.xml to D:\maven3.3.9\maven-repository\cnaf\service\serviceHandle\0.0.1-	  SNAPSHOT\serviceHandle-0.0.1-SNAPSHOT.pom
	通过路径D:\maven3.3.9\maven-repository\cnaf\service\即可以找到该jar包
注意：
	配置完Open Module Settings之后，项目中是还不会出现out目录的。是配好了tomcat，其中有deployment点加	号，设置了Artifacts。点击tomcat的run之后，才会生成的。
注意：
	每个项目都需要在重新配置Maven的settings.xml的位置
    Help --> Find Action --> Maven --> User Settings File
第一步：导入
1、如果怕搞坏eclipse项目，复制一份该项目到一个目录
2、一路Next
	File --> New --> Project from Existing Sources --> Import project from external model 
	--> Maven --> Next --> Keep project and moduals files in --> 复制到的那个目录 --> Next --> 		Open Project Struture after import(打勾都行) --> Next --> Use default project code style 
    --> Next --> Name -->JDK 1.7 --> JDK home path --> 自己的JDK安装路径 --> Finish
第二步：设置项目属性
1、注意：Libraries --> 中可以看到爆红的项，删除掉，点加号，重新导入，不是maven管理也可以。需要把jar包名		字和版本号记录下来，下载也好，mven-repository中拉出来也好。导入就可以了。
   注意：Facets --> 如果Maven项目是有web.xml的web项目，则Facets会自动识别出现Web。如果只是一个Maven管	 理jar包的普通项目，则此处空白即可。
2、项目右键 --> Open Module Settings --> 
	project --> Project compilter output --> H:\desktop\cnafSelfControl\out(项目名后面加out，表
	示out目录存放编译后的文件) -->(一般out目录会自动加上)
	
    Modules --> Dependencies --> 爆红的选中删掉，即点右侧的减号
    (org.eclipose.jst.j2ee.internal.web.container和		
	org.eclipose.jst.j2ee.internal.module.container) --> 剩余的全部勾选 --> Apply
    
    Libraries --> 中可以看到爆红的项，删除掉，点加号，重新导入，不是maven管理也可以。
	如果在设置里面，maven设置里面，设置了会下载jar包的Classes、Sources、JavaDocs，则Libraries里		面的后两项有的jar包没有，就会后两项爆红，删掉后两项即可(不删除也可以)，不会影响使用。
	如果后续build项目有报错找不到jar包，则再返回来导入
    
    Facets --> 加号 --> Web --> 选中项目 --> Deployment Descriptors --> path --> 点铅笔 --> 项目中
    选到web.xml --> Web Resource Directories --> H:\desktop\cnafSelfControl\WebContent -->
    source root --> create Artifacts --> Name --> 改成项目名称，这个名称是"http://ip:port/项名/"中
    的项目名 --> Available Elements --> 项目右键 --> put into output root --> Apply 
    或者
    Facets --> 空白即可
第三步：设置服务器属性
1、Run --> Edit Configurations --> Name --> 起一个名字 --> Deployment --> 加号 --> Artifacts -->
	Server --> URL中可以看到http://localhost:8082/cnafSelfControl/ --> 其中的canfSelfControl
	就是Open Module Settings的Artifacts中的Name --> Apply --> Run
第四步：执行maven命令
1、方法一：
	View --> Tool Windows --> Maven projects --> 找到弹框中的项目里的Lifecycle --> clean或install
2、方法二：
	Help --> Find Action --> Maven Projects --> 找到弹框中的项目里的Lifecycle --> clean或install
```

#### MAVEN

```python
https://blog.csdn.net/westos_linux/article/details/78968012
第一步：下载maven
第二步：配置maven-repository
第三步：修改settings.xml中的mirror镜像地址，改为aliyun的镜像
第四步：修改IDEA中的maven配置
	1、File --> Settings --> Maven --> User settings file --> 勾选Override --> 地址改为自己的			settings.xml地址
	2、Local repository --> 勾选Override --> 地址改为自己的maven-repository地址
```

#### SVN

```python
一、配置SVN
	https://blog.csdn.net/qq_27093465/article/details/74898489
	第一步、下载小乌龟
		(1)小乌龟官网地址：https://tortoisesvn.net/downloads.html
		(2)下载x64的.msi版本
		(3)安装过程，记得勾选command line client tools，因为默认是不勾选的
	第二步、IDEA中配置svn.exe
		File --> settings --> Version Control --> Subversion --> 第一行框内输入 
		--> G:\TortoiseSVN\bin\svn.exe
	第三步、IDEA中svn加导出的地址
		VCS --> Browse VCS Repository --> Browse Subversion Repository --> 
		下方显示SVN Repository --> 点加号 --> 写入Repository URL
二、使用SVN
	https://blog.csdn.net/ningjiebing/article/details/79702467
	下方的Version Control --> 
	Local Changes --> 刷新--> 本地和SVN相比改过的文件
	Incoming --> 新添加入SVN的文件情况
```

#### 自带功能设置

```python
一、tab页分行显示
	Window --> Editor Tabs --> Tabs placement --> Show Tabs in Single Row --> 去掉对勾
二、字体、北京、样式等设置
	第一步：代码样式
    	File --> Settings --> Editor --> Font --> 右侧Font --> DejaVu Sans Mono
    第二步：编辑器样式
    	File --> Appearance & Behavior --> Appearance --> Theme --> High contrast --> 
    	use custom font --> DejaVu Sans Mono --> Size --> 14 --> Background Image -->
        样式选择倒数第三个(图片可以显示全)
        -->需要关闭该窗口重启，已经打开的窗口样式不会改变
	第三步：输出终端等样式
    	File --> Settings --> Color Scheme --> Console Font --> Font --> Consolas --> 
    	--> Size --> 15 --> Use console font instead of the default(DejaVu Sans Mono,15)
		-->打勾 
        --> 需要关闭该窗口重启，已经打开的窗口样式不会改变
三、主题设置
	第一步：下载主题jar包
    	http://www.riaway.com/
     第二步：导入主题
    	File --> import settings --> 选择下载的jar包
    	File --> Settings --> Editor --> Color Scheme --> Scheme --> 选择下载的jar包
	第三步：适合自己的主题风格
    	Nice Python

```

#### 快捷键

```python
1、生成getter、setter方法 
	alt + insert 
	注意：锁掉小键盘，0键就是insert键
2、鼠标跳出括号 
	跳出双引号：shift + "
    跳出单引号：shift + '
    跳出括号：shift + )
    跳出中括号：shift + ]
	以此类推
3、复制一行
	ctrl + D
4、删除一行
	ctrl + Y
5、关闭Tab页面
	shift + click(mouse)
6、调整 --> 箭头跳至上一次代码位置
	https://blog.csdn.net/u010814849/article/details/76682701/
```



#### 运行报错

```python
一、运行maven的项目，点击tomcat的run报错
   	问题：Error:Cannot build artifact 'ssm:war exploded' because it is included into a circular 		dependency
	解决：在Open Module Settings的Artifacts中，有三个Artiface，分别是
		cnafInterfaceService
		cnafInterfaceService:war
		cnafInterfaceService:war exploded
         删掉后两个，因为希望url中是http://ip:port/cnafInterfaceService/
二、debug某maven的项目，报错
	问题：source code does not match the bytecode
    	我的问题是一个maven项目，通过maven依赖另一个maven项目。被依赖的项目通过maven的install指令打成		Jar包。可是一运行依赖别的项目的这个项目，就包奇怪的错误，比如：sql中某个标识符无效，可是我的sql		中压根没有这个字段好伐。
		被逼无奈，只能debug，这可好，不debug还好，一debug报的错越是压根没有见到过。就是上面写道的：
		source code does not match the bytecode
		百度之后，大家的解决办法，大都是把项目重新build，重新编译。我把被依赖的项目重新build，重新			install，把依赖别的项目的这个项目也重新build。运行，还是不行
	解决：然后，在我打开依赖别的项目的这个项目的open moduals settings的Artifacts的时候，赫然又看到，			Artifacts又变成了三个
		cnafInterfaceService
		cnafInterfaceService:war
		cnafInterfaceService:war exploded
		然后就是和第一个问题一样，把后两个全部删掉，再运行，OK了
	后记：可能出现Artifacts变成三个的原因，我回想了一下之前的操作，我把改项目也进行了rebuild，可能是重		新编译的时候，出现了好几个Artifacts。
三、右键项目Rebuild Module报错
	问题：java source 1.5中不支持diamond 运算符(eclipse导入IDEA)
		比如在代码上Map<String,Object> map = new HashMap<>()，
		eclipse中的Map<String,Object> map = new HashMap<String,Object>()变成了上面的，
		这个运算符就叫diamond运算符(钻石运算符)
	解决：项目 --> 右键 --> Open Module Settings --> Modules --> Language level -->
		发现是5 - 'enum' keyword, generics, autoboxing etc. -->
		下拉选择为 --> 7 - Diamonds, ARM, multi-catch etc.  --> Apply --> OK 
四、打开IDEA之后，maven项目一直在updating indices，花费很长时间
	方案一：
    	删除文件夹 --> C:\Users\Administrator\.IntelliJIdea2018.3\system\caches
		对我的情况效果不大
    方案二：
    	和方案一类似，在caches上下手
		File --> Invalidate Caches / Restart --> Validate and Restart
		对我的情况效果不大
    方案三：
		分别在项目的几个文件夹：plug-in、swftools、zgis等文件夹上 --> 右键 --> Mark Directory as
		--> Exclusion
		update indices不再对这几个文件夹进行检测。因为这几个文件夹我不用，而且每次都花费绝大时间。		
        注意：该方法需要注意，选择了exclude是因为你的模块开发不需要这部分文件。如果你的模块运行是需要这			些文件的，千万不能标记为exclude，因为build项目/tomcat run时候的自动build，都不会包含这部分文		  件。
         
         比如:我把pulg-in标记成了exclude，连登录页面样式都扭曲了，而且登录的jQuery的函数也不能用，页
           面F12查看，一堆找不到resource --> Failed to load resource: the server responded with a 		   status of 404 (Not Found):bootstrap.css/jquery-1.8.3.min.js/jquery.cookie.js等等
		 
         所以：上面标记的时候，不能包括plugin-in这个文件夹
五、软件一段时间就闪退
	问题：打开项目多的时候，特别是里面有大项目的时候，就会发生软件闪退。把IDEA安装包下的bin下的				idea64.exe.vmoptions和idea64.exe.vmoptions中的-Xmx最大内存改为1024m。没有解决问题
	解决：是因为用补丁破解的IDEA的原因，用第三方服务器破解就可以搞定
		东云网首页就有置顶的方法
		http://www.pydyun.com/
六、JSP页面标签处报错
	问题：原来在eclipse中显示正常的jsp页面，在idea的div结束标签处爆红，显示：Element span is not 			closed。可是原来正常，而且span的没有结束标签，你在div结束标签处给我报错，我猜想肯定是idea的设			置出错。
	解决：最后还百度下了plugins中jsp的一个插件，没有效果，最后在这个爆红的div中果真找到了其中一个span标		  签结束标签写错了。写成了<span>排序方式<span>。idea够强大的，检查够仔细，但是能在span处报错就更		   好了。
```

#### indexing在干嘛

```python
第一步：IntelliJ IDEA超快的搜索速度和强大的代码提示就是依靠缓存实现的。
	缓存文件很大，建立缓存也很花时间，在建立缓存时如果遇到断电或者强退等问题会导致以后打开文件出错等问
	题，解决办法就是把以前的缓存清理掉。
	缓存的的文件在:C:\Users\Administrator\.IntelliJIdea2018.3\system\caches
第二步：下面介绍如何清理缓存。
	File --> Invalidate Caches / Restart --> Validate and Restart
	我们选择清空并重启，这次启动需要重新建立索引，会花很长时间。
	我们找到缓存所在的硬盘目录，发现里面原来几百兆的东西，只剩下不到1兆了。
	打开上次打开的文件会出现一直Loading的现象，这很正常，是在重新建立索引。
	缓存文件很快增大到几十兆了，随着你的日常使用，很快又会增大到几百兆。
	也可以在启动idea前直接把这个chache文件夹删除，启动后也会正常重新建立索引。
网友同样问题：
	开发一个项目，需要一个很大的前端库，但是每次拷贝进去的时候都会触发 index，index 的速度也很慢，就算 	index 完成了敲代码也是一卡一卡的，所以希望能排除这个文件夹让其不 index，但是一直没有找到这个设置，		请问在哪设置？

	我在文件夹右键 Mark Directory as -> Excluded 这样不会 index 了，但是一用 springboot debug 运		行，此文件夹的文件就会 404
网友相似问题：
	一直在indexing
    这个是缓存库中的文件有问题，比如indexing的时候突然断电，或强制退出，删掉cache文件，清空，或者file下	  选项即可解决。即第一步和第二步的办法。
权宜之计：
	index的时候，把耗时间的文件排除出去，exclude，index之后再加回来
	分别在项目的几个文件夹：plug-in、swftools、zgis等文件夹上 --> 右键 --> Mark Directory as
	--> Exclusion	
	因为不加回来就会像第一个网友那样，404    
```

#### 同时启动两个项目

```python
情景描述：两个maven项目，一个是接口项目，另一个是调用接口的项目
Eclipse:两种方法
    方法一：同时部署在一个tomcat中，启动，完事儿，没有试过，但应该可以。
    方法二：通过配置JDK插件和tomcat插件，项目右键maven build --> 即可运行
    	--> tomcat端口号可在插件的pom.xml中配置
        示例：
      		<!--JDK版本 -->
			<plugin>
				<groupId>org.apache.maven.plugins</groupId>
				<artifactId>maven-compiler-plugin</artifactId>
				<version>2.5.1</version>
				<configuration>
					<source>1.7</source>
					<target>1.7</target>
					<encoding>UTF-8</encoding>
					<showWarnings>true</showWarnings>
				</configuration>
			</plugin>

			<!-- 配置Tomcat插件 ,用于启动项目 -->
			<plugin>
				<groupId>org.apache.tomcat.maven</groupId>
				<artifactId>tomcat7-maven-plugin</artifactId>
				<version>2.1</version>
				<configuration>
					<!-- 通过maven tomcat7:run运行项目时，访问项目的端口号 -->
					<port>8888</port>
					<!-- 项目访问路径  本例：localhost:9090,  如果配置的aa， 则访问路径为								localhost:9090/aa-->
					<path>/cnafInterfaceService</path>
					<uriEncoding>UTF-8</uriEncoding>
				</configuration>
			</plugin>
IDEA：方法简单
	Run --> Edit Configurations --> Http port --> 配置tomcat的端口号，两个项目配置成不一样的
	--> JMX port --> 配置JDK的端口号，两个项目配置成不一样的
	注意：Http port默认是8080，JMX port默认是1099    	
```

#### 打war包

```python
一、maven项目
	view --> Tool Windows --> Maven --> 添加自己的maven项目(如果有则不需要点加号添加)
	--> Lifecycle --> deployment --> 会在输出信息中有下面的一条信息    
	[INFO] Building war: H:\desktop\新建文件夹(2)\cnafInterfaceService\target\
	cnafInterfaceService.war的信息
	--> 到对应文件路径可以找到该war包    
```

#### 热部署

```python
IDEA热部署，修改代码不需要重启tomcat
https://blog.csdn.net/j_u_n1991/article/details/78859211
第一步：在Debug模式下
第二步：配置tomcat如下
	On 'Update' action:Update classes and resources
	On frame deactivation:Update classes and resources
	注意：1代表手动点击更新动作时（可用快捷键ctrl+F9），编译更新代码和资源； 2代表idea失去焦点时     
```



