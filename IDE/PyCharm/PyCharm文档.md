### 不记文档，白忙一场

------

#### 下载破解

```python
https://blog.csdn.net/u014044812/article/details/78727496
下载：idea官网：https://www.jetbrains.com/pycharm/
	注意：32-bit的jdk在安装的时候，需要勾选，否则启动IDEA的时候有问题
激活：有三种方法
	方法一：注册码激活
		下载安装完成IDEA(安装过程不需要安装javax86)，弹出激活窗口，选择注册码，在lanyu网址
		http://idea.lanyus.com/最下方点击获取注册码，添加即可，到2019年5月
	方法二：本地搭建激活服务器
		未尝试
	方法三：破解补丁激活
		未尝试
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
1、生成if `__name__` == '__main__': --> 键入main，就会有提醒出现
```

#### 运行报错

```python
一、pycharm.exe启动不了
	问题：下载pycharm的时候，没有下载x86的jdk，点击pycharm下的bin下的pycharm.exe报错，启动不了
	解决：我在pycharm包下发现了jre64包，所以点pycharm64.exe成功启动了。
    	之前看网上，C:\Users\Administrator\.PyCharm2018.3\config路径下的pycharm.exe.jdk编辑器打			开，写入自己电脑有的32位jdk到bin。pycharm64.exe.jdk写入自己电脑有的64位jdk到bin。就可以实现		  用自己的jdk来启动pycharm。不过pycharm包下有jre64包，看来Pycharm自带了64位的，没有带32位的，所		 以pycharm.exe不能启动，但是pycharm64.exe可以。
         注：idea下载点了x86jre，idea的安装包下有jre64和jre32两个包
```

