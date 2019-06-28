### 不记文档，白忙一场

------

#### 0、查看资源占用情况

> #### 一共12种
>
> ```python
> https://www.cnblogs.com/zhuiluoyu/p/6154898.html
> ```
>
> #### 常用
>
> ```python
> 1、free -h或者free -m
> 2、ps aux --sort=%mem（正序） 或者  ps aux --sort=-%mem  （倒叙）
> 3、top
> ```
>

#### 1、free命令内容详解

> #### 来源
>
> ```python
> https://www.cnblogs.com/pengdonglin137/p/3315124.html
> ```
>
> #### 详解
>
> ```python
> 实际内存占用：used-buffers-cached 即 total-free-buffers-cached
> 实际可用内存：buffers+cached+free
> 
> uffers是指用来给块设备做的缓冲大小，他只记录文件系统的metadata以及 tracking in-flight pages.
> cached是用来给文件做缓冲。
> 那就是说：buffers是用来存储，目录里面有什么内容，权限等等。而cached直接用来记忆我们打开的文件
> ```

#### 2、查看CPU个数、核数

> ```python
> # 总核数 = 物理CPU个数 X 每颗物理CPU的核数 
> # 总逻辑CPU数 = 物理CPU个数 X 每颗物理CPU的核数 X 超线程数
> 
> # 查看物理CPU个数
> cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
> 
> # 查看每个物理CPU中core的个数(即核数)
> cat /proc/cpuinfo| grep "cpu cores"| uniq
> 
> # 查看逻辑CPU的个数
> cat /proc/cpuinfo| grep "processor"| wc -l
> ```





