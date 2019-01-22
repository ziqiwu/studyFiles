### 不记文档，白忙一场

------

#### hbase一个节点显示dead region server

> ​	问题：
>
> ```python
> 104服务器，进入hbase shell，显示killed
> 按照辉哥文档，从上往下测试，命令jps，没有找到QuorumPeerMain进程。
> 命令zkServer.sh start之后，hbase shell进入成功。
> 但是http://10.18.72.11:16010/master-status页面显示，104还是dead region servers。
> ```
>
> ​	解决
>
> ```python
> 解决：
> 	/data/hbase-1.2.4/bin/hbase-daemon.sh start regionserver
>     ps -ef | grep hbase之后，看到
>     	root      6579     1  0 17:52 pts/9    00:00:00 bash /data/hbase-1.2.4/bin/hbase-		daemon.sh --config /data/hbase-1.2.4/conf foreground_start regionserver
> 网站来源：
> 	https://www.cnblogs.com/jun1019/p/6260492.html
> ```

