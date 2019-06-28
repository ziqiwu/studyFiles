### 不记文档，白忙一场

------

#### 0、启动生成IP

> ```python
> 第一步：cd /etc/sysconfig/network-script/
> 第二步：vi ifcfg-eth0
> 第三步：将onboot no改为onboot yes
> 第四步：reboot重启系统
> ```

#### 1、另一个程序锁定了yum...

> ```python
> 强制采用rm -f /var/run/yum.pid关闭yum进程即可
> ```

#### 2、yum安装不能解析阿里源

> ```python
> 报错："Couldn't resolve host 'mirrors.aliyun.com'"，Trying other mirror
> 解决：
> 	第一步：在网卡的配置文件中修改DNS
> 		vi /etc/sysconfig/network-scripts/ifcfg-eth0
> 		文末添加
>             DNS1=8.8.8.8
>             DNS2=8.8.4.4
> 	第二步：重启network 服务
> 		service network restart
> 来源：https://blog.csdn.net/zhugq_1988/article/details/47784031
> ```

#### 3、make报错jemalloc/jemalloc.h找不到

> ```python
> 基础：
>     1、tcmalloc，jemalloc和libc对应的三个内存分配器 性能优劣
>     2、malloc的全称是memory allocation，中文叫动态内存分配
>         allocate 美[ˈæləˌket]  v.分配
>         allocation  美[ˌæləˈkeɪʃn]  n.分配
>         allocator  美['æləkeɪtə]  n.分配器
>     3、来源：https://blog.csdn.net/libaineu2004/article/details/79400357
> 解决：
> 	指定内存分配器是lic，而不是默认的jemalloc
> 	make MALLOC=libc
> ```

