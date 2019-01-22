### 不记文档，白忙一场

------

#### 报错信息

**1、Commit failed with error**

> ```python
> 报错信息：
> 0 files committed, 1 file failed to commit: 20181228郭世杰提交，全部覆盖为自己的代码 svn: E155011: Commit failed (details follow): svn: E155011: File 'H:\desktop\serviceHandle\src\main\java\com\inter\statistic\service\impl\AirportsRealStockServiceImpl.java' is out of date svn: E160024: resource out of date; try updating
> 解决办法：
> 	第一步：文件还原，即revert
> 	第二步：文件更新，即update
> 	第三步：文件覆盖，即把自己的代码覆盖该文件
> 	第四步：文件上传，即commit
> ```
>

#### 初次提交整个项目

> ​	前提：
>
> ```python
> 下面的过程都是在MyEclipse中操作的。
> ```
>
> ​	概况：
>
> ```python
> 1、已经有的项目svn路径有：
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/cnaf-cg
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/cnafColService
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/cnafInterfaceService
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/serviceHandle
> 2、我的项目名称为：cnafSelfControl
> 3、我项目在SVN上的地址应该为：							
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/cnafSelfControl
> ```
>
> ​	过程：
>
> ```python
> 1、SVN资源库下，右键，新建，资源库位置，URL中写	
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/cnafSelfControl，直接报错，
> 	找不到该位置。所以应该先找到已经存在的，父类的SVN地址，新建远程文件夹，而不是新建资源库位置。
> 2、SVN资源库下，右键，新建，远程文件夹，  输入或选择父文件夹的URL，写  		
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf，文件夹，写cnafSelfControl
> 3、SVN资源库下，找到https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf地址，下拉找到
> 	刚刚新建的cnafSelfControl文件夹，右键，导入，在workspace中找到自己的项目。
> 4、然后SVN资源库下，右键，新建，资源库位置，URL中写
> 	https://sinosoft.itends.org/svn/repos/project/Y2017/1127cnaf/cnafSelfControl，这次不报	 错。稍等一段时间，会看到项目中的文件已经有了SVN标识
> ```