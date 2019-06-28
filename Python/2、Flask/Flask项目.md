### 不记文档，白忙一场

#### 搭建环境

```python
第一步：创建虚拟环境
1、python -m pip install --upgrade pip   --> 更新pip
2、pip install virtualenv   --> 安装虚拟环境包
3、pip install virtualenvwrapper-win    -->安装虚拟环境管理包（Linux环境下使用virtualenvwrapper） 
4、设置workon_home环境变量   -->在系统变量里新建即可， 变量名：WORKON_HOME，变量值：创建虚拟环境的目      录。不需要添加PATH
5、mkvirtualenv testevn   --> 创建虚拟环境
   (如果需要指定Python的版本，
   使用参数：--python=D:\ProgramData\Anaconda3\python.exe；
    如果需要使用公共的包，使用参数：--system-site-packages:)
6、激活虚拟环境  --> workon testevn
7、查看现有的虚拟环境   --> workon
8、退出虚拟环境    --> deactivate
9、删除虚拟环境    --> rmvirtualenv testevn
第二步：安装flask
1、mkvirtualenv flaskEnv  --> 创建虚拟环境
2、workon flaskenv  --> 进入虚拟环境
3、pip install flask  --> 安装flask
第三步：创建工程
1、桌面新建空文件夹，起名firstFlask。
2、File --> New Project --> 点击Location三个点找到桌面的firstFlask文件夹 --> 
	Project Interpreter --> Existing interpreter --> 点击三个点 --> Interpreter点击三个点 --> 
	找到D:\workon_home\env1\Scripts\python.exe(即自己新建的虚拟环境) --> 
	make available to all projects --> create --> open in a new window
3、右键项目 --> new --> python file --> Name --> 写manage.py --> 至此搭建完成  
```

#### 项目开发

**1、项目结构**

```python
project/
	
```

**2、项目模块**

> ```python
> 项目搭架子
> 	目录结构
> 	FLask跑起来的基础配置
> 	数据库表 --> Model
> 注册
> 	邮箱验证
> 登录
>     验证码验证
> 修改头像
> 	原来有
> 发表博客
> 	...
> 展示博客
> 	分页
> 缓存
> 	...
> 收藏
> 	用户和帖子之间是多对多的关系
> ```

**3、重写项目**

> ```python
> 尽量不写代码，尽量复制粘贴手上有的代码，但是要按模块一块儿一块儿来复现。
> ```