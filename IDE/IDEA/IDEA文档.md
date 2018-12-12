### 不记文档，白忙一场

------

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

#### 配置MAVEN

```python
https://blog.csdn.net/westos_linux/article/details/78968012
第一步：下载maven
第二步：配置maven-repository
第三步：修改settings.xml中的mirror镜像地址，改为aliyun的镜像
第四步：修改IDEA中的maven配置
	1、File --> Maven --> User settings file --> 勾选Override --> 地址改为自己的settings.xml地址
	2、Local repository --> 勾选Override --> 地址改为自己的maven-repository地址
```

#### 配置SVN

```python
https://blog.csdn.net/qq_27093465/article/details/74898489
第一步、下载小乌龟
	(1)小乌龟官网地址：https://tortoisesvn.net/downloads.html
	(2)下载x64的.msi版本
	(3)安装过程，记得勾选command line client tools，因为默认是不勾选的
第二步、IDEA中配置svn.exe
	File --> settings --> Version Control --> Subversion --> 第一行框内输入 
	--> G:\TortoiseSVN\bin\svn.exe
第三步、IDEA中svn加导出的地址
	VCS --> Checkout from Version Control --> Subversion --> 点击加号 --> 加入检出地址
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

#### 运行报错

```python
一、运行maven的项目，点击tomcat的run报错
   	问题：Error:Cannot build artifact 'ssm:war exploded' because it is included into a circular 		dependency
	解决：在Open Module Settings的Artifacts中，有三个Artiface，分别是
		cnafInterfaceService
		cnafInterfaceService:war
		cnafInterfaceService:war exploded
         删掉后两个，因为希望url中是http://ip:port/cnafInterfaceService/
```

