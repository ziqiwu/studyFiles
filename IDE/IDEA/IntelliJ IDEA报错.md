### 不记文档，白忙一场

------

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



