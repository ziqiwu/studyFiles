### 不记文档，白忙一场

------

#### 0、获取注册码

> ```python
> 1> 我用的是网上lanyu的注册码，到期时间为2019/05/04
> 2> 当时hosts文件加了一行0.0.0.0 account.jetbrains.com
> 3> 到期之后，登录了http://idea.lanyus.com/
> 4> 编辑 C:\Windows\System32\drivers\etc
> 	增加：
>         0.0.0.0 account.jetbrains.com
>         0.0.0.0 www.jetbrains.com
> 5> 点击"获得注册码"，ctrl + c
> 6> cmd --> pycharm64 --> 提示enter licences --> 选择activation code --> ctrl + v
> 7> ctrl + v 粘贴新的注册码 --> ok
> 8> 再次查看pycharm到期时间，变为了2020/03/11
> 注* 虽然pycharm到期时间，变为了2020/03/11。但是我相信，快到期之前，lanyu官网会同步更新的。
> ```

#### 1、自带功能设置

> ```python
> 一、tab页分行显示
> 	Window --> Editor Tabs --> Tabs placement --> Show Tabs in Single Row --> 去掉对勾
> 二、字体、北京、样式等设置
> 	第一步：代码样式
>     	File --> Settings --> Editor --> Font --> 右侧Font --> DejaVu Sans Mono
>     第二步：编辑器样式
>     	File --> Appearance & Behavior --> Appearance --> Theme --> High contrast --> 
>     	use custom font --> DejaVu Sans Mono --> Size --> 14 --> Background Image -->
>         样式选择倒数第三个(图片可以显示全)
>         -->需要关闭该窗口重启，已经打开的窗口样式不会改变
> 	第三步：输出终端等样式
>     	File --> Settings --> Color Scheme --> Console Font --> Font --> Consolas --> 
>     	--> Size --> 15 --> Use console font instead of the default(DejaVu Sans Mono,15)
> 		-->打勾 
>         --> 需要关闭该窗口重启，已经打开的窗口样式不会改变
> 三、主题设置
> 	第一步：下载主题jar包
>     	http://www.riaway.com/
>      第二步：导入主题
>     	File --> import settings --> 选择下载的jar包
>     	File --> Settings --> Editor --> Color Scheme --> Scheme --> 选择下载的jar包
> 	第三步：适合自己的主题风格
>     	Nice Python
> 
> ```
>

#### 2、快捷键

> ```python
> 1、生成if `__name__` == '__main__': --> 键入main，就会有提醒出现
> ```
>

#### 3、运行报错

> ```python
> 一、pycharm.exe启动不了
> 	问题：下载pycharm的时候，没有下载x86的jdk，点击pycharm下的bin下的pycharm.exe报错，启动不了
> 	解决：我在pycharm包下发现了jre64包，所以点pycharm64.exe成功启动了。
>     	之前看网上，C:\Users\Administrator\.PyCharm2018.3\config路径下的pycharm.exe.jdk编辑器打			开，写入自己电脑有的32位jdk到bin。pycharm64.exe.jdk写入自己电脑有的64位jdk到bin。就可以实现		  用自己的jdk来启动pycharm。不过pycharm包下有jre64包，看来Pycharm自带了64位的，没有带32位的，所		 以pycharm.exe不能启动，但是pycharm64.exe可以。
>          注：idea下载点了x86jre，idea的安装包下有jre64和jre32两个包
> ```
>

