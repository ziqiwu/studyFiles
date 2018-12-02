### 不记文档，白忙一场

#### 开发：创建虚拟环境

```python
一、window：
1、python -m pip install --upgrade pip   -->更新pip
2、pip install virtualenv   -->安装虚拟环境包
3、pip install virtualenvwrapper-win    -->安装虚拟环境管理包（Linux环境下使用virtualenvwrapper） 
4、设置workon_home环境变量   -->在系统变量里新建即可， 变量名：WORKON_HOME，变量值：创建虚拟环境的目      录。不需要添加PATH
5、mkvirtualenv testevn   -->创建虚拟环境
   (如果需要指定Python的版本，
   使用参数：--python=D:\ProgramData\Anaconda3\python.exe；
    如果需要使用公共的包，使用参数：--system-site-packages:)
6、激活虚拟环境  -->workon testevn
7、查看现有的虚拟环境   -->workon
8、退出虚拟环境    -->deactivate
9、删除虚拟环境    -->rmvirtualenv testevn
```

