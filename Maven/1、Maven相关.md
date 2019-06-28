### 不记文档，白忙一场

------

#### 0、mvn命令打包ojdbc6

> ```python
> mvn install:install-file -Dfile=H:\chrome_down_pack\jar\ojdbc6-11.2.0.1.0.jar -DgroupId=com.oracle -DartifactId=ojdbc6 -Dversion=11.2.0.1.0 -Dpackaging=jar -DgeneratePom=true
>         
> 注* 1> -Dfile是file的位置
>     2> -DgroupId是groupId的命名
>     3> -DartifactId是artifactId的命名
>     4> -Dversion是version版本号
>     5> -Dpackaging是packaging打包方式
>     6> -DgeneratePom是生成pom
> ```

#### 1、mvn命令打包java项目

> ```python
> CMD下：
>     mvn clean package -Dmaven.test.skip=true
> powershell下：
> 	mvn clean install package '-Dmaven.test.skip=true'
> 注* 一定不要写成mvn package clean -Dmaven.test.skip=true
> 	那样的话，每次target包中都是空的，因为先执行打包，后执行清除，每次都把刚打的包清除了。
> ```

#### 2、SNAPSHOT版本含义

> #### 简介
>
> ```python
> 深入理解MAVEN中SNAPSHOT版本和正式版本的区别
> 注* snap v.拍照；拍..的快照
> 	shot v.射击
> ```
>
> #### 来源
>
> ```python
> https://www.cnblogs.com/huang0925/p/5169624.html
> 注* 引申知识点 --> maven的pom.xml中repositories标签的作用
> 	https://blog.csdn.net/jikefzz1095377498/article/details/81629941
> ```
>
> #### 概述
>
> ```python
> 在Nexus仓库中，一个仓库一般分为public(Release)仓和SNAPSHOT仓，前者存放正式版本，后者存放快照版本。
> 
> 快照版本和正式版本的主要区别在于，本地获取这些依赖的机制有所不同。
> 
> 假设你依赖一个库的正式版本，构建的时候构建工具会先在本次仓库中查找是否已经有了这个依赖库，如果没有的话才会去远程仓库中去拉取。
> 
> 假设你依赖一个库的快照版本，每次项目构建时，会优先去远程仓库中查看是否有最新的依赖项目。
> ```

#### 3、Alpha、RC、GA版本含义

> #### 简介
>
> ```python
> 版本列表：
> 	Alpha、Beta、RC、GA、RTM、OEM、RVL、EVAL、RTL
> 	SNAPSHOT也是其中一种
> 一般会标识CURRENT，标识最新版本
> ```
>
> #### 备注
>
> ```python
> General Availability  一般可用性
> ```
>
> #### 概述
>
> ```python
> GA: 
> 	General Availability,正式发布的版本，在国外都是用GA来说明release版本的。
> ```
>
> #### 来源
>
> ```python
> https://blog.csdn.net/liliiii/article/details/45559139
> ```

#### 4、M1版本的含义

> #### 英文全称
>
> ```python
> M是MILESTONE的简写，里程碑的意思
> ```
>
> #### 示例
>
> ```python
> Spring Boot 2.2 首个里程碑版本 M1 已于昨天发布，可从里程碑仓库获取。官方表示该版本关闭了 140 多个 issue 和 PR。
> 
> 有以下值得关注的更新：
> 
> 将依赖项 Spring Data Moore 升级至 M2 版本
> 提高配置属性数量较多时的绑定速度
> 对 bean 进行延迟初始化的可选择支持
> 默认情况下禁用 JMX
> 其他依赖升级
> 使用执行器时，启动速度更快，内存占用更少
> 延迟初始化 (Lazy initialization)
> 
> 现在可以通过spring.main.lazy-initialization属性启用全局延迟初始化以减少启动时间。请注意，使用该功能会产生一定的性能开销：
> 
> 在启用任何延迟初始化时，处理 HTTP 请求可能需要更长时间
> 
> 通常在启动时发生的故障，现在可能会在启动后才发生
> 
> 详情请查看发布说明。
> 
> 如果希望使用 2.2 并尝试新功能，不妨在 https://start.spring.io 上引导一个新项目。
> ```
>
> #### 来源
>
> ```python
> https://www.oschina.net/news/105019/spring-boot-2-2-m1-released
> ```

#### 5、BUILD-xxx、SR版本含义

> #### 版本号含义
>
> | 版本号     | 含义       | 备注                                                         |
> | :--------- | :--------- | :----------------------------------------------------------- |
> | BUILD-XXX  | 开发版     | 一般是开发团队内部用的                                       |
> | GA         | 稳定版     | 内部开发到一定阶段了，各个模块集成后，经过全面测试，发现没有问题了，可以对外发型了，这个时候就叫GA（AenrallyAvailable）版，系统的核心功能已经可以使用。意思就是基本上可以使用了。 |
> | PRE(M1,M2) | 里程碑版   | 由于GA版还不属于公开的发行版，里面还有功能不完善的或者一些BUG，于是就有了milestone（里程碑）版，milestone版本主要修复一些BUG和调整UI。一个GA后，一般有多个里程碑，例如 M1 M2 M3 |
> | RC         | 候选发布版 | 从BUILD后GA再到M基本上系统就定型了，这个时候系统就进入RELEASE                                   candidates（RC候选发布）版，该阶段的软件类似于最终发行前的一个观察期，该期间只对一些发现的等级高的BUG进行修复，发布RC1,RC2等版本。 |
> | SR         | 正式发布版 | super rare 公开正式发布。正式发布板一般也有多个发布，例如SR1 SR2 SR3等等，一般是用来修复大BUG或优化。 |
>
> #### 来源
>
> ```python
> https://blog.csdn.net/a290450134/article/details/86635897
> ```

#### 6、pom修改maven仓库地址

> ```python
> 	补充： 修改maven仓库地址
> 	pom.xml中修改
> 
> 	<repositories>
>         <repository>
>             <id>nexus-aliyun</id>
>             <name>Nexus aliyun</name>
>             <layout>default</layout>
>             <url>http://maven.aliyun.com/nexus/content/groups/public</url>
>             <snapshots>
>                 <enabled>false</enabled>
>             </snapshots>
>             <releases>
>                 <enabled>true</enabled>
>             </releases>
>         </repository>
>     </repositories>
>     注* settings.xml中也可以修改，但是那是全局的，上面的修改时针对某一个项目的。
> ```