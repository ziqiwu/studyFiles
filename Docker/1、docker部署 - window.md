### 不记文档，白忙一场

------

#### 0、安装包来源

> ```python
> https://blog.csdn.net/Lixuanshengchao/article/details/81019944
> ```

#### 1、大神出错解决

> ```python
> https://www.cnblogs.com/ecology-lee/p/10017992.html
> ```

#### 2、我的安装记录

> ```python
> 1> 从"安装包来源下载.exe文件"，选择方式二安装
> 2> 一切顺利，安装完成后，桌面生成三个图标。双击Docker Quickstart Terminal
> 3> 启动报错"looks like something went wrong in step ‘looking for vboxmanage.exe’"
> 4> 按照"大神出错解决"的办法操作
> 5> 在安装目录D:\Docker\Docker Toolbox下编辑start.sh
> 	1、echo "安装路径测试：${DOCKER_TOOLBOX_INSTALL_PATH}"
> 	2、read param #自定义断点，否则程序继续执行
> 	3、发现docker安装路径${DOCKER_TOOLBOX_INSTALL_PATH}在控制台输出为空
> 	4、手动定义变量，给DOCKER_TOOLBOX_INSTALL_PATH赋值
> 	5、DOCKER_TOOLBOX_INSTALL_PATH="D:\Docker\Docker Toolbox"
> 	6、再次启动Docker Quickstart Terminal，输出没有找到boot2docker.iso
> 	7、将"安装包来源"中的boot2docker.iso放在C:\Users\Administrator\.docker\machine\cache下
> 	8、该目录下有很多同名的.temp文件，全部删除，是下载失败的文件
> 	9、再次启动Docker Quickstart Terminal，输出boot2docker.iso过期了out of date
> 		正在从github的地址下载
> 	10、复制该地址，从浏览器打开，会选择目录下载。完成后，还是放在									C:\Users\Administrator\.docker\machine\cache目录下
> 	11、再次启动Docker Quickstart Terminal，成功！！
> 注* 第一次成功启动的时候，花费时间较长！！之后，再次启动，很快。。
> ```

#### 3、安装rabbitmq

> #### 步骤
>
> ```python
> 1> docker images
> 2> docker ps
> 3> docker pull rabbitmq:management
> 4> docker run -d --name xiaoguozimq -p 15672:15672 -p 5672:5672 rabbitmq:management
> 5> 网页访问:
> 	http://192.168.99.100:15672/#/
> ```
>
> #### 注意
>
> ```python
> 访问地址：不是localhost:15672
> 因为docker是一个虚拟出来的容器，启动的时候，会打印出：
> docker is configured to use the default machine with IP 192.168.99.100
> ```

#### 记录

> ```python
> 1> docker window下的密码：
> 	https://www.jianshu.com/p/db768f5e6cdb
> 2> docker window打包springboot镜像
> 	https://blog.csdn.net/why154285/article/details/81067772
>         
>         
> 3> 控制台输出如下：
>     root@default:/tmp# docker build -t front:1.0-SNAPSHOT .
>     Sending build context to Docker daemon  18.31MB
>     Step 1/6 : FROM java:8
>     8: Pulling from library/java
>     5040bd298390: Pull complete 
>     fce5728aad85: Pull complete 
>     76610ec20bf5: Pull complete 
>     60170fec2151: Pull complete 
>     e98f73de8f0d: Pull complete 
>     11f7af24ed9c: Pull complete 
>     49e2d6393f32: Pull complete 
>     bb9cdec9c7f3: Pull complete 
>     Digest: sha256:c1ff613e8ba25833d2e1940da0940c3824f03f802c449f3d1815a66b7f8c0e9d
>     Status: Downloaded newer image for java:8
>      ---> d23bdf5b1b1b
>     Step 2/6 : VOLUME /tmp
>      ---> Running in 4c43ab48b28c
>     Removing intermediate container 4c43ab48b28c
>      ---> 8afc997b43f6
>     Step 3/6 : ADD docker-demo.jar app.jar
>      ---> 2fcb811f83ed
>     Step 4/6 : RUN sh -c 'touch /app.jar'
>      ---> Running in 09d5aa948d72
>     Removing intermediate container 09d5aa948d72
>      ---> 9fcb331c9bed
>     Step 5/6 : ENV JAVA_OPTS=""
>      ---> Running in 7684fc8135fe
>     Removing intermediate container 7684fc8135fe
>      ---> f4352dbeb706
>     Step 6/6 : ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]
>      ---> Running in 25a424e40e4a
>     Removing intermediate container 25a424e40e4a
>      ---> 72a3268febf0
>     Successfully built 72a3268febf0
>     Successfully tagged front:1.0-SNAPSHOT
> 
> ```
>
> #### 步骤记录
>
> ```python
> 1> 照视频做
> 2> maven执行打包命令，在target中复制出来jar包
> 3> 创建Dockerfile文件，编辑命令，复制出来
> 4> 登录virtualbox，进入默认的虚拟机，已经安装了docker
> 5> 将jar包和Dockerfile赋值到同一个目录下，执行命令docker build -t front:1.0-SNAPSHOT .
> ```
>
> #### 醒悟
>
> ```python
> 在window上安装docker并没有什么好稀奇。
> 不过是virtualbox虚拟出一个虚拟机，
> 在虚拟机上安装docker，
> 然后把springboot项目和Dockerfile项目放入虚拟机，执行docker命令而已。
> ```