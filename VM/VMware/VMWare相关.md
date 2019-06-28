### 不记文档，白忙一场

------

#### 0、报错

> #### 开启此虚拟机报错
>
> ```python
> 报错描述：
> 	无法打开内核设备 \\.\Global\vmx86: 系统找不到指定的文件
> 解决：
>     点击“开始→运行”，在运行框中输入 CMD 回车打开命令提示符，然后依次执行以下命令。
>     net start vmci
>     net start vmx86
>     net start VMnetuserif
>     sc config vmci=auto
>     sc config vmx86=auto
>     sc config VMnetuserif=auto
> 来源：
> 	https://wenwen.sogou.com/z/q332634440.htm
> ```