### 不记文档，白忙一场

------

#### 1、Xms/Xmx参数含义

> #### 来源
>
> ```python
> https://www.jianshu.com/p/bf54d8493626
> ```
>
> #### 详解
>
> ```python
> -Xms:初始堆大小    --source源，初始化大小，即最小
> -Xmx:最大堆大小    --max最大
> -XX:NewSize=n:设置年轻代大小(Xmn)  --n是new的意思
> -XX:NewRatio=n:设置年轻代和年老代的比值。如:为3，表示年轻代与年老代比值为1：3，年轻代占整个年轻代年     老代和的1/4
> -XX:SurvivorRatio=n:年轻代中Eden区与两个Survivor区的比值。注意Survivor区有两个。如：3，表示	       Eden：Survivor=3：2，一个Survivor区占整个年轻代的1/5-XX:MaxPermSize=n:设置持久代大小
> ```



